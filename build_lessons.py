"""
Builder script to generate lessons.json for Forex Beginners GH.
Contains all 14 comprehensive, human-like Ghanaian Forex lessons.
"""

import json

lessons_data = {
    "1": {
        "day": 1,
        "topic": "What is Forex? - Buying One Currency, Selling Another",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we begin our journey together: *Day 1: What is Forex?*\n"
            "We will explore how changing money at the Circle or Kejetia forex bureau is exactly "
            "how the global financial market works.\n\n"
            "Get your pens and notebooks ready. No noise today, pure foundational knowledge! 🇬🇭📖"
        ),
        "hook": "Have you ever walked past a Forex Bureau at Kwame Nkrumah Circle or Kejetia Market in Kumasi and wondered how they make money?",
        "lesson_text": (
            "Good evening class, today we learn: *What is Forex?*\n\n"
            "🎯 *1. THE HOOK: The Forex Bureau Story*\n"
            "Imagine your brother travels from the UK to Accra. When he arrives at Kotoka Airport, "
            "he holds British Pounds (£), but he cannot buy Waakye with Pounds! So he visits a Forex Bureau. "
            "He sells his Pounds and receives Ghana Cedis (GHS).\n"
            "Two weeks later, the Cedi weakens against the Pound. If the bureau buys at 19 GHS and sells at 20 GHS, "
            "that difference is their profit. *That is FOREX!*\n\n"
            "💡 *2. THE EXPLANATION: Breaking Down the Big Words*\n"
            "• **Forex** stands for **Foreign Exchange** (changing one nation's currency into another).\n"
            "• In the Forex market, currencies are traded in **PAIRS** (e.g., EUR/USD, GBP/USD, USD/GHS).\n"
            "• Whenever you trade, you are *simultaneously buying one currency and selling another*.\n"
            "• It is the largest financial market in the entire world, trading over *$7.5 Trillion* every single day. "
            "That is bigger than all the stock markets in America combined!\n\n"
            "📊 *3. REAL EXAMPLE WITH NUMBERS*\n"
            "Let's look at the **EUR/USD** pair:\n"
            "• Price = 1.0850. This means **1 Euro (€) costs 1.0850 US Dollars ($)**.\n"
            "• If you expect the Euro to gain strength against the Dollar, you **BUY**.\n"
            "• If the price rises to 1.0900, you close your trade and keep the difference as your profit.\n"
            "• If the Euro drops to 1.0800 instead, you take a loss.\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "You don't need millions of Cedis or a physical shop to trade Forex today. With an internet connection "
            "and a smartphone, you can participate right from your room. But remember: Forex is a skill, not a lottery ticket!\n\n"
            "Stay humble, focus on learning, and let's build your financial discipline step-by-step. God bless your effort!"
        ),
        "calculation_example": (
            "🔢 *Step-by-Step Currency Calculation:*\n"
            "• You hold $100 USD.\n"
            "• Today's exchange rate: 1 USD = 15.00 GHS.\n"
            "• You convert: 100 × 15.00 = 1,500 GHS.\n"
            "• Next month, rate moves to 1 USD = 16.00 GHS.\n"
            "• If you convert your 1,500 GHS back to USD at 15.00 cost, your capital's purchasing power shifted! "
            "In digital Forex, we trade these decimal movements without touching physical bank notes."
        ),
        "voice_script": (
            "Good evening students! Coach Prince here. In tonight's lesson, I want you to discard any fairy tale "
            "about getting rich overnight. Forex is simply foreign exchange—just like the bureau at Circle. "
            "We buy when a currency is cheap and sell when it is valuable. Watch the video below carefully, "
            "take your notes, and attempt tonight's quiz!"
        ),
        "image_type": "forex_bureau_exchange",
        "video_title": "Forex Trading For Beginners - What is Forex? (BabyPips)",
        "video_url": "https://www.youtube.com/watch?v=F18oW2c3cEU",
        "video_duration": "6 mins",
        "video_reason": "Clear, cartoon-style beginner visual explanation with zero get-rich-quick hype.",
        "notes_summary": (
            "📌 *Day 1 Key Takeaways Cheatsheet:*\n"
            "1. Forex = Foreign Exchange (trading currencies globally).\n"
            "2. Traded in PAIRS: Base Currency (first) / Quote Currency (second).\n"
            "3. Market volume: Over $7.5 Trillion daily.\n"
            "4. You make profit when price moves in your predicted direction.\n"
            "5. Rule #1: This is a professional business, not gambling!"
        ),
        "assignment": (
            "🎯 *DAY 1 ASSIGNMENT: Your First Currency Observation*\n\n"
            "Task: Check today's official exchange rate between the Ghana Cedi (GHS) and the US Dollar (USD).\n"
            "1. Find out how many Cedis buy 1 US Dollar today at your local bank or Google.\n"
            "2. Calculate: If you had $50 USD today, how many Cedis would you receive?\n"
            "3. In 2 simple sentences, write why you want to learn Forex trading.\n\n"
            "📤 *How to Submit:* Reply directly to Coach Prince in private chat or write it in your notebook!\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Gentle Reminder from Coach Prince!*\n\n"
            "Have you completed Day 1's assignment? Take 5 minutes before bed to check the USD/GHS rate "
            "and write your answers. Consistency is how master traders are made. Submit your answers!"
        ),
        "correction": (
            "✅ *DAY 1 ASSIGNMENT CORRECTION & TEACHER REVIEW*\n\n"
            "Good afternoon class! Let us review yesterday's assignment:\n"
            "• If 1 USD = 15.20 GHS, then $50 USD = 50 × 15.20 = 760.00 GHS.\n\n"
            "⚠️ *Common Beginner Mistake:*\n"
            "Many students mix up the Base and Quote currency. Remember: In USD/GHS, USD is the BASE currency (unit of 1) "
            "and GHS is the QUOTE currency (how many cedis you need to buy 1 dollar).\n"
            "Great job to everyone who submitted!"
        ),
        "quizzes": [
            {
                "question": "What does the word 'Forex' stand for?",
                "options": [
                    "Foreign Exchange",
                    "Forward Execution",
                    "Formal Export",
                    "Fortune Extension"
                ],
                "correct_idx": 0,
                "explanation": "Correct! Forex stands for Foreign Exchange—the global buying and selling of world currencies."
            },
            {
                "question": "In the currency pair EUR/USD, which currency is the 'Base' currency?",
                "options": [
                    "USD (US Dollar)",
                    "EUR (Euro)",
                    "Both of them",
                    "Neither"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! The first currency listed in any pair is always the Base currency. EUR is the base here."
            },
            {
                "question": "If EUR/USD is priced at 1.0850, what does it mean?",
                "options": [
                    "1 US Dollar costs 1.0850 Euros",
                    "1 Euro costs 1.0850 US Dollars",
                    "You need 108.5 Cedis to buy 1 Euro",
                    "You make $1.08 profit per minute"
                ],
                "correct_idx": 1,
                "explanation": "Well done! The exchange rate tells you how much of the second (quote) currency is needed to buy 1 unit of the first (base) currency."
            }
        ]
    },
    "2": {
        "day": 2,
        "topic": "Currency Pairs & Trading Sessions - Best Times to Trade in Ghana",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we study *Day 2: Currency Pairs & Trading Sessions*.\n"
            "Did you know the Forex market is open 24 hours a day, 5 days a week? But in Ghana, "
            "there are specific hours where the market moves fast and offers the best opportunities.\n"
            "Join me at 7:00 PM sharp! 🇬🇭⏰"
        ),
        "hook": "Have you noticed how Makola market is quiet at 5:00 AM, but by 11:00 AM it is buzzing with buyers and sellers? The Forex market is exactly the same!",
        "lesson_text": (
            "Good evening class, today we learn: *Currency Pairs & Trading Sessions*\n\n"
            "🎯 *1. THE HOOK: The Market Rush Hour*\n"
            "If you go to Makola Market at 2:00 AM, nobody is there. You cannot buy or sell anything. "
            "Around 10:00 AM to 2:00 PM, the market is crowded, money is flowing, and transactions happen fast. "
            "The international Forex market works on global time zones across London, New York, Tokyo, and Sydney.\n\n"
            "💡 *2. THE EXPLANATION: Types of Currency Pairs*\n"
            "Currencies are grouped into three categories:\n"
            "• **Major Pairs**: Always include the US Dollar ($) paired with another world economic power (EUR/USD, GBP/USD, USD/JPY, USD/CHF). These have the lowest trading fees (spread) and cleanest moves.\n"
            "• **Minor Pairs**: Major currencies without the US Dollar (EUR/GBP, GBP/JPY, EUR/AUD).\n"
            "• **Exotic Pairs**: One major currency paired with an emerging economy (USD/ZAR, USD/TRY). Beginners should stay away because fees are high!\n\n"
            "🌍 *3. THE 4 TRADING SESSIONS (GHANA TIME - GMT)*\n"
            "Ghana is on GMT (UTC+0), which gives us the **best geographic advantage** in the world!\n"
            "1. **Sydney Session**: 10:00 PM - 7:00 AM GMT (Quiet, low movement)\n"
            "2. **Tokyo (Asian) Session**: 12:00 AM - 9:00 AM GMT (Moderate movement in JPY and AUD)\n"
            "3. **London Session**: 8:00 AM - 4:00 PM GMT (Very active, high volume!)\n"
            "4. **New York Session**: 1:00 PM - 10:00 PM GMT (Massive movement!)\n\n"
            "🔥 **The Golden Window for Ghana:** From **1:00 PM to 4:00 PM GMT**, both London and New York are open at the same time! "
            "This is known as the **London/New York Overlap**. This is when liquidity is highest.\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "You do not need to sit in front of the screen all day. Trade during active sessions, protect your sleep, "
            "and remember: disciplined traders wait for the right market hours!"
        ),
        "calculation_example": (
            "🔢 *Session Timing Example:*\n"
            "• London opens at 8:00 AM GMT.\n"
            "• New York opens at 1:00 PM GMT.\n"
            "• Between 1:00 PM and 4:00 PM GMT, billions of dollars are moved between banks in the UK and USA. "
            "Spreads are tightest and price moves cleanly."
        ),
        "voice_script": (
            "Hello class, Coach Prince here. One mistake Ghanaian beginners make is waking up at 3 AM to trade pairs "
            "like EUR/USD when European and American banks are closed. Trade when the market is awake! "
            "Our sweet spot in Ghana is 8 AM to 4 PM. Listen to the video below and take note of the session hours."
        ),
        "image_type": "trading_sessions_clock",
        "video_title": "Forex Market Sessions & The Best Times to Trade (The Secret Mindset)",
        "video_url": "https://www.youtube.com/watch?v=Gk74VqC1kCg",
        "video_duration": "8 mins",
        "video_reason": "Explains global time zone overlaps simply with clear visual clocks.",
        "notes_summary": (
            "📌 *Day 2 Key Takeaways Cheatsheet:*\n"
            "1. Major pairs always contain the US Dollar (e.g. EUR/USD, GBP/USD).\n"
            "2. Beginners should stick to Majors (cheaper spread, high liquidity).\n"
            "3. London Session: 8:00 AM - 4:00 PM GMT.\n"
            "4. New York Session: 1:00 PM - 10:00 PM GMT.\n"
            "5. Best time to trade in Ghana: 1:00 PM - 4:00 PM (Overlap window)."
        ),
        "assignment": (
            "🎯 *DAY 2 ASSIGNMENT: Finding Your Trading Window*\n\n"
            "1. List the 4 Major Currency Pairs you would like to follow.\n"
            "2. What time in Ghana (GMT) does the London & New York session overlap happen?\n"
            "3. Look at your daily personal schedule (school, work, family). Which 2-hour window during the day is best for you to study the charts?\n\n"
            "📤 *How to Submit:* Reply to Coach Prince in private chat or write down in your notebook.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Time management is the hallmark of a professional trader. Have you written down your daily 2-hour study window? Submit your Day 2 assignment!"
        ),
        "correction": (
            "✅ *DAY 2 ASSIGNMENT CORRECTION*\n\n"
            "Good afternoon class! London/New York overlap is strictly **1:00 PM to 4:00 PM GMT**.\n"
            "The top 4 majors recommended for beginners are: EUR/USD, GBP/USD, USD/JPY, and USD/CHF.\n"
            "Notice how quiet pairs are outside their respective sessions. Build the habit of trading during market hours!"
        ),
        "quizzes": [
            {
                "question": "Which of the following is considered a 'Major' currency pair?",
                "options": [
                    "EUR/GBP",
                    "EUR/USD",
                    "USD/ZAR",
                    "AUD/NZD"
                ],
                "correct_idx": 1,
                "explanation": "Correct! Major pairs always pair a leading currency directly with the US Dollar (USD). EUR/USD is the world's most traded major pair."
            },
            {
                "question": "What is the best time window to trade in Ghana (GMT) due to high volume?",
                "options": [
                    "2:00 AM - 4:00 AM GMT",
                    "1:00 PM - 4:00 PM GMT (London & NY Overlap)",
                    "10:00 PM - 12:00 AM GMT",
                    "Only on Sunday evenings"
                ],
                "correct_idx": 1,
                "explanation": "Excellent! Between 1:00 PM and 4:00 PM GMT, both London and New York financial centers are active at the same time."
            },
            {
                "question": "Why should beginners avoid trading 'Exotic' currency pairs like USD/ZAR or USD/TRY?",
                "options": [
                    "They are illegal in Ghana",
                    "They have very high trading fees (spread) and erratic spikes",
                    "They only move 1 pip per day",
                    "They only trade in physical cash"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! Exotic pairs carry wide spreads and wild erratic jumps that can wipe a beginner's demo account quickly."
            }
        ]
    },
    "3": {
        "day": 3,
        "topic": "How to Download MT5 + Create a Demo Account Step-by-Step",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we do *Day 3: How to Download MT5 and Create a Demo Account*.\n"
            "No real money! A Demo account gives you virtual money so you can practice without losing a single pesewa.\n"
            "Get your smartphone or laptop ready! 🇬🇭📱"
        ),
        "hook": "Before an airline lets a pilot fly a real plane with 300 passengers, where do they train? In a flight simulator! In Forex, MT5 Demo is our simulator.",
        "lesson_text": (
            "Good evening class, today we learn: *How to Download MT5 & Create a Demo Account*\n\n"
            "🎯 *1. THE HOOK: The Flight Simulator Analogy*\n"
            "Nobody becomes a commercial pilot by jumping into a Boeing 777 on day one. They spend months in a simulator "
            "crashing virtual planes until they master every button and control without risking any human lives. "
            "In Forex, **MetaTrader 5 (MT5)** is your simulator. You trade with real live price quotes, but using 100% virtual practice money.\n\n"
            "💡 *2. THE EXPLANATION: What is MetaTrader 5 (MT5)?*\n"
            "• **MT5** is the world's most popular free software that connects you to currency charts and allows you to place Buy and Sell orders.\n"
            "• It is available on Android (Google Play Store), iPhone (Apple App Store), Windows, and Mac.\n"
            "• A **Demo Account** provides fake money (e.g. $3,000 or $5,000 virtual balance) so you can press buttons, make mistakes, and learn freely.\n\n"
            "📲 *3. STEP-BY-STEP SETUP GUIDE (Takes 3 Minutes):*\n"
            "1. Open **Google Play Store** or **Apple App Store** on your phone.\n"
            "2. Search for: **MetaTrader 5** and tap Install.\n"
            "3. Open the app. It will ask: *'Open a demo account?'* Tap **Accept** or **Open Demo**.\n"
            "4. Choose an initial deposit of **$3,000** (choose the smallest virtual balance possible, do NOT choose $100,000! Keep it realistic).\n"
            "5. Look at the bottom menu: **Quotes** (currency list), **Charts** (the price graphs), and **Trade** (your balance).\n\n"
            "⚠️ *CRITICAL COACH PRINCE RULE:*\n"
            "Never deposit real money now. Anyone asking you to send MTN MoMo or deposit cash into a broker account right now is deceiving you. "
            "We stay on Demo for at least 30 to 60 days until our strategy is proven!"
        ),
        "calculation_example": (
            "🔢 *Realistic Demo Account Sizing:*\n"
            "• If you intend to start live trading later with $100 or $200, practicing on a $100,000 demo account creates a false illusion.\n"
            "• Configure your demo balance between $500 and $3,000 so the profit and loss figures match your real-world emotional reality."
        ),
        "voice_script": (
            "Good evening students! Today is practical day. Download MetaTrader 5 on your phone right now. "
            "Open a free demo account. Familiarize yourself with the Quotes tab and the Chart tab. "
            "Watch the walkthrough video below so you don't get lost in the settings."
        ),
        "image_type": "mt5_interface_walkthrough",
        "video_title": "How To Use MetaTrader 5 (MT5) For Beginners - Mobile Guide",
        "video_url": "https://www.youtube.com/watch?v=kYI9QJvh6V4",
        "video_duration": "9 mins",
        "video_reason": "Clean step-by-step phone screen demonstration of installing MT5 and opening a demo account.",
        "notes_summary": (
            "📌 *Day 3 Key Takeaways Cheatsheet:*\n"
            "1. MT5 = MetaTrader 5 (The trading terminal).\n"
            "2. Demo Account = Virtual money with real live market prices.\n"
            "3. Quotes Tab = List of pairs with Bid and Ask prices.\n"
            "4. Chart Tab = Visual price action candlesticks.\n"
            "5. Rule: Never trade live until demo results are consistently profitable!"
        ),
        "assignment": (
            "🎯 *DAY 3 ASSIGNMENT: Install MT5 & Take a Screenshot*\n\n"
            "1. Download MetaTrader 5 on your mobile phone or PC.\n"
            "2. Open a free Demo Account.\n"
            "3. Go to the 'Quotes' screen and locate **EURUSD**.\n"
            "4. Tap on EURUSD and open the **Chart**.\n"
            "5. Type 'DONE' to Coach Prince once your demo account is ready!\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Check-in:*\n"
            "Did you download MT5 today? If you are stuck on any screen, ask in the Discussion Group! We are here to help you get set up."
        ),
        "correction": (
            "✅ *DAY 3 ASSIGNMENT CORRECTION & FEEDBACK*\n\n"
            "Well done class! If you opened your demo and saw EURUSD moving, congratulations—you are officially looking at real-time global financial data.\n"
            "Common mistake: Don't open 10 different demo accounts. Stick to one and treat every virtual dollar with respect."
        ),
        "quizzes": [
            {
                "question": "What is the primary purpose of a Forex Demo Account?",
                "options": [
                    "To withdraw free Cedis to your MTN MoMo",
                    "To practice trading with virtual money on real live market prices",
                    "To gamble without internet",
                    "To buy shares in a local Ghanaian company"
                ],
                "correct_idx": 1,
                "explanation": "Correct! A demo account is your flight simulator—you practice with fake money on real live market conditions."
            },
            {
                "question": "Why should you choose a realistic demo balance (like $1,000 or $3,000) instead of $1,000,000?",
                "options": [
                    "MT5 charges you if you pick $1,000,000",
                    "A realistic balance trains proper risk management and emotional discipline",
                    "The broker will ban you",
                    "Larger balances make the charts move slower"
                ],
                "correct_idx": 1,
                "explanation": "Exactly! If you practice with $1,000,000, making $100 looks like nothing. But on a realistic account, $20 is a big percentage!"
            },
            {
                "question": "On the MT5 mobile app, which tab displays the list of currency pairs and live prices?",
                "options": [
                    "Mailbox",
                    "Quotes",
                    "Journal",
                    "Settings"
                ],
                "correct_idx": 1,
                "explanation": "Well done! The 'Quotes' tab is where you view all available currency pairs and their live buying and selling prices."
            }
        ]
    },
    "4": {
        "day": 4,
        "topic": "Candlesticks - Green = Buyers Won, Red = Sellers Won",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we tackle *Day 4: Japanese Candlesticks*.\n"
            "What do those green and red bars on your chart actually mean? They tell the story of a tug-of-war "
            "between buyers (Bulls) and sellers (Bears). Don't miss tonight's class! 🇬🇭📊"
        ),
        "hook": "Picture an inter-school tug-of-war competition between two strong teams. At the end of 5 minutes, whoever dragged the rope across the line won that round. Candlesticks show the exact same battle!",
        "lesson_text": (
            "Good evening class, today we learn: *Japanese Candlesticks*\n\n"
            "🎯 *1. THE HOOK: The Tug-of-War Battle*\n"
            "Every second in the Forex market, two groups are fighting:\n"
            "• **Bulls (Buyers)**: Pushing price UP.\n"
            "• **Bears (Sellers)**: Pushing price DOWN.\n"
            "A Japanese candlestick is simply a snapshot of who won the battle over a specific time period (e.g., 1 hour, 4 hours, or 1 day).\n\n"
            "💡 *2. THE ANATOMY OF A CANDLESTICK (4 Key Numbers)*\n"
            "Every single candle gives you 4 critical pieces of information (OHLC):\n"
            "1. **Open (O)**: The price where the time period started.\n"
            "2. **High (H)**: The highest price reached during the battle (tip of the upper wick).\n"
            "3. **Low (L)**: The lowest price reached during the battle (tip of the lower wick).\n"
            "4. **Close (C)**: The final price when time expired.\n\n"
            "🟢 **GREEN (Bullish) CANDLE:**\n"
            "• Price closed **HIGHER** than it opened.\n"
            "• Buyers won that round! The thick rectangle is the **Body**, and the thin sticks poking out are the **Wicks (or Shadows)**.\n\n"
            "🔴 **RED (Bearish) CANDLE:**\n"
            "• Price closed **LOWER** than it opened.\n"
            "• Sellers won that round!\n\n"
            "🕯️ *3. WHAT DO WICKS (SHADOWS) MEAN?*\n"
            "A long wick at the top means buyers tried to push price up, but sellers slapped them back down (**Rejection**).\n"
            "A long wick at the bottom means sellers tried to push price down, but buyers stepped in aggressively and pushed it back up.\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "Candlesticks are the language of the market. When you look at a chart, don't just see colors—see the human emotion "
            "of fear and greed playing out in real time!"
        ),
        "calculation_example": (
            "🔢 *Candlestick Calculation on EUR/USD (1-Hour Candle):*\n"
            "• Open: 1.0820\n"
            "• High: 1.0865\n"
            "• Low: 1.0815\n"
            "• Close: 1.0860\n"
            "Close (1.0860) > Open (1.0820) ➡️ Result: A solid Green Bullish Candle with a body of +40 pips and a small upper wick of 5 pips."
        ),
        "voice_script": (
            "Coach Prince here students. Candlesticks were invented hundreds of years ago by Japanese rice traders. "
            "They tell you who is in control: Green means buyers won, Red means sellers won. Long wicks show price rejection. "
            "Watch the video and learn to read the story behind every candle."
        ),
        "image_type": "candlestick_anatomy",
        "video_title": "Understanding Candlestick Charts For Beginners (Rayner Teo)",
        "video_url": "https://www.youtube.com/watch?v=9g0H5z7u2kE",
        "video_duration": "9 mins",
        "video_reason": "Rayner Teo explains Open, High, Low, Close with zero confusion and clear chart animations.",
        "notes_summary": (
            "📌 *Day 4 Key Takeaways Cheatsheet:*\n"
            "1. Green Candle = Bullish (Close is higher than Open).\n"
            "2. Red Candle = Bearish (Close is lower than Open).\n"
            "3. Body = Distance between Open and Close.\n"
            "4. Wicks = Highest and Lowest extremes reached.\n"
            "5. Long bottom wick = Buyers rejecting lower prices (Bullish sign)."
        ),
        "assignment": (
            "🎯 *DAY 4 ASSIGNMENT: Spotting Candlesticks on MT5*\n\n"
            "1. Open your MT5 app and switch to the **EURUSD** chart on the **1-Hour (H1)** timeframe.\n"
            "2. Look at the last closed candle on the chart.\n"
            "3. Answer: Is it Green (Bullish) or Red (Bearish)?\n"
            "4. Does it have a longer wick on top or on the bottom?\n\n"
            "📤 *How to Submit:* Reply to Coach Prince with your answer.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Open your MT5 chart right now and check the H1 candle on EURUSD. Reading candles is your core visual skill!"
        ),
        "correction": (
            "✅ *DAY 4 ASSIGNMENT CORRECTION*\n\n"
            "Great job inspecting your charts! When a candle has a long wick at the bottom, notice how price often struggles to go lower. "
            "Understanding wicks prevents you from buying at the very top or selling at the very bottom."
        ),
        "quizzes": [
            {
                "question": "What does a Green (or Bullish) candlestick indicate?",
                "options": [
                    "Price closed higher than it opened (Buyers won)",
                    "Price closed lower than it opened (Sellers won)",
                    "The broker is offline",
                    "Trading is closed for the day"
                ],
                "correct_idx": 0,
                "explanation": "Correct! When the closing price is higher than the opening price, the candle is green (bullish)—buyers were in control."
            },
            {
                "question": "What do the thin lines poking out of the candle body (wicks/shadows) represent?",
                "options": [
                    "Computer glitches in MT5",
                    "The highest and lowest prices reached during that period",
                    "The spread charged by your broker",
                    "The number of traders in Ghana"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! The wicks show the extreme highs and lows reached before price pulled back."
            },
            {
                "question": "If you see a candle with a very long lower wick and a small body at the top, what happened?",
                "options": [
                    "Sellers took total control permanently",
                    "Sellers tried pushing down, but aggressive buyers pushed price back up (rejection)",
                    "Nothing happened",
                    "Price dropped to zero"
                ],
                "correct_idx": 1,
                "explanation": "Excellent! That is a hammer/rejection pattern showing buyers fiercely defending lower price levels."
            }
        ]
    },
    "5": {
        "day": 5,
        "topic": "Pips, Lots & Leverage - The Math Behind Your Profits and Losses",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we study the most critical mathematical foundation in Forex: *Day 5: Pips, Lots & Leverage*.\n"
            "If you don't understand lot size, you can blow your entire account in 2 minutes. "
            "Tonight, we calculate everything with simple numbers. Be on time! 🇬🇭🔢"
        ),
        "hook": "If you buy 1 plantain chips at the roadside for 5 Cedis, your risk is 5 Cedis. But what if a wholesaler brings 1,000 packs to your house on credit? That is leverage!",
        "lesson_text": (
            "Good evening class, today we learn: *Pips, Lots & Leverage*\n\n"
            "🎯 *1. THE HOOK: The Wholesaler Credit Analogy*\n"
            "Imagine you want to sell bags of rice at Kejetia. One bag costs 500 GHS, but you only have 50 GHS in your pocket. "
            "A wealthy uncle tells you: *'Take 10 bags on credit, sell them, return my money, and keep the profit.'* "
            "That credit multiplier is what we call **LEVERAGE**. It magnifies both your gains and your losses!\n\n"
            "💡 *2. DEFINING THE BIG THREE WORDS*\n\n"
            "1. **PIP (Percentage In Point):**\n"
            "• In most currency pairs, a pip is the **4th decimal digit** (0.0001).\n"
            "• Example: If EUR/USD moves from 1.0850 to 1.0855, it moved **5 Pips**.\n"
            "• (For JPY pairs, a pip is the 2nd decimal digit: 0.01).\n\n"
            "2. **LOT SIZE (Volume):**\n"
            "How many units of currency you are trading:\n"
            "• **Standard Lot (1.00)** = 100,000 units (~$10 per pip movement)\n"
            "• **Mini Lot (0.10)** = 10,000 units (~$1 per pip movement)\n"
            "• **Micro Lot (0.01)** = 1,000 units (~$0.10 / 10 cents per pip movement)\n\n"
            "⚠️ **COACH PRINCE GOLDEN RULE FOR BEGINNERS:**\n"
            "Always, always trade **0.01 (Micro Lot)**! If the market moves 20 pips against you, you only lose $2. "
            "If you foolishly use 1.00 lot on a small account, a 20-pip move will wipe out $200 in seconds!\n\n"
            "3. **LEVERAGE:**\n"
            "Leverage allows you to control a large trade with a small deposit (margin). 1:100 leverage means $1 controls $100. "
            "Use leverage like fire: it can cook your food, or it can burn down your house if you misuse it!\n\n"
            "📝 *3. SUMMARY & ENCOURAGEMENT*\n"
            "Do not be in a rush to make big money with big lot sizes. Master the micro lot first!"
        ),
        "calculation_example": (
            "🔢 *Step-by-Step Profit/Loss Calculation:*\n"
            "• Trade: BUY EUR/USD at 1.0820\n"
            "• Lot Size: 0.01 (Micro Lot = $0.10 per pip)\n"
            "• Price moves to 1.0870\n"
            "• Pips gained = 1.0870 - 1.0820 = 50 pips.\n"
            "• Profit = 50 pips × $0.10 = **+$5.00**.\n"
            "• If lot size was 0.10, profit = 50 × $1.00 = +$50.00.\n"
            "• But if price dropped 50 pips, loss would be -$50.00!"
        ),
        "voice_script": (
            "Students, Coach Prince here. Tonight's lesson is where most beginners fail because of greed. "
            "They open a $50 account and use a 0.50 lot size. Two candle wicks and their money is gone! "
            "Promise me today: In Candlemaster Academy, our default lot size is 0.01. Watch the video and master the math."
        ),
        "image_type": "pip_lot_calculator_cheatsheet",
        "video_title": "What is a Pip & Lot Size in Forex? (ForexSignals TV)",
        "video_url": "https://www.youtube.com/watch?v=i89Tsq0Mh-I",
        "video_duration": "7 mins",
        "video_reason": "Crystal clear breakdown of pip counting and micro lot calculations.",
        "notes_summary": (
            "📌 *Day 5 Key Takeaways Cheatsheet:*\n"
            "1. Pip = 4th decimal place (0.0001) in EUR/USD.\n"
            "2. 0.01 Lot = Micro lot ($0.10 per pip) ➡️ BEST FOR BEGINNERS.\n"
            "3. 0.10 Lot = Mini lot ($1.00 per pip).\n"
            "4. 1.00 Lot = Standard lot ($10.00 per pip).\n"
            "5. High leverage without risk control is the #1 cause of account blowouts!"
        ),
        "assignment": (
            "🎯 *DAY 5 ASSIGNMENT: Pip & Lot Calculation Practice*\n\n"
            "Calculate the following on paper:\n"
            "1. EUR/USD moved from 1.0800 to 1.0845. How many pips is that?\n"
            "2. If you traded with a **0.01 lot size**, how much profit or loss in US Dollars did you make?\n"
            "3. If someone used a **0.10 lot size** on that same move, how much did they make?\n\n"
            "📤 *How to Submit:* Send your answers to Coach Prince.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Grab your phone calculator and do the 3 math questions from Day 5. Understanding pip values makes you fearless on the charts!"
        ),
        "correction": (
            "✅ *DAY 5 ASSIGNMENT CORRECTION*\n\n"
            "Here are the exact answers:\n"
            "1. 1.0845 - 1.0800 = **45 Pips**.\n"
            "2. On 0.01 lot size: 45 pips × $0.10 = **$4.50 profit**.\n"
            "3. On 0.10 lot size: 45 pips × $1.00 = **$45.00 profit**.\n"
            "Notice how lot size multiplies your result by 10x! Keep your lot size small to protect your capital."
        ),
        "quizzes": [
            {
                "question": "If EUR/USD moves from 1.0910 to 1.0940, how many pips did it gain?",
                "options": [
                    "3 pips",
                    "30 pips",
                    "300 pips",
                    "0.3 pips"
                ],
                "correct_idx": 1,
                "explanation": "Correct! 1.0940 - 1.0910 = 0.0030, which equals 30 pips."
            },
            {
                "question": "What is the recommended lot size for all beginners starting out?",
                "options": [
                    "1.00 (Standard Lot)",
                    "0.50 Lot",
                    "0.01 (Micro Lot)",
                    "5.00 Lot"
                ],
                "correct_idx": 2,
                "explanation": "Spot on! 0.01 (Micro Lot) keeps your risk around 10 cents per pip so mistakes cost you virtually nothing while learning."
            },
            {
                "question": "What does financial 'Leverage' do in Forex trading?",
                "options": [
                    "Guarantees that your trades will always win",
                    "Allows you to control larger positions with smaller capital, multiplying gains and losses",
                    "Sends money to your MoMo automatically",
                    "Freezes market charts"
                ],
                "correct_idx": 1,
                "explanation": "Well done! Leverage magnifies both potential profits and potential losses. Always manage it with care."
            }
        ]
    },
    "6": {
        "day": 6,
        "topic": "Buy/Sell, Stop Loss & Take Profit - Placing Your First Demo Trade",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we reach a huge milestone: *Day 6: Placing Your First Demo Trade*.\n"
            "We will learn the two most important defense tools in trading: **Stop Loss (SL)** and **Take Profit (TP)**.\n"
            "Have your MT5 app ready tonight! 🇬🇭🎯"
        ),
        "hook": "When you enter a trotro from Kaneshie to Madina, you tell the driver where to drop you, and you wear your seatbelt in case of emergency. Take Profit is your bus stop, Stop Loss is your seatbelt!",
        "lesson_text": (
            "Good evening class, today we learn: *Buy/Sell, Stop Loss & Take Profit*\n\n"
            "🎯 *1. THE HOOK: The Seatbelt & Bus Stop Analogy*\n"
            "Imagine traveling in a car without brakes or a seatbelt. If an accident happens, disaster is guaranteed. "
            "In Forex trading, placing a trade without a **Stop Loss** is like driving at 120 km/h with no brakes! "
            "One unexpected news announcement can wipe your account while you are asleep.\n\n"
            "💡 *2. THE TWO BUTTONS: BUY & SELL*\n"
            "• **BUY (Go Long):** You click Buy when you anticipate price will go **UP**.\n"
            "• **SELL (Go Short):** You click Sell when you anticipate price will go **DOWN**. (Yes! In Forex, you can make profit when prices drop!).\n\n"
            "🛡️ *3. YOUR TWO AUTOMATIC PROTECTION ORDERS*\n\n"
            "1. **STOP LOSS (SL) - Your Financial Seatbelt:**\n"
            "• A pre-set order that automatically closes your trade if the market moves against you.\n"
            "• It decides *in advance* the maximum amount of money you are willing to lose (e.g. $2 or $3).\n"
            "• Once set, you can turn off your phone and sleep soundly knowing your account cannot be wiped out.\n\n"
            "2. **TAKE PROFIT (TP) - Your Destination Bus Stop:**\n"
            "• A pre-set price target that automatically locks in your profit and closes the trade when price reaches your goal.\n"
            "• You don't need to stare at the screen all day waiting to close manually.\n\n"
            "📲 *4. HOW TO PLACE THE TRADE ON MT5 (Step-by-Step):*\n"
            "1. Open MT5 ➡️ Go to **Quotes** ➡️ Tap **EURUSD** ➡️ Tap **New Order**.\n"
            "2. Ensure lot size is set to **0.01**.\n"
            "3. If current price is 1.0850 and you want to **BUY**:\n"
            "   - Set **SL** at: 1.0820 (30 pips below entry).\n"
            "   - Set **TP** at: 1.0910 (60 pips above entry).\n"
            "4. Tap the blue **BUY** button!\n\n"
            "📝 *5. SUMMARY & ENCOURAGEMENT*\n"
            "Professional traders always know their risk *before* they enter a trade. Never enter a trade without a Stop Loss!"
        ),
        "calculation_example": (
            "🔢 *Risk vs Reward Example:*\n"
            "• Entry: BUY EURUSD at 1.0850 (0.01 lot)\n"
            "• Stop Loss: 1.0820 (Risk = 30 pips = -$3.00)\n"
            "• Take Profit: 1.0910 (Target = 60 pips = +$6.00)\n"
            "• Risk-to-Reward Ratio = 1:2. You risk $3 to potentially make $6!"
        ),
        "voice_script": (
            "Good evening students! Today you place your very first trade on demo. Do not fear making mistakes; "
            "that is what virtual money is for. Remember Coach Prince's rule: Never enter any trade without setting "
            "your Stop Loss. Watch the video below to see the exact buttons to press on your phone."
        ),
        "image_type": "buy_sell_sl_tp_chart",
        "video_title": "How to Place Orders, Set Stop Loss & Take Profit in MT5",
        "video_url": "https://www.youtube.com/watch?v=n7z5z3b72hU",
        "video_duration": "8 mins",
        "video_reason": "Practical mobile walkthrough showing exactly where to enter SL and TP numbers.",
        "notes_summary": (
            "📌 *Day 6 Key Takeaways Cheatsheet:*\n"
            "1. BUY = Expecting prices to rise.\n"
            "2. SELL = Expecting prices to fall.\n"
            "3. Stop Loss (SL) = Automatic protection against major loss.\n"
            "4. Take Profit (TP) = Automatic closing when target is reached.\n"
            "5. Golden Rule: No trade is ever placed without a pre-calculated Stop Loss!"
        ),
        "assignment": (
            "🎯 *DAY 6 ASSIGNMENT: Place Your First Demo Order*\n\n"
            "1. Open your MT5 Demo account.\n"
            "2. Open EURUSD.\n"
            "3. Set lot size to **0.01**.\n"
            "4. Place 1 Demo trade (Buy or Sell) with both a Stop Loss and a Take Profit set.\n"
            "5. Message Coach Prince: What price did you enter, and where is your Stop Loss?\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Don't be shy! Open MT5 and place that 0.01 demo order with your SL and TP. Practice builds confidence."
        ),
        "correction": (
            "✅ *DAY 6 ASSIGNMENT CORRECTION*\n\n"
            "Kudos to everyone who placed their first demo trade! If your Stop Loss got hit, congratulations—your seatbelt worked! "
            "A small controlled loss is a normal operating expense in this business. As long as your risk was small ($1-$3), you did perfectly."
        ),
        "quizzes": [
            {
                "question": "What is the primary function of a Stop Loss (SL)?",
                "options": [
                    "To double your deposit speed",
                    "To automatically limit your maximum potential loss if the market goes against you",
                    "To hide your account from the broker",
                    "To prevent taxes in Ghana"
                ],
                "correct_idx": 1,
                "explanation": "Correct! A Stop Loss acts as your automated safety brake, capping your maximum loss to an acceptable amount."
            },
            {
                "question": "In a BUY trade on EUR/USD, where must your Stop Loss be placed?",
                "options": [
                    "Above the entry price",
                    "Below the entry price",
                    "At exactly the entry price",
                    "Stop Loss is not needed for Buy trades"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! When you Buy, you expect price to rise. Therefore, your safety Stop Loss must be placed below your entry price."
            },
            {
                "question": "Can a trader make profit in Forex when currency prices are dropping?",
                "options": [
                    "No, you can only make money when prices go up",
                    "Yes, by opening a SELL (Short) order",
                    "Only if you pay extra fees to MT5",
                    "Only on weekends"
                ],
                "correct_idx": 1,
                "explanation": "Well done! In Forex, you can open a SELL order to profit from downwards market price movements."
            }
        ]
    },
    "7": {
        "day": 7,
        "topic": "Midway Q&A + Foundation Review Test",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Today is *Day 7: Midway Review & Q&A Day*!\n"
            "No heavy new topic today. We pause, answer every burning question in the Discussion Group, "
            "and take our comprehensive Week 1 Review Test. Be active in the group today! 🇬🇭🤝"
        ),
        "hook": "In construction, if the foundation is weak, adding a second floor will make the whole building collapse. Today we solidify our Week 1 foundation!",
        "lesson_text": (
            "Good evening class, today we do: *Midway Q&A + Foundation Review*\n\n"
            "🎯 *1. THE HOOK: The Strong Foundation*\n"
            "You cannot build a multi-story house in East Legon on swampy sand. If your basics are shaky, "
            "advanced strategies like Support & Resistance, Market Structure, and Risk Management will confuse you. "
            "Today, we inspect our Week 1 foundation.\n\n"
            "📚 *2. WEEK 1 FLASH REVISION:*\n"
            "• **Day 1 (What is Forex):** Exchanging currencies in pairs (Base/Quote). Over $7.5 Trillion daily.\n"
            "• **Day 2 (Sessions):** Best time in Ghana is London/NY overlap (1:00 PM - 4:00 PM GMT).\n"
            "• **Day 3 (MT5 & Demo):** Flight simulator practice. Never deposit real money while learning.\n"
            "• **Day 4 (Candlesticks):** Green = Bulls won, Red = Bears won. Wicks show price rejection.\n"
            "• **Day 5 (Pips & Lots):** 0.01 micro lot ($0.10/pip). Respect leverage or get burned.\n"
            "• **Day 6 (SL & TP):** Stop loss is your seatbelt. Never enter a trade without it.\n\n"
            "💬 *3. TODAY'S Q&A MISSION IN DISCUSSION GROUP:*\n"
            "Head over to our Discussion Group right now! Ask Coach Prince any question from Days 1 to 6. "
            "No question is too simple. If you are confused about anything, let's clear it today!\n\n"
            "📝 *4. ENCOURAGEMENT*\n"
            "You are already ahead of 90% of beginners who rush to gamble their money without studying. "
            "Celebrate your discipline, take today's review quiz, and rest well for Week 2!"
        ),
        "calculation_example": (
            "🔢 *Foundation Checklist:*\n"
            "1. Can you calculate pips? (1.0850 to 1.0880 = 30 pips)\n"
            "2. Can you calculate dollar value? (30 pips on 0.01 = $3.00)\n"
            "3. Do you have MT5 active on your phone with demo balance ready? If YES to all three, you are ready for Week 2!"
        ),
        "voice_script": (
            "Hello students! Coach Prince here. We have completed one full week together. I am very proud of your progress. "
            "Today we are reviewing all six lessons and answering your questions live in the group. "
            "Take the review quiz seriously and let's get ready for Week 2."
        ),
        "image_type": "midway_review_mindmap",
        "video_title": "Forex Trading For Beginners - The Complete Basics Recap",
        "video_url": "https://www.youtube.com/watch?v=7uKxZ8X9uFw",
        "video_duration": "10 mins",
        "video_reason": "Comprehensive recap of all foundational terminology and MT5 order mechanics.",
        "notes_summary": (
            "📌 *Week 1 Review Cheatsheet:*\n"
            "1. Major pairs: Low spread, high liquidity.\n"
            "2. Ghana timing: 1 PM - 4 PM GMT is optimal.\n"
            "3. 0.01 lot size protects small accounts.\n"
            "4. Always set Stop Loss.\n"
            "5. Focus on the learning process, not quick cash!"
        ),
        "assignment": (
            "🎯 *DAY 7 ASSIGNMENT: Week 1 Self-Assessment*\n\n"
            "1. Post 1 question or 1 concept from Week 1 you want Coach Prince to re-explain in the Discussion Group.\n"
            "2. Complete the Day 7 Review Quiz below.\n"
            "3. Ensure your MT5 demo account is working smoothly.\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Join the Discussion Group today and drop your questions! Let us make sure every student is on the same page before tomorrow."
        ),
        "correction": (
            "✅ *DAY 7 REVIEW SUMMARY*\n\n"
            "Thank you everyone for the great questions in the Discussion Group! We answered queries on pip counting, "
            "MT5 navigation, and session times. You are now fully prepared to learn chart analysis starting tomorrow!"
        ),
        "quizzes": [
            {
                "question": "If you buy EUR/USD at 1.0800 with 0.01 lot and set TP at 1.0850, how much profit will you make if TP is hit?",
                "options": [
                    "$0.50",
                    "$5.00",
                    "$50.00",
                    "$500.00"
                ],
                "correct_idx": 1,
                "explanation": "Correct! 1.0850 - 1.0800 = 50 pips. On a 0.01 micro lot ($0.10/pip), 50 × $0.10 = $5.00."
            },
            {
                "question": "Why is 1:00 PM to 4:00 PM GMT the best time to trade for someone living in Ghana?",
                "options": [
                    "Internet in Ghana is fastest at that time",
                    "London and New York sessions overlap, creating peak market volume and tight spreads",
                    "All banks close at 1:00 PM",
                    "MT5 only opens at 1:00 PM"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! The London/New York session overlap brings peak global trading volume."
            },
            {
                "question": "Which of these actions is a recipe for blowing your Forex account?",
                "options": [
                    "Using 0.01 lot size and setting a Stop Loss",
                    "Trading without a Stop Loss and using a huge lot size like 1.00 on a small account",
                    "Practicing on a Demo account for 30 days",
                    "Studying during the London session"
                ],
                "correct_idx": 1,
                "explanation": "Well done! Trading without a Stop Loss and using excessive lot sizes is the fastest way to lose capital."
            }
        ]
    },
    "8": {
        "day": 8,
        "topic": "Support & Resistance - Where Price Bounces Like a Tennis Ball",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we enter technical analysis: *Day 8: Support & Resistance*.\n"
            "How do professional traders know where price will bounce? Think of a floor and a ceiling in a room. "
            "Join me at 7:00 PM! 🇬🇭🎾"
        ),
        "hook": "If you bounce a tennis ball inside your bedroom, it hits the floor and bounces up. If you throw it upwards, it hits the ceiling and bounces down. Price does the exact same thing on charts!",
        "lesson_text": (
            "Good evening class, today we learn: *Support & Resistance (Floor & Ceiling)*\n\n"
            "🎯 *1. THE HOOK: The Tennis Ball Room*\n"
            "Inside a room, the floor prevents you from falling down, and the ceiling prevents you from floating up. "
            "If you drop a tennis ball, it hits the floor and bounces UP. When it hits the ceiling, it bounces DOWN. "
            "In Forex charts, price bounces between invisible floors and ceilings created by previous buying and selling decisions.\n\n"
            "💡 *2. DEFINING SUPPORT & RESISTANCE*\n\n"
            "🟢 **SUPPORT (The Floor):**\n"
            "• A price level where falling price stops, reverses, and bounces back **UP**.\n"
            "• Why? Because buyers (Bulls) see the price as 'cheap' and step in with large buy orders.\n"
            "• *Trader mindset:* Look to **BUY** near strong Support levels.\n\n"
            "🔴 **RESISTANCE (The Ceiling):**\n"
            "• A price level where rising price stops, reverses, and turns back **DOWN**.\n"
            "• Why? Because sellers (Bears) see the price as 'expensive' and take profits or sell heavily.\n"
            "• *Trader mindset:* Look to **SELL** near strong Resistance levels.\n\n"
            "🔄 *3. THE ROLE REVERSAL RULE: Broken Floor Becomes Ceiling*\n"
            "What happens if a heavy bowling ball breaks through the floor of the 2nd story? It lands on the 1st story! "
            "Now, that broken floor is above you—it has become your **ceiling**!\n"
            "• When a **Support is broken**, it frequently turns into new **Resistance**.\n"
            "• When a **Resistance is broken**, it frequently turns into new **Support**.\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "Support and Resistance are not razor-thin lines; think of them as **zones** or areas on the chart. "
            "Identify the floor and ceiling before placing any trade!"
        ),
        "calculation_example": (
            "🔢 *Chart Example:*\n"
            "• EUR/USD drops to 1.0800 on Monday and bounces up to 1.0900.\n"
            "• On Wednesday, it drops again to 1.0802 and bounces back up.\n"
            "• ➡️ 1.0800 is a clear **Support zone**! Traders place Buy orders around 1.0805 with a Stop Loss just below the floor at 1.0780."
        ),
        "voice_script": (
            "Coach Prince here students. Support and Resistance is the bread and butter of technical analysis. "
            "Don't buy when price is hitting a ceiling (Resistance), and don't sell when price is sitting on a floor (Support). "
            "Watch the video and practice drawing your first horizontal lines."
        ),
        "image_type": "support_resistance_bounce_diagram",
        "video_title": "Support and Resistance Made Easy For Beginners",
        "video_url": "https://www.youtube.com/watch?v=uK481W_8Q9Q",
        "video_duration": "8 mins",
        "video_reason": "Visual explanation of bounce zones and the role reversal principle.",
        "notes_summary": (
            "📌 *Day 8 Key Takeaways Cheatsheet:*\n"
            "1. Support = Floor where price bounces UP (Buy area).\n"
            "2. Resistance = Ceiling where price bounces DOWN (Sell area).\n"
            "3. Support/Resistance are zones, not single lines.\n"
            "4. Broken Support often becomes new Resistance.\n"
            "5. Never buy directly into a strong resistance level!"
        ),
        "assignment": (
            "🎯 *DAY 8 ASSIGNMENT: Spotting Floor & Ceiling on MT5*\n\n"
            "1. Open EURUSD or GBPUSD on the **4-Hour (H4)** timeframe.\n"
            "2. Look back over the past 2 weeks.\n"
            "3. Identify 1 price level where price bounced up multiple times (Support).\n"
            "4. Identify 1 price level where price was rejected downwards multiple times (Resistance).\n"
            "5. Send the two price numbers to Coach Prince!\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Look for the mountain peaks and valley floors on your H4 chart. Write down the numbers for today's assignment!"
        ),
        "correction": (
            "✅ *DAY 8 ASSIGNMENT CORRECTION*\n\n"
            "Excellent work identifying levels! Always look for levels that have been tested at least twice. "
            "The more times a level bounces price without breaking, the stronger it is."
        ),
        "quizzes": [
            {
                "question": "What is 'Support' in Forex technical analysis?",
                "options": [
                    "A customer service line from your broker",
                    "A price floor where buying pressure stops price from falling and bounces it up",
                    "The maximum deposit amount allowed on MoMo",
                    "A government subsidy"
                ],
                "correct_idx": 1,
                "explanation": "Correct! Support is a price level where buyers enter the market, preventing price from falling further."
            },
            {
                "question": "What often happens when an old Resistance (ceiling) is broken to the upside?",
                "options": [
                    "It turns into new Support (floor)",
                    "The market crashes permanently",
                    "Trading is paused by MT5",
                    "It becomes completely invalid forever"
                ],
                "correct_idx": 0,
                "explanation": "Spot on! In market structure, broken resistance frequently flips to act as new support on a retest."
            },
            {
                "question": "As a beginner, what is the smartest action when price is approaching a major Resistance ceiling?",
                "options": [
                    "Buy with the biggest lot size possible",
                    "Look for sell signals or wait to see if price gets rejected or breaks through",
                    "Turn off your phone",
                    "Deposit real cash immediately"
                ],
                "correct_idx": 1,
                "explanation": "Well done! Buying into a ceiling is dangerous. You look for selling opportunities or wait for a confirmed breakout."
            }
        ]
    },
    "9": {
        "day": 9,
        "topic": "Trend - Uptrend, Downtrend & Range (The Market River)",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we study the trader's greatest ally: *Day 9: Market Trends*.\n"
            "'The trend is your friend until the bend at the end.' "
            "Learn how to tell whether the market is flowing up, down, or sideways. See you at 7:00 PM! 🇬🇭🌊"
        ),
        "hook": "Have you ever tried swimming upstream against the Volta River? You will get tired and drown! But if you swim in the direction of the river current, you move smoothly with little effort.",
        "lesson_text": (
            "Good evening class, today we learn: *Market Trends (Uptrend, Downtrend, Range)*\n\n"
            "🎯 *1. THE HOOK: Swimming with the River Current*\n"
            "If you jump into the river Volta and swim against the current, you waste all your energy and risk drowning. "
            "If you swim in the direction of the flowing water, the river carries you with speed. "
            "In Forex trading, the **TREND** is that river current. Trading with the trend is easy; fighting the trend destroys accounts!\n\n"
            "💡 *2. THE 3 MARKET CONDITIONS*\n\n"
            "📈 **1. UPTREND (Bull Market):**\n"
            "• Price is making **Higher Highs (HH)** and **Higher Lows (HL)**.\n"
            "• Every peak is higher than the previous peak; every dip is higher than the previous dip.\n"
            "• *Action:* We only look for **BUY** opportunities!\n\n"
            "📉 **2. DOWNTREND (Bear Market):**\n"
            "• Price is making **Lower Highs (LH)** and **Lower Lows (LL)**.\n"
            "• Every peak is lower than the previous peak; every drop creates a new low.\n"
            "• *Action:* We only look for **SELL** opportunities!\n\n"
            "↔️ **3. RANGE / SIDEWAYS (Consolidation):**\n"
            "• Price is bouncing between a horizontal Support floor and Resistance ceiling without moving in any direction.\n"
            "• *Action:* Wait patiently or buy at support and sell at resistance.\n\n"
            "📐 *3. DRAWING A TRENDLINE*\n"
            "Connect at least two consecutive Higher Lows in an uptrend with a straight diagonal line. "
            "As long as price stays above that trendline, the bullish current remains strong!\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "Never try to guess the top or bottom of a strong moving market. Ride the wave, follow the trend, "
            "and protect your peace of mind."
        ),
        "calculation_example": (
            "🔢 *Trend Identification Example on GBP/USD:*\n"
            "• Swing Low 1: 1.2500\n"
            "• Swing High 1: 1.2600\n"
            "• Swing Low 2: 1.2540 (Higher Low - HL)\n"
            "• Swing High 2: 1.2680 (Higher High - HH)\n"
            "➡️ Since 1.2540 > 1.2500 and 1.2680 > 1.2600, this is a textbook **Uptrend**. Look to buy on dips!"
        ),
        "voice_script": (
            "Students, Coach Prince here. Beginners love trying to guess when a fast-moving market will reverse. "
            "Don't stand in front of a moving trotro! If the market is going up, buy. If it is going down, sell. "
            "Watch the video and learn how to identify Higher Highs and Lower Lows."
        ),
        "image_type": "market_trends_hh_hl_diagram",
        "video_title": "How to Identify Trends and Market Structure Like a Pro",
        "video_url": "https://www.youtube.com/watch?v=ZkL28z9L6v4",
        "video_duration": "9 mins",
        "video_reason": "Visual demonstration of swing highs, swing lows, and drawing diagonal trendlines.",
        "notes_summary": (
            "📌 *Day 9 Key Takeaways Cheatsheet:*\n"
            "1. Uptrend = Higher Highs (HH) + Higher Lows (HL) ➡️ ONLY BUY.\n"
            "2. Downtrend = Lower Highs (LH) + Lower Lows (LL) ➡️ ONLY SELL.\n"
            "3. Sideways/Range = Price trapped between horizontal levels.\n"
            "4. Never trade against a clear trend.\n"
            "5. Rule: The trend is your friend until it bends!"
        ),
        "assignment": (
            "🎯 *DAY 9 ASSIGNMENT: Identify Market Direction*\n\n"
            "1. Open your MT5 app.\n"
            "2. Check **GBPUSD** on the **Daily (D1)** timeframe.\n"
            "3. Answer: Is GBPUSD currently in an Uptrend, a Downtrend, or a Range?\n"
            "4. What was the last Higher High or Lower Low you spotted?\n\n"
            "📤 *How to Submit:* Message your analysis to Coach Prince.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Zoom out on your MT5 chart to the Daily timeframe. Look at the big picture trend and submit your Day 9 answer!"
        ),
        "correction": (
            "✅ *DAY 9 ASSIGNMENT CORRECTION*\n\n"
            "Great analysis by everyone! Remember: Higher timeframes (Daily and 4-Hour) always tell the real truth about the market. "
            "If the Daily chart is in a Downtrend, do not take random Buys on the 1-minute chart!"
        ),
        "quizzes": [
            {
                "question": "What defines a healthy Uptrend on a price chart?",
                "options": [
                    "Series of Higher Highs (HH) and Higher Lows (HL)",
                    "Series of Lower Highs (LH) and Lower Lows (LL)",
                    "A straight flat horizontal line",
                    "Red candlesticks only"
                ],
                "correct_idx": 0,
                "explanation": "Correct! An uptrend is characterised by price constantly reaching higher peaks (Higher Highs) and higher troughs (Higher Lows)."
            },
            {
                "question": "If a market is in a clear, aggressive Downtrend, what should a beginner trader look to do?",
                "options": [
                    "Only look for Sell opportunities in line with the trend",
                    "Try to buy at the lowest point to get rich quick",
                    "Trade with 5.00 lot size",
                    "Ignore the chart"
                ],
                "correct_idx": 0,
                "explanation": "Spot on! Always align yourself with the trend. In a downtrend, selling at pullback highs offers the highest probability."
            },
            {
                "question": "What is a 'Consolidation' or 'Ranging' market?",
                "options": [
                    "When price is trapped between horizontal support and resistance without clear directional momentum",
                    "When MT5 is disconnected from internet",
                    "When the US Dollar is deleted",
                    "When only buyers are trading"
                ],
                "correct_idx": 0,
                "explanation": "Well done! A range occurs when price moves sideways between a floor and ceiling."
            }
        ]
    },
    "10": {
        "day": 10,
        "topic": "Simple Strategy - The Trend + Pullback Technique",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we combine our knowledge into a complete rule-based strategy: *Day 10: Trend + Pullback*.\n"
            "You don't need 20 confusing indicators. A simple 3-step strategy practiced 100 times will make you consistent. "
            "Be ready at 7:00 PM! 🇬🇭🏹"
        ),
        "hook": "When an archer wants to shoot an arrow forward with great speed, what do they do first? They pull the string BACKWARDS! The pullback is the market gathering power.",
        "lesson_text": (
            "Good evening class, today we learn: *The Trend + Pullback Strategy*\n\n"
            "🎯 *1. THE HOOK: The Bow and Arrow Analogy*\n"
            "If you want to fire an arrow across a soccer pitch, you do not push the arrow with your hand. "
            "You pull the string backwards towards your chest (a pullback), hold your breath, and release! "
            "In Forex, even when price is in a massive uptrend, it cannot move straight up forever. It must pause, "
            "pull back to catch breath, and gather fresh buyers. That pullback is your golden entry window!\n\n"
            "💡 *2. THE 3-STEP TREND + PULLBACK STRATEGY RULES*\n\n"
            "**STEP 1: Determine the Trend (The Compass)**\n"
            "• Look at the **4-Hour (H4)** chart. Is price making Higher Highs (Uptrend) or Lower Lows (Downtrend)?\n"
            "• *Rule:* We ONLY trade in the direction of the H4 trend.\n\n"
            "**STEP 2: Wait Patiently for the Pullback (The Retracement)**\n"
            "• In an Uptrend, do NOT chase green candles at the top! Wait for price to drop back down to an old broken Resistance level (now Support) or a trendline.\n"
            "• In a Downtrend, wait for price to rally back up to an old Support level (now Resistance).\n\n"
            "**STEP 3: Spot the Rejection Candle (The Trigger)**\n"
            "• Once price reaches that level, look for a rejection candlestick (e.g. a green candle with a long lower wick confirming buyers are back).\n"
            "• **Entry:** Place order.\n"
            "• **Stop Loss:** Just below the pullback swing low.\n"
            "• **Take Profit:** At the previous swing high (1:2 Risk-to-Reward ratio).\n\n"
            "📝 *3. SUMMARY & ENCOURAGEMENT*\n"
            "Trading is not about being in the market 24/7. It is like being a sniper hunter: you wait in the bush for 2 hours, "
            "take 1 clean shot, and go home!"
        ),
        "calculation_example": (
            "🔢 *Strategy Execution Numbers:*\n"
            "• Uptrend on EUR/USD: H4 making Higher Highs.\n"
            "• Price pulls back from 1.0920 down to support at 1.0850.\n"
            "• Rejection pin bar forms at 1.0850.\n"
            "• **BUY Entry:** 1.0855\n"
            "• **Stop Loss:** 1.0830 (Risk = 25 pips = $2.50 on 0.01 lot)\n"
            "• **Take Profit:** 1.0915 (Reward = 60 pips = $6.00)\n"
            "• Risk/Reward = 1:2.4!"
        ),
        "voice_script": (
            "Coach Prince here students. Most beginners lose money because of FOMO: Fear Of Missing Out. "
            "They see a massive green candle and buy at the very top, right before the pullback crashes into them! "
            "Never buy at the top. Let the arrow pull back to support, then shoot. Watch the video below."
        ),
        "image_type": "trend_pullback_strategy_diagram",
        "video_title": "The Trend Pullback Trading Strategy - Step by Step",
        "video_url": "https://www.youtube.com/watch?v=K1pW-r49G7Q",
        "video_duration": "9 mins",
        "video_reason": "Clear mechanical strategy with defined entries, stop loss, and take profit rules.",
        "notes_summary": (
            "📌 *Day 10 Key Takeaways Cheatsheet:*\n"
            "1. Step 1: Identify Trend on H4 (Higher Highs / Lower Lows).\n"
            "2. Step 2: Wait for pullback into a Key Support or Resistance zone.\n"
            "3. Step 3: Wait for a candlestick wick rejection trigger.\n"
            "4. Stop Loss goes beyond the swing point.\n"
            "5. Minimum 1:2 Risk-to-Reward ratio on every trade."
        ),
        "assignment": (
            "🎯 *DAY 10 ASSIGNMENT: Spotting a Pullback Setup*\n\n"
            "1. Open EURUSD or GBPUSD on the **1-Hour (H1)** chart.\n"
            "2. Find a previous example where price was trending, pulled back to an old level, and bounced in the trend direction.\n"
            "3. Write down: What was the entry price, where would your SL be placed, and where was the TP?\n\n"
            "📤 *How to Submit:* Reply to Coach Prince with your setup numbers.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Discipline means waiting for the setup to come to you. Analyze the H1 chart and submit your Day 10 numbers!"
        ),
        "correction": (
            "✅ *DAY 10 ASSIGNMENT CORRECTION*\n\n"
            "Well done class! Notice how entering on a pullback gives you a much smaller Stop Loss and a much bigger Take Profit. "
            "That is the secret to high risk-to-reward trading."
        ),
        "quizzes": [
            {
                "question": "Why should you avoid buying immediately after a gigantic green candle has already shot up 100 pips?",
                "options": [
                    "You are buying at the expensive top right before the natural market pullback occurs",
                    "MT5 stops functioning",
                    "Brokers will cancel your order",
                    "Green candles are illegal to buy"
                ],
                "correct_idx": 0,
                "explanation": "Correct! Chasing extended moves leads to buying at the high, right before early buyers take profits and price pulls back."
            },
            {
                "question": "In the Trend + Pullback strategy, what role does the 4-Hour (H4) chart play?",
                "options": [
                    "It acts as our directional compass to confirm the overall market trend",
                    "It is used only on weekends",
                    "It calculates broker commissions",
                    "It generates random numbers"
                ],
                "correct_idx": 0,
                "explanation": "Spot on! The higher timeframe gives you the macro direction so you don't trade against the river current."
            },
            {
                "question": "What is the recommended minimum Risk-to-Reward ratio for this strategy?",
                "options": [
                    "1:0.5 (Risk $2 to make $1)",
                    "1:2 (Risk $1 to make $2 or more)",
                    "10:1 (Risk $10 to make $1)",
                    "No target needed"
                ],
                "correct_idx": 1,
                "explanation": "Well done! With a 1:2 ratio, even if you lose 5 out of 10 trades, you still walk away profitable!"
            }
        ]
    },
    "11": {
        "day": 11,
        "topic": "Risk Management - Never Risk More Than 1-2% Per Trade",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we study the single lesson that separates profitable traders from broke gamblers: *Day 11: Risk Management*.\n"
            "Never risk your rent, chop money, or school fees. Tonight, we master the 1-2% capital preservation rule. "
            "Be there at 7:00 PM! 🇬🇭🛡️"
        ),
        "hook": "If you are a fisherman going out to sea at Jamestown, you do not throw your only fishing net overboard during a storm. You preserve your boat and your net so you can fish again tomorrow!",
        "lesson_text": (
            "Good evening class, today we learn: *Risk Management (The 1-2% Rule)*\n\n"
            "🎯 *1. THE HOOK: The Jamestown Fisherman*\n"
            "A fisherman from Jamestown or Cape Coast knows that bad weather and rough waves will happen. "
            "He never risks his boat on a single risky trip. If one day yields zero fish, he returns safely home "
            "because his boat is intact. In trading, your **capital** is your boat. If your boat sinks, you are out of business!\n\n"
            "💡 *2. THE GOLDEN 1% - 2% RULE*\n"
            "• On any single trade, you must **NEVER risk more than 1% to 2%** of your total account balance.\n"
            "• If your account is **$100**, 1% risk = **$1.00**.\n"
            "• If your account is **$500**, 1% risk = **$5.00**.\n"
            "• If your account is **$1,000**, 1% risk = **$10.00**.\n\n"
            "Why is this so powerful? Because even if you suffer **10 consecutive losses in a row** (which happens to the best traders), "
            "you still have 90% of your account alive and well! But if you risk 20% per trade, 5 losses will wipe you out completely.\n\n"
            "🚫 *THE THREE UNFORGIVABLE SINS IN FOREX:*\n"
            "1. **Never trade with money you cannot afford to lose:** Never trade with school fees, hospital money, rent, or chop money.\n"
            "2. **Never revenge trade:** If a trade hits your Stop Loss, do NOT double your lot size in anger to get back your money. Walk away from the screen!\n"
            "3. **Never remove your Stop Loss:** Hoping that price will 'turn back around' is how accounts are liquidated.\n\n"
            "📝 *3. SUMMARY & ENCOURAGEMENT*\n"
            "Trading longevity is everything. The market will always be here tomorrow. Protect your capital with military discipline!"
        ),
        "calculation_example": (
            "🔢 *Position Sizing Math:*\n"
            "• Account Balance: $200\n"
            "• 2% Maximum Risk = $4.00\n"
            "• Stop Loss distance on chart: 40 pips\n"
            "• Pip value on 0.01 lot = $0.10/pip\n"
            "• 40 pips × $0.10 = $4.00 risk.\n"
            "• ➡️ Exact allowable lot size = **0.01**. Perfect match!"
        ),
        "voice_script": (
            "Coach Prince here students. Listen to me with your two ears: Forex is not a sprint; it is an endurance marathon. "
            "I don't care if a strategy has a 90% win rate—if you risk 25% per trade, one bad day will finish you. "
            "Keep your risk at 1-2%. Watch the video and learn how professional hedge funds manage risk."
        ),
        "image_type": "risk_management_drawdown_table",
        "video_title": "Forex Risk Management & Position Sizing Calculator",
        "video_url": "https://www.youtube.com/watch?v=2TzFm9u2z3U",
        "video_duration": "8 mins",
        "video_reason": "Shows mathematical tables proving why risking 1-2% protects traders from blowout drawdowns.",
        "notes_summary": (
            "📌 *Day 11 Key Takeaways Cheatsheet:*\n"
            "1. Risk 1% to 2% maximum per trade.\n"
            "2. $100 account ➡️ Max risk $1 - $2 per trade.\n"
            "3. 10 losses at 1% = You still have ~90% capital left.\n"
            "4. Never trade with rent, school fees, or emergency money.\n"
            "5. Never revenge trade after a loss!"
        ),
        "assignment": (
            "🎯 *DAY 11 ASSIGNMENT: Calculate Your Maximum Risk*\n\n"
            "Calculate the following on paper:\n"
            "1. If a student has an account of $300, what is the maximum dollar risk at 2%?\n"
            "2. If your Stop Loss is 30 pips away, what lot size gives you approximately that risk?\n"
            "3. Write down: 'I will never trade with money I cannot afford to lose.'\n\n"
            "📤 *How to Submit:* Send your answer to Coach Prince.\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Calculate your risk numbers before you sleep tonight. Risk management is what makes you an unshakeable trader."
        ),
        "correction": (
            "✅ *DAY 11 ASSIGNMENT CORRECTION*\n\n"
            "Here is the breakdown:\n"
            "1. $300 × 2% = **$6.00 maximum risk**.\n"
            "2. With a 30-pip Stop Loss, a 0.02 lot size ($0.20/pip) = 30 × 0.20 = $6.00 risk. (Or a 0.01 lot size for extra safety: $3.00 risk).\n"
            "Discipline in risk management is the secret of veteran traders."
        ),
        "quizzes": [
            {
                "question": "What is the maximum recommended percentage of your account to risk on any single trade?",
                "options": [
                    "1% to 2%",
                    "20% to 50%",
                    "100% (All in)",
                    "15%"
                ],
                "correct_idx": 0,
                "explanation": "Correct! Risking only 1% to 2% ensures you can survive long losing streaks without damaging your capital base."
            },
            {
                "question": "If you have a $200 trading account, what is the maximum dollar amount you should risk per trade at 2%?",
                "options": [
                    "$4.00",
                    "$40.00",
                    "$100.00",
                    "$0.20"
                ],
                "correct_idx": 0,
                "explanation": "Spot on! $200 × 0.02 = $4.00 maximum loss per trade."
            },
            {
                "question": "What is 'Revenge Trading'?",
                "options": [
                    "A regulated trading strategy approved by banks",
                    "Trading aggressively with bigger lot sizes right after a loss out of anger and emotion",
                    "Closing profitable trades early",
                    "Changing currency pairs"
                ],
                "correct_idx": 1,
                "explanation": "Well done! Revenge trading is an emotional response to a loss that almost always leads to blowing an account."
            }
        ]
    },
    "12": {
        "day": 12,
        "topic": "Trading Psychology - Mastering Greed, Fear & Discipline",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we examine the battlefield between your ears: *Day 12: Trading Psychology*.\n"
            "Trading is 20% strategy and 80% emotional control. "
            "Learn how to master Greed, Fear, and FOMO like a seasoned professional. See you at 7:00 PM! 🇬🇭🧠"
        ),
        "hook": "Why does a student who does brilliantly on demo sometimes lose everything when they switch to real money? Because the chart didn't change—their heartbeat and emotions changed!",
        "lesson_text": (
            "Good evening class, today we learn: *Trading Psychology (Greed, Fear & Emotional Control)*\n\n"
            "🎯 *1. THE HOOK: The Heartbeat Shift*\n"
            "Have you noticed that on demo trading, you are relaxed, patient, and you follow all rules? "
            "Why? Because your hard-earned Cedis are not at stake. But the moment real money is introduced, "
            "your pulse quickens, your hands sweat, and fear takes over. "
            "The market does not beat traders—**their own unmanaged emotions beat them!**\n\n"
            "💡 *2. THE THREE EMOTIONAL ENEMIES:*\n\n"
            "👹 **1. GREED:**\n"
            "• Thinking: *'Let me use 1.00 lot so I can buy an iPhone tomorrow.'*\n"
            "• Refusing to take profit when the target is reached, hoping it goes to the moon.\n"
            "• *Cure:* Stick strictly to your planned Take Profit and 0.01 lot size.\n\n"
            "😨 **2. FEAR:**\n"
            "• Fear of losing money makes you close winning trades too early (taking $0.50 profit on a $10 move).\n"
            "• Fear makes you freeze and fail to take high-quality valid setups.\n"
            "• *Cure:* Only risk an amount of money ($1 or $2) you are 100% emotionally prepared to lose.\n\n"
            "🏃‍♂️ **3. FOMO (Fear Of Missing Out):**\n"
            "• Seeing a green candle exploding on Telegram or WhatsApp status and jumping in without any analysis.\n"
            "• *Cure:* The market operates 24 hours a day, 5 days a week. Another setup will come tomorrow. Be patient!\n\n"
            "🧘 *3. THE TRADER'S MINDSET CHECKLIST:*\n"
            "• Accept losses as part of the business, just like a market woman accepts that some tomatoes may spoil.\n"
            "• Never look at the dollar amount during an open trade; look at the percentage and the price levels.\n"
            "• Keep a **Trading Journal**: Write down why you entered, how you felt, and what happened.\n\n"
            "📝 *4. SUMMARY & ENCOURAGEMENT*\n"
            "A calm mind makes sound decisions. Trade like a stoic professional, not an excited gambler."
        ),
        "calculation_example": (
            "🔢 *The 10-Trade Probability Mindset:*\n"
            "• Even with a 60% win rate strategy, you can get 4 losses in a row at random.\n"
            "• Win, Loss, Loss, Loss, Win, Loss, Win, Win, Win, Win.\n"
            "• If you panicked on trade 3 and quit or oversized, you missed the winning streak! Think in blocks of 20 trades."
        ),
        "voice_script": (
            "Good evening students! Coach Prince here. Today's lesson is close to my heart. "
            "Forex will reveal your true character: your patience, your greed, your discipline. "
            "Treat trading like running a clean shop at Makola. You don't scream when one customer walks away; "
            "you smile and serve the next. Watch the video below on psychology."
        ),
        "image_type": "trading_psychology_cycle",
        "video_title": "Trading Psychology: How to Overcome Fear, Greed and FOMO",
        "video_url": "https://www.youtube.com/watch?v=wE4zF24eX1I",
        "video_duration": "9 mins",
        "video_reason": "Relatable breakdown of psychological cycles in financial markets.",
        "notes_summary": (
            "📌 *Day 12 Key Takeaways Cheatsheet:*\n"
            "1. Trading is 80% psychology and 20% strategy.\n"
            "2. Greed leads to overleveraging; Fear leads to premature exits.\n"
            "3. FOMO causes traders to enter at the worst possible prices.\n"
            "4. Accept losses as normal business operating costs.\n"
            "5. Think in blocks of 20 trades, never judge yourself on 1 trade."
        ),
        "assignment": (
            "🎯 *DAY 12 ASSIGNMENT: Your Trading Discipline Code*\n\n"
            "1. Which emotion do you struggle with the most: Greed (wanting fast money), Fear (scared to lose), or FOMO (jumping in late)?\n"
            "2. Write down your personal rule for dealing with that emotion.\n"
            "3. Send your answer to Coach Prince in private chat.\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Be honest with yourself tonight. Identifying your emotional weakness is the first step to conquering it!"
        ),
        "correction": (
            "✅ *DAY 12 ASSIGNMENT FEEDBACK*\n\n"
            "I loved reading your honest reflections. Almost every beginner deals with FOMO or fear of losing. "
            "Recognizing it before you click Buy or Sell is what protects your balance. Excellent maturity, class!"
        ),
        "quizzes": [
            {
                "question": "What is 'FOMO' in Forex trading psychology?",
                "options": [
                    "Foreign Orders Monthly Output",
                    "Fear Of Missing Out—rushing into trades without a valid setup because price is already moving fast",
                    "A trading fee charged by banks",
                    "A type of chart indicator"
                ],
                "correct_idx": 1,
                "explanation": "Correct! FOMO makes traders impulsively buy at tops and sell at bottoms because they fear missing profits."
            },
            {
                "question": "How should a disciplined trader view a losing trade?",
                "options": [
                    "As a personal failure that must be avenged immediately",
                    "As a normal business operating cost that is kept small with a Stop Loss",
                    "As proof that Forex is rigged",
                    "By deleting MT5"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! Just like any business incurs expenses, small losses are the natural operating cost of trading."
            },
            {
                "question": "Why is keeping a Trading Journal recommended by top professionals?",
                "options": [
                    "To show off on social media",
                    "To track your setups, emotions, and mistakes so you can systematically improve",
                    "Because Telegram requires it",
                    "To print it for the broker"
                ],
                "correct_idx": 1,
                "explanation": "Well done! A journal turns random guesses into measurable, improvable professional data."
            }
        ]
    },
    "13": {
        "day": 13,
        "topic": "Live Demo Trading Together - Step-by-Step Execution Walkthrough",
        "teaser": (
            "🌅 *Good morning class! Coach Prince here.*\n\n"
            "Tonight at *7:00 PM GMT*, we put everything together: *Day 13: Live Demo Trading Walkthrough*.\n"
            "We go through the full 5-step checklist from opening the chart to setting the Stop Loss and closing the trade. "
            "Have MT5 open on your phone tonight! 🇬🇭🚀"
        ),
        "hook": "Before an airplane takes off from Kotoka Airport, the pilot and co-pilot run through a written pre-flight checklist: fuel, engines, flaps, radio. Today, we build your pre-trade checklist!",
        "lesson_text": (
            "Good evening class, today we do: *Live Demo Trading Walkthrough*\n\n"
            "🎯 *1. THE HOOK: The Pilot's Pre-Flight Checklist*\n"
            "A pilot never says: *'I feel like taking off today without checking fuel.'* "
            "They pull out their physical clipboard and check every box. If even one box fails, the plane does not leave the tarmac! "
            "From today onwards, you never place a trade without going through your 5-point checklist.\n\n"
            "📋 *COACH PRINCE'S 5-POINT PRE-TRADE CHECKLIST:*\n\n"
            "1. **Trend Check (H4 Chart):**\n"
            "   - Is the overall market making Higher Highs (Bullish) or Lower Lows (Bearish)?\n"
            "   - *Rule:* Only trade in this direction.\n\n"
            "2. **Key Level Check (Support/Resistance):**\n"
            "   - Has price pulled back into a meaningful zone? (Old broken resistance or strong support floor).\n\n"
            "3. **Candlestick Rejection Trigger:**\n"
            "   - Is there a clear rejection wick confirming buyers or sellers are entering?\n\n"
            "4. **Risk Calculation:**\n"
            "   - Is my lot size strictly **0.01**?\n"
            "   - Is my risk less than **2%** of my account?\n\n"
            "5. **Order Execution & Set SL/TP:**\n"
            "   - Enter order, set Stop Loss below swing point, set Take Profit at minimum 1:2 ratio.\n"
            "   - Close the app and let the trade play out without staring at it!\n\n"
            "📝 *2. SUMMARY & ENCOURAGEMENT*\n"
            "Trading with a checklist removes emotion and guarantees professional consistency. "
            "Practice this exact walkthrough on your demo today!"
        ),
        "calculation_example": (
            "🔢 *Pre-Trade Walkthrough Checklist in Action:*\n"
            "• Pair: EUR/USD\n"
            "• H4 Trend: Uptrend ✅\n"
            "• Key Level: 1.0850 Support Floor ✅\n"
            "• Candle: 1-hour bullish hammer with lower wick rejection ✅\n"
            "• Lot Size: 0.01 ✅\n"
            "• Risk: 25 pips ($2.50) / Reward: 50 pips ($5.00) (1:2 ratio) ✅\n"
            "➡️ All 5 boxes checked! Safe to execute."
        ),
        "voice_script": (
            "Hello students! Coach Prince here. Tonight we are acting like airline captains. "
            "Never guess or hope. Pull out your 5-point checklist. If all 5 conditions are met, place the demo trade with confidence. "
            "If even one condition is missing, you wait! Watch the live walkthrough video below."
        ),
        "image_type": "pre_trade_checklist_diagram",
        "video_title": "Live Trade Execution Walkthrough on MT5 Step-by-Step",
        "video_url": "https://www.youtube.com/watch?v=Vp6_1-8j_s0",
        "video_duration": "9 mins",
        "video_reason": "Full live screen demonstration checking all conditions before placing orders.",
        "notes_summary": (
            "📌 *Day 13 Key Takeaways Cheatsheet:*\n"
            "1. Box 1: H4 Trend direction confirmed.\n"
            "2. Box 2: Price at Key Support or Resistance zone.\n"
            "3. Box 3: Candlestick rejection wick present.\n"
            "4. Box 4: 0.01 Lot size & maximum 2% risk calculated.\n"
            "5. Box 5: SL and TP entered immediately upon execution."
        ),
        "assignment": (
            "🎯 *DAY 13 ASSIGNMENT: Execute a Checklist Demo Trade*\n\n"
            "1. Open your MT5 Demo account.\n"
            "2. Follow all 5 steps of the checklist.\n"
            "3. Place 1 trade with 0.01 lot size, SL, and TP.\n"
            "4. Send a text to Coach Prince listing: Pair, Entry, SL, TP, and why you entered!\n\n"
            "⏰ *Deadline:* Tomorrow 12:00 PM GMT."
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Reminder:*\n"
            "Execute your checklist trade on MT5 tonight. Tomorrow is our grand graduation day! Finish strong."
        ),
        "correction": (
            "✅ *DAY 13 ASSIGNMENT FEEDBACK*\n\n"
            "Superb execution! I reviewed many submissions and loved seeing students wait for valid levels instead of "
            "pressing buttons blindly. You are trading like true professionals now."
        ),
        "quizzes": [
            {
                "question": "What should a trader do if 4 out of 5 checklist conditions are met, but 1 condition is missing?",
                "options": [
                    "Wait patiently on the sidelines until all conditions are satisfied",
                    "Double the lot size to compensate",
                    "Place the trade anyway because 4 is close enough",
                    "Switch to real money"
                ],
                "correct_idx": 0,
                "explanation": "Correct! If even one condition is missing, professional discipline dictates that you wait for a cleaner opportunity."
            },
            {
                "question": "Why should you close the MT5 app after placing your trade with SL and TP set?",
                "options": [
                    "To save phone battery",
                    "To prevent emotional micromanagement, panic exits, and stress",
                    "Because MT5 disconnects when watched",
                    "So the broker cannot find you"
                ],
                "correct_idx": 1,
                "explanation": "Spot on! Staring at every pip fluctuation induces anxiety and causes traders to interfere with good trades."
            },
            {
                "question": "What is the biggest advantage of using a written pre-trade checklist?",
                "options": [
                    "It eliminates emotional impulse trades and enforces repeatable consistency",
                    "It ensures 100% win rate every day",
                    "It gives you free Cedis from your broker",
                    "It makes the market move twice as fast"
                ],
                "correct_idx": 0,
                "explanation": "Well done! A checklist transforms emotional gambling into structured, systematic trading execution."
            }
        ]
    },
    "14": {
        "day": 14,
        "topic": "Graduation, Language of the Market & Coach Prince's Ultimate Strategy",
        "teaser": (
            "🎓 *Good morning class! Coach Prince here.*\n\n"
            "Today is our *GRAND GRADUATION DAY: Day 14!* 🇬🇭🎉\n"
            "You have journeyed from total zero to truly understanding the **Language of the Market** "
            "(Candlestick Wicks, Market Structure, BOS, CHoCH, Supply & Demand, and Risk Management)!\n\n"
            "Tonight at *7:00 PM GMT*, we celebrate your graduation with your official **Certificate of Completion**, "
            "AND I unveil my personal **Ultimate Strategy Masterclass (Top-Down Execution Trap)** for those ready to trade like masters!\n"
            "Get ready for a historic class! 📜🎓⭐"
        ),
        "hook": "Two weeks ago, you didn't know what a Pip, a Lot, or a Candlestick was. Today, you understand the true language of the market: how institutions move price, how to spot Break of Structure, and how to protect your capital. Look at how far you have come!",
        "lesson_text": (
            "Good evening class, today we celebrate: *Graduation, The Language of the Market & The Ultimate Strategy*\n\n"
            "🎯 *1. THE CELEBRATION: You Now Speak the Language of the Market!*\n"
            "Two weeks ago, Forex charts looked like random zigzag lines. Today, you can read the market like a open book:\n"
            "• **Candlesticks:** You don't just see green and red; you see buyers and sellers fighting for liquidity, and rejection wicks showing where price was defended.\n"
            "• **Market Structure:** You understand Higher Highs (HH) & Higher Lows (HL) in an uptrend, and Lower Lows (LL) & Lower Highs (LH) in a downtrend.\n"
            "• **BOS & CHoCH:** You spot Break of Structure (trend continuation) and Change of Character (the early warning sign of trend reversal).\n"
            "• **Order Blocks & Fair Value Gaps (FVG):** You know where banks left huge orders and where price must return to fill liquidity.\n"
            "• **Risk Management:** You know that 0.01 micro lot and 1-2% risk is your lifetime armor.\n\n"
            "I, Coach Prince, am extremely proud of every single one of you!\n\n"
            "📜 *2. HOW TO CLAIM YOUR FREE GRADUATION CERTIFICATE:*\n"
            "1. Take tonight's Final Graduation Quiz below.\n"
            "2. Score at least 2 out of 3 questions correctly.\n"
            "3. Send the command `/certificate` to Coach Prince in private chat, and the bot will generate "
            "your official, personalized **Forex Fundamentals Certificate of Completion**!\n\n"
            "⭐ *3. THE NEXT LEVEL: COACH PRINCE'S ULTIMATE STRATEGY (200 TELEGRAM STARS)*\n"
            "For students who have mastered this foundation and want to take the final leap into professional trading, "
            "I have packaged my personal institutional trading system:\n"
            "👑 **Coach Prince's Ultimate Strategy: Top-Down Multi-Timeframe Execution & POI Sniping**\n\n"
            "Inside this Masterclass:\n"
            "• **Daily (D1):** Read macro bias and identify current boundaries (Buy / Sell / Stay Off).\n"
            "• **4-Hour (H4):** Refine structural zones and discard ancient history.\n"
            "• **1-Hour (H1):** Spot unmitigated origins and Fair Value Gaps (Mitigated = Weak Liquidity!).\n"
            "• **15-Minute (M15):** The Execution Trap — set tight Stop Loss behind rejection wicks and target 1:3 to 1:5+ RR.\n"
            "• **Full Video Masterclass Link + High-Res Strategy Blueprint Chart + Lifetime VIP Access.**\n\n"
            "👉 *How to Unlock:* Send `/strategy` to Coach Prince in private chat to unlock with **200 Telegram Stars**!\n\n"
            "📝 *4. FINAL BLESSING FROM COACH PRINCE*\n"
            "May your trading journey be filled with patience, humility, and steady growth. Protect your money first, "
            "never gamble, and let discipline guide every click. Congratulations, Graduates!"
        ),
        "calculation_example": (
            "🔢 *The 1-Year Compound Growth Vision:*\n"
            "• If you grow a $100 account by just 5% to 8% per month with disciplined risk management:\n"
            "• In 12 months, you build habits worth thousands of dollars. The skill you acquired cannot be taken away!"
        ),
        "voice_script": (
            "My dear students! Coach Prince here on our final graduation night. I salute your persistence. "
            "You now understand the language of the market. Claim your graduation certificate with /certificate, "
            "and if you are ready to master my personal top-down execution strategy, type /strategy to unlock the masterclass! "
            "Discipline over greed, forever. God bless you all!"
        ),
        "image_type": "graduation_safe_live_roadmap",
        "video_title": "Coach Prince's Ultimate Strategy: Top-Down Multi-Timeframe Analysis",
        "video_url": "https://youtu.be/Sdj6XbXbowM?si=if7Lig8J0A02suPV",
        "video_duration": "14 mins",
        "video_reason": "Coach Prince's masterclass breaking down the power of top-down analysis from Daily to 15M entry traps.",
        "notes_summary": (
            "📌 *Graduate's Permanent Code of Conduct:*\n"
            "1. Speak the language of the market: Read structure, BOS, CHoCH, and FVG.\n"
            "2. Trade demo for at least 30 more days before going live.\n"
            "3. Start live with small capital ($50 - $100) and 0.01 lot only.\n"
            "4. Never risk more than 1% - 2% per trade.\n"
            "5. Never trade with rent, school fees, or emergency money.\n"
            "6. Always use a Stop Loss on every single position!\n"
            "7. Type /strategy to unlock Coach Prince's 200 Stars Masterclass."
        ),
        "assignment": (
            "🎯 *DAY 14 FINAL ASSIGNMENT: Claim Your Certificate & Graduation Post*\n\n"
            "1. Complete the Day 14 Final Test below.\n"
            "2. Type `/certificate` in private chat with Coach Prince to receive your graduation certificate.\n"
            "3. Share a short message in the Discussion Group about what was the #1 most valuable lesson you learned over these 14 days!\n"
            "4. Optional: Type `/strategy` in private chat to unlock Coach Prince's 200 Stars Ultimate Strategy Masterclass!\n\n"
            "🎉 *Congratulations to all graduates of Candlemaster Academy!*"
        ),
        "assignment_reminder": (
            "🔔 *Coach Prince Graduation Reminder:*\n"
            "Take the final test and type /certificate to receive your official graduation certificate! "
            "To unlock Coach Prince's Top-Down Masterclass, send /strategy in private chat. You earned it!"
        ),
        "correction": (
            "🎓 *CONGRATULATIONS GRADUATES OF CANDLEMASTER ACADEMY!*\n\n"
            "You have officially completed the 14-Day Forex Fundamentals Curriculum. "
            "You now speak the language of the market. Continue practicing on demo, stay active in our Discussion Group, "
            "and remember: Capital preservation comes first. Type /strategy anytime to review Coach Prince's Ultimate Strategy!"
        ),
        "quizzes": [
            {
                "question": "What is the very first step before depositing real money into a live broker?",
                "options": [
                    "Borrowing money from friends or taking a bank loan",
                    "Consistently practicing on a Demo account for at least 30 to 60 days with a trading journal",
                    "Buying expensive VIP signals from WhatsApp",
                    "Quitting your job"
                ],
                "correct_idx": 1,
                "explanation": "Correct! Demo mastery is the only safe bridge before risking real hard-earned Cedis."
            },
            {
                "question": "When you eventually open your first live account, what lot size and risk rule should you follow?",
                "options": [
                    "0.01 micro lot with maximum 1-2% risk per trade",
                    "1.00 lot to double your money in 24 hours",
                    "No Stop Loss so you never take a loss",
                    "Deposit your entire school fees"
                ],
                "correct_idx": 0,
                "explanation": "Spot on! Starting with 0.01 micro lot and 1-2% risk keeps your emotions calm and your capital protected."
            },
            {
                "question": "What is the golden motto of Coach Prince and Candlemaster Academy?",
                "options": [
                    "Get rich quick with 100x leverage",
                    "Discipline over greed, protect capital first, and master the skill step-by-step",
                    "Signals are better than education",
                    "Never use a Stop Loss"
                ],
                "correct_idx": 1,
                "explanation": "Well done! Discipline, risk management, and step-by-step education are the true pillars of lasting success in Forex."
            }
        ]
    }
}

with open("lessons.json", "w", encoding="utf-8") as f:
    json.dump(lessons_data, f, indent=2, ensure_ascii=False)

print("Successfully generated lessons.json with all 14 comprehensive days!")

