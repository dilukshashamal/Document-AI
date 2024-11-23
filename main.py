from flask import Flask

# Create the Flask app instance
app = Flask(__name__, template_folder='app/template')

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
