"""
Database management module for Forex Beginners GH.
Uses SQLite with thread-safe async helper methods.
"""

import os
import sqlite3
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any
from config import DB_PATH

class Database:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    async def init_db(self):
        """Creates tables and indexes if they do not exist."""
        def _sync_init():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                # Students table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        full_name TEXT,
                        level TEXT DEFAULT 'Total Beginner',
                        current_day INTEGER DEFAULT 1,
                        registered_at TEXT,
                        last_active_at TEXT,
                        is_active INTEGER DEFAULT 1
                    )
                """)

                # Quiz attempts
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS quiz_attempts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        day INTEGER,
                        question_idx INTEGER,
                        selected_option INTEGER,
                        is_correct INTEGER,
                        attempted_at TEXT,
                        UNIQUE(user_id, day, question_idx)
                    )
                """)

                # Assignment submissions
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS assignment_submissions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        day INTEGER,
                        submission_text TEXT,
                        status TEXT DEFAULT 'Submitted',
                        submitted_at TEXT
                    )
                """)

                # Question logs (for research & identifying tricky topics)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS question_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        username TEXT,
                        chat_id TEXT,
                        chat_type TEXT,
                        question_text TEXT,
                        bot_response TEXT,
                        topic TEXT,
                        student_understood INTEGER DEFAULT NULL,
                        created_at TEXT
                    )
                """)

                # Bot state key-value store (current active day, auto-post pause, etc.)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS bot_state (
                        key TEXT PRIMARY KEY,
                        value TEXT
                    )
                """)

                # VIP Purchases table (Telegram Stars 200 for Coach Prince's Ultimate Strategy)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS vip_purchases (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER UNIQUE,
                        username TEXT,
                        amount_stars INTEGER DEFAULT 200,
                        telegram_charge_id TEXT,
                        purchased_at TEXT,
                        is_vip INTEGER DEFAULT 1
                    )
                """)

                # Active Polls mapping table (to accurately track quiz scores from channels)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS active_polls (
                        poll_id TEXT PRIMARY KEY,
                        day INTEGER,
                        question_idx INTEGER,
                        correct_option_id INTEGER,
                        created_at TEXT
                    )
                """)

                # Set initial state if empty or respect CURRENT_DAY environment variable
                env_day = os.getenv("CURRENT_DAY", "").strip()
                if env_day.isdigit() and 1 <= int(env_day) <= 14:
                    cursor.execute("""
                        INSERT INTO bot_state (key, value) VALUES ('current_day', ?)
                        ON CONFLICT(key) DO UPDATE SET value = ?
                    """, (env_day, env_day))
                else:
                    cursor.execute("INSERT OR IGNORE INTO bot_state (key, value) VALUES ('current_day', '1')")
                cursor.execute("INSERT OR IGNORE INTO bot_state (key, value) VALUES ('auto_post_paused', '0')")
                conn.commit()

        await asyncio.to_thread(_sync_init)

    # ---------------- Student Operations ---------------- #

    async def register_student(self, user_id: int, username: Optional[str], full_name: str, level: str = "Total Beginner") -> bool:
        """Registers a new student or updates existing student record."""
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO students (user_id, username, full_name, level, current_day, registered_at, last_active_at, is_active)
                    VALUES (?, ?, ?, ?, 1, ?, ?, 1)
                    ON CONFLICT(user_id) DO UPDATE SET
                        username = excluded.username,
                        full_name = excluded.full_name,
                        last_active_at = excluded.last_active_at,
                        is_active = 1
                """, (user_id, username, full_name, level, now, now))
                conn.commit()
                return True
        return await asyncio.to_thread(_sync)

    async def get_student(self, user_id: int) -> Optional[Dict[str, Any]]:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE user_id = ?", (user_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
        return await asyncio.to_thread(_sync)

    async def update_student_activity(self, user_id: int, day: Optional[int] = None):
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                if day is not None:
                    cursor.execute("""
                        UPDATE students 
                        SET last_active_at = ?, current_day = MAX(current_day, ?)
                        WHERE user_id = ?
                    """, (now, day, user_id))
                else:
                    cursor.execute("UPDATE students SET last_active_at = ? WHERE user_id = ?", (now, user_id))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_all_students(self, active_only: bool = True) -> List[Dict[str, Any]]:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                if active_only:
                    cursor.execute("SELECT * FROM students WHERE is_active = 1")
                else:
                    cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()
                return [dict(r) for r in rows]
        return await asyncio.to_thread(_sync)

    # ---------------- Quiz Operations ---------------- #

    async def record_quiz_attempt(self, user_id: int, day: int, question_idx: int, selected_option: int, is_correct: bool):
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO quiz_attempts (user_id, day, question_idx, selected_option, is_correct, attempted_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(user_id, day, question_idx) DO UPDATE SET
                        selected_option = excluded.selected_option,
                        is_correct = excluded.is_correct,
                        attempted_at = excluded.attempted_at
                """, (user_id, day, question_idx, selected_option, 1 if is_correct else 0, now))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_student_quiz_stats(self, user_id: int) -> Dict[str, Any]:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT COUNT(*) as total_attempts,
                           SUM(is_correct) as correct_answers,
                           COUNT(DISTINCT day) as days_quizzed
                    FROM quiz_attempts
                    WHERE user_id = ?
                """, (user_id,))
                row = cursor.fetchone()
                total = row["total_attempts"] or 0
                correct = row["correct_answers"] or 0
                days = row["days_quizzed"] or 0
                pct = (correct / total * 100) if total > 0 else 0.0
                return {
                    "total_attempts": total,
                    "correct_answers": correct,
                    "days_quizzed": days,
                    "accuracy_pct": round(pct, 1)
                }
        return await asyncio.to_thread(_sync)

    async def get_student_day_quiz_score(self, user_id: int, day: int) -> Dict[str, Any]:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT COUNT(*) as total, SUM(is_correct) as correct
                    FROM quiz_attempts
                    WHERE user_id = ? AND day = ?
                """, (user_id, day))
                row = cursor.fetchone()
                return {
                    "total": row["total"] or 0,
                    "correct": row["correct"] or 0
                }
        return await asyncio.to_thread(_sync)

    # ---------------- Assignment Operations ---------------- #

    async def record_assignment_submission(self, user_id: int, day: int, text: str):
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO assignment_submissions (user_id, day, submission_text, status, submitted_at)
                    VALUES (?, ?, ?, 'Submitted', ?)
                """, (user_id, day, text, now))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_student_assignment_count(self, user_id: int) -> int:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT COUNT(DISTINCT day) as completed_assignments
                    FROM assignment_submissions
                    WHERE user_id = ?
                """, (user_id,))
                row = cursor.fetchone()
                return row["completed_assignments"] or 0
        return await asyncio.to_thread(_sync)

    # ---------------- Question & Discussion Logs ---------------- #

    async def log_question(self, user_id: int, username: Optional[str], chat_id: str, chat_type: str, 
                           question_text: str, bot_response: str, topic: str = "General") -> int:
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO question_logs (user_id, username, chat_id, chat_type, question_text, bot_response, topic, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (user_id, username, str(chat_id), chat_type, question_text, bot_response, topic, now))
                conn.commit()
                return cursor.lastrowid
        return await asyncio.to_thread(_sync)

    async def update_question_understanding(self, log_id: int, understood: bool):
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE question_logs
                    SET student_understood = ?
                    WHERE id = ?
                """, (1 if understood else 0, log_id))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_latest_question_for_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM question_logs
                    WHERE user_id = ?
                    ORDER BY id DESC LIMIT 1
                """, (user_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
        return await asyncio.to_thread(_sync)

    async def get_hardest_topics(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Identifies topics where students had the most questions or replied NO."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT topic, COUNT(*) as question_count,
                           SUM(CASE WHEN student_understood = 0 THEN 1 ELSE 0 END) as confused_count
                    FROM question_logs
                    GROUP BY topic
                    ORDER BY question_count DESC
                    LIMIT ?
                """, (limit,))
                rows = cursor.fetchall()
                return [dict(r) for r in rows]
        return await asyncio.to_thread(_sync)

    # ---------------- System State (Curriculum Day & Pauses) ---------------- #

    async def get_state(self, key: str, default: str = "") -> str:
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT value FROM bot_state WHERE key = ?", (key,))
                row = cursor.fetchone()
                return row["value"] if row else default
        return await asyncio.to_thread(_sync)

    async def set_state(self, key: str, value: str):
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO bot_state (key, value) VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value = excluded.value
                """, (key, value))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_system_stats(self) -> Dict[str, Any]:
        """Aggregate stats for /stats command."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) as total_students FROM students")
                total_students = cursor.fetchone()["total_students"] or 0

                cursor.execute("SELECT COUNT(*) as active_students FROM students WHERE is_active = 1")
                active_students = cursor.fetchone()["active_students"] or 0

                cursor.execute("""
                    SELECT COUNT(*) as total_quizzes, 
                           SUM(is_correct) as correct_quizzes 
                    FROM quiz_attempts
                """)
                q_row = cursor.fetchone()
                t_q = q_row["total_quizzes"] or 0
                c_q = q_row["correct_quizzes"] or 0
                avg_score = round((c_q / t_q * 100), 1) if t_q > 0 else 0.0

                cursor.execute("SELECT COUNT(*) as total_questions FROM question_logs")
                total_questions = cursor.fetchone()["total_questions"] or 0

                cursor.execute("SELECT COUNT(*) as total_assignments FROM assignment_submissions")
                total_assignments = cursor.fetchone()["total_assignments"] or 0

                cursor.execute("SELECT COUNT(*) as total_vips FROM vip_purchases WHERE is_vip = 1")
                total_vips = cursor.fetchone()["total_vips"] or 0

                return {
                    "total_students": total_students,
                    "active_students": active_students,
                    "total_quizzes_taken": t_q,
                    "quiz_accuracy_pct": avg_score,
                    "total_questions_asked": total_questions,
                    "total_assignments_submitted": total_assignments,
                    "total_vip_students": total_vips
                }
        return await asyncio.to_thread(_sync)

    # ---------------- VIP Strategy Purchase (Telegram Stars) ---------------- #

    async def record_vip_purchase(self, user_id: int, username: Optional[str], amount_stars: int = 200, charge_id: str = "") -> bool:
        """Records a successful Telegram Stars purchase of Coach Prince's Ultimate Strategy."""
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO vip_purchases (user_id, username, amount_stars, telegram_charge_id, purchased_at, is_vip)
                    VALUES (?, ?, ?, ?, ?, 1)
                    ON CONFLICT(user_id) DO UPDATE SET
                        username = excluded.username,
                        amount_stars = excluded.amount_stars,
                        telegram_charge_id = excluded.telegram_charge_id,
                        purchased_at = excluded.purchased_at,
                        is_vip = 1
                """, (user_id, username, amount_stars, charge_id, now))
                conn.commit()
                return True
        return await asyncio.to_thread(_sync)

    async def is_vip_student(self, user_id: int) -> bool:
        """Checks if a student has unlocked Coach Prince's Ultimate Strategy."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT is_vip FROM vip_purchases WHERE user_id = ? AND is_vip = 1", (user_id,))
                row = cursor.fetchone()
                return bool(row)
        return await asyncio.to_thread(_sync)

    async def get_all_vip_students(self) -> List[Dict[str, Any]]:
        """Returns all students who purchased the Ultimate Strategy."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vp.*, s.full_name
                    FROM vip_purchases vp
                    LEFT JOIN students s ON vp.user_id = s.user_id
                    WHERE vp.is_vip = 1
                    ORDER BY vp.id DESC
                """)
                rows = cursor.fetchall()
                return [dict(r) for r in rows]
        return await asyncio.to_thread(_sync)

    async def grant_vip_access(self, user_id: int, username: Optional[str] = "Granted by Owner") -> bool:
        """Allows Boss Prince to manually grant VIP access to a student."""
        return await self.record_vip_purchase(user_id=user_id, username=username, amount_stars=200, charge_id="MANUAL_GRANT")

    # ---------------- Active Polls Mapping & Leaderboard ---------------- #

    async def register_poll(self, poll_id: str, day: int, question_idx: int, correct_option_id: int):
        """Maps a Telegram poll ID to its curriculum day and correct answer."""
        now = datetime.utcnow().isoformat()
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO active_polls (poll_id, day, question_idx, correct_option_id, created_at)
                    VALUES (?, ?, ?, ?, ?)
                """, (poll_id, day, question_idx, correct_option_id, now))
                conn.commit()
        await asyncio.to_thread(_sync)

    async def get_poll_info(self, poll_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves question and correct answer for a Telegram poll ID."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM active_polls WHERE poll_id = ?", (poll_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
        return await asyncio.to_thread(_sync)

    async def get_submissions_for_day(self, day: int, limit: int = 20) -> List[Dict[str, Any]]:
        """Retrieves student assignment submissions for a specific day."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT sub.*, s.full_name, s.username
                    FROM assignment_submissions sub
                    LEFT JOIN students s ON sub.user_id = s.user_id
                    WHERE sub.day = ?
                    ORDER BY sub.id DESC
                    LIMIT ?
                """, (day, limit))
                rows = cursor.fetchall()
                return [dict(r) for r in rows]
        return await asyncio.to_thread(_sync)

    async def get_leaderboard(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Returns top students by quiz performance and assignment participation."""
        def _sync():
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT s.user_id, s.full_name, s.username,
                           COUNT(DISTINCT q.id) as total_quizzes,
                           SUM(CASE WHEN q.is_correct = 1 THEN 1 ELSE 0 END) as correct_answers,
                           COUNT(DISTINCT a.id) as total_assignments
                    FROM students s
                    LEFT JOIN quiz_attempts q ON s.user_id = q.user_id
                    LEFT JOIN assignment_submissions a ON s.user_id = a.user_id
                    GROUP BY s.user_id
                    HAVING total_quizzes > 0 OR total_assignments > 0
                    ORDER BY correct_answers DESC, total_assignments DESC
                    LIMIT ?
                """, (limit,))
                rows = cursor.fetchall()
                return [dict(r) for r in rows]
        return await asyncio.to_thread(_sync)

# Global instance
db = Database()

