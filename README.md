# TI-84-Offline
Offline Math Program for TI-84 Plus CE Python


![Python-Emblem](https://github.com/user-attachments/assets/528f6a89-09db-44c8-9205-207508b711ab)


A fully offline math tutor and solver built in Python for the TI-84 Plus CE Python edition.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-TI--84%20Plus%20CE%20Python-blue)
![Language](https://img.shields.io/badge/Language-Python-green)

---

## What It Does

TI-84 Offline is a math tutor that runs entirely on your calculator with no internet 
connection, no external hardware, and no subscriptions required.

Type a problem naturally at the prompt — like `3x+2=11` or `x^2-5x+6=0` — and it 
automatically detects the problem type and solves it. Every answer includes a full 
step-by-step walkthrough that pauses between each step so nothing scrolls off screen, 
plus a verification check to confirm the answer is correct.

---

## Solvers

| Mode | What it solves | Example input |
|------|---------------|---------------|
| Linear | ax + b = c | `3x+2=11` |
| Quadratic | ax² + bx + c = 0 | `x^2-5x+6=0` |
| Systems 2x2 | Two equations, two unknowns | `2x+3y=12` / `x-y=1` |
| Systems 3x3 | Three equations, three unknowns | `x+y+z=6` / `2x-y+z=3` / `x+2y-z=2` |
| Inequality | ax + b > c | `3x+2>11` |
| Slope/Mid/Dist | Given two points | x1=0 y1=0 x2=3 y2=4 |
| Radicals | Simplify, solve, rationalize | `sqrt(48)` → 4√3 |
| Statistics | Mean, median, std dev, regression | `4 7 2 9 3` |

---

## Installation

### What you need
- TI-84 Plus CE Python edition
- TI Connect CE (free download from TI's website)
- The USB-A to Mini-B Cable

### Steps
1. Download all `.py` files from this repo
2. Open TI Connect CE on your PC
3. Connect your calculator via USB
4. Open Calculator Explorer in TI Connect CE
5. Drag all 8 files onto the calculator at once
6. On the calc: `[apps]` → `Python` → `Files` → `MATH_AI` → `Run`

---

## Usage

When the program starts you'll see:
```
MATH AI v4.0
Problem or ENTER=menu
>
```

You can either:
- Type a problem directly — the program detects the type automatically
- Press ENTER — opens the guided menu to pick a solver manually

### Example
```
> 3x+2=11

LINEAR
------
3x+2=11

Step 1: Isolate x term
Subtract 2 both sides
3x+2-2 = 11-2
3x = 9
[ENTER] next step

Step 2: Solve for x
Divide both sides by 3
3x/3 = 9/3

Answer: x=3.0
[ENTER] next step

Step 3: Verify
3(3.0)+2 = 11.0
Expected: 11
Correct!
```

---

## How It Works

The program is split across 9 small files so it never exceeds the calculator's 
limited RAM. Each solver only loads into memory when needed, then gets cleared 
immediately after. 

---

## Files
```
TI-84-Offline/
├── README.md
├── LICENSE
├── math_ai.py    ← main menu and router
├── lin.py        ← linear equation solver
├── quad.py       ← quadratic equation solver
├── sys_.py       ← systems of 2 equations
├── sys3.py       ← systems of 3 equations
├── ineq.py       ← inequality solver
├── slope.py      ← slope, midpoint, distance
├── rad.py        ← radicals and roots
└── stat.py       ← statistics and regression
```

---

## Requirements

- TI-84 Plus CE Python edition
- OS version 5.8.0 or later
- TI Connect CE for transferring files


---

## License

MIT License — see [LICENSE](LICENSE) for details.

#GL on whatever you need this on ;)
