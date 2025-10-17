import os
import json
from typing import Optional

SESSION_FILE = os.path.join(os.path.dirname(__file__), "session.json")

def load_session() -> Optional[str]:
    """Devuelve el usuario de la sesión activa (si existe)."""
    if not os.path.exists(SESSION_FILE):
        return None
    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("user")
    except Exception:
        return None

def cerrar_sesion() -> bool:
    """Cierra la sesión eliminando el archivo de sesión. Devuelve True si había sesión y se cerró."""
    user = load_session()
    if not user:
        print("🔒 No hay sesión activa.")
        return False
    try:
        os.remove(SESSION_FILE)
    except OSError:
        pass
    print(f"✅ Sesión cerrada para {user}.")
    return True

if __name__ == "__main__":
    cerrar_sesion()