# ☕ Coffee Machine - Python Console App

A Python-based console simulation of a coffee machine that serves **espresso**, **latte**, and **cappuccino**, handles ingredient resources, takes coin input, calculates change, and tracks profits.

---

## 📋 Features

- Menu with prices and ingredient requirements.
- Tracks and manages available resources (water, milk, coffee).
- Accepts payment in coins: quarters, dimes, nickels, and pennies.
- Calculates and returns change if payment exceeds cost.
- Rejects the transaction if insufficient resources or money.
- Supports special commands:
  - `report` — shows remaining ingredients and earnings.
  - `off` — shuts down the machine.

---

## 🧠 How It Works

1. User selects a drink (`espresso`, `latte`, or `cappuccino`).
2. Machine checks if there are enough resources.
3. User inserts coins.
4. Machine processes the payment:
   - If payment is sufficient → drink is served, change is returned.
   - If not → refund the money.
5. Resources and profit are updated accordingly.

---

## ▶️ Running the Project

Make sure Python is installed, then run:

```bash
python coffee_machine.py
