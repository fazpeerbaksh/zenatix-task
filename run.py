from myapp import app
import os

if __name__ == '__main__':
    app.secret_key = os.environ.get('APP_SECRET')
    app.run(debug=True)