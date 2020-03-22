"""? Писать ли комментарий в начале модулей

? как называть модуль main.py, app.py или ещё как-то
"""

from server import app

# ? Определять ли main функцию
def main():
    app.run(host='0.0.0.0')


# Всегда ли писать __name__ == "__main__" ?
if __name__ == "__main__":
    main()
