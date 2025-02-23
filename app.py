<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Inicial</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            transition: background-color 0.3s, color 0.3s;
        }
        
        .black-theme {
            background-color: #000;
            color: white;
        }
        
        .purple-theme {
            background-color: #6A0DAD;
            color: white;
        }

        .navbar {
            background-color: #333;
            padding: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .profile-menu {
            position: relative;
            cursor: pointer;
        }

        .profile-menu img {
            width: 30px;
            height: 30px;
            border-radius: 50%;
        }

        .dropdown {
            display: none;
            position: absolute;
            top: 40px;
            right: 0;
            background-color: #444;
            padding: 10px;
            border-radius: 5px;
            width: 150px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .dropdown a {
            color: white;
            padding: 10px;
            text-decoration: none;
            display: block;
        }

        .dropdown a:hover {
            background-color: #555;
        }

        .product {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 10px;
        }

        .btn {
            display: inline-block;
            background-color: #ff4500;
            color: white;
            padding: 10px;
            text-decoration: none;
            border-radius: 5px;
        }

        .btn:hover {
            background-color: #ff6347;
        }
    </style>
</head>
<body class="black-theme">

    <div class="navbar">
        <div>DESENVOLVEDOR: GALEGO</div>
        <div class="profile-menu" onclick="toggleDropdown()">
            <img src="https://via.placeholder.com/30" alt="Perfil">
            <div class="dropdown" id="dropdownMenu">
                <a href="{{ url_for('logout') }}">Sair</a>
                <a href="javascript:void(0);" onclick="toggleTheme()">Trocar Tema</a>
            </div>
        </div>
    </div>

    <h1>Bem-vindo à Loja de Bots</h1>

    <div class="product">
        <h2>Bot de Venda</h2>
        <p>Este bot realiza vendas de forma semi automática no seu servidor.</p>
        <a href="https://discord.gg/tBcfB5j3Yf" class="btn">Comprar</a>
    </div>

    <div class="product">
        <h2>Bot de Moderação</h2>
        <p>Este bot ajuda na moderação do seu servidor, com várias funcionalidades.</p>
        <a href="https://discord.gg/tBcfB5j3Yf" class="btn">Comprar</a>
    </div>

    <div class="product">
        <h2>Bot de Ticket</h2>
        <p>Gerencie tickets e suporte no seu servidor com esse bot.</p>
        <a href="https://discord.gg/tBcfB5j3Yf" class="btn">Comprar</a>
    </div>

    <div class="product">
        <h2>Clone de Server</h2>
        <p>Clone um servidor mandando o link para o adm.</p>
        <a href="https://discord.gg/tBcfB5j3Yf" class="btn">Comprar</a>
    </div>

    <div class="product">
        <h2>Nitro Gift</h2>
        <p>Compre Nitro Gift para você ou amigos.</p>
        <a href="https://discord.gg/tBcfB5j3Yf" class="btn">Comprar</a>
    </div>

    <script>
        function toggleDropdown() {
            var dropdown = document.getElementById('dropdownMenu');
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        }

        function toggleTheme() {
            var body = document.body;
            if (body.classList.contains('black-theme')) {
                body.classList.remove('black-theme');
                body.classList.add('purple-theme');
            } else {
                body.classList.remove('purple-theme');
                body.classList.add('black-theme');
            }
        }

        window.onclick = function(event) {
            if (!event.target.matches('.profile-menu, .profile-menu *')) {
                var dropdown = document.getElementById('dropdownMenu');
                if (dropdown.style.display === 'block') {
                    dropdown.style.display = 'none';
                }
            }
        }
    </script>
</body>
</html>
