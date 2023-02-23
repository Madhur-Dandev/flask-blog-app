from flask import Blueprint, render_template
views = Blueprint("views", __name__, static_folder="static",
                  template_folder="template")


@views.route("/")
def index():
    return "<h1>Hello World!</h1>"
