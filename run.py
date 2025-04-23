from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename='request_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Optional: log to console as well
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Import routes AFTER setting up the app and logging
from app.routes import main
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)