📬 Email News App
This is a simple Python script that fetches the latest Tesla-related news using NewsAPI and prints the article titles and descriptions. It can be extended to save news to CSV, PDF, or send them via email.

🧠 Features
Fetches real-time news from NewsAPI

Filters articles by keyword (tesla)

Displays article title and description

Easily extendable to export or email articles

🛠️ Requirements
Python 3.6+

requests module

Install dependencies using pip:

bash
Copy
Edit
pip install requests
🚀 How to Run
Clone this repository or download the files.

Replace the API key in main.py with your own from https://newsapi.org.

python
Copy
Edit
api_key = "YOUR_API_KEY"
Run the script:

bash
Copy
Edit
python main.py
You’ll see output like:

markdown
Copy
Edit
Tesla Model 3 hits new record sales
The Tesla Model 3 has become the most sold EV this year.
--------------------------------------------------------------------------------
...
📦 File Structure
bash
Copy
Edit
email-news-app/
│
├── main.py         # Main script to fetch and display news
├── tesla_news.csv  # (Optional) Saved news articles in CSV format
└── README.md       # You're here!
🔑 Get a NewsAPI Key
Go to https://newsapi.org/register

Sign up and copy your free API key

Replace it in main.py

