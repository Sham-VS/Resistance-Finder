# 🧮 **Resistance Finder** - Color Code ↔ Resistance Converter

This Python project allows you to **convert resistor values to color codes** and **vice versa**, using the standard **3-band resistor** color system.


---


## 🚀 **Features**

- 🔁 **Two-way conversion:**
  - Convert numeric resistance (e.g., `4700`) to **color bands** (e.g., `Yellow | Violet | Red`)
  - Convert **color bands** (e.g., `red`, `violet`, `orange`) to numeric resistance (e.g., `27000` ohms)
- ✅ **Validates inputs** and handles incorrect entries
- 🔄 **Loop-based user interface** for continuous use


---


## 🧠 **How It Works**

### 📌 **Color Code to Resistance**
- You input **3 color names** (e.g., `green`, `blue`, `yellow`)
- It calculates resistance using the formula:  
  > **(1st_digit × 10 + 2nd_digit) × (10 ^ multiplier)**

### 📌 **Resistance to Color Code**
- You input a **numeric resistance value** (e.g., `470`)
- It identifies the **first two digits** and the **number of trailing zeros**, then maps them to colors


---


## 🎨 **Standard Color Mapping**

| **Color** | **Value** |
|----------:|:----------|
| Black     | 0         |
| Brown     | 1         |
| Red       | 2         |
| Orange    | 3         |
| Yellow    | 4         |
| Green     | 5         |
| Blue      | 6         |
| Violet    | 7         |
| Gray      | 8         |
| White     | 9         |


---


## 📂 **How to Run**

1. Make sure **Python 3** is installed.
2. Clone this repo or copy the script to your machine.
3. Run the script in terminal:
   ```bash
   python resistance_finder.py
   ```

---
