

# 🌧️ Monsoon Incident Reporting System (MIRS)

A smart, local-first incident reporting platform designed for district administration to monitor and manage monsoon-related emergencies such as flooding, blocked drains, road collapses, power outages, and waterlogging.

> Developed by a data science student as a civic tech initiative, with local reporting, REST APIs, real-time chat, and analytics dashboards.

---

## 📌 Project Features

* ✅ **Submit Incidents**: Citizens and officials can report monsoon-related incidents with location, image, and severity.
* 🗂 **Incident Database**: Local file-based or SQLite database for easy offline storage and access.
* 💬 **Chat Integration**: Built-in local TCP/IP chat for report-specific discussion (via Tkinter GUI).
* 📊 **Analytics Dashboard**: Visualize trends, top affected areas, and word cloud of reports.
* 🔄 **API Access**: Clean RESTful endpoints with `curl`/CLI compatibility for integration and automation.
* 🖥️ **GUI & Mobile Ready**: Tkinter-based desktop GUI, with optional mobile client (Kivy).

---

## 🧱 Project Structure

```
monsoon_incident_reporting/
├── backend/              # Flask or FastAPI API
│   ├── app.py
│   ├── db.json
│   └── utils.py
│
├── desktop_gui/          # Tkinter GUI with Chat integration
│   ├── main.py
│   └── chat_extension.py
│
├── analytics/            # Data Science analytics & plots
│   ├── flood_trends.py
│   └── plots/
│
├── mobile_app/           # (Optional) Kivy-based mobile submission
│   └── main.py
│
├── os_tasks/             # OS-style event/watchdog functionality
│   └── log_monitor.py
│
├── tests/                # curl and Python API tests
│   ├── curl_requests.sh
│   └── test_api.py
│
├── README.md
└── requirements.txt
```

---

## 🌐 API Endpoints

| Method | Endpoint            | Description                       |
| ------ | ------------------- | --------------------------------- |
| POST   | `/report`           | Submit a new incident report      |
| GET    | `/reports`          | Retrieve all reports              |
| GET    | `/report/<id>`      | View a specific report            |
| GET    | `/report/<id>/chat` | Get chat log for a report         |
| POST   | `/report/<id>/chat` | Post message in report discussion |
| GET    | `/stats/summary`    | Get summary of incident analytics |
| GET    | `/stats/daily`      | View daily time-series trends     |

---



---

## 📊 Sample Analytics Output

* **Bar chart**: Reports per day
* **Pie chart**: Severity levels (High, Medium, Low)
* **Heatmap**: Incident density by area (optional future work)
* **Word Cloud**: From all incident descriptions

---

## 🛠 Technologies Used

* **Python** – core language
* **Flask / FastAPI** – REST API backend
* **Tkinter** – GUI interface + chat
* **Kivy** – mobile app (optional)
* **Matplotlib / WordCloud / Pandas** – analytics
* **Watchdog / OS Lib** – OS-level file monitoring
* **cURL / Requests** – API testing & scripting

---



---

## 🎀 Frills

* GPS-based location tagging
* GIS integration
* Role-based access for admins
* SMS/email alerts on severe incidents
* Cloud sync & backup options

---

## 🙌 Acknowledgements

Built as a civic-tech project to support local flood management and disaster mitigation during monsoon season.

District-level use case supported by direct feedback from divisional administration.

