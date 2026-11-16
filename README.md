# 🇬🇭 Candlemaster Academy - AI Teacher Bot (Coach Prince)

**Coach Prince** is an automated AI Forex teacher that operates completely **in place of you (the owner)** for **Candlemaster Academy**. 

### 💡 Core Concept: Students Never Need to Start the Bot!
- **You (the Owner)** are the one who starts and controls the bot.
- **Students do NOT need to click `/start` or message the bot in private.**
- Students simply join your 2 Channels and Discussion Group:
  1. **Channel 1 (@ForexLessonsGH):** Students read lessons, view charts, watch verified YouTube videos, and take interactive **Telegram Quiz Polls** directly inside the channel with 1 tap!
  2. **Channel 2 (@ForexAssignmentsGH):** Students see their daily homework assignments, reminders, and next-day solutions.
  3. **Discussion Group:** Students ask questions. Coach Prince replies to them 24/7 like a patient Ghanaian teacher, explaining big words, using relatable Ghana examples (Cedis, Dollars, Makola, Trotro), checking if they understood, and re-explaining if they say NO.

---

## 🏛️ System Architecture

```
                               ┌────────────────────────────────────────┐
                               │   YOU (OWNER / TEACHER)                │
                               │   Starts bot & controls curriculum     │
                               └───────────────────┬────────────────────┘
                                                   │
                                                   ▼
                               ┌────────────────────────────────────────┐
                               │      Coach Prince (AI Teacher Bot)       │
                               │      Teaches in place of you 24/7      │
                               └───────────────────┬────────────────────┘
                                                   │
        ┌──────────────────────────────────────────┼──────────────────────────────────────────┐
        ▼                                          ▼                                          ▼
CHANNEL 1: LESSONS                         CHANNEL 2: ASSIGNMENTS                     DISCUSSION GROUP
@ForexLessonsGH                            @ForexAssignmentsGH                        Forex Beginners Discussion
• Morning Teaser at 9:00 AM GMT            • Daily Task at 7:30 PM GMT                • Linked to Channel 1
• Full Lesson + Chart at 7:00 PM GMT       • Night Reminder at 9:30 PM GMT            • Students ask questions freely
• 3 Native Quiz Polls at 7:15 PM GMT       • Next-Day Answer at 12:00 PM GMT          • Coach Prince answers 24/7
  (Students tap to vote in channel!)                                                    (3-step human teaching loop)
```

---

## ⏰ Daily Automated Schedule (Ghana Time — GMT)

| Time (GMT) | Destination | Content Posted |
| :---: | :--- | :--- |
| **09:00 AM** | Channel 1 (`@ForexLessonsGH`) | **Morning Teaser:** *"Tonight 7pm — Day X: [Topic]. Get ready."* |
| **07:00 PM** | Channel 1 (`@ForexLessonsGH`) | **Full Lesson:** Text + Educational Diagram Chart + Verified YouTube Video + Voice Note Script + Safety Disclaimer |
| **07:15 PM** | Channel 1 (`@ForexLessonsGH`) | **Interactive Flash Quiz:** 3 Native Telegram Quiz Polls posted directly to the channel (Students vote with 1 tap, no bot start required!) |
| **07:30 PM** | Channel 2 (`@ForexAssignmentsGH`) | **Daily Assignment:** Clear practice task on MT5 Demo account + submission guidelines |
| **09:30 PM** | Channel 2 (`@ForexAssignmentsGH`) | **Night Reminder:** Gentle reminder to practice and complete the assignment |
| **12:00 PM** | Channel 2 (`@ForexAssignmentsGH`) | **Correction Post:** Detailed answer + common beginner mistakes + automatically advances to next day! |
| **24/7 Anytime** | Discussion Group | **Q&A Teaching:** Coach Prince tags students and answers questions in 3 steps |

---

## 👨‍🏫 Coach Prince's Teaching Personality & Guardrails

- **Persona:** Warm, patient, fatherly Ghanaian teacher (SHS level).
- **Relatable Ghana Analogies:** Kwame Nkrumah Circle Forex Bureau, Kejetia Market, Makola Market women, Trotro fares, and MTN MoMo.
- **3-Step Answering Method (Discussion Group):**
  1. **Simple Answer:** Direct, clear, zero jargon.
  2. **Real-Life Ghana Example:** Relatable story with Cedis/Dollars/Market.
  3. **Check Understanding:** *"Does that make sense? Reply with YES or NO."*
- **Adaptive Re-Explanation:** If the student replies `"NO"` or `"I don't understand"`, Coach Prince apologizes warmly and explains with a **brand new analogy**.
- **Anti-Scam & Anti-Signal Guardrail:**
  - If a student asks for signals, deposits, or "double money", Coach Prince rebuffs firmly:
    > *"We don't do that here. In Candlemaster Academy, we learn to protect our money first. Let's focus on today's lesson."*
- **Zero Real Money Pressure:** Students are trained strictly on MT5 Demo accounts with **1-2% risk** and **0.01 micro lot** sizing.

---

## 📅 The 14-Day Curriculum

- **Day 1:** What is Forex? (Buying/Selling currencies, Forex bureau example)
- **Day 2:** Currency Pairs & Trading Sessions (Best time in Ghana: 1:00 PM - 4:00 PM GMT)
- **Day 3:** Downloading MT5 & Creating a Demo Account (Flight simulator)
- **Day 4:** Japanese Candlesticks (Green = Buyers won, Red = Sellers won)
- **Day 5:** Pips, Lots & Leverage (0.01 micro lot = $0.10/pip safety rule)
- **Day 6:** Buy/Sell, Stop Loss & Take Profit (Your seatbelt & destination)
- **Day 7:** Midway Review, Q&A & Foundation Test
- **Day 8:** Support & Resistance (Floor and ceiling bounce zones)
- **Day 9:** Market Trends (Uptrend Higher Highs vs Downtrend Lower Lows)
- **Day 10:** Simple Strategy (Trend + Pullback technique)
- **Day 11:** Risk Management (Never risk more than 1-2%, protect chop money/rent)
- **Day 12:** Trading Psychology (Mastering Greed, Fear, and FOMO)
- **Day 13:** Live Demo Trading Walkthrough (5-point pre-flight checklist)
- **Day 14:** Final Graduation Test, Digital Certificate & Safe Live Roadmap

---

## 🚀 Setup Instructions for the Owner (Non-Technical Guide)

### STEP 1: Create Your Bot on BotFather
1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`.
3. Set bot name: `Coach Prince | Forex Teacher`.
4. Set username: e.g. `ForexTeacherGHBot`.
5. Copy the **HTTP API Token** (e.g. `789123456:AAH...`).

---

### STEP 2: Create Channels & Group on Telegram
1. **Channel 1 (Lessons):** Create a Public Channel named `Forex Lessons GH` (e.g. `@ForexLessonsGH`).
2. **Channel 2 (Assignments):** Create a Public Channel named `Forex Assignments GH` (e.g. `@ForexAssignmentsGH`).
3. **Discussion Group:** Create a Group named `Forex Beginners Discussion`.

---

### STEP 3: Link Discussion Group to Channel 1
1. Open **Channel 1 (Forex Lessons GH)** ➡️ Tap Channel Title ➡️ Tap the **Pencil (Edit)** icon.
2. Tap **Discussion** ➡️ Link the **Forex Beginners Discussion** group ➡️ Save.

---

### STEP 4: Add Bot as Administrator
> [!IMPORTANT]
> The bot must be an Administrator with permission to post messages!

1. In **Channel 1**: Channel Info ➡️ Administrators ➡️ Add your bot ➡️ Enable **Post Messages**.
2. In **Channel 2**: Channel Info ➡️ Administrators ➡️ Add your bot ➡️ Enable **Post Messages**.
3. In **Discussion Group**: Add your bot as an Administrator so it can read and reply to student questions.

---

### STEP 5: Configure `.env`
Open the `.env` file and enter your details:

```env
# Token from @BotFather
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ_your_token_here

# Channel 1: Lessons
LESSONS_CHANNEL_ID=@ForexLessonsGH

# Channel 2: Assignments
ASSIGNMENTS_CHANNEL_ID=@ForexAssignmentsGH

# Group: Discussion Group
DISCUSSION_GROUP_ID=@YourDiscussionGroupUsername

# Your personal Telegram User ID (Message @userinfobot on Telegram to get your ID)
ADMIN_IDS=123456789

# AI API Keys (Optional - Bot works 100% with built-in offline brain if left empty!)
GEMINI_API_KEY=
OPENAI_API_KEY=

# Timezone (Ghana is GMT / UTC+0 year-round)
TIMEZONE=Africa/Accra
```

---

### STEP 6: Run Diagnostic Check & Start
Run the diagnostic script to ensure tokens and permissions are working:
```bash
python setup_check.py
```

Then start Coach Prince:
```bash
python bot.py
```

---

## 🎮 Owner Commands (Your Control Panel)

Send these commands to the bot from your admin Telegram account:

| Command | What it does |
| :--- | :--- |
| `/start` | Opens your **Teacher Control Panel** showing active day and scheduler status |
| `/start_teaching` | **Kicks off Day 1 immediately** — posts morning brief, lesson, chart, 3 quiz polls, and assignment! |
| `/post` | Force posts today's full package (Lesson + Chart + 3 Quiz Polls + Assignment) right now |
| `/post Day [X]` | Force posts a specific day immediately (e.g. `/post 2`) |
| `/post_quiz` | Sends today's 3 interactive Telegram native quiz polls to Channel 1 |
| `/next_day` | Advances the curriculum to the next day |
| `/set_day [1-14]` | Jumps active curriculum to any specific day |
| `/pause` | Pauses automated scheduled daily posting |
| `/resume` | Resumes automated scheduled daily posting |
| `/announce [msg]` | Broadcasts an official announcement to both channels simultaneously |
| `/status` | View live operational status, active day, student questions & VIP sales |
| `/strategy` | Access Coach Prince's Ultimate Strategy Masterclass Blueprint |
| `/vip_list` | View all students who paid 200 Telegram Stars and total revenue |
| `/grant_vip [user_id]` | Manually grant free VIP strategy access to any student |
| `/submissions [day]` | View student homework submissions for any curriculum day |
| `/leaderboard` | View top 5 performing students in the academy |
| `/help` | Comprehensive help guide for teacher commands |

---

## 🎓 Student Commands Reference

Students have access to these interactive commands in private chat:

| Command | What it does |
| :--- | :--- |
| `/start` | Welcome hub with interactive quick action buttons |
| `/today` | Read today's lesson text and chart on demand |
| `/notes` | View today's summary cheatsheet |
| `/my_progress` | View personal quiz score, accuracy %, homework submissions & VIP status |
| `/leaderboard` | See the top academy students ranked by accuracy and homework discipline |
| `/certificate` | Claim personalized Certificate of Completion (Day 14) |
| `/strategy` | Unlock or review Coach Prince's Ultimate Strategy Masterclass (200 Stars) |
| `/help` | Complete student guide to learning in Candlemaster Academy |

---

## ⭐ Coach Prince's Ultimate Strategy (200 Telegram Stars Masterclass)

On **Day 14 (Graduation)**, students celebrate mastering the **Language of the Market** (Candlestick wicks, Market Structure, BOS, CHoCH, Order Blocks, and FVG).

Students can then unlock the **Capstone Masterclass: Coach Prince's Ultimate Strategy**:
- **Price:** 200 Telegram Stars (`XTR`), processed automatically via Telegram's native Stars payment engine.
- **Top-Down 5-Tier Framework:** Daily (Macro Bias) ➡️ 4H (Refinement) ➡️ 1H (Internal Structure & FVG) ➡️ 15M (Execution Trap with tight SL behind rejection wicks & 1:3 to 1:5+ RR).
- **Masterclass Delivery:** Instantly delivers the custom high-res infographic blueprint (`coach_prince_ultimate_strategy.png`), detailed case study rules, and direct video masterclass link (`https://youtu.be/Sdj6XbXbowM?si=if7Lig8J0A02suPV`).

---

## 🌐 24/7 Cloud Hosting for Free (Render / Railway)

To keep Coach Prince teaching 24/7 without keeping your laptop on:

1. Push this project folder to your GitHub repository.
2. Sign up for free at [render.com](https://render.com).
3. Create a **New Background Worker** using the included `render.yaml` or `Procfile`.
4. Add your `BOT_TOKEN` in the Environment Variables on Render.
5. Deploy! Coach Prince will run in the cloud, post on time every day, and answer your students 24/7.
