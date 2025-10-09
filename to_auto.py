import os
import getpass
import platform
import sys

print(platform.version())



def add_to_startup_W(file_path = os.path.realpath('Calendars.py')): # ДОБАВЕНИЕ БАТ-ФАЙЛА ДЛЯ РЕЗЕРВИРОВАНИЯ ПО ИНТЕРВАЛУ В ВИНДОВСС
    # имя текущего пользователя
    USER_NAME = getpass.getuser()

    # Путь к папке автозагрузки
    bat_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    # C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

    # Создаем bat-файл
    bat_file_path = os.path.join(bat_path, "autoopen.bat")

    try: 
        with open(bat_file_path, 'w+') as f: # ЗАПИСЬ КОМАНД В БАТ
            f.write(f'start "" "{file_path}"')
        print(f"Файл автозагрузки создан: {bat_file_path}")
        
    except Exception as e:
        print(f"Ошибка при создании файла автозагрузки: {e}")


def add_to_startup_LOS(): # ДОБАВЕНИЕ БАТ-ФАЙЛА ДЛЯ РЕЗЕРВИРОВАНИЯ ПО ИНТЕРВАЛУ В ИНУКС\МАК-ОС

    # НАБОР КОМАНД ДЛЯ БАТ
    script = f"""#!/bin/bash 
echo "Creating backup..."
cp -r {os.path.realpath('Calendars.py')}
echo "autoopen completed!"
"""

    filename = "autoopen.sh"
    try:
        # ПРЕДОСТАВЛЕНИЕ ПРАВ ДОСТУПА К ФАЙЛУ В UNIX
        # 7 - ВЛАДЕЛЕЦ: READ WRITE EXECUTE
        # 5 5 - ЧТЕНИЕ, ВЫПОЛНЕНИЕ
        os.chmod(filename, 0o755)
        
        with open(filename, 'w') as f: # ДОБАВЛЕНИЕ КОДА В ФАЙЛ АФТОЗАПУСКА ДЛЯ РАБОТЫ ФАЙЛА CALENDARS
            f.write(script)
        print(f"Файл автозагрузки создан: {filename}")

    except Exception as e:
        print(f"Ошибка при создании файла автозагрузки: {e}")
        

def start(): # ПРОВЕРКА ОПЕРАЦИОННОЙ СИСТЕМЫ
    if platform.system()=='Windows':
        add_to_startup_W()
    else:
        add_to_startup_LOS()




