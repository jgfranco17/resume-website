# Launches an instance of the Flask application
from web import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)