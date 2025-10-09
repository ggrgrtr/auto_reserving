import reses
import Graphics
import to_auto

to_auto.start()

datas = reses.read_info_saves()

window = Graphics.my_window(datas) # СОЗДАНИЕ ЭКЗЕМПЛЯРА ОКНА С ВОЗМОЖНОСТЬЮ ВЫБОРА ПРОШЛЫХ РЕЗЕРВОВ
window.windows() # СОЗДАНИЕ ОКНА ПО ЭКЗЕМПЛЯРУ

generalReserveDir_name, MotherPath, copy_from, calendar, count = window.returned_data()

files = reses.dir_i(MotherPath, generalReserveDir_name, copy_from, calendar,
                    count)  # СОЗДАНИЕ ТЕКУЩЕГО РЕЗЕРВА ЧЕРЕЗ ЭКЗЕМПЛЯРА КЛАССА 
files.reserve_i()  # создание резерва в директории current_backup

exc=files.to_saveData(datas)  # сохранение данных о резервах

if exc!=True: # ЕСЛИ ДАННЫЕ О НОВОМ РЕЗЕРВЕ НЕ СОХРАНИЛИСЬ -> ОКНО ОШИБКИ
    window.window_Err(exc)

datas.clear()