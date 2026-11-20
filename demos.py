"""Project demo pages. Add a new entry to DEMOS to create /projects/<slug>.

shots:  file is relative to static/. Use file=None for a "coming soon" placeholder.
video:  put an .mp4 in static/video/ and set "video" to its file name, or set "youtube" to a video id.
"""

DEMOS = {
    "cafeteria-pos": {
        "title": "Cafeteria POS",
        "summary": (
            "End-to-end point-of-sale system built for cafeterias. "
            "Staff authenticate, build orders placed by customers from a live menu with real-time stock, "
            "and customers make payments to complete the order either by cash or M-Pesa STK Push. "
            "The same system tracks expenses, surfaces sales analytics, works offline as a PWA, "
            "and runs in production on Railway with media served from Cloudinary."
        ),
        "tags": [
            "Python",
            "Django",
            "PostgreSQL",
            "M-Pesa STK Push",
            "PWA",
            "Cloudinary",
            "Railway",
        ],
        "video": "cafeteria-pos-demo.mp4",
        "youtube": "",
        "flow": [
            (
                "Staff login",
                "Each waiter signs in with their own account. Role-based access protects orders, "
                "expenses and reports so every action is attributable.",
            ),
            (
                "Build the order",
                "Browse items by category, see live stock badges, adjust quantities in a sticky cart, "
                "and optionally add customer name or table number — designed for speed at peak service.",
            ),
            (
                "Choose payment method",
                "Complete the sale with cash, credit, or M-Pesa. Selecting M-Pesa triggers an STK Push "
                "to the customer’s phone number.",
            ),
            (
                "STK Push & confirmation",
                "Customer approves the payment with their PIN . "
                "Safaricom’s callback hits the server and marks the payment successful automatically.",
            ),
            (
                "Receipt & live records",
                "A permanent order record and receipt are created. Stock is decremented, the dashboard "
                "KPIs refresh, and sales analytics update in real time.",
            ),
        ],
        "features": [
            "M-Pesa STK Push (CustomerBuyGoodsOnline / PINLESS Till) with real callback handling",
            "Cash, credit and mobile-money payment paths in one order flow",
            "Live stock feedback on the order screen — prevents overselling",
            "Dashboard KPIs + low-stock alerts for at-a-glance operations",
            "Expense tracking with staff attribution",
            "Sales analytics (revenue, top sellers, payment mix)",
            "Offline-first PWA: service worker, offline queue and fallback page",
            "Media on Cloudinary (no broken image 404s in production)",
            "Production deployment on Railway (Gunicorn + PostgreSQL + Whitenoise)",
            "Null-safe templates and robust error handling on payment / logout / expenses",
            "Receipt generation after successful payment",
            "Dark + gold visual system tuned for long service shifts",
        ],
        "shots": [
            {
                "file": "img/projects/cafeteria-pos/01-login.webp",
                "title": "Staff Login",
                "caption": "Clean dark form with gold accents. Role-based access protects sales and expense data.",
            },
            {
                "file": "img/projects/cafeteria-pos/02-dashboard.webp",
                "title": "Dashboard",
                "caption": "KPI cards (revenue, orders, average ticket, low-stock alerts) plus recent orders for instant situational awareness.",
            },
            {
                "file": "img/projects/cafeteria-pos/03-new-order.webp",
                "title": "New Order",
                "caption": "Category tabs, live stock indicators, and a sticky cart. Designed for speed during peak service.",
            },
            {"file": None, "title": "STK push payment",
             "caption": "Screenshot of the M-Pesa prompt coming soon."},
            {
                "file": "img/projects/cafeteria-pos/04-orders.webp",
                "title": "All Orders",
                "caption": "Filterable list with clear status badges (Paid, Pending, Credit). Easy search and date filters.",
            },
            {
                "file": "img/projects/cafeteria-pos/05-menu.webp",
                "title": "Menu Items",
                "caption": "CRUD for products with images (Cloudinary), prices and categories. Instant availability control.",
            },
            {
                "file": "img/projects/cafeteria-pos/06-stock.webp",
                "title": "Stock Levels",
                "caption": "Visual stock overview with low-stock warnings so staff never sell what they don’t have.",
            },
            {
                "file": "img/projects/cafeteria-pos/07-expenses.webp",
                "title": "Expenses",
                "caption": "Track daily costs with paid-by attribution. Null-safe templates keep the list stable under incomplete data.",
            },
            {
                "file": "img/projects/cafeteria-pos/08-analytics.webp",
                "title": "Sales Analytics",
                "caption": "Charts and summaries for revenue trends, top items and payment-method mix — ready for management decisions.",
            },
        ],
        "principles": [
            {
                "title": "Speed-first order flow",
                "text": "Category tabs, live stock badges and a sticky cart keep staff moving during peak service without hunting for controls.",
            },
            {
                "title": "Dark + gold visual system",
                "text": "High-contrast dark UI with gold accents reduces eye strain on long shifts and makes status and money amounts easy to scan.",
            },
            {
                "title": "Live stock feedback",
                "text": "Every menu item shows current stock. The system never lets staff sell what is already zero.",
            },
            {
                "title": "Clear status language",
                "text": "Paid, Pending, Credit and low-stock states use consistent colour and wording so the whole team reads the same signals.",
            },
            {
                "title": "Role-aware & auditable",
                "text": "Login gates every action. Expenses record who paid them. Orders and payments leave a clear trail for the owner.",
            },
        ],
    },
"biashara-smart-hub": {
        "title": "Biashara Smart Hub",
        "summary": ("An AI-powered business intelligence platform for Kenyan small and medium enterprises. "
                    "Owners record sales, expenses and stock, watch a live dashboard, get sales forecasts and a "
                    "credit score, and reach it from a web app, USSD on any phone or WhatsApp. "
                    "Built as a final-year project at Masinde Muliro University and pitched to SMEs."),
        "tags": ["Python", "Django", "REST API", "React PWA", "ARIMA/Prophet", "Celery",
                 "M-Pesa Daraja API", "Africa's Talking", "SQLite/MySQL"],
        "video": "biashara-smart-hub-demo.mp4",
        "youtube": "",
        "flow": [
            ("Register and set up", "Sign up with phone and OTP or email, then create one or more business profiles with an M-Pesa till or paybill."),
            ("Record the business", "Enter sales, expenses and stock movements, one by one or by CSV import, from the web app, USSD or WhatsApp."),
            ("Get AI insights", "The dashboard updates live while forecasting models predict next month's sales and expenses and score credit readiness."),
            ("Act on them", "Receive low-stock and cash-flow alerts, export reports, and apply for a loan with a ready Loan Readiness Report."),
        ],
        "features": [
            "Phone and OTP registration, email login and password recovery",
            "JWT authentication with token refresh",
            "Multiple business profiles per account",
            "Owner and staff roles with role-based permissions",
            "Sales, expense and stock transaction entry",
            "Categories, payment modes, tags and custom categories",
            "Bulk entry and CSV/Excel import of legacy records",
            "Edit and delete with confirmation and server-side validation",
            "Real-time dashboard: sales, expenses, profit and loss, cash flow, top sellers",
            "Interactive line, bar and pie charts",
            "AI sales and expense forecasts (ARIMA/Prophet) with monthly retraining",
            "Inventory tracking with reorder points and suggested reorder quantities",
            "Low-stock and cash-flow alerts by SMS and WhatsApp",
            "Daily, weekly, monthly and custom-period reports",
            "Profit and loss and inventory status reports",
            "Report export to HTML, CSV and PDF with charts",
            "Credit scoring out of 100 from transaction history",
            "Loan Readiness Report (PDF) and one-click loan application",
            "M-Pesa Daraja integration: incoming payment callbacks and premium payments",
            "Progressive Web App with offline entry and automatic sync",
            "USSD menu for feature phones on Safaricom and Airtel",
            "WhatsApp bot answering questions like \"Sales today?\"",
            "Audit trail of every add, edit and delete",
            "English and Swahili interface, alerts and reports",
            "Automated daily backups and full data export",
            "Swagger API documentation and Docker deployment",
        ],
        "shots": [
            {"file": None, "title": "Registration and login", "caption": "Phone and OTP or email sign-up, with JWT-secured sessions."},
            {"file": None, "title": "Business profile", "caption": "Business name, sector, location and M-Pesa till or paybill. Multiple businesses per account."},
            {"file": None, "title": "Dashboard", "caption": "Sales, expenses, profit and loss, cash flow and top sellers with live charts."},
            {"file": None, "title": "Add transaction", "caption": "Record sales, expenses and stock with category and payment mode, or import from CSV."},
            {"file": None, "title": "Inventory", "caption": "Stock levels, reorder points and suggested reorder quantities."},
            {"file": None, "title": "AI forecast", "caption": "Next-month sales and expense forecast with the credit score."},
            {"file": None, "title": "Reports and export", "caption": "Sales, profit and loss and inventory reports as HTML, CSV or PDF."},
            {"file": None, "title": "Loan readiness", "caption": "Credit score and the Loan Readiness Report for banks and lenders."},
            {"file": None, "title": "USSD and WhatsApp", "caption": "Feature-phone menu and WhatsApp bot for quick queries and alerts."},
            {"file": None, "title": "Staff, audit trail and language", "caption": "Staff roles, activity log and English/Swahili switch."},
        ],
    },
}