# ELIANA-Remote-Acces-Trojan

A Python-based Command-and-Control tool designed for **authorized Vulnerability Assessment & Penetration Testing (VAPT)** engagements.  
This tool enables security testers with explicit permission to remotely execute commands, collect system information, and perform surveillance through a Telegram Bot interface.

<img width="413" height="584" alt="Image" src="https://github.com/user-attachments/assets/dd105739-85e3-4ab4-ba3e-79b6ae55e377" />


⚙️ ELIANA-RAT Setup

🚀 Quick Start
bash
# 1. Clone the repository
git clone https://github.com/Adrilaw/ELIANA-Remote-Access-Trojan.git

# 2. Navigate to the directory
cd ELIANA-Remote-Access-Trojan

# 3. Install dependencies
pip install -r requirements.txt
📋 Setup Instructions
STEP 1: Get Your Telegram Credentials
1. Get Your Telegram User ID
Watch this tutorial: How to Get Telegram User ID

Quick Method:

Open Telegram Web: https://web.telegram.org

Search for "@userinfobot"

Send /start command

Bot will reply with your User ID

Copy the numeric ID (e.g., 85463344)

2. Create a Telegram Bot & Get API Token
Watch this tutorial: How to Create Telegram Bot

Quick Method:

Open Telegram, search for "@BotFather"

Send /newbot command

Choose a name for your bot (e.g., "MyTestBot")

Choose a username (must end with 'bot', e.g., "mytestbot")

Copy the API Token (e.g., 857228:AAHV9S9dRWQFgBUY9XgUg5Sp5SNY9BNnSKw)

STEP 2: Configure ELIANA_RAT.py
Open the file in a text editor:

bash
# Windows
notepad ELIANA_RAT.py

# Linux/Mac
nano ELIANA_RAT.py
Find these lines (around line 4-5):

python
TELEGRAM_TOKEN = "Bot API Key"
TELEGRAM_CHAT_ID = "User ID"
Replace with your credentials:

python
TELEGRAM_TOKEN = "Bot Api Key"  # Your Bot API Token
TELEGRAM_CHAT_ID = "User ID"  # Your User ID
Example of correct configuration:

python
# ==================== CONFIG ====================
# REPLACE THESE WITH YOUR CREDENTIALS!
TELEGRAM_TOKEN = "Bot Api Key "
TELEGRAM_CHAT_ID = "User ID"
# ===============================================
STEP 3: Test the RAT
bash
# Run the Python script
python3 ELIANA_RAT.py
Expected Output:

text
╔══════════════════════════════════════╗
║       ELIANA RAT v2.0 - Active       ║
╠══════════════════════════════════════╣
║ Target: 5285463344                   ║
║ User: Administrator                  ║
║ System: Windows 10                   ║
╚══════════════════════════════════════╝
📡 Waiting for commands...
You should receive a Telegram message: "✅ Connection Established"


# 🚀 Features

# 📸 Media Capture
`webcam` - Take webcam photo

`webcam` 10 - Record webcam video (specify seconds)

`audio 10` - Record microphone audio (specify seconds)

# 📁 File Operations
`ls` - List files in current directory

`cd` folder - Change to folder

`read` file.txt - Read file contents

`download URL` - Download file from URL

`upload file.txt` - Upload file to operator

`pwd` - Show current directory

# 💻 System Information
`sysinfo` - Show detailed system information

`ps` - List running processes

`netstat` - Show network connections

`ip` - Show network configuration

`wifi` - Extract WiFi passwords

# ⚡ System Control
`shutdown` - Shutdown computer

`reboot` - Restart computer

`lock` - Lock workstation

`defender` - Disable Windows Defender

# 🔧 Utilities
`cmd command` - Execute shell command

`clear` - Clear terminal (simulated)



✨ Key Features

✅ True Persistence - Survives reboot via Registry, Scheduled Tasks, and Startup folder

✅ Complete Surveillance - Screenshots, audio recording, webcam capture, screen recording

✅ Credential Harvesting - Chromium browser detection and data extraction

✅ File Operations - Upload/download files without disk writes

✅ Stealthy - Fileless operations, jittered beacons, history protection

✅ Reliable - Multiple fallback methods for all operations


# ✍🏼 About Author

I'm Dodin Mel-Adrien also known as Kidpentester/Adrilaw built this as an intern , to demonstrate the use of telegram to gain access to a windows machine without being detected by antivirus software , this tool was explicitly designed for vulnerability assesment and penetration testing . My inspiration to build this came from my wife , she inspired me in a way I can’t fully describe. Her strength, beauty, and resilience showed me what it means to keep moving forward no matter what stands in the way. Watching how she never let anything break her spirit made me want to push myself harder, to build things, to improve my skills, and to create tools that help me grow in my cybersecurity journey. Her character reminded me that when someone is strong and unstoppable, you feel motivated to chase your goals with the same energy. 

# Credits

🔥 https://github.com/FebVeg/TGRS

🔥 https://github.com/gunzf0x/BypassAMSI_PSRevshell

# License
ELIANA-Remote-Acces-Trojan is licensed under the [GNU General Public License](LICENSE) and the [ELIANA-Remote-Acces-Trojan Commercial License](C-LICENSE)- see the LICENSE file for details.

⚠️ Legal & Ethical Notice

This tool is strictly for use in authorized security assessments with explicit written permission.
Unauthorized use, including but not limited to surveillance, credential harvesting, or persistence installation, is illegal and unethical.
Use responsibly and always operate within your legal boundaries.
