# from ntpath import join
# from dotenv import load_dotenv
# load_dotenv(join(__file__))
from flask import Flask
from views.views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="")

if __name__ == "__main__":
    app.run(debug=True)
