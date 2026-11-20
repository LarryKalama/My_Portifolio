import os
from datetime import date

from flask import Flask, abort, render_template, request

from demos import DEMOS

app = Flask(__name__)

NAV = [("Home", "home"), ("About", "about"), ("Resume", "resume"),
       ("Skills", "skills"), ("Services", "services"),
       ("Projects", "projects"), ("Contact", "contact")]


@app.context_processor
def inject_globals():
    # CV button links to static/files/cv.pdf if it exists, otherwise stays inactive
    cv_file = os.path.join(app.static_folder, "files", "cv.pdf")
    endpoint = request.endpoint
    if endpoint == "project_detail":      # keep "Projects" highlighted on demo pages
        endpoint = "projects"
    return {
        "nav": NAV,
        "current": endpoint,
        "year": date.today().year,
        "cv_url": "/static/files/cv.pdf" if os.path.exists(cv_file) else "#",
        "demos": DEMOS,
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/projects/<slug>")
def project_detail(slug):
    demo = DEMOS.get(slug)
    if demo is None:
        abort(404)
    video_ok = bool(demo.get("video")) and os.path.exists(
        os.path.join(app.static_folder, "video", demo["video"]))
    return render_template("project_detail.html", d=demo, slug=slug, video_ok=video_ok)


if __name__ == "__main__":
    app.run(debug=True)

