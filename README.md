# Slacking
Maintain your online active status on Slack while AFK.

---
### Installation
Clone this repository
```
git clone https://github.com/imran-salim/slacking.git
```

Set up a Python virtual environment
```
python -m venv .venv
```

Activate your Python virtual environment
```
source .venv/bin/activate
```

Install PyAutoGUI
```
pip install pyautogui
```

### Usage
```
python slacking.py
```
Default number of minutes is 5

```
python slacking.py <minutes> <failsafe> <pause>
```
\<minutes: int\> (optional)

\<failsafe: str\> (optional)
y or n

\<pause: float\> (optional)

---
### Disclaimer
Do not actually use this script at work.
