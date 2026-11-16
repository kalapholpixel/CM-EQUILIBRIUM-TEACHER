"""
Configuration module for Forex Beginners GH - AI Teacher Bot.
Loads environment variables and defines system constants.
"""

import os
from typing import List
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Telegram Credentials
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "").strip()

# Telegram Channels & Group IDs (or @channel_usernames)
# Channel 1: Lessons Channel (Only bot posts lessons)
LESSONS_CHANNEL_ID: str = os.getenv("LESSONS_CHANNEL_ID", "@ForexLessonsGH").strip()

# Channel 2: Assignments Channel (Only bot posts assignments and corrections)
ASSIGNMENTS_CHANNEL_ID: str = os.getenv("ASSIGNMENTS_CHANNEL_ID", "@ForexAssignmentsGH").strip()

# Group: Discussion Group (Linked to Channel 1, students ask questions)
DISCUSSION_GROUP_ID: str = os.getenv("DISCUSSION_GROUP_ID", "").strip()

# Admin Telegram User IDs (comma-separated if multiple)
ADMIN_IDS_RAW: str = os.getenv("ADMIN_IDS", "").strip()
ADMIN_IDS: List[int] = []
if ADMIN_IDS_RAW:
    for admin_id_str in ADMIN_IDS_RAW.split(","):
        admin_id_str = admin_id_str.strip()
        if admin_id_str.isdigit():
            ADMIN_IDS.append(int(admin_id_str))

# AI Engine Credentials (either Gemini or OpenAI)
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "").strip()

# Database Path
DB_PATH: str = os.getenv("DB_PATH", "forex_teacher.db").strip()

# Timezone (Ghana is GMT / UTC+0 year-round)
TIMEZONE: str = os.getenv("TIMEZONE", "Africa/Accra").strip()

# Bot & Academy Identity
BOT_NAME: str = "Coach Prince (Forex Teacher)"
SCHOOL_NAME: str = "Candlemaster Academy"
PROJECT_NAME: str = "Candlemaster Academy - Forex AI Teacher"

# Mandatory Safety Disclaimer
DISCLAIMER_TEXT: str = (
    "⚠️ *EDUCATIONAL DISCLAIMER:*\n"
    "Forex trading carries significant risk of loss. Never trade with money you cannot afford "
    "to lose (chop money, rent, or school fees). At Candlemaster Academy, Coach Prince is here to teach you "
    "the truth about the market—we NEVER give trading signals, NEVER ask for your MoMo PIN, and NEVER "
    "tell you to deposit real money until you master demo trading."
)

