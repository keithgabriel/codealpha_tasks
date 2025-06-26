# 🛡️ Basic Network Intrusion Detection System (NIDS) using Snort

## 📍 Project Description
This project demonstrates how to configure and run a basic Network Intrusion Detection System (NIDS) using Snort on a Windows machine. It includes rule setup, real-time alerting, and traffic monitoring through command-line execution.

---

## ✅ Features Implemented
- Installed Snort and dependencies on Windows
- Configured snort.conf file
- Wrote and activated a custom rule to detect ICMP (ping) traffic
- Ran Snort on a specific network interface
- Triggered alerts using ping 8.8.8.8
- Logged alerts and captured screenshot evidence

---

## 🛠️ Tools & Technologies
- Snort 2.9.20-WIN64 GRE
- Npcap (WinPcap Compatibility Mode)
- Command Prompt (Admin Mode)
- Text Editor: Notepad++ / VS Code
- Windows OS

---

## 📁 Project Folder Structure
Snort-NIDS-Project/
│
├── rules/
│ └── local.rules
│
├── etc/
│ └── snort.conf
│
├── log/
│ └── [Snort logs generated here after running]
│
├── screenshots/
│ └── icmp_alert_console.png
│
├── run_command.txt
└── README.md



---

## 🚀 How to Run Snort
1. Open CMD as Administrator
2. Navigate to the Snort bin directory:
cd C:\Snort\bin


3. Check your network interface:
snort -W


4. Run Snort with your chosen interface:
snort -i 4 -A console -c C:\Snort\etc\snort.conf -l C:\Snort\log


> Note: Replace -i 4 with the correct interface index from step 3.

5. In another CMD window, trigger an ICMP alert:
ping 8.8.8.8


6. Watch Snort console for alerts like:
[] [1:1000001:1] ICMP Packet Detected []



---

## 🔍 Sample Custom Rule (ICMP Detection)
```snort
alert icmp any any -> any any (msg:"ICMP Packet Detected"; sid:1000001; rev:1;)
Located in: C:\Snort\rules\local.rules

📸 Screenshot Evidence

📦 Run Command File
Check run_command.txt for the exact command used and full execution steps.

📚 References
Snort Official Docs

Cisco Talos Rules

Npcap Installer

📝 Author
Keith Gabriel 
Cybersecurity Enthusiast | Computer Science Student

---