"""
APScheduler module for Forex Beginners GH.
Automates daily scheduled broadcasts to Channel 1 (Lessons) and Channel 2 (Assignments)
based on Ghana Time (GMT / UTC+0).
The bot acts completely on behalf of the teacher/owner.
"""

import json
import logging
from datetime import datetime
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    LESSONS_CHANNEL_ID,
    ASSIGNMENTS_CHANNEL_ID,
    DISCUSSION_GROUP_ID,
    TIMEZONE,
    DISCLAIMER_TEXT
)
from database import db
from chart_generator import get_chart_for_day

logger = logging.getLogger(__name__)

# Load curriculum
def load_lessons_catalog():
    try:
        with open("lessons.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading lessons.json: {e}")
        return {}

LESSONS = load_lessons_catalog()

class BotScheduler:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone(TIMEZONE))

    async def get_current_day(self) -> int:
        day_str = await db.get_state("current_day", "1")
        try:
            return int(day_str)
        except ValueError:
            return 1

    async def set_current_day(self, day: int):
        day_clamped = max(1, min(14, day))
        await db.set_state("current_day", str(day_clamped))

    # ---------------- 9:00 AM Teaser Broadcast ---------------- #
    async def post_morning_teaser(self, force_day: int = None):
        """09:00 GMT: Posts morning teaser to Lessons Channel (Channel 1)."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1" and force_day is None:
            logger.info("Auto-post is paused. Skipping 9am teaser.")
            return

        current_day = force_day if force_day is not None else await self.get_current_day()
        day_data = LESSONS.get(str(current_day))
        if not day_data:
            return

        teaser_msg = (
            f"🌅 *CANDLEMASTER ACADEMY - MORNING BRIEF*\n\n"
            f"{day_data['teaser']}\n\n"
            f"📍 Channel: {LESSONS_CHANNEL_ID}\n"
            f"⏰ Full Lesson: Tonight 7:00 PM GMT sharp."
        )

        try:
            await self.bot.send_message(
                chat_id=LESSONS_CHANNEL_ID,
                text=teaser_msg,
                parse_mode="Markdown"
            )
            logger.info(f"Posted 9am teaser for Day {current_day} to {LESSONS_CHANNEL_ID}")
        except Exception as e:
            logger.error(f"Failed to post 9am teaser: {e}")

    # ---------------- 7:00 PM Full Lesson Broadcast ---------------- #
    async def post_full_lesson(self, force_day: int = None):
        """19:00 GMT: Posts complete lesson with chart, text, video, and voice script to Channel 1."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1" and force_day is None:
            logger.info("Auto-post is paused. Skipping 7pm lesson.")
            return

        day = force_day if force_day is not None else await self.get_current_day()
        day_data = LESSONS.get(str(day))
        if not day_data:
            logger.warning(f"No lesson data found for Day {day}")
            return

        # 1. Send Visual Educational Chart
        chart_path = get_chart_for_day(day)
        try:
            if chart_path:
                with open(chart_path, "rb") as photo_file:
                    await self.bot.send_photo(
                        chat_id=LESSONS_CHANNEL_ID,
                        photo=photo_file,
                        caption=f"📊 *Day {day} Visual Guide: {day_data['topic']}*",
                        parse_mode="Markdown"
                    )
        except Exception as e:
            logger.error(f"Error sending lesson chart: {e}")

        # 2. Send Full Lesson Text
        full_text = (
            f"🇬🇭 *DAY {day}: {day_data['topic'].upper()}*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{day_data['lesson_text']}\n\n"
            f"{day_data['calculation_example']}\n\n"
            f"🎬 *Recommended Video Lesson:*\n"
            f"• *Title:* {day_data['video_title']} ({day_data['video_duration']})\n"
            f"• *Watch Link:* {day_data['video_url']}\n"
            f"• *Why Watch:* {day_data['video_reason']}\n\n"
            f"🎙️ *Coach Prince Voice Note Script:*\n"
            f"_{day_data['voice_script']}_\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"{DISCLAIMER_TEXT}\n\n"
            f"👉 Quick Quiz polls incoming right below!\n"
            f"👉 Assignment drops in 30 minutes in {ASSIGNMENTS_CHANNEL_ID}!\n"
            f"👉 Questions? Ask in the linked Discussion Group!"
        )

        reply_markup = None
        if day == 14:
            try:
                me = await self.bot.get_me()
                if me and me.username:
                    reply_markup = InlineKeyboardMarkup([
                        [
                            InlineKeyboardButton("🎓 Claim Certificate (Free)", url=f"https://t.me/{me.username}?start=certificate"),
                            InlineKeyboardButton("⭐ Unlock Ultimate Strategy (200 Stars)", url=f"https://t.me/{me.username}?start=strategy_200")
                        ]
                    ])
            except Exception as e:
                logger.warning(f"Could not construct Day 14 inline buttons: {e}")

        try:
            await self.bot.send_message(
                chat_id=LESSONS_CHANNEL_ID,
                text=full_text,
                parse_mode="Markdown",
                disable_web_page_preview=False,
                reply_markup=reply_markup
            )
            logger.info(f"Posted 7pm lesson for Day {day} to {LESSONS_CHANNEL_ID}")
        except Exception as e:
            logger.error(f"Failed to post 7pm lesson: {e}")

    # ---------------- 7:15 PM Interactive Quiz Polls Broadcast ---------------- #
    async def post_quiz_polls(self, force_day: int = None, target_chat: str = None):
        """19:15 GMT: Posts 3 interactive Telegram native quiz polls directly to the channel/group."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1" and force_day is None:
            return

        day = force_day if force_day is not None else await self.get_current_day()
        day_data = LESSONS.get(str(day))
        if not day_data or "quizzes" not in day_data:
            return

        chat = target_chat or LESSONS_CHANNEL_ID

        # Introductory banner
        try:
            await self.bot.send_message(
                chat_id=chat,
                text=f"🧠 *DAY {day} FLASH QUIZ (3 QUESTIONS)*\n"
                     f"Test your understanding of today's lesson below. Tap your answer to see instant feedback!",
                parse_mode="Markdown"
            )
        except Exception as e:
            logger.error(f"Error sending quiz intro banner: {e}")

        # Send each quiz question as a native Telegram Quiz Poll
        for idx, q in enumerate(day_data["quizzes"]):
            try:
                question_text = f"Q{idx + 1}: {q['question']}"
                # Telegram limits: question <= 300 chars, explanation <= 200 chars
                poll_msg = await self.bot.send_poll(
                    chat_id=chat,
                    question=question_text[:300],
                    options=q["options"][:10],
                    type="quiz",
                    correct_option_id=q["correct_idx"],
                    explanation=q["explanation"][:200],
                    is_anonymous=False
                )
                if poll_msg and poll_msg.poll:
                    await db.register_poll(
                        poll_id=poll_msg.poll.id,
                        day=day,
                        question_idx=idx,
                        correct_option_id=q["correct_idx"]
                    )
            except Exception as e:
                logger.error(f"Failed to post quiz poll {idx + 1} for Day {day}: {e}")

        logger.info(f"Posted Day {day} quiz polls to {chat}")

    # ---------------- 7:30 PM Assignment Broadcast ---------------- #
    async def post_assignment(self, force_day: int = None):
        """19:30 GMT: Posts daily assignment to Channel 2 (Assignments)."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1" and force_day is None:
            return

        day = force_day if force_day is not None else await self.get_current_day()
        day_data = LESSONS.get(str(day))
        if not day_data:
            return

        assign_msg = (
            f"📝 *DAY {day} OFFICIAL ASSIGNMENT*\n"
            f"Topic: {day_data['topic']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{day_data['assignment']}\n\n"
            f"💡 Remember: Practice on your MT5 Demo account. Never risk real money.\n"
            f"⏰ Submission Deadline: Tomorrow 12:00 PM GMT."
        )

        try:
            await self.bot.send_message(
                chat_id=ASSIGNMENTS_CHANNEL_ID,
                text=assign_msg,
                parse_mode="Markdown"
            )
            logger.info(f"Posted 7:30pm assignment for Day {day} to {ASSIGNMENTS_CHANNEL_ID}")
        except Exception as e:
            logger.error(f"Failed to post assignment: {e}")

    # ---------------- 9:30 PM Assignment Reminder ---------------- #
    async def post_night_reminder(self):
        """21:30 GMT: Posts submission reminder to Channel 2."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1":
            return

        current_day = await self.get_current_day()
        day_data = LESSONS.get(str(current_day))
        if not day_data:
            return

        reminder_text = (
            f"⏰ *NIGHT REMINDER (9:30 PM GMT)*\n\n"
            f"{day_data['assignment_reminder']}\n\n"
            f"Post your answers in the Discussion Group or compare them with tomorrow's 12:00 PM correction!"
        )

        try:
            await self.bot.send_message(
                chat_id=ASSIGNMENTS_CHANNEL_ID,
                text=reminder_text,
                parse_mode="Markdown"
            )
            logger.info(f"Posted 9:30pm reminder for Day {current_day}")
        except Exception as e:
            logger.error(f"Failed to post 9:30pm reminder: {e}")

    # ---------------- 12:00 PM Assignment Correction Broadcast ---------------- #
    async def post_afternoon_correction(self):
        """12:00 GMT (Next Day): Posts assignment answer/correction to Channel 2."""
        paused = await db.get_state("auto_post_paused", "0")
        if paused == "1":
            return

        current_day = await self.get_current_day()
        day_data = LESSONS.get(str(current_day))
        if not day_data:
            return

        correction_text = (
            f"📖 *ASSIGNMENT REVIEW & CORRECTION*\n"
            f"Day {current_day}: {day_data['topic']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{day_data['correction']}\n\n"
            f"📌 Check your notes and correct any mistakes. Tonight at 7:00 PM, we advance!"
        )

        try:
            await self.bot.send_message(
                chat_id=ASSIGNMENTS_CHANNEL_ID,
                text=correction_text,
                parse_mode="Markdown"
            )
            logger.info(f"Posted 12:00pm correction for Day {current_day}")

            # Advance current day to next day after noon review
            if current_day < 14:
                await self.set_current_day(current_day + 1)
                logger.info(f"Advanced curriculum to Day {current_day + 1}")
        except Exception as e:
            logger.error(f"Failed to post 12pm correction: {e}")

    def start(self):
        """Registers all cron triggers for Ghana Time (GMT)."""
        # 9:00 AM GMT - Morning Teaser (Channel 1)
        self.scheduler.add_job(
            self.post_morning_teaser,
            CronTrigger(hour=9, minute=0, timezone=pytz.timezone(TIMEZONE)),
            id="morning_teaser"
        )

        # 7:00 PM GMT - Full Lesson (Channel 1)
        self.scheduler.add_job(
            self.post_full_lesson,
            CronTrigger(hour=19, minute=0, timezone=pytz.timezone(TIMEZONE)),
            id="full_lesson"
        )

        # 7:15 PM GMT - Interactive Quiz Polls (Channel 1)
        self.scheduler.add_job(
            self.post_quiz_polls,
            CronTrigger(hour=19, minute=15, timezone=pytz.timezone(TIMEZONE)),
            id="quiz_polls"
        )

        # 7:30 PM GMT - Daily Assignment (Channel 2)
        self.scheduler.add_job(
            self.post_assignment,
            CronTrigger(hour=19, minute=30, timezone=pytz.timezone(TIMEZONE)),
            id="daily_assignment"
        )

        # 9:30 PM GMT - Night Reminder (Channel 2)
        self.scheduler.add_job(
            self.post_night_reminder,
            CronTrigger(hour=21, minute=30, timezone=pytz.timezone(TIMEZONE)),
            id="night_reminder"
        )

        # 12:00 PM GMT - Assignment Correction (Channel 2)
        self.scheduler.add_job(
            self.post_afternoon_correction,
            CronTrigger(hour=12, minute=0, timezone=pytz.timezone(TIMEZONE)),
            id="noon_correction"
        )

        self.scheduler.start()
        logger.info("BotScheduler started successfully with Ghana GMT triggers (09:00, 19:00, 19:15, 19:30, 21:30, 12:00).")
