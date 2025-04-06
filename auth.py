usuarios = {
    "admin": "1234",
    "usuario1": "senha123",
    "usuario2": "teste456",
    "pedru": "Drumond@2022"
}

def autenticar_usuario(username, password):
    return username in usuarios and usuarios[username] == password