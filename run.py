from app import create_app

# Criar a aplicação Flask
app = create_app()

# Rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
