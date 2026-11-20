# Larry Kalama | Portfolio

Personal portfolio of **Larry Kalama**, a systems developer with a focus on **software engineering, network engineering and cybersecurity**, based in Mombasa, Kenya.

**Live site:** https://larry-kalama.vercel.app

## About

I'm a BSc Information Technology graduate (Masinde Muliro University of Science and Technology). I build business systems in Python and Django with M-Pesa payments, and I have hands-on experience with enterprise networks from my attachment at Kenya Power (Cisco routing and switching, fiber optics, microwave links and SCADA support).

## Pages

| Page | What it shows |
| --- | --- |
| Home | Introduction and quick links |
| About | Background, focus areas and key facts |
| Resume | Education, experience, certifications and downloadable CV |
| Skills | Networking, software, cybersecurity and ICT support |
| Services | What I can do for clients |
| Projects | Selected projects with filters (Network, Software, Security) |
| Project demos | Video, screenshots with a zoomable viewer and a feature list for each software project |
| Contact | Email, phone, WhatsApp and location |

## Featured projects

- **Cafeteria POS**: point-of-sale system where staff log in, take orders and customers pay with an M-Pesa STK push. Includes stock control, expenses and sales analytics.
- **Horizon Aqua Management System (HAMS)**: full-stack system that replaced manual book recording for a water supplier, with inventory, sales, customers, deliveries and M-Pesa integration.
- **Biashara Smart Hub**: AI-powered business intelligence platform for SMEs with forecasting, credit scoring, reports, and web, USSD and WhatsApp access.

## Tech stack

- **Backend:** Python, Flask, Jinja2 templates
- **Frontend:** HTML, CSS (variable-driven theme), vanilla JavaScript
- **Image viewer:** custom zoom viewer built on the native `<dialog>` element (wheel, drag, pinch, keyboard)
- **Hosting:** Vercel, with automatic deploys from this repository

## Project structure

```
.
├── app.py                 # Flask app and routes
├── demos.py               # Data for each project demo page
├── requirements.txt
├── vercel.json
├── templates/             # Jinja2 templates (base.html, pages, project_detail.html)
└── public/
    └── static/            # CSS, JavaScript, images, video, CV
```

Static files live in `public/static` because Vercel serves the `public/` folder from its CDN.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Add a project demo

1. Add an entry to `DEMOS` in `demos.py` (title, summary, tags, steps, features, screenshots).
2. Put images in `public/static/img/projects/<name>/` and a video in `public/static/video/`.
3. Add or update the project card in `templates/projects.html`.
4. Commit and push. Vercel redeploys automatically.

## Contact

- Email: larrykalama8@gmail.com
- Phone / WhatsApp: +254 702 372 099
- Location: Mombasa, Kenya

© Larry Kalama