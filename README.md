# 🔫 Roblox Username Finder Suite

**A lightweight Windows tool to search for short and available Roblox usernames.**  
No login, no Python — just a fast, simple desktop app for username hunters.

---

## 🚀 Features

- **Finder Fast (Random Mode)**  
  Quickly checks random usernames with optional digits anywhere in the name.  
  → Fastest way to find something available.

- **Finder (Ordered Mode)**  
  Sequentially scans usernames by length.  
  → Good for targeted, predictable name patterns.

- **Get CSRF Token Utility**  
  Instantly fetches a valid **X-CSRF-TOKEN** from Roblox API — useful when testing requests or debugging 403 issues.

All username checks use Roblox’s official validation endpoint:  
`https://auth.roblox.com/v1/usernames/validate`

---

## 🖥️ Download & Run

1. Go to the **[Releases](../../releases)** tab and download **`RBX-Username-Suite.exe`**  
2. Double-click to open — no installation or Python required.  
3. If SmartScreen appears → click **More info → Run anyway** (unsigned indie app).

✅ Works on **Windows 10/11 (64-bit)**  
🌐 Requires an internet connection.

---

## ⚙️ Quick Start

1. Open the app  
2. Select **Finder Fast** *(recommended)*  
3. Set target lengths (e.g. `4, 5`)  
4. Set **Required digits** to `1–2`  
5. Click **Start** — a popup appears if a name is free.

💡 **Tip:** Roblox allows **3+ characters**, but 3-char names are almost always taken.  
Try **4–5 characters** with **1–2 digits** for best results.

---

## 🧩 Troubleshooting

- **Nothing happens when opening:** Antivirus/SmartScreen might block it → Right-click → *Run anyway*.  
- **Too Many Requests (429):** You’ve hit the rate limit → Increase delay/backoff in settings and retry later.  
- **403 Forbidden:** Click **Get CSRF Token** first, then try again.

---

## 🔒 Privacy

- No login required  
- No data stored or uploaded  
- Uses only Roblox’s public validation endpoint

---

## 👤 dev
Made with in **daxk** 🤑🤑🤑
