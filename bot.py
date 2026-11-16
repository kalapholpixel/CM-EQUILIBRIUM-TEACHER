"""
Forex Beginners GH - AI Teacher Bot (Coach Prince)
Main bot script managing 2 Channels, 1 Discussion Group, and Private Teacher Controls.

The bot acts completely in place of the human teacher (the owner).
Students do NOT need to start the bot: they simply join the channels and group.
The owner starts and commands the bot.
"""

import os
import json
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict, Any, List, Optional
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LabeledPrice,
    PollAnswer,
    PreCheckoutQuery
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    PreCheckoutQueryHandler,
    ContextTypes,
    filters
)

from config import (
    BOT_TOKEN,
    LESSONS_CHANNEL_ID,
    ASSIGNMENTS_CHANNEL_ID,
    DISCUSSION_GROUP_ID,
    ADMIN_IDS,
    BOT_NAME,
    PROJECT_NAME,
    DISCLAIMER_TEXT
)
from database import db
from ai_teacher import ai_teacher
from chart_generator import get_chart_for_day, generate_certificate, generate_ultimate_strategy_chart
from scheduler import BotScheduler, LESSONS

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Temporary user quiz session tracker for optional private quizzes
USER_QUIZ_SESSIONS: Dict[int, Dict[str, Any]] = {}

def is_admin(user_id: int) -> bool:
    """Checks if the user is the authorized bot administrator (the teacher/owner)."""
    if not ADMIN_IDS:
        return True  # If no admin IDs are explicitly set, the user running the command is treated as owner
    return user_id in ADMIN_IDS

async def send_safe_message(bot, chat_id: Any, text: str, reply_markup=None, parse_mode: str = "Markdown", disable_web_page_preview: bool = True):
    """
    Safely sends a message. If Markdown parsing fails due to unescaped symbols,
    gracefully falls back to plain text so messages are NEVER lost.
    """
    try:
        return await bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview
        )
    except Exception as e:
        logger.warning(f"send_safe_message: Markdown parse failed ({e}), falling back to plain text.")
        plain = text.replace('*', '').replace('_', '').replace('`', '')
        return await bot.send_message(
            chat_id=chat_id,
            text=plain,
            reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview
        )

# ==============================================================================
# OWNER / TEACHER COMMANDS (CONTROL PANEL)
# ==============================================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles /start:
    - If args (e.g. strategy_200): handles direct action.
    - If OWNER: Displays the Teacher Control Panel with 1-tap interactive inline buttons.
    - If STUDENT: Registers them and offers quick access to Channels, Certificate, & Ultimate Strategy.
    """
    user = update.effective_user
    chat = update.effective_chat

    # Direct deep-link routing
    if context.args:
        arg = context.args[0].lower()
        if arg in ("strategy_200", "strategy", "vip"):
            await strategy_command(update, context)
            return
        elif arg == "certificate":
            await student_certificate_command(update, context)
            return

    # Always ensure student/user record is tracked
    await db.register_student(
        user_id=user.id,
        username=user.username,
        full_name=user.full_name or user.first_name
    )

    # 1. OWNER / TEACHER EXPERIENCE
    if is_admin(user.id):
        current_day = await db.get_state("current_day", "1")
        paused = await db.get_state("auto_post_paused", "0")
        day_data = LESSONS.get(current_day, {})
        topic = day_data.get("topic", "Forex Basics")

        owner_panel = (
            f"👑 *WELCOME BOSS PRINCE! TEACHER CONTROL PANEL*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"I am **{BOT_NAME}**, actively teaching on your behalf across:\n"
            f"• **Channel 1 (Lessons):** {LESSONS_CHANNEL_ID}\n"
            f"• **Channel 2 (Assignments):** {ASSIGNMENTS_CHANNEL_ID}\n"
            f"• **Discussion Group:** Active 24/7 monitoring\n\n"
            f"📅 *Active Curriculum Day:* Day {current_day} of 14\n"
            f"📌 *Today's Topic:* _{topic}_\n"
            f"⏱️ *Auto-Post Scheduler:* {'PAUSED ⏸️' if paused == '1' else 'ACTIVE ▶️ (Ghana GMT)'}\n\n"
            f"🚀 *Quick Commands:*\n"
            f"• `/start_teaching` - Kick off Day 1 right now\n"
            f"• `/post` - Force post today's complete package\n"
            f"• `/post Day [X]` - Force post specific day (e.g. `/post 2`)\n"
            f"• `/strategy` - View Coach Prince's Ultimate Strategy Masterclass\n"
            f"• `/vip_list` - View students who paid 200 Stars\n"
            f"• `/grant_vip [user_id]` - Manually unlock strategy for someone\n"
            f"• `/status` - Live operational & revenue status\n\n"
            f"👇 *Or use 1-Tap Control Buttons below:*"
        )
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🚀 Force Post Today", callback_data="owner_post_today"),
                InlineKeyboardButton("⏩ Next Day", callback_data="owner_next_day")
            ],
            [
                InlineKeyboardButton("📊 Academy Status", callback_data="owner_status"),
                InlineKeyboardButton("⭐ VIP Students (200★)", callback_data="owner_vip_list")
            ],
            [
                InlineKeyboardButton("⏸️/▶️ Toggle Pause", callback_data="owner_toggle_pause"),
                InlineKeyboardButton("👑 My Strategy Blueprint", callback_data="owner_view_strategy")
            ]
        ])
        await send_safe_message(context.bot, chat.id, owner_panel, reply_markup=keyboard)
        return

    # 2. STUDENT EXPERIENCE
    student_msg = (
        f"Akwaaba! 🇬🇭 I am **{BOT_NAME}**, your dedicated Forex teacher in **{PROJECT_NAME}**.\n\n"
        "💡 *Good news:* You do **NOT** need to chat with me here to learn! "
        "I post all lessons, interactive quizzes, charts, and assignments directly in our channels:\n\n"
        f"📖 **Lessons Channel:** {LESSONS_CHANNEL_ID} (Clean lessons at 7:00 PM GMT)\n"
        f"📝 **Assignments Channel:** {ASSIGNMENTS_CHANNEL_ID} (Daily homework & corrections)\n"
        f"💬 **Discussion Group:** Ask your questions anytime, and I will answer you right there!\n\n"
        "⭐ *Masterclass:* On Day 14, you can unlock **Coach Prince's Ultimate Strategy (Top-Down Execution Trap)** "
        "for 200 Telegram Stars!\n\n"
        "Use the quick buttons below to explore:"
    )
    student_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⭐ Unlock Ultimate Strategy (200 Stars)", callback_data="buy_strategy_stars")
        ],
        [
            InlineKeyboardButton("🎓 Claim Certificate", callback_data="student_cert"),
            InlineKeyboardButton("📖 Today's Lesson", callback_data="student_today")
        ]
    ])
    await send_safe_message(context.bot, chat.id, student_msg, reply_markup=student_keyboard)

async def start_teaching_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /start_teaching - Kicks off Day 1 and unpauses auto-scheduler."""
    if not is_admin(update.effective_user.id):
        return

    await db.set_state("current_day", "1")
    await db.set_state("auto_post_paused", "0")

    scheduler = context.bot_data.get("scheduler")
    if scheduler:
        # Post morning teaser, lesson, quiz polls, and assignment for Day 1
        await update.message.reply_text("🚀 Starting Day 1 curriculum now across both channels...")
        await scheduler.post_morning_teaser(force_day=1)
        await scheduler.post_full_lesson(force_day=1)
        await scheduler.post_quiz_polls(force_day=1)
        await scheduler.post_assignment(force_day=1)

        await update.message.reply_text(
            f"✅ *DAY 1 IS LIVE!*\n\n"
            f"• Full lesson and chart posted to {LESSONS_CHANNEL_ID}\n"
            f"• 3 Interactive Quiz Polls posted to {LESSONS_CHANNEL_ID}\n"
            f"• Day 1 assignment posted to {ASSIGNMENTS_CHANNEL_ID}\n\n"
            f"Students can now learn and take the quiz directly in the channel without starting the bot! 🇬🇭",
            parse_mode="Markdown"
        )

async def admin_post_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /post [Day X] - Force posts lesson, chart, quiz, and assignment."""
    if not is_admin(update.effective_user.id):
        return

    args = context.args
    scheduler = context.bot_data.get("scheduler")
    if not scheduler:
        await update.message.reply_text("Scheduler not ready.")
        return

    if args:
        day_token = args[1] if args[0].lower() == "day" and len(args) > 1 else args[0]
        try:
            day = int(day_token)
        except ValueError:
            await update.message.reply_text("Usage: `/post Day [1-14]` or just `/post` for today.", parse_mode="Markdown")
            return
    else:
        day = await scheduler.get_current_day()

    await update.message.reply_text(f"Posting Day {day} package to channels...")
    await scheduler.post_full_lesson(force_day=day)
    await scheduler.post_quiz_polls(force_day=day)
    await scheduler.post_assignment(force_day=day)

    await update.message.reply_text(
        f"✅ Day {day} package (Lesson + Chart + 3 Quiz Polls + Assignment) posted successfully!",
        parse_mode="Markdown"
    )

async def admin_post_quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /post_quiz - Sends today's 3 Telegram Native Quiz Polls to Channel 1."""
    if not is_admin(update.effective_user.id):
        return

    scheduler = context.bot_data.get("scheduler")
    if scheduler:
        current_day = await scheduler.get_current_day()
        await scheduler.post_quiz_polls(force_day=current_day)
        await update.message.reply_text(f"✅ Day {current_day} quiz polls posted directly to {LESSONS_CHANNEL_ID}!")

async def admin_next_day_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /next_day - Advances the active curriculum day."""
    if not is_admin(update.effective_user.id):
        return

    current_day = int(await db.get_state("current_day", "1"))
    if current_day < 14:
        new_day = current_day + 1
        await db.set_state("current_day", str(new_day))
        day_data = LESSONS.get(str(new_day), {})
        await update.message.reply_text(f"✅ Advanced to *Day {new_day} of 14*: _{day_data.get('topic', '')}_", parse_mode="Markdown")
    else:
        await update.message.reply_text("🎓 Curriculum has reached Day 14 (Graduation Day)!")

async def admin_set_day_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /set_day [1-14] - Sets the active curriculum day."""
    if not is_admin(update.effective_user.id):
        return

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: `/set_day [1-14]` (e.g. `/set_day 5`)", parse_mode="Markdown")
        return

    target_day = int(context.args[0])
    if 1 <= target_day <= 14:
        await db.set_state("current_day", str(target_day))
        day_data = LESSONS.get(str(target_day), {})
        await update.message.reply_text(f"✅ Active day set to *Day {target_day}*: _{day_data.get('topic', '')}_", parse_mode="Markdown")
    else:
        await update.message.reply_text("Day must be between 1 and 14.")

async def admin_pause_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /pause - Pauses automated daily posting."""
    if not is_admin(update.effective_user.id):
        return
    await db.set_state("auto_post_paused", "1")
    await update.message.reply_text("⏸️ Automatic daily scheduled posting has been **PAUSED**.", parse_mode="Markdown")

async def admin_resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /resume - Resumes automated daily posting."""
    if not is_admin(update.effective_user.id):
        return
    await db.set_state("auto_post_paused", "0")
    await update.message.reply_text("▶️ Automatic daily scheduled posting has been **RESUMED**.", parse_mode="Markdown")

async def admin_announce_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /announce [message] - Broadcasts to both channels."""
    if not is_admin(update.effective_user.id):
        return
    if not context.args:
        await update.message.reply_text("Usage: `/announce [Your announcement text]`", parse_mode="Markdown")
        return

    announcement = " ".join(context.args)
    formatted_msg = (
        f"📢 *OFFICIAL ANNOUNCEMENT - CANDLEMASTER ACADEMY*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{announcement}\n\n"
        f"— Coach Prince & Management"
    )

    sent_channels = []
    for ch_id in (LESSONS_CHANNEL_ID, ASSIGNMENTS_CHANNEL_ID):
        try:
            await context.bot.send_message(chat_id=ch_id, text=formatted_msg, parse_mode="Markdown")
            sent_channels.append(ch_id)
        except Exception as e:
            logger.error(f"Error sending announcement to {ch_id}: {e}")

    await update.message.reply_text(f"✅ Announcement sent to: {', '.join(sent_channels)}")

async def admin_status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /status - Live academy status."""
    if not is_admin(update.effective_user.id):
        return

    sys_stats = await db.get_system_stats()
    hardest = await db.get_hardest_topics(limit=4)
    current_day = await db.get_state("current_day", "1")
    paused = await db.get_state("auto_post_paused", "0")
    day_data = LESSONS.get(current_day, {})

    msg = (
        f"📊 *CANDLEMASTER ACADEMY - LIVE OPERATIONAL STATUS*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 *Current Curriculum Day:* Day {current_day} of 14\n"
        f"📌 *Topic:* {day_data.get('topic', 'General')}\n"
        f"⏱️ *Schedule Engine:* {'PAUSED ⏸️' if paused == '1' else 'ACTIVE ▶️ (Ghana GMT)'}\n\n"
        f"📡 *Channel 1 (Lessons):* {LESSONS_CHANNEL_ID}\n"
        f"📝 *Channel 2 (Assignments):* {ASSIGNMENTS_CHANNEL_ID}\n"
        f"💬 *Discussion Group:* {DISCUSSION_GROUP_ID or 'Linked Group'}\n\n"
        f"👥 *Enrolled Students:* {sys_stats['total_students']}\n"
        f"📝 *Assignments Logged:* {sys_stats['total_assignments_submitted']}\n"
        f"💬 *Questions Answered by Coach Prince:* {sys_stats['total_questions_asked']}\n"
        f"⭐ *VIP Strategy Purchases (200★):* {sys_stats.get('total_vip_students', 0)} students\n\n"
        f"🔥 *Hardest Topics from Student Questions:*\n"
    )

    if hardest:
        for t in hardest:
            confused = t["confused_count"] or 0
            msg += f"• *{t['topic']}*: {t['question_count']} questions ({confused} re-explained)\n"
    else:
        msg += "• No student questions logged yet.\n"

    await update.message.reply_text(msg, parse_mode="Markdown")

# ==============================================================================
# DISCUSSION GROUP 24/7 LISTENER (COACH PRINCE TEACHING IN THE GROUP)
# ==============================================================================

async def handle_incoming_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Monitors the discussion group and private messages 24/7.
    Answers student questions like a patient human teacher in 3 steps:
    1) Simple Answer
    2) Real-life Ghana Example
    3) Check understanding (YES/NO)
    Re-explains if student says NO.
    """
    if not update.message or not update.message.text:
        return

    text = update.message.text.strip()
    user = update.effective_user
    chat = update.effective_chat
    chat_type = chat.type  # 'group', 'supergroup', 'private'
    user_name = user.first_name or user.username or "Student"

    # In groups: Respond if replied to bot, tagged, or asking a question
    bot_username = context.bot.username or ""
    is_private = (chat_type == "private")
    is_reply_to_bot = (
        update.message.reply_to_message and 
        update.message.reply_to_message.from_user and 
        update.message.reply_to_message.from_user.id == context.bot.id
    )
    is_tagged = (f"@{bot_username.lower()}" in text.lower()) if bot_username else False
    is_question = "?" in text or text.lower().startswith((
        "how", "what", "why", "when", "where", "can i", "is it", "please explain", "coach"
    ))

    # Skip general chat between members unless it's addressed to the bot or asking a question
    if not is_private and not is_reply_to_bot and not is_tagged and not is_question:
        return

    # 1. Handle "YES" / "NO" & Confusion Understanding Follow-ups
    text_clean = text.lower().strip()
    confusion_phrases = (
        "no", "i don't understand", "i do not understand", "still confused", 
        "explain again", "i am lost", "i'm lost", "not clear", "don't get it", 
        "dont get it", "further explanation", "feather explanation", "explain more",
        "break it down", "confusing", "hard to understand", "what do you mean",
        "please explain more", "can you elaborate", "i need help understanding"
    )
    if any(phrase in text_clean for phrase in confusion_phrases) or text_clean in ("no", "nope", "nah"):
        latest_q = await db.get_latest_question_for_user(user.id)
        if latest_q:
            await db.update_question_understanding(latest_q["id"], understood=False)
        re_explanation = await ai_teacher.re_explain(user_name, original_question=latest_q["question_text"] if latest_q else None)
        await send_safe_message(context.bot, chat.id, re_explanation)
        return

    understanding_phrases = (
        "yes", "i understand", "makes sense", "thank you", "clear now", 
        "got it", "i get it", "crystal clear", "clear", "ayekoo", "well understood"
    )
    if any(phrase in text_clean for phrase in understanding_phrases) or text_clean in ("yes", "yeah", "yep"):
        latest_q = await db.get_latest_question_for_user(user.id)
        if latest_q:
            await db.update_question_understanding(latest_q["id"], understood=True)
        affirmation = (
            f"@{user_name}, Ayekoo! 🎉 That is music to my ears as your teacher.\n"
            "Keep practicing, stay humble, and remember: capital preservation comes first. God bless your effort!"
        )
        await send_safe_message(context.bot, chat.id, affirmation)
        return

    # 2. Check for Assignment Submission (if sent directly)
    is_homework_text = any(kw in text_clean for kw in ["assignment", "homework", "my submission", "my answers", "task 1", "task 2", "task 3", "solution"]) and len(text.split()) >= 6
    if is_homework_text:
        current_day = int(await db.get_state("current_day", "1"))
        await db.record_assignment_submission(user.id, current_day, text)
        ack_msg = (
            f"@{user_name}, Coach Prince has received your Day {current_day} assignment submission! 📝\n\n"
            "Well done for taking action and doing the homework. Compare your findings with tomorrow's "
            f"12:00 PM correction post in {ASSIGNMENTS_CHANNEL_ID}!"
        )
        await send_safe_message(context.bot, chat.id, ack_msg)
        return

    # 3. Answer with 3-Step Human Teaching Loop
    clean_query = text.replace(f"@{bot_username}", "").strip()
    response_text, topic = await ai_teacher.answer_question(user_name, clean_query)

    # Log into database to track difficult topics
    await db.log_question(
        user_id=user.id,
        username=user.username,
        chat_id=str(chat.id),
        chat_type=chat_type,
        question_text=clean_query,
        bot_response=response_text,
        topic=topic
    )

    feedback_markup = None
    if is_private:
        feedback_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("✅ Understood!", callback_data="feedback_understood"),
                InlineKeyboardButton("❌ Still Confused (Explain Simpler)", callback_data="feedback_confused")
            ]
        ])

    await send_safe_message(context.bot, chat.id, response_text, reply_markup=feedback_markup)

# ==============================================================================
# OPTIONAL STUDENT HELPER COMMANDS
# ==============================================================================

async def student_today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Optional: /today - Sends today's lesson text."""
    day_str = await db.get_state("current_day", "1")
    day = int(day_str)
    day_data = LESSONS.get(str(day))
    if not day_data:
        await update.message.reply_text("Lesson not found.")
        return

    chart_path = get_chart_for_day(day)
    if chart_path and os.path.exists(chart_path):
        try:
            with open(chart_path, "rb") as photo:
                await update.message.reply_photo(
                    photo=photo,
                    caption=f"📊 *Day {day} Chart: {day_data['topic']}*",
                    parse_mode="Markdown"
                )
        except Exception:
            pass

    msg = (
        f"🇬🇭 *DAY {day}: {day_data['topic'].upper()}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{day_data['lesson_text']}\n\n"
        f"🎬 *Recommended Video:* [{day_data['video_title']}]({day_data['video_url']})\n\n"
        f"{DISCLAIMER_TEXT}"
    )
    await update.message.reply_text(msg, parse_mode="Markdown", disable_web_page_preview=False)

async def student_notes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Optional: /notes - Sends today's notes."""
    day = int(await db.get_state("current_day", "1"))
    day_data = LESSONS.get(str(day))
    if day_data:
        msg = f"📚 *STUDY NOTES: DAY {day}*\n\n{day_data['notes_summary']}"
        await update.message.reply_text(msg, parse_mode="Markdown")

async def student_certificate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Optional: /certificate - Generates completion certificate on graduation."""
    user = update.effective_user
    current_day = int(await db.get_state("current_day", "1"))

    if current_day < 14 and not is_admin(user.id):
        await update.message.reply_text(
            f"Coach Prince here! 🎓 We are currently on Day {current_day}. "
            "Certificates are unlocked on Day 14 (Graduation Day). Keep following the daily lessons in the channel!"
        )
        return

    cert_path = generate_certificate(student_name=user.full_name or user.first_name)
    caption = (
        f"🎓 *CONGRATULATIONS, {user.full_name.upper()}!*\n\n"
        "Here is your official Certificate of Completion for the 14-Day Forex Fundamentals Course at Candlemaster Academy.\n"
        "Remember Coach Prince's rule: Stay on demo for 30 more days, risk 1-2% only, and never trade without a Stop Loss!"
    )
    with open(cert_path, "rb") as cert_file:
        await update.message.reply_photo(photo=cert_file, caption=caption, parse_mode="Markdown")

async def student_progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Optional: /my_progress - Student views their personal learning score and status."""
    user = update.effective_user
    chat = update.effective_chat
    
    current_day = int(await db.get_state("current_day", "1"))
    quiz_stats = await db.get_student_quiz_stats(user.id)
    assign_count = await db.get_student_assignment_count(user.id)
    is_vip = await db.is_vip_student(user.id)
    
    vip_badge = "UNLOCKED ⭐ (Masterclass VIP)" if is_vip else "Free Tier (Send /strategy to unlock)"
    cert_status = "Available Now! (Type /certificate)" if current_day >= 14 else f"Unlocks on Day 14 (Currently on Day {current_day})"
    
    msg = (
        f"📊 *MY LEARNING PROGRESS — CANDLEMASTER ACADEMY*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Student:* {user.full_name}\n"
        f"📅 *Active Academy Day:* Day {current_day} of 14\n\n"
        f"🧠 *Quiz Poll Performance:*\n"
        f"• Questions Attempted: **{quiz_stats['total_attempts']}**\n"
        f"• Correct Answers: **{quiz_stats['correct_answers']}**\n"
        f"• Accuracy Rate: **{quiz_stats['accuracy_pct']}%**\n\n"
        f"📝 *Homeworks Submitted:* **{assign_count}**\n"
        f"⭐ *Coach Prince Ultimate Strategy:* **{vip_badge}**\n"
        f"📜 *Graduation Certificate:* **{cert_status}**\n\n"
        f"Keep practicing on your MT5 demo account. God bless your effort!"
    )
    await send_safe_message(context.bot, chat.id, msg)

async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Optional: /leaderboard - Displays top academy students."""
    leaders = await db.get_leaderboard(limit=5)
    if not leaders:
        await send_safe_message(context.bot, update.effective_chat.id, "🏆 No student scores recorded on the leaderboard yet.")
        return
        
    msg = (
        f"🏆 *CANDLEMASTER ACADEMY — STUDENT LEADERBOARD*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Top performers leading in quiz accuracy and homework discipline:\n\n"
    )
    medals = ["🥇", "🥈", "🥉", "🏅", "🏅"]
    for i, lead in enumerate(leaders):
        m = medals[i] if i < len(medals) else "🏅"
        uname = f"@{lead['username']}" if lead.get("username") else "Student"
        name = lead.get("full_name") or uname
        corr = lead.get("correct_answers") or 0
        total_q = lead.get("total_quizzes") or 0
        acc = round((corr / total_q * 100), 1) if total_q > 0 else 0.0
        hw = lead.get("total_assignments") or 0
        msg += f"{m} *{name}* ({uname})\n   • Quizzes: {corr}/{total_q} ({acc}%) | Homeworks: {hw}\n\n"
        
    msg += "Consistent daily discipline is how great traders are made! 🇬🇭"
    await send_safe_message(context.bot, update.effective_chat.id, msg)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles /help for both Boss Prince and students."""
    user = update.effective_user
    chat = update.effective_chat
    
    if is_admin(user.id):
        admin_help = (
            f"👑 *BOSS PRINCE — TEACHER COMMAND CENTER*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"• `/start` - Open Teacher Control Panel & 1-tap buttons\n"
            f"• `/start_teaching` - Kick off Day 1 curriculum across channels\n"
            f"• `/post` - Force post today's package (Lesson + Chart + Quizzes + Homework)\n"
            f"• `/post Day [X]` - Force post specific day (e.g. `/post 2`)\n"
            f"• `/next_day` - Advance curriculum to next day\n"
            f"• `/set_day [1-14]` - Set specific day\n"
            f"• `/pause` / `/resume` - Pause or resume scheduled posting\n"
            f"• `/submissions [day]` - View student homework submissions\n"
            f"• `/strategy` - View Coach Prince's Ultimate Strategy blueprint\n"
            f"• `/vip_list` - View students who paid 200 Telegram Stars\n"
            f"• `/grant_vip [user_id]` - Manually unlock VIP strategy for someone\n"
            f"• `/leaderboard` - View top students\n"
            f"• `/announce [msg]` - Broadcast to both channels simultaneously\n"
            f"• `/status` - Live academy analytics and hardest topics"
        )
        await send_safe_message(context.bot, chat.id, admin_help)
        return
        
    student_help = (
        f"🇬🇭 *COACH PRINCE — STUDENT HELP GUIDE*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Akwaaba! Here is how to learn with **{PROJECT_NAME}**:\n\n"
        f"1️⃣ **Daily Lessons:** Read lessons and view charts at 7:00 PM GMT in {LESSONS_CHANNEL_ID}.\n"
        f"2️⃣ **Daily Quizzes:** Tap your answer on the 3 interactive quiz polls posted right below each lesson!\n"
        f"3️⃣ **Daily Homework:** Practice on MT5 Demo and send your answers/screenshots here in private chat!\n"
        f"4️⃣ **Ask Questions:** In the Discussion Group, Coach Prince answers 24/7 in 3 simple steps.\n\n"
        f"📌 *Student Commands:*\n"
        f"• `/today` - Read today's lesson text\n"
        f"• `/notes` - View today's summary cheatsheet\n"
        f"• `/my_progress` - Check your personal quiz score & assignments\n"
        f"• `/leaderboard` - View top students in the academy\n"
        f"• `/certificate` - Claim completion certificate (Day 14)\n"
        f"• `/strategy` - Unlock Coach Prince's Ultimate Strategy (200 Stars)"
    )
    await send_safe_message(context.bot, chat.id, student_help)

async def admin_submissions_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /submissions [day] - Reviews student homework submissions."""
    if not is_admin(update.effective_user.id):
        return
        
    day = int(context.args[0]) if (context.args and context.args[0].isdigit()) else int(await db.get_state("current_day", "1"))
    subs = await db.get_submissions_for_day(day, limit=15)
    
    if not subs:
        await update.message.reply_text(f"📝 No student submissions logged for Day {day} yet.")
        return
        
    msg = f"📝 *STUDENT SUBMISSIONS — DAY {day} ({len(subs)} submissions)*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for s in subs:
        uname = f"@{s['username']}" if s.get("username") else "Student"
        name = s.get("full_name") or uname
        txt = (s.get("submission_text") or "")[:150]
        msg += f"👤 *{name}* ({uname}):\n_{txt}_\n\n"
        
    await send_safe_message(context.bot, update.effective_chat.id, msg)

# ==============================================================================
# COACH PRINCE'S ULTIMATE STRATEGY (200 TELEGRAM STARS MASTERCLASS)
# ==============================================================================

async def send_strategy_invoice(bot, chat_id: int):
    """Sends the official 200 Telegram Stars invoice for Coach Prince's Ultimate Strategy."""
    await bot.send_invoice(
        chat_id=chat_id,
        title="Coach Prince's Ultimate Strategy",
        description="Master Coach Prince's Top-Down Multi-Timeframe Strategy & POI Sniping (D1 to M15 Execution Trap).",
        payload="coach_prince_ultimate_strategy",
        currency="XTR",
        prices=[LabeledPrice("Ultimate Strategy Masterclass", 200)],
        provider_token="",  # Must be empty string for Telegram Stars!
        start_parameter="strategy_200"
    )

async def deliver_ultimate_strategy(bot, chat_id: int, user_name: str):
    """Delivers Coach Prince's Ultimate Strategy Masterclass directly to the student."""
    chart_path = generate_ultimate_strategy_chart()
    
    # 1. Send Strategy Blueprint Chart
    if os.path.exists(chart_path):
        try:
            with open(chart_path, "rb") as photo:
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=photo,
                    caption=(
                        f"👑 *COACH PRINCE'S ULTIMATE STRATEGY BLUEPRINT*\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"Welcome @{user_name}! Here is your complete institutional roadmap: "
                        f"From Daily Macro Bias to the 15-Minute Execution Trap."
                    ),
                    parse_mode="Markdown"
                )
        except Exception as e:
            logger.error(f"Error sending strategy chart: {e}")

    # 2. Part 1: Top-Down Multi-Timeframe Framework
    part1_text = (
        "📖 *PART 1: THE TOP-DOWN TIMEFRAME HIERARCHY*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🎯 *1. DAILY (D1) — MACRO BIAS & BOUNDARIES*\n"
        "• **Purpose:** Tells you where the market is pointing and whether to BUY, SELL, or FOLD YOUR HANDS.\n"
        "• **Action:** Map the recent strong Resistance ceiling and Demand floor where price is currently reacting.\n"
        "• **Key Rule:** Focus ONLY on recent levels! Do not zoom out to ancient charts from 6 months ago that have already played out.\n"
        "• Identify the last Break of Structure (BOS) and its Origin.\n\n"
        "🎯 *2. 4-HOUR (H4) — STRUCTURE REFINEMENT*\n"
        "• **Purpose:** Refine the daily origin zone down into a precise 4-Hour Order Block.\n"
        "• **Action:** Map intermediate BOS and Change of Character (CHoCH).\n"
        "• Note pending major swing zones so you know where price will eventually head without forcing premature trades.\n\n"
        "🎯 *3. 1-HOUR / 30-MIN (H1/M30) — INTERNAL STRUCTURE & POI SCOUTING*\n"
        "• **Purpose:** Break down what is happening INSIDE the higher timeframe leg.\n"
        "• **Crucial Rule:** Differentiate *mitigated* vs *unmitigated* order blocks!\n"
        "  - If price has already tapped/mitigated an origin, it is WEAK and likely to break.\n"
        "  - Target ONLY fresh, **unmitigated origins with Fair Value Gaps (FVG)**!\n"
        "• Do not wait weeks for a higher-TF zone: trade the internal move towards it.\n\n"
        "🎯 *4. 15-MIN (M15) — THE EXECUTION TRAP ZONE*\n"
        "• **This is Coach Prince's primary entry timeframe.**\n"
        "• Spot localized micro BOS and fresh unmitigated Order Blocks with FVG.\n"
        "• **Set your trap:** Place a limit order at the start of the order block / FVG.\n"
        "• **Stop Loss:** Set tightly just beyond the last rejection wick!\n"
        "• **Take Profit:** Target opposing demand/supply liquidity for asymmetric **1:3 to 1:5+ Risk:Reward**.\n\n"
        "🎯 *5. LOWER TIMEFRAMES (M5 / M3 / M1) — CONFIRMATION ENTRY (OPTIONAL)*\n"
        "• For traders who want sniper confirmation before clicking: wait for price to tap the 15M POI, drop to M3/M1, and wait for a micro CHoCH + FVG retest before pulling the trigger."
    )
    await send_safe_message(bot, chat_id, part1_text)

    # 3. Part 2: The 5 Golden Rules, Live Video Link, and Case Study
    part2_text = (
        "👑 *PART 2: THE 5 GOLDEN TRAPPING RULES & VIDEO MASTERCLASS*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "1️⃣ **Never Be Too Lazy for Top-Down Analysis:** Every trading session starts from the Daily. Knowing which timeframe is in control prevents late entries and emotional chasing.\n\n"
        "2️⃣ **Recency Over Ancient History:** The market reacts to recent orders. Keep your chart clean and uncluttered.\n\n"
        "3️⃣ **Mitigated Origins Are Liquidity:** Old mitigated zones break easily. Fresh unmitigated zones with FVG are where institutional reactions happen.\n\n"
        "4️⃣ **Don't Force Faraway Higher-TF Zones:** If the Daily demand is 300 pips away, use the 15M structure to 'sell to buy' or 'buy to sell' on the internal journey.\n\n"
        "5️⃣ **Hard SL Behind the Wick & Close MT5:** Once your trap is set, your risk is fixed (1-2% only). Close the app and let the market play out!\n\n"
        "🎬 *WATCH COACH PRINCE'S FULL VIDEO BREAKDOWN:*\n"
        "👉 [Click Here to Watch Coach Prince's Video Masterclass](https://youtu.be/Sdj6XbXbowM?si=if7Lig8J0A02suPV)\n"
        "*(Study the live GBP/JPY multi-timeframe breakdown in this video carefully!)*\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💡 *VIP TIP:* Type `/strategy` anytime to review your masterclass materials. Keep practicing on demo and stay disciplined!"
    )
    await send_safe_message(bot, chat_id, part2_text, disable_web_page_preview=False)

async def strategy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles /strategy and /unlock_strategy:
    - If already purchased / VIP: delivers the masterclass immediately.
    - If not purchased: presents the masterclass overview and sends the 200 Stars invoice.
    """
    user = update.effective_user
    chat = update.effective_chat
    
    is_vip = await db.is_vip_student(user.id)
    # Owner always has free VIP access
    if is_admin(user.id) or is_vip:
        await send_safe_message(context.bot, chat.id, "👑 *WELCOME VIP TRADER!* Accessing Coach Prince's Ultimate Strategy Masterclass...")
        await deliver_ultimate_strategy(context.bot, chat.id, user.first_name)
        return

    # Non-VIP: Explain value & send invoice
    intro = (
        f"👑 *COACH PRINCE'S ULTIMATE STRATEGY MASTERCLASS*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        "Are you ready to stop guessing and trade with true institutional clarity?\n\n"
        "In this Masterclass, Coach Prince breaks down his exact **Top-Down Multi-Timeframe Execution Framework**:\n"
        "• **Daily (D1):** Read Macro Bias & establish boundaries (Buy / Sell / Stay Off)\n"
        "• **4-Hour (H4):** Refine structural zones & spot intermediate BOS / CHoCH\n"
        "• **1-Hour (H1):** Discard mitigated zones & scout high-probability FVGs\n"
        "• **15-Min (M15):** The Execution Trap — set tight SL beyond rejection wicks & target 1:3 to 1:5+ RR\n"
        "• **5-Point Trapping Protocol:** Recent zones, unmitigated order blocks, and trade management\n"
        "• **Full Video Masterclass Link + High-Res Strategy Blueprint Chart**\n\n"
        "⭐ *Price:* **200 Telegram Stars** (One-time lifetime unlock)\n\n"
        "Tap the invoice below to unlock your Masterclass immediately with Telegram Stars! 👇"
    )
    await send_safe_message(context.bot, chat.id, intro)
    try:
        await send_strategy_invoice(context.bot, chat.id)
    except Exception as e:
        logger.error(f"Error sending Stars invoice: {e}")
        await send_safe_message(
            context.bot,
            chat.id,
            "💡 *Note:* Telegram Stars invoices must be opened in private chat. Send `/strategy` to Coach Prince in private!"
        )

async def precheckout_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Validates Telegram Stars checkout before charge."""
    query = update.pre_checkout_query
    if query.invoice_payload != "coach_prince_ultimate_strategy":
        await query.answer(ok=False, error_message="Order verification failed. Please try again.")
    else:
        await query.answer(ok=True)

async def successful_payment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles confirmed Telegram Stars payment (200 Stars)."""
    payment = update.message.successful_payment
    user = update.effective_user
    chat = update.effective_chat
    
    if payment.currency == "XTR":
        await db.record_vip_purchase(
            user_id=user.id,
            username=user.username,
            amount_stars=payment.total_amount,
            charge_id=payment.telegram_payment_charge_id
        )
        logger.info(f"Student {user.id} (@{user.username}) successfully paid 200 Stars!")
        
        await update.message.reply_text(
            f"🎉 *CONGRATULATIONS {user.first_name.upper()}!*\n\n"
            f"Payment of **{payment.total_amount} Telegram Stars** confirmed! 🌟\n"
            "You have officially unlocked **Coach Prince's Ultimate Strategy Masterclass**.\n"
            "Here is your complete blueprint:",
            parse_mode="Markdown"
        )
        await deliver_ultimate_strategy(context.bot, chat.id, user.first_name)

async def admin_grant_vip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /grant_vip [user_id] - Manually grants VIP strategy access."""
    if not is_admin(update.effective_user.id):
        return
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: `/grant_vip [Telegram_User_ID]`", parse_mode="Markdown")
        return
    target_id = int(context.args[0])
    await db.grant_vip_access(target_id, username="Granted by Boss Prince")
    await update.message.reply_text(f"✅ VIP Strategy access successfully granted to user ID `{target_id}`!", parse_mode="Markdown")

async def admin_vip_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Owner command: /vip_list - Displays all students who unlocked the Ultimate Strategy."""
    if not is_admin(update.effective_user.id):
        return
    vips = await db.get_all_vip_students()
    if not vips:
        await update.message.reply_text("⭐ No students have unlocked the Ultimate Strategy yet.")
        return
    total_stars = sum(v.get("amount_stars", 200) for v in vips)
    msg = (
        f"⭐ *CANDLEMASTER ACADEMY — VIP STUDENTS ROSTER*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Total VIP Students: **{len(vips)}**\n"
        f"Total Stars Generated: **{total_stars} ⭐**\n\n"
    )
    for v in vips:
        uname = f"@{v['username']}" if v.get("username") else "Student"
        name = v.get("full_name") or uname
        dt = (v.get("purchased_at") or "")[:10]
        msg += f"• `{v['user_id']}` | {name} ({uname}) | {v.get('amount_stars', 200)}★ | {dt}\n"
    await send_safe_message(context.bot, update.effective_chat.id, msg)

async def handle_callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles inline keyboard button clicks."""
    query = update.callback_query
    await query.answer()
    data = query.data
    user = update.effective_user
    chat = update.effective_chat
    
    # 1. Student button clicks
    if data == "buy_strategy_stars":
        await strategy_command(update, context)
        return
    elif data == "student_cert":
        await student_certificate_command(update, context)
        return
    elif data == "student_today":
        await student_today_command(update, context)
        return
    elif data == "feedback_understood":
        await query.edit_message_reply_markup(reply_markup=None)
        affirmation = (
            f"@{user.first_name}, Ayekoo! 🎉 That is music to my ears as your teacher.\n"
            "Keep practicing, stay humble, and remember: capital preservation comes first. God bless your effort!"
        )
        await send_safe_message(context.bot, chat.id, affirmation)
        return
    elif data == "feedback_confused":
        await query.edit_message_reply_markup(reply_markup=None)
        latest_q = await db.get_latest_question_for_user(user.id)
        if latest_q:
            await db.update_question_understanding(latest_q["id"], understood=False)
        re_explanation = await ai_teacher.re_explain(user.first_name, original_question=latest_q["question_text"] if latest_q else None)
        await send_safe_message(context.bot, chat.id, re_explanation)
        return
        
    # 2. Owner button clicks
    if is_admin(user.id):
        scheduler = context.bot_data.get("scheduler")
        if data == "owner_post_today":
            if scheduler:
                day = await scheduler.get_current_day()
                await send_safe_message(context.bot, chat.id, f"🚀 Posting Day {day} package now across channels...")
                await scheduler.post_full_lesson(force_day=day)
                await scheduler.post_quiz_polls(force_day=day)
                await scheduler.post_assignment(force_day=day)
                await send_safe_message(context.bot, chat.id, f"✅ Day {day} package posted successfully to both channels!")
        elif data == "owner_next_day":
            current_day = int(await db.get_state("current_day", "1"))
            if current_day < 14:
                new_day = current_day + 1
                await db.set_state("current_day", str(new_day))
                await send_safe_message(context.bot, chat.id, f"⏩ Advanced curriculum to Day {new_day} of 14!")
            else:
                await send_safe_message(context.bot, chat.id, "🎓 Curriculum is at Day 14 (Graduation Day)!")
        elif data == "owner_status":
            await admin_status_command(update, context)
        elif data == "owner_vip_list":
            await admin_vip_list_command(update, context)
        elif data == "owner_toggle_pause":
            paused = await db.get_state("auto_post_paused", "0")
            new_state = "0" if paused == "1" else "1"
            await db.set_state("auto_post_paused", new_state)
            status_text = "PAUSED ⏸️" if new_state == "1" else "RESUMED ▶️"
            await send_safe_message(context.bot, chat.id, f"⏱️ Daily auto-posting schedule is now **{status_text}**.")
        elif data == "owner_view_strategy":
            await deliver_ultimate_strategy(context.bot, chat.id, user.first_name)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Listens to native Telegram quiz poll answers.
    Records student participation and score in database.
    """
    answer: PollAnswer = update.poll_answer
    user = answer.user
    selected_options = answer.option_ids
    
    if not selected_options:
        return
        
    user_id = user.id
    username = user.username
    full_name = user.full_name or user.first_name
    
    # Register/update student in DB
    await db.register_student(user_id=user_id, username=username, full_name=full_name)
    
    # Map poll to day and check if correct
    poll_id = answer.poll_id
    poll_info = await db.get_poll_info(poll_id)
    
    if poll_info:
        day = poll_info["day"]
        q_idx = poll_info["question_idx"]
        correct_opt = poll_info["correct_option_id"]
        is_correct = (selected_options[0] == correct_opt)
    else:
        day = int(await db.get_state("current_day", "1"))
        q_idx = 0
        is_correct = True
    
    # Record quiz attempt
    await db.record_quiz_attempt(
        user_id=user_id,
        day=day,
        question_idx=q_idx,
        selected_option=selected_options[0],
        is_correct=is_correct
    )
    logger.info(f"Recorded quiz vote from {full_name} ({user_id}) for Day {day} Q{q_idx + 1} | Correct: {is_correct}")

async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Listens to screenshot/photo submissions from students (MT5 demo chart homework).
    """
    if not update.message or not update.message.photo:
        return
        
    caption = (update.message.caption or "").strip()
    user = update.effective_user
    chat = update.effective_chat
    user_name = user.first_name or "Student"
    
    current_day = int(await db.get_state("current_day", "1"))
    photo_file_id = update.message.photo[-1].file_id
    
    submission_content = f"[Screenshot: {photo_file_id}] {caption}"
    await db.record_assignment_submission(user.id, current_day, submission_content)
    
    ack_msg = (
        f"@{user_name}, Coach Prince has received your Day {current_day} MT5 chart screenshot! 📸📊\n\n"
        "Excellent discipline! Practicing on your MT5 demo and marking your levels is exactly how professional traders are forged.\n"
        f"Compare your analysis with tomorrow's 12:00 PM review post in {ASSIGNMENTS_CHANNEL_ID}!"
    )
    await send_safe_message(context.bot, chat.id, ack_msg)

# ==============================================================================
# MAIN BOT INITIALIZATION
# ==============================================================================

async def post_init(application: Application):
    """Initializes SQLite database and starts Ghana GMT scheduler."""
    logger.info("Initializing SQLite database...")
    await db.init_db()

    logger.info("Starting Ghana GMT daily scheduler...")
    scheduler = BotScheduler(application.bot)
    scheduler.start()
    application.bot_data["scheduler"] = scheduler

    logger.info(f"{BOT_NAME} is fully online and active in place of the teacher!")

class HealthCheckHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler to satisfy cloud hosting health checks (Hugging Face Spaces, Render, etc.)."""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = (
            "<!DOCTYPE html><html><head><title>Candlemaster AI Teacher</title></head>"
            "<body style='font-family: Arial, sans-serif; text-align: center; padding-top: 60px; background: #0f172a; color: #f8fafc;'>"
            "<h1>Candlemaster Academy Bot</h1>"
            "<p style='color: #4ade80; font-size: 22px; font-weight: bold;'>&#9679; Status: Online and Active 24/7</p>"
            "<p style='color: #94a3b8;'>Running on behalf of Coach Prince</p>"
            "</body></html>"
        )
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Suppress standard HTTP request logging in console

def start_health_check_server():
    """Starts a lightweight HTTP server on the port specified by PORT env var (default 7860 for Hugging Face)."""
    port = int(os.getenv("PORT", 7860))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        logger.info(f"Health-check web server listening on port {port}")
    except Exception as e:
        logger.warning(f"Could not start health check web server on port {port}: {e}")

def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN is missing! Please set it in your .env file.")
        return

    # Build Application
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    # Commands
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("start_teaching", start_teaching_command))
    application.add_handler(CommandHandler("post", admin_post_command))
    application.add_handler(CommandHandler("post_quiz", admin_post_quiz_command))
    application.add_handler(CommandHandler("next_day", admin_next_day_command))
    application.add_handler(CommandHandler("set_day", admin_set_day_command))
    application.add_handler(CommandHandler("pause", admin_pause_command))
    application.add_handler(CommandHandler("resume", admin_resume_command))
    application.add_handler(CommandHandler("announce", admin_announce_command))
    application.add_handler(CommandHandler("status", admin_status_command))
    application.add_handler(CommandHandler("grant_vip", admin_grant_vip_command))
    application.add_handler(CommandHandler("vip_list", admin_vip_list_command))
    application.add_handler(CommandHandler("submissions", admin_submissions_command))

    # Student & Masterclass commands
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("strategy", strategy_command))
    application.add_handler(CommandHandler("unlock_strategy", strategy_command))
    application.add_handler(CommandHandler("my_progress", student_progress_command))
    application.add_handler(CommandHandler("leaderboard", leaderboard_command))
    application.add_handler(CommandHandler("today", student_today_command))
    application.add_handler(CommandHandler("notes", student_notes_command))
    application.add_handler(CommandHandler("certificate", student_certificate_command))

    # Telegram Stars Payments (200 Stars for Ultimate Strategy)
    application.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    # Interactive Inline Button Callbacks
    application.add_handler(CallbackQueryHandler(handle_callback_query))

    # Interactive Quiz Poll Answer Tracking
    application.add_handler(PollAnswerHandler(handle_poll_answer))

    # MT5 Demo Screenshot Homework Submissions (Photos)
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))

    # 24/7 Discussion Group & Question Listener
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_incoming_message))

    # Start lightweight health-check HTTP server (for Hugging Face Spaces / Render Web Services)
    start_health_check_server()

    # Run bot
    print(f"Starting {BOT_NAME} on behalf of the teacher...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
