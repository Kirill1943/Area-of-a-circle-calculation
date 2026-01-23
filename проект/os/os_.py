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
    from math_and_intelect import main_расчетов, ports, периметр_и_площадь
except ImportError:
    main_расчетов = lambda: None

def bootloader(boot_=True):
    con = Cons()
    if boot_:
        # ... (код bootloader опущен для краткости) ...
        pass

def main():
    con = Cons()

    default_settings = {"user": "visae", "version": "1.0"}

    # Если файла нет ИЛИ он пустой/битый
    if not os.path.exists(CONFIG_PATH) or os.stat(CONFIG_PATH).st_size == 0:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            # Запись происходит здесь:
            json.dump(default_settings, f, indent=4) 
        settings = default_settings
    else:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
            try:
                settings = json.load(file)
            except json.JSONDecodeError:
                # Если файл поврежден, используем настройки по умолчанию как запасной вариант
                settings = default_settings
    # -----------------------------------------------

    size = shutil.get_terminal_size().columns
    con.print('[#ad3bff]#[/]'*size)
    header_text = f"{settings['user'].capitalize()} OS {settings['version']}"
    con.print(f'[#1bb3a3]{header_text.center(size)}[/]')
    con.print('[#ad3bff]#[/]'*size)

    while True:
        command = input(f"{settings['user']}@os {settings['version']}: ").strip().lower() 
        if command == 'help':
            print(
'''
help - показывает это окно
version - показывает версию ос
exit, e - выйти
cal - калькулятор
''')
        elif command == 'version':
            print(f"Version: {settings['version']}")
        elif command == 'cal':
            main_расчетов.main()
        elif not command:
            continue
        elif command in ['exit', 'e']:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(f'команда \'{command}\' не определена')

if __name__ == "__main__":
    main()
