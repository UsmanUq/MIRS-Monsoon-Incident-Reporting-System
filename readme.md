Folder Distribution for IRS---Incident-Reporting-System


 	├── backend
   		├── app.py                    # Flask/FastAPI backend server
   		├── db.json                   # Local DB for reports (or use SQLite)
   		├── reports/                  # Folder to store report images/files
   		└── utils.py                  # Helper functions (file ops, analytics)

     
	├── mobile_app                   
		   └── main.py                   # App to view/submit reports

 	├── desktop_gui/                    					
 		├── main.py                   # Entry point for GUI
 		└── chat_extension.py         # Chat tied to incidents

	├── analytics
   		├── generate_stats.py         # Script for DS visualizations
   		├── stats.png                 # Generated graphs
   		└── wordcloud.png             # Word cloud from report text

	├── os_tasks
   		└── file_watcher.py           # Simulate OS event monitoring

	├── tests/
   		├── curl_requests.sh          # curl tests for API
   		└── test_api.py               # Unittests for endpoints

	├── README.md                     
		└── readme.md
  		└── requirements
