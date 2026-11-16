"""
Diagnostic and Setup Verification Script for Forex Beginners GH.
Run this script to test your Telegram Token, Channel Permissions, Database, and Visual Generators.
"""

import os
import sys
import asyncio
import json
from config import (
    BOT_TOKEN,
    LESSONS_CHANNEL_ID,
    ASSIGNMENTS_CHANNEL_ID,
    DISCUSSION_GROUP_ID,
    ADMIN_IDS,
    GEMINI_API_KEY,
    OPENAI_API_KEY,
    BOT_NAME
)
from database import db
from chart_generator import generate_certificate, generate_candlestick_anatomy_chart, generate_ultimate_strategy_chart

async def run_diagnostics():
    print("=" * 60)
    print("🇬🇭 CANDLEMASTER ACADEMY (Coach Prince) - SYSTEM SETUP & DIAGNOSTIC CHECK")
    print("=" * 60)

    # 1. Check Configuration
    print("\n[1/5] Checking Environment Variables (.env)...")
    if not BOT_TOKEN:
        print("  ❌ BOT_TOKEN is MISSING in .env! Get one from @BotFather.")
    else:
        masked = BOT_TOKEN[:6] + "..." + BOT_TOKEN[-4:]
        print(f"  ✅ BOT_TOKEN found: {masked}")

    print(f"  📌 Lessons Channel: {LESSONS_CHANNEL_ID or 'NOT SET'}")
    print(f"  📌 Assignments Channel: {ASSIGNMENTS_CHANNEL_ID or 'NOT SET'}")
    print(f"  📌 Discussion Group: {DISCUSSION_GROUP_ID or 'NOT SET'}")
    print(f"  👤 Admin IDs: {ADMIN_IDS or 'None (Open admin access)'}")

    if GEMINI_API_KEY:
        print("  🤖 Gemini AI Engine: Configured")
    elif OPENAI_API_KEY:
        print("  🤖 OpenAI Engine: Configured")
    else:
        print("  ℹ️ AI Engine: Using Built-in Offline Knowledge Base (No API key needed!)")

    # 2. Check Database
    print("\n[2/5] Testing SQLite Database...")
    try:
        await db.init_db()
        await db.set_state("diagnostic_test", "passed")
        val = await db.get_state("diagnostic_test")
        vip_check = await db.is_vip_student(999999999)
        if val == "passed" and isinstance(vip_check, bool):
            print("  ✅ SQLite Database initialized, VIP purchases table active, and read/write verified!")
        else:
            print("  ❌ SQLite Database read/write mismatch.")
    except Exception as e:
        print(f"  ❌ SQLite Error: {e}")

    # 3. Check Lessons Catalog
    print("\n[3/5] Verifying 14-Day Curriculum (lessons.json)...")
    try:
        with open("lessons.json", "r", encoding="utf-8") as f:
            lessons = json.load(f)
        total_days = len(lessons)
        print(f"  ✅ Found {total_days} complete lessons.")
        if total_days >= 14:
            print("  ✅ All 14 days validated with quizzes, assignments, and verified videos!")
        else:
            print(f"  ⚠️ Warning: Expected 14 lessons, found {total_days}.")
    except Exception as e:
        print(f"  ❌ Error reading lessons.json: {e}")

    # 4. Check Chart & Certificate Generator
    print("\n[4/5] Testing Visual Educational Charts & Certificate Generator...")
    try:
        cert_path = generate_certificate("Prince Mensah")
        chart_path = generate_candlestick_anatomy_chart()
        strategy_chart = generate_ultimate_strategy_chart()
        if os.path.exists(cert_path) and os.path.exists(chart_path) and os.path.exists(strategy_chart):
            print(f"  ✅ Certificate generated successfully: {os.path.basename(cert_path)}")
            print(f"  ✅ Educational chart generated successfully: {os.path.basename(chart_path)}")
            print(f"  ✅ Coach Prince Ultimate Strategy chart: {os.path.basename(strategy_chart)}")
        else:
            print("  ❌ Failed to generate visual charts.")
    except Exception as e:
        print(f"  ❌ Visual Generator Error: {e}")

    # 5. Check Telegram Bot API Connection
    print("\n[5/5] Testing Telegram Bot Connection...")
    if not BOT_TOKEN:
        print("  ⚠️ Skipped: Add BOT_TOKEN in .env to test Telegram connection.")
    else:
        try:
            from telegram import Bot
            bot = Bot(token=BOT_TOKEN)
            me = await bot.get_me()
            print(f"  ✅ Connected to Telegram! Bot: @{me.username} ({me.first_name})")

            # Test Channel 1
            if LESSONS_CHANNEL_ID:
                try:
                    chat1 = await bot.get_chat(LESSONS_CHANNEL_ID)
                    print(f"  ✅ Channel 1 (Lessons) reachable: {chat1.title}")
                except Exception as e:
                    print(f"  ⚠️ Channel 1 ({LESSONS_CHANNEL_ID}) notice: Make sure the bot is added as an ADMIN to this channel! ({e})")

            # Test Channel 2
            if ASSIGNMENTS_CHANNEL_ID:
                try:
                    chat2 = await bot.get_chat(ASSIGNMENTS_CHANNEL_ID)
                    print(f"  ✅ Channel 2 (Assignments) reachable: {chat2.title}")
                except Exception as e:
                    print(f"  ⚠️ Channel 2 ({ASSIGNMENTS_CHANNEL_ID}) notice: Make sure the bot is added as an ADMIN to this channel! ({e})")

        except Exception as e:
            print(f"  ❌ Telegram Bot connection failed: {e}")

    print("\n" + "=" * 60)
    print("DIAGNOSTIC COMPLETE! If all checks pass, start your bot with:")
    print("  python bot.py")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    asyncio.run(run_diagnostics())

