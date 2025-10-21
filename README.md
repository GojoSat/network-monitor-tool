# Network Monitor Tool

A lightweight Python application for monitoring TCP connectivity and analyzing port status.

GitHub Repo: [https://github.com/GojoSat/network-monitor-tool.git](https://github.com/GojoSat/network-monitor-tool.git)

## ✨ Features
- Check multiple ports and measure response time  
- Multi-threaded scanning for faster results  
- SQLite database for storing monitoring history  
- Simple GUI built with Tkinter  
- Export results to text file

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** socket, threading, tkinter, sqlite3
- **Supported OS:** Windows / Linux

## 🚀 Usage
1. Run the tool:
   ```bash
   python main.py
   ```
2. Enter host (e.g., `google.com`) and port range (e.g., `20-80`)
3. Click **Start Scan**
4. View results or export them

## 📂 Project Structure
```
network_monitor_tool/
├── main.py
├── scanner.py
├── database.py
├── README.md
└── scan_results.txt
```

## 📸 Example Output
```
Scanning host: google.com (20-80)
[✔] Port 80 open - 42 ms
[✘] Port 25 closed
[✔] Port 443 open - 38 ms
```

## 📘 Purpose & Practical Value
- **Network Diagnostics:** Quickly check whether key services (e.g., HTTP, DB, SSH) are reachable.  
- **Performance Insight:** Measure latency to evaluate network quality.  
- **Automation:** Save and export data for batch analysis.  
- **Learning:** Demonstrates Python networking, threading, database, and GUI integration.

## ⚠️ Troubleshooting
| Issue | Cause | Solution |
|--------|--------|----------|
| GUI not showing | Python too old | Use Python 3.8+ |
| Empty results | Host unreachable / Firewall | Try another host |
| Export error | File permission | Run as admin |
| DB error | Locked file | Delete old `monitor_results.db` |
| Latency unstable | Network fluctuation | Adjust timeout |

## 🧠 Interview Talking Points
- “This project helped me understand how TCP sockets and threading work in real scenarios.”  
- “I modularized GUI, logic, and database for maintainability.”  
- “It’s a practical tool I could actually use for server monitoring.”  

## 📘 License
MIT License
