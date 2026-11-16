"""
Chart and Educational Diagram Generator for Forex Beginners GH.
Generates visual learning charts and graduation certificates using Pillow and Matplotlib.
"""

import os
from io import BytesIO
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for server environments
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ensure charts cache directory exists
CHARTS_DIR = os.path.join(os.path.dirname(__file__), "generated_charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

def generate_candlestick_anatomy_chart() -> str:
    """Generates an educational diagram of Bullish vs Bearish Candlesticks."""
    output_path = os.path.join(CHARTS_DIR, "candlestick_anatomy.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    # Green Bullish Candle (Left)
    ax.plot([2, 2], [1, 9], color='#22c55e', linewidth=3)  # Wick
    rect_bull = patches.Rectangle((1.5, 3), 1, 4, linewidth=2, edgecolor='#22c55e', facecolor='#22c55e')
    ax.add_patch(rect_bull)

    # Red Bearish Candle (Right)
    ax.plot([6, 6], [1, 9], color='#ef4444', linewidth=3)  # Wick
    rect_bear = patches.Rectangle((5.5, 3), 1, 4, linewidth=2, edgecolor='#ef4444', facecolor='#ef4444')
    ax.add_patch(rect_bear)

    # Bullish Labels
    ax.text(2, 9.3, "High (Highest Price)", color='#f8fafc', ha='center', fontsize=10, weight='bold')
    ax.text(2, 0.5, "Low (Lowest Price)", color='#f8fafc', ha='center', fontsize=10, weight='bold')
    ax.text(0.7, 7, "Close ->", color='#22c55e', ha='right', fontsize=10, weight='bold')
    ax.text(0.7, 3, "Open ->", color='#22c55e', ha='right', fontsize=10, weight='bold')
    ax.text(2, 5, "REAL BODY\n(Buyers Won)", color='#ffffff', ha='center', va='center', fontsize=9, weight='bold')
    ax.text(2, -0.8, "BULLISH CANDLE\n(Price Moved UP)", color='#22c55e', ha='center', fontsize=11, weight='bold')

    # Bearish Labels
    ax.text(6, 9.3, "High (Highest Price)", color='#f8fafc', ha='center', fontsize=10, weight='bold')
    ax.text(6, 0.5, "Low (Lowest Price)", color='#f8fafc', ha='center', fontsize=10, weight='bold')
    ax.text(7.3, 7, "<- Open", color='#ef4444', ha='left', fontsize=10, weight='bold')
    ax.text(7.3, 3, "<- Close", color='#ef4444', ha='left', fontsize=10, weight='bold')
    ax.text(6, 5, "REAL BODY\n(Sellers Won)", color='#ffffff', ha='center', va='center', fontsize=9, weight='bold')
    ax.text(6, -0.8, "BEARISH CANDLE\n(Price Moved DOWN)", color='#ef4444', ha='center', fontsize=11, weight='bold')

    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-1.5, 10.5)
    ax.axis('off')
    plt.title("Coach Prince's Candlestick Anatomy Guide (Candlemaster Academy)", 
              color='#38bdf8', fontsize=14, weight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_support_resistance_chart() -> str:
    """Generates Support and Resistance bounce diagram."""
    output_path = os.path.join(CHARTS_DIR, "support_resistance.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    # Price path
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 8, 5, 8.1, 5.1, 8.2, 5.0, 9.5, 10]
    ax.plot(x, y, color='#38bdf8', linewidth=2.5, marker='o', markersize=6)

    # Resistance line (Ceiling)
    ax.axhline(8, color='#ef4444', linestyle='--', linewidth=2.5)
    ax.text(0.2, 8.3, "CEILING / RESISTANCE (Sellers step in - Look to SELL)", color='#ef4444', fontsize=10, weight='bold')

    # Support line (Floor)
    ax.axhline(5, color='#22c55e', linestyle='--', linewidth=2.5)
    ax.text(0.2, 4.4, "FLOOR / SUPPORT (Buyers step in - Look to BUY)", color='#22c55e', fontsize=10, weight='bold')

    # Annotations
    ax.annotate("Bounce Down", xy=(3, 8.1), xytext=(3, 9.2),
                arrowprops=dict(facecolor='#ef4444', shrink=0.08, width=2),
                color='#fca5a5', weight='bold', ha='center')
    ax.annotate("Bounce Up", xy=(4, 5.1), xytext=(4, 3.8),
                arrowprops=dict(facecolor='#22c55e', shrink=0.08, width=2),
                color='#86efac', weight='bold', ha='center')

    ax.set_ylim(3, 11)
    ax.set_xlim(-0.5, 8.5)
    ax.axis('off')
    plt.title("Support & Resistance: The Floor & Ceiling Principle", color='#f8fafc', fontsize=13, weight='bold', pad=12)

    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_trend_diagram() -> str:
    """Generates Trend diagram showing Higher Highs & Higher Lows."""
    output_path = os.path.join(CHARTS_DIR, "market_trends.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    # Uptrend path
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [2, 5, 3.5, 7, 5.2, 9, 7.5]
    ax.plot(x, y, color='#22c55e', linewidth=3, marker='o', markersize=7)

    # Trendline
    ax.plot([0, 6], [1.7, 7.3], color='#fbbf24', linestyle='-', linewidth=2.5, label='Ascending Trendline')

    # Higher Highs (HH)
    ax.text(1, 5.4, "HH 1\n(1.0850)", color='#86efac', ha='center', weight='bold', fontsize=9)
    ax.text(3, 7.4, "HH 2\n(1.0920)", color='#86efac', ha='center', weight='bold', fontsize=9)
    ax.text(5, 9.4, "HH 3\n(1.0990)", color='#86efac', ha='center', weight='bold', fontsize=9)

    # Higher Lows (HL)
    ax.text(0, 1.2, "Low\n(1.0780)", color='#fde047', ha='center', weight='bold', fontsize=9)
    ax.text(2, 2.7, "HL 1\n(1.0815)", color='#fde047', ha='center', weight='bold', fontsize=9)
    ax.text(4, 4.4, "HL 2\n(1.0870)", color='#fde047', ha='center', weight='bold', fontsize=9)

    ax.text(0.5, 8.5, "UPTREND = Higher Highs (HH) + Higher Lows (HL)\nGolden Rule: ONLY LOOK FOR BUY TRADES!", 
            color='#38bdf8', fontsize=11, weight='bold', bbox=dict(boxstyle="round,pad=0.5", facecolor='#334155', edgecolor='#38bdf8'))

    ax.set_ylim(0.5, 10.5)
    ax.axis('off')
    plt.title("Understanding Market Trends - Riding The River Current", color='#f8fafc', fontsize=13, weight='bold', pad=12)

    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_sessions_chart() -> str:
    """Generates Trading Sessions Timeline focused on Ghana GMT."""
    output_path = os.path.join(CHARTS_DIR, "trading_sessions.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    sessions = [
        ("Sydney", 22, 31, '#64748b'),      # 10 PM to 7 AM (next day)
        ("Tokyo (Asia)", 0, 9, '#3b82f6'),    # 12 AM to 9 AM
        ("London", 8, 16, '#10b981'),        # 8 AM to 4 PM
        ("New York", 13, 22, '#f59e0b')      # 1 PM to 10 PM
    ]

    y_pos = [3, 2, 1, 0]
    for (name, start, end, color), y in zip(sessions, y_pos):
        width = end - start
        ax.barh(y, width, left=start if start < 24 else start-24, height=0.5, color=color, edgecolor='#ffffff', linewidth=1)
        ax.text(start + 0.5 if start < 24 else 0.5, y, f"{name}", color='#ffffff', va='center', weight='bold', fontsize=10)

    # Highlight Overlap Window (13:00 to 16:00 GMT)
    ax.axvspan(13, 16, color='#22c55e', alpha=0.25, label='London / NY Overlap')
    ax.text(14.5, 3.6, "GOLDEN GHANA WINDOW (1:00 PM - 4:00 PM GMT)\nLondon & NY Overlap = Peak Movement!", 
            color='#4ade80', ha='center', weight='bold', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#1e293b', edgecolor='#4ade80'))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(["New York", "London", "Tokyo", "Sydney"], color='#cbd5e1', weight='bold')
    ax.set_xticks(range(0, 25, 2))
    ax.set_xticklabels([f"{h:02d}:00" for h in range(0, 25, 2)], color='#cbd5e1')
    ax.set_xlabel("Time in Ghana (GMT / UTC+0)", color='#94a3b8', weight='bold', labelpad=10)
    ax.grid(axis='x', linestyle=':', color='#475569')

    plt.title("Forex 24-Hour Trading Sessions (Ghana Time - GMT)", color='#38bdf8', fontsize=13, weight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_pip_lot_guide_chart() -> str:
    """Generates a comprehensive Pip, Lot Size, and Leverage reference table."""
    output_path = os.path.join(CHARTS_DIR, "pip_lot_guide.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    # Title
    ax.text(5, 9.2, "Coach Prince's Pips, Lots & Leverage Guide", color='#fbbf24', fontsize=14, weight='bold', ha='center')
    ax.text(5, 8.6, "Candlemaster Academy • Strict Risk Protocol for Beginners", color='#94a3b8', fontsize=10, weight='bold', ha='center')

    # Table of lot sizes
    lot_data = [
        ("MICRO LOT", "0.01", "1,000 units", "~$0.10 / pip", "RECOMMENDED FOR ALL BEGINNERS (Max safety)"),
        ("MINI LOT", "0.10", "10,000 units", "~$1.00 / pip", "For experienced traders ($1,000+ capital)"),
        ("STANDARD LOT", "1.00", "100,000 units", "~$10.00 / pip", "HIGH RISK (Can blow a small account in seconds)")
    ]

    y = 6.8
    for name, size, units, pip_val, desc in lot_data:
        color = '#22c55e' if '0.01' in size else ('#f59e0b' if '0.10' in size else '#ef4444')
        rect = patches.FancyBboxPatch((0.5, y - 0.7), 9.0, 1.4, boxstyle='round,pad=0.2', facecolor='#1e293b', edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        ax.text(0.8, y + 0.2, f"{name} ({size})", color=color, fontsize=12, weight='bold')
        ax.text(0.8, y - 0.3, f"Volume: {units} | 1 Pip Value: {pip_val}", color='#ffffff', fontsize=10)
        ax.text(5.5, y - 0.3, desc, color='#cbd5e1', fontsize=9, style='italic')
        y -= 2.0

    # Safety box
    rect_rule = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.5, boxstyle='round,pad=0.2', facecolor='#334155', edgecolor='#38bdf8', linewidth=1.5)
    ax.add_patch(rect_rule)
    ax.text(5, 1.4, "[!] COACH PRINCE'S GOLDEN SAFETY RULE:", color='#38bdf8', fontsize=10, weight='bold', ha='center')
    ax.text(5, 0.8, "On a $100 Demo/Live account: 20 pips loss with 0.01 = -$2 (Account Safe)\n"
                    "20 pips loss with 1.00 lot = -$200 (Account Wiped Out Instantly!)", color='#e2e8f0', fontsize=9, ha='center')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_risk_management_chart() -> str:
    """Generates the 1-2% risk rule and account drawdown recovery table."""
    output_path = os.path.join(CHARTS_DIR, "risk_management_drawdown.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    ax.text(5, 9.3, "Coach Prince's Risk Management & Drawdown Table", color='#ef4444', fontsize=14, weight='bold', ha='center')
    ax.text(5, 8.7, "Why Never Risking More Than 1-2% Protects Your Chop Money & Capital", color='#94a3b8', fontsize=9, weight='bold', ha='center')

    # Drawdown table
    headers = ["Account Loss", "Remaining Balance", "Gain Required to Break Even", "Difficulty"]
    rows = [
        ("10%", "$90", "+11.1%", "Easy (1-2 good trades)"),
        ("20%", "$80", "+25.0%", "Moderate (Need disciplined plan)"),
        ("30%", "$70", "+42.9%", "Hard (Psychological pressure begins)"),
        ("50%", "$50", "+100.0%", "Extreme (Must DOUBLE your account!)"),
        ("80%", "$20", "+400.0%", "Near Impossible (Gambling zone)")
    ]

    y = 7.5
    for i, h in enumerate(headers):
        ax.text(0.5 + i * 2.3, y, h, color='#fbbf24', fontsize=9.5, weight='bold')

    y -= 0.3
    ax.plot([0.5, 9.5], [y, y], color='#475569', linewidth=1)

    for loss, rem, gain, diff in rows:
        y -= 0.8
        color = '#22c55e' if '10%' in loss else ('#eab308' if '20%' in loss else '#ef4444')
        ax.text(0.5, y, loss, color=color, fontsize=9.5, weight='bold')
        ax.text(2.8, y, rem, color='#ffffff', fontsize=9.5)
        ax.text(5.1, y, gain, color=color, fontsize=9.5, weight='bold')
        ax.text(7.4, y, diff, color='#cbd5e1', fontsize=8.5)

    # Box at bottom
    rect = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.4, boxstyle='round,pad=0.2', facecolor='#1e293b', edgecolor='#22c55e', linewidth=1.5)
    ax.add_patch(rect)
    ax.text(5, 1.3, "[*] THE 1-2% RULE: YOUR BULLETPROOF VEST", color='#22c55e', fontsize=10, weight='bold', ha='center')
    ax.text(5, 0.75, "If you risk only 1% per trade, you can lose 10 trades in a row and still have 90% of your money!\n"
                    "Capital preservation comes first, profits come second.", color='#e2e8f0', fontsize=8.5, ha='center')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_trend_pullback_chart() -> str:
    """Generates Trend + Pullback Strategy diagram."""
    output_path = os.path.join(CHARTS_DIR, "trend_pullback_strategy.png")
    if os.path.exists(output_path):
        return output_path

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    # Wave path
    x = [0, 2, 3.5, 6, 7.5, 9.5]
    y = [2, 6, 4.2, 8.5, 6.8, 10]
    ax.plot(x, y, color='#22c55e', linewidth=3, marker='o', markersize=6)

    # Broken resistance turned support lines
    ax.plot([1.5, 5.0], [6, 6], color='#fbbf24', linestyle='--', linewidth=1.8)
    ax.text(5.1, 6, "Broken High -> Becomes Support Floor", color='#fbbf24', fontsize=8.5, weight='bold')

    ax.plot([5.5, 8.5], [8.5, 8.5], color='#fbbf24', linestyle='--', linewidth=1.8)
    ax.text(8.6, 8.5, "New High Broken", color='#fbbf24', fontsize=8.5, weight='bold')

    # Buy Entry Annotations
    ax.annotate("BUY ENTRY 1\n(Pullback Bounce)", xy=(3.5, 4.2), xytext=(3.5, 2.3),
                arrowprops=dict(facecolor='#22c55e', shrink=0.08, width=2),
                color='#86efac', weight='bold', ha='center', fontsize=9)

    ax.annotate("BUY ENTRY 2\n(Pullback Bounce)", xy=(7.5, 6.8), xytext=(7.5, 4.9),
                arrowprops=dict(facecolor='#22c55e', shrink=0.08, width=2),
                color='#86efac', weight='bold', ha='center', fontsize=9)

    ax.text(1.5, 9.2, "TREND + PULLBACK STRATEGY", color='#38bdf8', fontsize=12, weight='bold')
    ax.text(1.5, 8.5, "Golden Rule: Never chase green candles at the peak!\nWait patiently for price to pull back like an arrow drawn on a bow.", color='#cbd5e1', fontsize=8.5)

    ax.set_ylim(1, 11)
    ax.set_xlim(-0.5, 11.5)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    return output_path

def generate_ultimate_strategy_chart() -> str:
    """
    Generates Coach Prince's Ultimate Strategy Masterclass Diagram:
    Top-Down Multi-Timeframe Structure & POI Sniping Framework.
    """
    output_path = os.path.join(CHARTS_DIR, "coach_prince_ultimate_strategy.png")
    # Regenerate cleanly
    try:
        fig, ax = plt.subplots(figsize=(12, 7.2), dpi=150)
        fig.patch.set_facecolor('#090d16')
        ax.set_facecolor('#0f172a')

        # Header Title
        ax.text(6.0, 9.4, "COACH PRINCE'S ULTIMATE STRATEGY MASTERCLASS", color='#fbbf24', fontsize=14, weight='bold', ha='center')
        ax.text(6.0, 8.9, "Top-Down Multi-Timeframe Execution & POI Sniping Framework (HCNFX Masterclass)", color='#38bdf8', fontsize=9.5, weight='bold', ha='center')

        # 4 Timeframe Columns
        columns = [
            ("1. DAILY (D1)", "Macro Bias & Major Bounds", [
                "• Determines General Bias (Buy / Sell / Stay Off)",
                "• Maps recent Resistance & Demand zones",
                "• Identifies major Break of Structure (BOS)",
                "• Discards ancient history; focuses on RECENCY!"
            ], '#3b82f6'),
            ("2. 4-HOUR (H4)", "Structure Refinement", [
                "• Refines Daily origin to H4 Order Block",
                "• Tracks intermediate BOS & CHoCH swings",
                "• Identifies pending major supply/demand zones",
                "• Confirms whether price is expanding or pulling back"
            ], '#10b981'),
            ("3. 1-HOUR / 30M", "Internal Structure & POI", [
                "• Maps internal leg structure between swings",
                "• Identifies Fair Value Gaps (FVG) & sweeps",
                "• Discards Mitigated zones (Mitigated = Weak!)",
                "• Targets ONLY Fresh, Unmitigated Origins"
            ], '#8b5cf6'),
            ("4. 15-MIN (M15)", "The Execution Trap", [
                "• Primary Entry Timeframe (Set Your Traps!)",
                "• Limit order entry on 15M Unmitigated OB + FVG",
                "• Tight Hard Stop Loss just above rejection wick",
                "• Asymmetric TP at opposing demand (1:3 to 1:5+ RR)"
            ], '#ef4444')
        ]

        x_starts = [0.4, 3.3, 6.2, 9.1]
        for idx, (title, subtitle, points, col) in enumerate(columns):
            x = x_starts[idx]
            # Draw Column Box
            rect = patches.FancyBboxPatch((x, 2.7), 2.6, 5.7, boxstyle='round,pad=0.2', facecolor='#1e293b', edgecolor=col, linewidth=2)
            ax.add_patch(rect)
            ax.text(x + 1.3, 8.0, title, color=col, fontsize=10.5, weight='bold', ha='center')
            ax.text(x + 1.3, 7.55, subtitle, color='#94a3b8', fontsize=7.5, weight='bold', ha='center')

            y_pos = 6.9
            for pt in points:
                ax.text(x + 0.15, y_pos, pt, color='#f1f5f9', fontsize=7.2, va='top')
                y_pos -= 0.95

            # Arrow to next timeframe
            if idx < 3:
                ax.annotate('', xy=(x + 2.85, 5.5), xytext=(x + 2.6, 5.5),
                            arrowprops=dict(arrowstyle='->', color='#fbbf24', lw=2.5))

        # Bottom Banner: The 5 Golden Trapping Rules
        rect_bot = patches.FancyBboxPatch((0.4, 0.4), 11.3, 1.9, boxstyle='round,pad=0.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=1.8)
        ax.add_patch(rect_bot)
        ax.text(6.0, 1.95, "★ COACH PRINCE'S 5 GOLDEN TRAPPING RULES ★", color='#fbbf24', fontsize=9.5, weight='bold', ha='center')
        rules_text = (
            "1. NEVER BE TOO LAZY to do Top-Down Analysis: Each timeframe tells you where price is reacting and when to stay off.\n"
            "2. RECENCY OVER ANCIENT HISTORY: Focus only on current relevant zones; do not waste time on played-out charts.\n"
            "3. MITIGATED VS UNMITIGATED: Mitigated origins are weak and likely to break. Trade fresh unmitigated zones with FVG.\n"
            "4. DO NOT FORCE HIGHER-TF ZONES: When the D1/H4 zone is far away, read internal structure to trade the journey towards it.\n"
            "5. HARD STOP LOSS & HIGH RR: Set your SL strictly beyond the rejection wick. Never risk your account on hope."
        )
        ax.text(6.0, 1.15, rules_text, color='#e2e8f0', fontsize=7.2, ha='center', va='center')

        ax.set_xlim(0, 12.1)
        ax.set_ylim(0, 9.8)
        ax.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches='tight')
        plt.close()
        return output_path
    except Exception as e:
        print(f"Error generating ultimate strategy chart: {e}")
        return output_path

def generate_certificate(student_name: str, completion_date: str = None) -> str:
    """
    Generates a personalized high-resolution Certificate of Completion.
    Returns the file path of the generated certificate image.
    """
    if not completion_date:
        completion_date = datetime.now().strftime("%B %d, %Y")

    cert_filename = f"certificate_{abs(hash(student_name)) % 1000000}.png"
    cert_path = os.path.join(CHARTS_DIR, cert_filename)

    width, height = 1200, 850
    image = Image.new("RGB", (width, height), color="#0f172a")
    draw = ImageDraw.Draw(image)

    # Elegant Multi-Layer Border with Ghanaian Gold and Green colors
    draw.rectangle([(20, 20), (width - 20, height - 20)], outline="#d97706", width=4)
    draw.rectangle([(30, 30), (width - 30, height - 30)], outline="#059669", width=2)
    draw.rectangle([(40, 40), (width - 40, height - 40)], outline="#fbbf24", width=1)

    # Corner decorative brackets
    bracket_size = 50
    corners = [(45, 45), (width - 45, 45), (45, height - 45), (width - 45, height - 45)]
    for cx, cy in corners:
        draw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill="#fbbf24")

    # Header Badges
    draw.text((width // 2, 90), "CANDLEMASTER ACADEMY • GHANA", fill="#94a3b8", anchor="mm")
    draw.text((width // 2, 160), "CERTIFICATE OF COMPLETION", fill="#fbbf24", anchor="mm")
    draw.text((width // 2, 210), "This is proudly presented to", fill="#cbd5e1", anchor="mm")

    # Student Name (Large & Highlighted)
    cleaned_name = student_name.strip() or "Valued Student"
    draw.text((width // 2, 290), cleaned_name, fill="#ffffff", anchor="mm")
    draw.line([(width // 2 - 250, 330), (width // 2 + 250, 330)], fill="#d97706", width=2)

    # Citation Body Text
    body_text = (
        "For successfully completing the intensive 14-Day Forex Fundamentals Curriculum\n"
        "at Candlemaster Academy, demonstrating proficiency in Currency Mechanics, Technical Analysis,\n"
        "Disciplined 1-2% Risk Management, and Safe MT5 Demo Execution."
    )
    draw.multiline_text((width // 2, 420), body_text, fill="#e2e8f0", anchor="mm", align="center", spacing=12)

    # Golden Seal (Left Bottom)
    seal_x, seal_y = 220, 650
    draw.ellipse([(seal_x - 65, seal_y - 65), (seal_x + 65, seal_y + 65)], outline="#fbbf24", width=3, fill="#1e293b")
    draw.ellipse([(seal_x - 55, seal_y - 55), (seal_x + 55, seal_y + 55)], outline="#d97706", width=1)
    draw.text((seal_x, seal_y - 15), "★ OFFICIAL ★", fill="#fbbf24", anchor="mm")
    draw.text((seal_x, seal_y + 12), "VERIFIED", fill="#34d399", anchor="mm")

    # Instructor Signature (Right Bottom)
    sig_x, sig_y = width - 260, 650
    draw.line([(sig_x - 140, sig_y + 10), (sig_x + 140, sig_y + 10)], fill="#94a3b8", width=1)
    draw.text((sig_x, sig_y - 20), "Coach Prince", fill="#38bdf8", anchor="mm")
    draw.text((sig_x, sig_y + 30), "Coach Prince (Head Instructor)", fill="#cbd5e1", anchor="mm")
    draw.text((sig_x, sig_y + 52), "Candlemaster Academy", fill="#64748b", anchor="mm")

    # Date and Verification ID
    draw.text((width // 2, 750), f"Awarded on: {completion_date}  |  Accra, Ghana (GMT)", fill="#94a3b8", anchor="mm")
    draw.text((width // 2, 780), f"Verification Token: CMA-FX-{abs(hash(student_name)) % 999999:06d}", fill="#64748b", anchor="mm")

    image.save(cert_path, "PNG")
    return cert_path

def get_chart_for_day(day: int) -> str:
    """Returns the visual educational chart path for a given lesson day."""
    if day in (1, 2):
        return generate_sessions_chart()
    elif day in (3, 4):
        return generate_candlestick_anatomy_chart()
    elif day in (5, 6):
        return generate_pip_lot_guide_chart()
    elif day in (7, 8):
        return generate_support_resistance_chart()
    elif day == 9:
        return generate_trend_diagram()
    elif day == 10:
        return generate_trend_pullback_chart()
    elif day in (11, 12):
        return generate_risk_management_chart()
    elif day in (13, 14):
        return generate_ultimate_strategy_chart()
    else:
        return generate_ultimate_strategy_chart()
