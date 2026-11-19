"""
Coach Prince AI Teacher & Research Engine for Forex Beginners GH.
Handles human-like 3-step teaching, anti-scam guardrails, re-explanations,
and intelligent fallback research.
"""

import os
import json
import logging
import asyncio
from typing import Dict, Any, Optional, Tuple
from config import GEMINI_API_KEY, OPENAI_API_KEY, BOT_NAME, DISCLAIMER_TEXT

logger = logging.getLogger(__name__)

# Initialize AI Clients if keys are available
_gemini_model = None
_openai_client = None

if GEMINI_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        _gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        logger.info("Google Gemini model initialized successfully.")
    except Exception as e:
        logger.warning(f"Could not initialize Gemini: {e}")

if OPENAI_API_KEY:
    try:
        from openai import OpenAI
        _openai_client = OpenAI(api_key=OPENAI_API_KEY)
        logger.info("OpenAI client initialized successfully.")
    except Exception as e:
        logger.warning(f"Could not initialize OpenAI: {e}")

COACH_PRINCE_SYSTEM_PROMPT = f"""
You are {BOT_NAME}, an experienced, warm, fatherly, and patient Ghanaian Forex teacher for 'Candlemaster Academy'.
Your mission is to teach total beginners (SHS students, university youth, and beginners in Ghana) how the financial markets work from zero to hero.

CRITICAL RULES:
1. TONE: Warm, patient, humble, friendly, encouraging, like a dedicated Ghanaian teacher.
2. LANGUAGE: Simple, clear English. Explain every technical term immediately.
3. GHANAIAN EXAMPLES: Use relatable Ghanaian analogies in every explanation (Ghana Cedis GHS, US Dollars, Makola market woman, Kejetia, Trotro fares, MTN Mobile Money MoMo, Circle Forex Bureau).
4. ABSOLUTE PROHIBITIONS:
   - NEVER give trading signals ("Buy EURUSD now").
   - NEVER encourage anyone to deposit real money or promise profits ("You will make $100/day").
   - NEVER ask for passwords, MoMo PINs, or broker credentials.
   - If asked about signals, doubling money, or deposits, firmly but gently reply:
     "We don't do that here. In Candlemaster Academy, we learn to protect our money first. Let's focus on today's lesson."
5. THE LANGUAGE OF THE MARKET:
   - Emphasize reading the true language of the market: Candlesticks (rejection wicks, buyers vs sellers), Market Structure (Higher Highs/Lows, Lower Lows/Highs), Break of Structure (BOS), Change of Character (CHoCH), Order Blocks (Supply & Demand), and Fair Value Gaps (FVG).
6. COACH PRINCE'S ULTIMATE STRATEGY (MASTERCLASS):
   - Your signature trading system is 'Coach Prince's Ultimate Strategy: Top-Down Multi-Timeframe Execution & POI Sniping' (Daily Macro Bias -> 4H Structure Refinement -> 1H Internal FVG Scouting -> 15M Execution Trap).
   - Students learn the fundamentals for 14 days for free. On Day 14, they can unlock the full Ultimate Strategy Masterclass for 200 Telegram Stars by sending /strategy in private chat.
7. 3-STEP TEACHING METHOD FOR QUESTIONS:
   Whenever a student asks a question, structure your answer into 3 distinct sections:
   1️⃣ Simple Answer: Direct, jargon-free explanation.
   2️⃣ Real-life Ghana Example: An everyday story (market woman, trotro, forex bureau).
   3️⃣ Check Understanding: Always end with: "Does that make sense to you? Type YES or NO."
8. RE-EXPLANATIONS:
   If the student replies "NO" or "I don't understand", NEVER repeat what you said. Apologize warmly for not being clear enough, and explain using a totally new, even simpler analogy.
"""

# Built-in Fallback Knowledge Base (Active even with NO API keys configured)
FALLBACK_KNOWLEDGE_BASE = {
    "what_is_forex": {
        "keywords": ["what is forex", "forex mean", "fx mean", "explain forex", "how does forex work"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "Forex means **Foreign Exchange**. It is simply buying one country's currency while selling another's, "
            "because the exchange rate between them is always moving.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "Think of your brother coming from London with £100 Pounds. He goes to the Forex Bureau at Circle "
            "and changes it to Cedis. The Bureau gives him 19 GHS per Pound. If the Pound becomes stronger tomorrow "
            "at 20 GHS, those who held Pounds made a profit. In digital Forex, you trade that exact price change on your phone!\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "pips": {
        "keywords": ["what is pip", "pips", "how to calculate pip", "pip count"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "A **PIP** (Percentage In Point) is the tiny unit used to measure how far a currency price has moved. "
            "On most pairs like EUR/USD, it is the **4th decimal number** (0.0001).\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "Imagine a loaf of bread costs 10 Cedis and 50 Pesewas. If it increases by 1 Pesewa to 10.51, "
            "that 1 Pesewa shift is like 1 pip in Forex! When EUR/USD moves from 1.0850 to 1.0860, it moved 10 pips.\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "lot_size": {
        "keywords": ["lot size", "micro lot", "standard lot", "what lot", "0.01"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "A **Lot Size** is the volume or quantity of currency you are trading. It controls how much money "
            "you win or lose for every single pip the price moves.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "If you go to Makola and buy 1 tin of milk, your risk is small. If the price drops by 1 Cedi, you only lose 1 Cedi. "
            "That is like a **0.01 Micro Lot** ($0.10 per pip). But if you foolishly buy 1,000 cartons on credit (**1.00 Standard Lot**), "
            "a small price drop will wipe you out! Beginners must ALWAYS stick to 0.01.\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "stop_loss": {
        "keywords": ["stop loss", "what is sl", "sl", "protect money", "take profit", "tp"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "A **Stop Loss (SL)** is an automatic emergency brake that closes your trade if the market goes against you, "
            "protecting the rest of your money. **Take Profit (TP)** automatically locks in your gains when price reaches your goal.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "When you enter a Trotro, you put on your seatbelt (Stop Loss) so you are safe if there is a sudden stop. "
            "And you tell the mate: 'Drop me at Madina Zongo Junction' (Take Profit). You don't ride past your destination!\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "best_time": {
        "keywords": ["best time", "what time", "sessions", "ghana time", "when to trade"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "The best time to trade Forex in Ghana is from **1:00 PM to 4:00 PM GMT**.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "If you go to Kejetia market at midnight, the gates are locked and you can't buy anything. "
            "Between 1 PM and 4 PM Ghana time, the banks in London and the banks in New York are BOTH open at the same time! "
            "Billions of dollars are moving, so price moves cleanly with low trading fees.\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "deposit_money": {
        "keywords": ["deposit", "how much to start", "real money", "live account", "momo deposit"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "Right now, do NOT deposit any real money! In **Candlemaster Academy**, we trade strictly on our **Demo account** "
            "for at least 30 to 60 days until our strategy and discipline are proven.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "You cannot learn how to drive a car for 3 days and then enter a Formula 1 race! Practice on the driving simulator first. "
            "When you are ready after Day 14, you can start live with just $50 to $100 chop money you can afford to lose.\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "ultimate_strategy": {
        "keywords": ["ultimate strategy", "coach prince strategy", "top down analysis", "top-down", "200 stars", "how to unlock strategy", "secret strategy", "poi"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "**Coach Prince's Ultimate Strategy** is a multi-timeframe execution system: "
            "We use the **Daily (D1)** chart for Macro Bias, **4-Hour (H4)** for structure refinement, "
            "**1-Hour (H1)** to scout Fair Value Gaps (FVG) and unmitigated zones, and the **15-Minute (M15)** "
            "to set high-precision entry traps with tight Stop Loss and 1:3 to 1:5+ Risk:Reward!\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "Think of a police checkpoint on the Accra-Kumasi highway. The police don't chase every speeding car on foot; "
            "they set a well-planned checkpoint at a narrow toll gate and wait for the cars to come to them! That is how we set traps on the 15M chart.\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Type `/strategy` in private chat with Coach Prince to unlock the full Masterclass for 200 Telegram Stars!"
        )
    },
    "market_structure": {
        "keywords": ["market structure", "bos", "break of structure", "choch", "change of character", "language of the market"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "Market structure is the true language of price. **BOS (Break of Structure)** means the current trend is continuing "
            "(making Higher Highs or Lower Lows). **CHoCH (Change of Character)** is the very first warning that buyers or sellers have surrendered and a reversal is starting!\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "Imagine a Trotro traveling from Accra to Kumasi. Every bus stop it passes without turning back is a BOS (continuing journey). "
            "If the driver suddenly makes a sharp U-turn back to Accra, that U-turn is a CHoCH!\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    },
    "order_block_fvg": {
        "keywords": ["order block", "fvg", "fair value gap", "imbalance", "mitigation", "unmitigated"],
        "answer": (
            "1️⃣ *Simple Answer:*\n"
            "An **Order Block (OB)** is the institutional footprint where banks placed massive orders. "
            "A **Fair Value Gap (FVG)** is an imbalance in price delivery. Fresh **Unmitigated** order blocks hold price like a fortress, "
            "while already **Mitigated** zones are weak and likely to break.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "If a cement vendor has 500 bags reserved for an estate contractor, that warehouse is an Order Block. "
            "Once all 500 bags are collected (mitigated), the warehouse is empty and cannot protect price anymore!\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
    }
}

class AITeacher:
    def __init__(self):
        self.gemini = _gemini_model
        self.openai = _openai_client

    def is_scam_or_signal_request(self, text: str) -> bool:
        """Detects if a user is asking for trading signals, VIP groups, or get-rich-quick methods."""
        lowered = text.lower()
        keywords = [
            "signal", "signals", "vip group", "double my money", "double money",
            "make money fast", "ponzi", "investment plan", "guaranteed profit",
            "deposit money", "deposit real", "real money deposit", "make 1000 cedis",
            "get rich", "trade for me", "account management"
        ]
        return any(kw in lowered for kw in keywords)

    async def answer_question(self, user_name: str, question: str, previous_context: Optional[str] = None) -> Tuple[str, str]:
        """
        Answers a student's question in Coach Prince's 3-step format.
        Returns: (bot_response_text, detected_topic)
        """
        clean_name = user_name.strip() if user_name else "Student"

        # Check Anti-Scam / Anti-Signal guardrail
        if self.is_scam_or_signal_request(question):
            response = (
                f"@{clean_name}, Coach Prince here.\n\n"
                "We don't do that here! In **Candlemaster Academy**, we are here to build real lifetime trading skills, "
                "not to gamble or sell signals. Anyone promising you guaranteed profits or asking you to send MoMo "
                "for VIP signals is trying to empty your pocket.\n\n"
                "Let us stay disciplined and focus on today's lesson. Does that make sense? Reply with **YES** or **NO**."
            )
            return response, "Anti-Signal Guardrail"

        # Try AI generation first if Gemini or OpenAI is configured
        ai_response = await self._generate_ai_response(clean_name, question, previous_context)
        if ai_response:
            return ai_response, "AI Research & Teaching"

        # Fallback to Built-in Knowledge Base
        q_lowered = question.lower()
        for topic_key, data in FALLBACK_KNOWLEDGE_BASE.items():
            for kw in data["keywords"]:
                if kw in q_lowered:
                    response = f"@{clean_name}, good question!\n\n" + data["answer"]
                    return response, topic_key

        # Generic intelligent Coach Prince response
        default_response = (
            f"@{clean_name}, Coach Prince here.\n\n"
            "1️⃣ *Simple Answer:*\n"
            f"Good question regarding '{question}'. In Forex, every price movement reflects the supply and demand "
            "between major global banks and commercial traders.\n\n"
            "2️⃣ *Real-Life Ghana Example:*\n"
            "Think of buying tomatoes at Makola market: When a new truck arrives from Burkina Faso, tomatoes are plentiful, "
            "so the price drops (Sellers' market). When tomatoes are scarce during dry season, the market women charge more (Buyers' market).\n\n"
            "3️⃣ *Check Understanding:*\n"
            "Does that make sense to you? Reply with **YES** or **NO**."
        )
        return default_response, "General Forex"

    async def re_explain(self, user_name: str, original_question: Optional[str] = None) -> str:
        """
        Provides an alternative, even simpler explanation when a student types 'NO' or 'I don't understand'.
        """
        clean_name = user_name.strip() if user_name else "My friend"

        if self.gemini:
            try:
                prompt = (
                    f"Student {clean_name} said 'NO' or 'I do not understand' to the previous explanation of: {original_question or 'the forex concept'}.\n"
                    "As Coach Prince, apologize warmly for not being clear enough. Do NOT repeat previous words. "
                    "Use a totally different, ultra-simple Ghanaian analogy (like buying trotro fuel, sending MoMo with e-levy, or selling fried plantain). "
                    "Keep it short and finish with: 'Does this new example make it clearer for you? Reply YES or NO.'"
                )
                res = await asyncio.to_thread(self.gemini.generate_content, prompt)
                if res and res.text:
                    return f"@{clean_name}, don't worry at all! A good teacher never tires of explaining.\n\n" + res.text.strip()
            except Exception as e:
                logger.warning(f"Gemini re-explain error: {e}")

        # Built-in re-explanation fallback
        return (
            f"@{clean_name}, don't worry at all! A patient teacher never tires of explaining.\n\n"
            "Let me put it in a completely different way:\n\n"
            "Imagine you want to buy a pair of sneakers at Kantamanto Market. The vendor says 200 Cedis. "
            "You negotiate down to 180 Cedis because you believe you can sell it to your friend in school for 220 Cedis. "
            "That 40 Cedi difference is your profit for doing the exchange!\n\n"
            "In Forex, we don't carry physical shoes—we simply exchange currencies right on our smartphone screen when the exchange rate shifts.\n\n"
            "Does this new example make it clearer for you? Reply **YES** or **NO**."
        )

    async def _generate_ai_response(self, user_name: str, question: str, previous_context: Optional[str]) -> Optional[str]:
        """Calls Gemini or OpenAI to synthesize a human-like response asynchronously."""
        user_prompt = f"Student Name: @{user_name}\nStudent Question: {question}\n"
        if previous_context:
            user_prompt += f"Recent Chat Context: {previous_context}\n"

        # Try Gemini (non-blocking)
        if self.gemini:
            try:
                full_prompt = f"{COACH_PRINCE_SYSTEM_PROMPT}\n\n{user_prompt}"
                response = await asyncio.to_thread(self.gemini.generate_content, full_prompt)
                if response and response.text:
                    return response.text.strip()
            except Exception as e:
                logger.warning(f"Gemini generation error: {e}")

        # Try OpenAI (non-blocking)
        if self.openai:
            try:
                def _call_openai():
                    return self.openai.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": COACH_PRINCE_SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=0.7,
                        max_tokens=600
                    )
                completion = await asyncio.to_thread(_call_openai)
                if completion and completion.choices:
                    text = completion.choices[0].message.content
                    if text:
                        return text.strip()
            except Exception as e:
                logger.warning(f"OpenAI generation error: {e}")

        return None

# Global instance
ai_teacher = AITeacher()
