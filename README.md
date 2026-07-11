<h1 align="center">🛡️ AnyGrab 🛡️</h1>

<p align="center">
  <a href="https://www.python.org" target="_blank"><img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" /></a>
  <a href="https://t.me/swezy" target="_blank"><img src="https://img.shields.io/badge/Telegram-@Swezy-blue?style=for-the-badge&logo=telegram" /></a>
  <br>
  <code>Leave a ⭐ if you like this Repository</code>
</p>

---

## 🚩 Project overview

**AnyGrab** is a Python utility that continuously **monitors AnyDesk connections** on your system and displays **remote IP addresses and ports** in a beautiful **gradient CLI interface**. It includes a **persistent blacklist** to avoid duplicate entries and supports **console transparency** for a sleek look.

> [!CAUTION]
> This tool is intended for **educational and personal monitoring purposes only**.
> Do **not** use it for unauthorized access, exploitation, or malicious activity.
> The author and contributors are **not** responsible for any misuse of this code.

---

## ✨ Features

* 👀 **Monitor AnyDesk Connections** — Detect running AnyDesk processes and log their active connections.
* 🧠 **Persistent Blacklist** — Avoid duplicate IP addresses by storing them in a persistent blacklist.
* 🌈 **Gradient CLI Interface** — Uses `rgbprint` for beautiful color gradients and scrolling messages.
* 🖥️ **Console Transparency** — Adjustable transparency for a modern and aesthetic CLI.
* ⚡ **Real-time Monitoring** — Continuously checks AnyDesk connections and prints updates in real-time.

---

## 🧭 How It Works

1. Run the tool (`python main.py`).
2. The program **monitors AnyDesk processes** on your system.
3. When AnyDesk is detected, it **grabs active remote connections** and displays:
   * Remote IP
   * Port
4. The program **ignores local-link addresses** (`169.254.x.x`) and common ports like 80 and 443.
5. **Duplicate IPs are blacklisted** automatically to avoid repeated notifications.
6. The CLI displays messages in **color gradients** and scroll animations for a premium visual experience.

---

## 🧰 Requirements

* 🐍 Python **3.9+**
* 📦 Dependencies:

    ```bash
    pip install rgbprint psutil colorama
    ```

* 🖥️ Windows operating system (for console transparency and netstat)

---

## 📝 Repository structure

```/
├─ assets/ ➔ Screenshots of the Program in action
│ └─ preview.png ➔ A screenshot of the Program running
├─ main.py ➔ Main program logic and CLI
├─ LICENSE ➔ License file
└─ README.md ➔ Read me file
```

---

## 🖼️ Preview

<p align="center">
  <img src="https://img.shields.io/badge/UI-Gradient%20CLI-blueviolet?style=for-the-badge"/>
  <br><br>
  <img src="https://github.com/SwezyDev/AnyGrab/blob/main/assets/preview.png?raw=true" alt="Program preview">
</p>

---

## ⚙️ Technical Details

* Uses `psutil` to detect running AnyDesk processes.
* Uses `socket` to capture TCP connections.
* Filters out **LISTENING** ports and local-link addresses.
* Console transparency is implemented via `ctypes` and Windows API.
* Gradient and scrolling effects are handled via the `rgbprint` library.
* Persistent blacklist ensures each IP is printed only once.

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙌 Credits & contact

* Maintainer: [@SwezyDev](https://github.com/SwezyDev) — reach out via Telegram: [@Swezy](https://t.me/swezy)
* Inspiration: System monitoring utilities and public security research.

---

## 🚨 Disclaimer

This project is intended for **personal learning and monitoring**.
Do **not** use it to intrude on other people's systems or conduct unauthorized actions.
This tool is **not affiliated with, endorsed by, or sponsored by AnyDesk** in any way.

---

## 📣 Final note

This project is made for **educational purposes and visual monitoring**.
Use responsibly — do **not** exploit or misuse.