from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Café Aurora - Tu rincón favorito ☕</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background: #f4f1ee;
            color: #333;
            text-align: center;
        }
        header {
            background: #6f4e37;
            color: white;
            padding: 20px;
        }
        nav button {
            margin: 10px;
            padding: 10px 20px;
            background: #d7ccc8;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
        }
        nav button:hover {
            background: #bcaaa4;
        }
        .menu-section {
            display: none;
            padding: 20px;
            animation: fadeIn 0.5s;
        }
        .active {
            display: block;
        }
        .item {
            background: white;
            border-radius: 10px;
            margin: 10px auto;
            padding: 15px;
            width: 300px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        footer {
            background: #6f4e37;
            color: white;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>☕ Café Aurora</h1>
        <p>Tu rincón favorito para disfrutar un buen café</p>
    </header>

    <nav>
        <button onclick="showMenu('cafes')">Cafés</button>
        <button onclick="showMenu('postres')">Postres</button>
        <button onclick="showMenu('bebidas')">Bebidas frías</button>
    </nav>

    <section id="cafes" class="menu-section active">
        <div class="item"><h3>Espresso</h3><p>Fuerte y aromático. $2.00</p></div>
        <div class="item"><h3>Capuccino</h3><p>Con espuma de leche. $2.50</p></div>
        <div class="item"><h3>Latte</h3><p>Suave y cremoso. $3.00</p></div>
    </section>

    <section id="postres" class="menu-section">
        <div class="item"><h3>Cheesecake</h3><p>Con salsa de frutos rojos. $3.50</p></div>
        <div class="item"><h3>Brownie</h3><p>Chocolate intenso. $2.80</p></div>
        <div class="item"><h3>Croissant</h3><p>Recién horneado. $1.50</p></div>
    </section>

    <section id="bebidas" class="menu-section">
        <div class="item"><h3>Frappé de café</h3><p>Refrescante y cremoso. $3.20</p></div>
        <div class="item"><h3>Limonada</h3><p>Natural y fresca. $2.00</p></div>
        <div class="item"><h3>Té helado</h3><p>Con toque de menta. $2.20</p></div>
    </section>

    <footer>
        <p>© 2025 Café Aromas · Hecho con ❤️ y Flask</p>
    </footer>

    <script>
        function showMenu(id) {
            document.querySelectorAll('.menu-section').forEach(section => {
                section.classList.remove('active');
            });
            document.getElementById(id).classList.add('active');
        }
    </script>
</body>
</html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

