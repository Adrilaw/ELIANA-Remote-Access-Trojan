# C2-PowerShell-Telegram-VAPT

A PowerShell-based Command-and-Control tool designed for **authorized Vulnerability Assessment & Penetration Testing (VAPT)** engagements.  
This tool enables security testers with explicit permission to remotely execute commands, collect system information, and perform surveillance through a Telegram Bot interface.

## ⚙️ Complete Command List

# Basic System Commands
sessionid ls                        # List directory contents  
sessionid pwd                       # Show current directory  
sessionid whoami                    # Show current user context  
sessionid ps                        # List running processes  
sessionid netstat                   # Show network connections  
sessionid sysinfo                   # Get system information  

# Basic System Commands
sessionid ls                        # List directory contents
sessionid pwd                       # Show current directory  
sessionid whoami                    # Show current user context
sessionid ps                        # List running processes
sessionid netstat                   # Show network connections
sessionid sysinfo                   # Get system information

# Surveillance & Recording 
sessionid screenshot                # Capture screen and upload  
sessionid record-audio [sec]        # Record audio (e.g., record-audio 10)  
sessionid webcam-shot               # Take webcam photo  
sessionid webcam-record [sec]       # Record webcam video (e.g., webcam-record 15)  
sessionid screen-record [sec]       # Record screen (e.g., screen-record 20)  

# Data Collection
sessionid dump-creds                # Detect and extract browser credentials  
sessionid download [file_path]      # Upload file from target to C2  
sessionidupload [URL] [dest]        # Download file from URL to target  

# Persistance & Management
sessionid persist                  # Install multi-method persistence (survives reboot)  
sessionid unpersist                # Remove all persistence methods  
sessionid exit                     # Terminate C2 session  

# Custom Commands
sessioid [any powershell]          # Execute any PowerShell command
sessioid ALL [command]             # Execute on all active sessions

✨ Key Features

✅ True Persistence - Survives reboot via Registry, Scheduled Tasks, and Startup folder

✅ Complete Surveillance - Screenshots, audio recording, webcam capture, screen recording

✅ Credential Harvesting - Chromium browser detection and data extraction

✅ File Operations - Upload/download files without disk writes

✅ Stealthy - Fileless operations, jittered beacons, history protection

✅ Reliable - Multiple fallback methods for all operations

⚙️ Setup Instructions

Before using this script, you must update the Telegram credentials in the script:

$global:TG_CHAT_ID = "your-user-id"         # Replace with your Telegram Chat ID  
$global:TG_API_TOKEN = "your-bots-api-key"  # Replace with your Telegram Bot API Token  

How to create a Telegram Bot and obtain credentials

Open Telegram and search for BotFather

Send /newbot and follow the instructions to create your bot

Copy the API token provided by BotFather and set it as TG_API_TOKEN

To get your Chat ID, send a message to your bot and use bots like @userinfobot or Telegram API tools

⚠️ Legal & Ethical Notice

This tool is strictly for use in authorized security assessments with explicit written permission.
Unauthorized use, including but not limited to surveillance, credential harvesting, or persistence installation, is illegal and unethical.
Use responsibly and always operate within your legal boundaries.
