"""Project demo pages. Add a new entry to DEMOS to create /projects/<slug>.

kind:   optional label above the title (default "Software project").
download: optional {"file": "files/lab.pkt", "label": "..."} shown as a button when the file exists in static/.
shots:  file is relative to static/. Use file=None for a "coming soon" placeholder.
video:  put an .mp4 in static/video/ and set "video" to its file name, or set "youtube" to a video id.
"""

DEMOS = {
    "cafeteria-pos": {
        "title": "Cafeteria POS",
        "summary": ("A point-of-sale system for a cafeteria. Staff log in, build an order from the menu, "
                    "and the customer pays with an M-Pesa STK push prompt on their phone. Stock, expenses "
                    "and sales reports are handled in the same system."),
        "tags": ["Python", "Django", "M-Pesa Daraja API", "STK Push"],
        "video": "cafeteria-pos-demo.mp4",
        "youtube": "",
        "flow": [
            ("Log in", "Each waiter signs in with their own account, so every order is linked to who took it."),
            ("Build the order", "Pick items by category, set quantities, and add an optional customer name and table number."),
            ("Pay by STK push", "A payment prompt is sent to the customer's phone and they enter their M-Pesa PIN."),
            ("Order recorded", "The order appears in the orders list, stock updates, and sales figures feed the reports."),
        ],
        "features": [
            "Role-based login for staff",
            "Order screen with categories, live stock counts and a cart",
            "M-Pesa STK push payment",
            "Orders list with status filter and printing",
            "Menu and category management",
            "Stock levels with low-stock and out-of-stock alerts",
            "Expense tracking with date filters and CSV export",
            "Sales analytics: payment methods, top-selling items, waiter performance",
        ],
        "shots": [
            {"file": "img/projects/cafeteria-pos/01-login.webp", "title": "Staff login",
             "caption": "Each user signs in with their own account."},
            {"file": "img/projects/cafeteria-pos/02-dashboard.webp", "title": "Dashboard",
             "caption": "Today's orders and sales, pending credit and low-stock items at a glance, with recent orders and one-click Add Stock."},
            {"file": "img/projects/cafeteria-pos/03-new-order.webp", "title": "New order",
             "caption": "Items by category with live stock counts, a cart with quantities, optional customer and table, and Place Order."},
            {"file": None, "title": "STK push payment",
             "caption": "Screenshot of the M-Pesa prompt coming soon."},
            {"file": "img/projects/cafeteria-pos/04-orders.webp", "title": "All orders",
             "caption": "Every order with its waiter, total and status. Filter by status, view or print."},
            {"file": "img/projects/cafeteria-pos/05-menu.webp", "title": "Menu items",
             "caption": "Items with category, price and availability. Search, edit, delete and manage categories."},
            {"file": "img/projects/cafeteria-pos/06-stock.webp", "title": "Stock levels",
             "caption": "Current stock, unit, reorder level and status, with filters for low and out-of-stock items."},
            {"file": "img/projects/cafeteria-pos/07-expenses.webp", "title": "Expenses",
             "caption": "Expenses by category with totals, date filters and CSV export."},
            {"file": "img/projects/cafeteria-pos/08-analytics.webp", "title": "Sales analytics",
             "caption": "Total sales, order count, average order, payment methods and top-selling items for any date range."},
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
    "peer-to-peer-network": {
        "kind": "Network project",
        "title": "Peer-to-Peer Network Lab",
        "summary": ("A peer-to-peer network built and tested in Cisco Packet Tracer. Computers connect to one "
                    "another directly, with no central server, and each one can share its own resources and "
                    "reach every other peer."),
        "tags": ["Cisco Packet Tracer", "LAN", "IP Addressing", "Switching", "Connectivity Testing"],
        "video": "peer-to-peer-network-demo.mp4",
        "youtube": "",
        "download": {"file": "files/peer-to-peer-network.pkt", "label": "Download Packet Tracer file"},
        "flow": [
            ("Plan the topology", "Decide how many peers are needed and how they connect to one another."),
            ("Build it in Packet Tracer", "Place the end devices and the switch, then cable them together."),
            ("Address every peer", "Give each computer an IP address and subnet mask in the same network."),
            ("Test connectivity", "Use ping between peers to prove that every computer can reach the others."),
        ],
        "features": [
            "No dedicated server: every computer is both client and server",
            "All peers on one LAN, connected through a switch",
            "Static IP addressing and subnet masks on every host",
            "Peer-to-peer communication verified with ping",
            "Packet flow inspected in Packet Tracer simulation mode",
            "Downloadable .pkt file so the lab can be opened and tried",
        ],
        "shots": [
            {"file": None, "title": "Network topology", "caption": "The peers and the switch laid out in Packet Tracer."},
            {"file": None, "title": "IP configuration", "caption": "Addresses and subnet masks set on the peers."},
            {"file": None, "title": "Connectivity test", "caption": "Ping results between peers."},
            {"file": None, "title": "Simulation mode", "caption": "A packet travelling between two peers."},
        ],
    },
}
