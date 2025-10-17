# login module

def login(username, password):

    if not username or not password:
        return False
    return True

import hashlib
import getpass
from typing import Optional


_USUARIOS_PLAINTEXT = {
    "admin": "1234",
    "barbara": "abcd",
    "julia": "qwerty",
}

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

USUARIOS = {u: _hash_password(p) for u, p in _USUARIOS_PLAINTEXT.items()}


def authenticate(username: str, password: str) -> bool:
    """Verifica si las credenciales son válidas."""
    if username not in USUARIOS:
        return False
    return USUARIOS[username] == _hash_password(password)


def login(prompt_cli: bool = True, max_attempts: int = 3,
          username: Optional[str] = None, password: Optional[str] = None) -> Optional[str]:
    """
    Proceso de login.
    - Si se pasan username/password, hace la autenticación directamente y devuelve el usuario o None.
    - Si prompt_cli=True solicita credenciales por consola (oculta la contraseña) hasta max_attempts.
    Retorna el nombre de usuario al iniciar sesión correctamente, o None si falla.
    """
    # Credenciales directas (uso programático)
    if username is not None and password is not None:
        return username if authenticate(username, password) else None

    # Flujo interactivo por consola
    intentos = 0
    while intentos < max_attempts:
        usuario = input("Usuario: ").strip()
        contraseña = getpass.getpass("Contraseña: ")
        if authenticate(usuario, contraseña):
            print(f"✅ Bienvenido {usuario}, has iniciado sesión correctamente.")
            return usuario
        else:
            intentos += 1
            print(f"❌ Credenciales incorrectas. Intentos restantes: {max_attempts - intentos}")
    print("🔒 Has superado el número máximo de intentos.")
    return None


if __name__ == "__main__":
    # Ejecuta el login en modo interactivo si se ejecuta como script
    login()