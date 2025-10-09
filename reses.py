import shutil
import os


# ЧТЕНИЕ ДАННЫХ СОЗДАННЫ РЕЗЕРВОВ И СОЗДАНИЕ СЛОВАРЯ ИЗ ПОЛУЧЕННЫХ ЗНАЧЕНИЙ
def read_info_saves():
    with open('data.txt', 'r', encoding='utf-8') as f:
        a = f.readlines()
        a = [r.rstrip('\n') for r in a]
        data = {}
        for i in range(0, len(a) - 4):
            if a[i][0:3] == '-> ':
                data[a[i][3:]] = [a[i + 1], a[i + 2], a[i + 3], a[i + 4]]
    a.clear()
    return data


# def upd_saveFile(datas,path):


class dir_i:  # класс директории, которую резервируем

    def __init__(self, MotherPath, generalDir, copy_from, calendar, reserve_count): # ПУТЬ РЕЗЕРВА \ НАЗВАНИЕ РЕЗЕРВА \ ИЗНАЧАЬНЫЙ ПУТЬ \ ВРЕМЯ \ НОМЕР РЕЗЕРВА
        
        # СООЗДАНИЕ ПОЛНОГО ПУТИ ДО МЕСТА РЕЗЕРВИРОВАНИЯ
        self.MotherPath = MotherPath
        self.generalDir = generalDir.replace('\n','')
        self.copy_from = copy_from.replace('/', '\\')
        self.source_path = os.path.join(MotherPath, generalDir)
        self.calendar = calendar
        self.reserve_count = int(reserve_count) + 1
        self.source_path = self.source_path.replace('/', '\\')
        self.source_path = self.source_path[0:-1]
        self.final_path = os.path.join(self.source_path, f"reserve_{self.reserve_count}")
        self.final_path = self.final_path.replace('/', '\\')

    def to_saveData(self, datas):  # сохранение данных о резервах
        if self.exeption != True:
            return self.exeption
        datas[self.generalDir] = [self.MotherPath, self.copy_from, self.calendar, self.reserve_count]
        print('reses:')
        print(self.generalDir,self.calendar)
        print(datas)
        open('data.txt', 'w').close()  # форматирование файла

        with open('data.txt', 'a', encoding='utf-8') as f:
            for x in datas:
                f.writelines(f'-> {x}\n')
                f.writelines(f'{datas[x][0]}\n')  # \n witn writelines
                f.writelines(f'{datas[x][1]}\n')
                f.writelines(f'{datas[x][2]}\n')
                f.writelines(f'{datas[x][3]}\n')
        return self.exeption


    def save_vers(self): # ДЛЯ АВТОМАТИЧЕСКОГО РЕЗЕРВИРОВАНИЯ ИЗМЕНЕНИЕ НОМЕРА РЕЗЕРВА
        with open('data.txt', 'r', encoding='utf-8') as f:
            t=f.readlines()
        for i in range(len(t)):
            if t[i]==self.generalDir:
                t[i+3]=self.reserve_count+1
                break
        f.close()

        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(t)
        f.close()


    # def create_dir_i(self):
    #
    #     os.makedirs(self.final_path, 0o777, True)
    #
    #     return self.final_path

    def reserve_i(self): # СОЗДАНИЕ РЕЗЕРВА С ПОМОЩЬЮ ПОЛНОГО ПУТИ К ИЗНАЧАЛЬНОЙ ПАПКЕ И ПУТИ РЕЗЕРВИРОВАНИЯ
        try:
            shutil.copytree(self.copy_from, self.final_path)
            self.exeption = True
        except Exception as e:
            self.exeption = e


# ФУНКЦИЯ АВТОМАТИЧЕСКОГО РЕЗЕРВИРОВАНИЯ ПО ПЕРЕДАННОМУ ПРОМЕЖУТКУ: Ч Д Н М
def calendar_saves(date):

    datas = read_info_saves()

    cal=[]
    for i in datas:
        if datas[i][2]==date:
            cal.append(i)
    
    if len(cal)==0:
        return

    for i in cal:
        name=i
        MotherPath=datas[i][0]
        copy_from=datas[i][1]
        calendar=datas[i][2]
        fileX = dir_i(MotherPath, name, copy_from, calendar,
                            datas[i][3]) 
        fileX.reserve_i()  # создание резерва в директории current_backup
        fileX.save_vers()



def console_show():
    os.system("start run /k python main.py")


