from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
import reses


# ФУНКЦИИ РЕЗЕРВИРОВАНИЯ ПО ВЫБРАННОМУ ПАРАМЕТРУ: ЧАС ДЕНЬ НЕДЕЛЯ МЕСЯЦ
def hour():
    reses.calendar_saves('час')
    print(f"Выполнено в {time.ctime()}")

def day():
    reses.calendar_saves('день')
    print(f"Выполнено в {time.ctime()}")

def week():
    reses.calendar_saves('неделя')
    print(f"Выполнено в {time.ctime()}")

def month():
    reses.calendar_saves('месяц')
    print(f"Выполнено в {time.ctime()}")



# Создаем фоновый планировщик
scheduler = BackgroundScheduler()


# ДОБАВЛЕНИЕ ЗАДАЧ В ПЛАНИРОВЩИК
scheduler.add_job(
    month,
    trigger=CronTrigger(day=1, hour=9, minute=0),
    id='месяц'
)

scheduler.add_job(
    week,
    trigger=CronTrigger(day_of_week='mon', hour=9, minute=0),
    id='неделя'
)

scheduler.add_job( # По расписанию каждый день в 14:30
    day,
    trigger=CronTrigger(hour=14, minute=30),
    id='день'
)

scheduler.add_job(
    hour,
    'interval',
    minutes=60,
    id='час'
)


# scheduler.pause_job()


# Запускаем планировщик
scheduler.start()

# ПОТОКОВЫЙ ЦИКЛ ПРОВЕРКИ ИНТЕРВАЛА И ЗАПУСКА РЕЗЕРВИРОВАНИЯ
try:
    # Основной поток продолжает работу
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    scheduler.shutdown()