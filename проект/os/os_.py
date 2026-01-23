import sys
import os, shutil
from rich.console import Console as Cons
import json
from time import sleep

# --- НАСТРОЙКА ПУТЕЙ ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, 'settings.json')
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

os.system('cls' if os.name == 'nt' else 'clear')

try:
    from math_and_intelect import main_расчетов
except ImportError:
    main_расчетов = None

def main():
    con = Cons()

    # Дефолтные настройки
    default_settings = {"user": "kirill", "version": "1.5.5", "start": 9, "color": {"fon": "#ff6600", "text": "#ff0000"}}


    # --- ЗАГРУЗКА И ОБНОВЛЕНИЕ СЧЕТЧИКА ---
    if not os.path.exists(CONFIG_PATH) or os.stat(CONFIG_PATH).st_size == 0:
        settings = default_settings
    else:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
            try:
                settings = json.load(file)
            except json.JSONDecodeError:
                settings = default_settings

    # Увеличиваем счетчик запусков
    settings["start"] = settings.get("start", 0) + 1
    
    # Сохраняем обновленные настройки (теперь счетчик реально пишется в JSON)
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

    def draw_ui():
        """Функция для отрисовки шапки, чтобы не дублировать код"""
        c_fon = settings.get("color", {}).get("fon", "#ad3bff")
        c_text = settings.get("color", {}).get("text", "#1bb3a3")
        size = shutil.get_terminal_size().columns
        os.system('cls' if os.name == 'nt' else 'clear')
        
        con.print(f'[{c_fon}]#[/]' * size)
        # Добавили инфу о запусках в шапку!
        header_text = f"{settings.get('user', 'User').capitalize()} OS {settings.get('version', '1.0')} (Запуск #{settings['start']})"
        con.print(f'[{c_text}]{header_text.center(size)}[/]')
        con.print(f'[{c_fon}]#[/]' * size)

    draw_ui()

    while True:
        command = input(f"{settings.get('user', 'user')}@os: ").strip().lower() 
        
        if command == 'help':
            print('''
help    - показывает это окно
version - показывает версию ос
cls     - очистить экран
exit, e - выйти
cal     - калькулятор
restart - полная перезагрузка интерфейса
''')
        elif command == 'version':
            print(f"Version: {settings.get('version', '1.0')} (Runs: {settings.get('start')})")
            
        elif command == 'cls' or command == 'restart':
            draw_ui()
            if command == 'restart':
                con.print("[yellow]Система перезагружена...[/]")

        elif command == 'cal':
            if main_расчетов:
                main_расчетов.main()
            else:
                print("Ошибка: калькулятор не найден!")
                
        elif not command:
            continue
            
        elif command in ['exit', 'e']:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(f'команда \'{command}\' не определена')

if __name__ == "__main__":
    main()
