import os
import getpass
import platform
import sys


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







# ДОБАВЕНИЕ БАТ-ФАЙЛА ДЛЯ РЕЗЕРВИРОВАНИЯ ПО ИНТЕРВАЛУ В ИНУКС
def add_to_startup_Linux(file_path=os.path.realpath('Calendars.py')):
    

    # Определяем домашнюю директорию
    home_dir = os.path.expanduser('~')
    
    # Для Linux путь:    ~/.config/autostart/
    autostart_dir = os.path.join(home_dir, '.config', 'autostart')
    desktop_file = os.path.join(autostart_dir, 'autoopen.desktop')
    
    # НАБОР КОМАНД ДЛЯ БАТ
    # Exec= - выбор интерпритатора python3, либо, если файл скомпилирован, то без интерпритатора прямой путь к файлу .exe
    # X-GNOME-Autostart-enabled=true - разрешение автозапуска   
    desktop_content = f"""[Desktop Entry]
Type=Application
Name=AutoOpen
Exec=python3 "{file_path}"
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
"""
    try:
        os.makedirs(autostart_dir, exist_ok=True)
        with open(desktop_file, 'w') as f:  # ДОБАВЛЕНИЕ КОДА В ФАЙЛ АФТОЗАПУСКА ДЛЯ РАБОТЫ ФАЙЛА CALENDARS
            f.write(desktop_content)
        
        # ПРЕДОСТАВЛЕНИЕ ПРАВ ДОСТУПА К ФАЙЛУ В UNIX
        # 7 - ВЛАДЕЛЕЦ: READ WRITE EXECUTE
        # 5 5 - ЧТЕНИЕ, ВЫПОЛНЕНИЕ
        os.chmod(desktop_file, 0o755)
        print(f"Файл автозагрузки создан: {desktop_file}")

    except Exception as e:
        print(f"Ошибка при создании файла автозагрузки: {e}")
    


# Для macOS
def add_to_startup_MAC(file_path=os.path.realpath('Calendars.py')):
            # Создаем launchd plist файл
        plist_dir = os.path.join(home_dir, 'Library', 'LaunchAgents')
        plist_file = os.path.join(plist_dir, 'com.user.autoopen.plist')
        
        # нашел код для бат файла на макОС
        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.autoopen</string>
    <key>ProgramArguments</key>
    <array>
        <string>python3</string>
        <string>{file_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
        try:
            os.makedirs(plist_dir, exist_ok=True)
            with open(plist_file, 'w') as f:
                f.write(plist_content)
            print(f"Файл автозагрузки создан: {plist_file}")
            return True
        except Exception as e:
            print(f"Ошибка при создании файла автозагрузки: {e}")
            return False




def start():
    file_path = os.path.realpath('Calendars.py')
    
    # существует ли основной файл
    if not os.path.exists(file_path):
        print(f"Ошибка: основной файл {file_path} не найден!")
        return
    
    syst = platform.system()
    
    if syst == 'Windows':
        add_to_startup_W()
    elif syst =='Linux':
        add_to_startup_LOS()
    elif syst=='Darwin':
        add_to_startup_MAC()
    else:
        print(f"Неподдерживаемая операционная система: {syst}")


# Дополнительная функция для удаления из автозагрузки
def remove_from_startup():
    system = platform.system()
    
    if system == 'Windows':
        bat_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', "autoopen.bat")
        if os.path.exists(bat_path):
            os.remove(bat_path)
            print("Файл автозагрузки удален")
    
    elif system == 'Linux':
        desktop_file = os.path.expanduser('~/.config/autostart/autoopen.desktop')
        if os.path.exists(desktop_file):
            os.remove(desktop_file)
            print("Файл автозагрузки удален")
    
    elif system == 'Darwin':
        plist_file = os.path.expanduser('~/Library/LaunchAgents/com.user.autoopen.plist')
        if os.path.exists(plist_file):
            os.remove(plist_file)
            print("Файл автозагрузки удален")

