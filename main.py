from flask import Flask
from src.RAG_end_to_end.logger import logging
from src.RAG_end_to_end.app import chat  # Import chat function from app.py

app = Flask(__name__)

# Define route
app.add_url_rule("/get", view_func=chat, methods=["GET", "POST"])

if __name__ == '__main__':
    logging.info("The app is running")
    app.run(host="0.0.0.0", port=8080, debug=True)
