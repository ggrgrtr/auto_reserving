import tkinter as graphic
import reses
from tkinter import filedialog
from tkinter import ttk


# ФАЙЛ СОЗДАНИЯ ПОЛЬЗОВАТЕЛЬСКИХ ОКОН 
# РАБОТА С TKINTER

class my_window:

    def __init__(self, data):
        self.textInput = ''
        self.dir_which_reserve = ''
        self.dirPlace_toReserve = ''
        self.selected_value = ''
        self.options = []
        self.calendar_options = ('час', 'день', 'неделю', 'месяц')
        self.calendar_value = ''
        self.data = data

        if len(self.data) != 0:
            for x in self.data:
                self.options.append(x)


    # ОКНО ОШИБКИ (ЕСЛИ РЕЗЕРВИРОВАНИЕ НЕ УДАЛОСЬ)
    def window_Err(self, exc):

        root1 = graphic.Tk()
        root1.title("WINDOW")
        root1.geometry("700x250")

        label_exc = graphic.Label(root1, text=f'Ошибка:\n {exc}') # exc - причина ошибки, передаваемая в функцию
        label_exc.config(foreground="#ffffff", background='#ff6b6b', font='Courier 13')
        label_exc.pack(side=graphic.TOP)
        label_exc.place(x=10, y=30)

        def end():
            root1.destroy()

        # кнопка завершения
        buttonEr = graphic.Button(root1, text="Понятно", command=end)
        buttonEr.pack()
        root1.update_idletasks()
        buttonEr.place(x=10, y=30 + label_exc.winfo_height() + 2)

        root1.mainloop()

    # ВОЗВРАЩЕНИЕ ПОЛУЧЕННЫХ ОТ ПОЛЬЗОВАТЕЛЯ ДАННЫХ
    def returned_data(self):
        try:
            count = self.data[self.selected_value][3]
            print('self.data:', self.data[self.selected_value][3])
        except:
            count = 0
        return self.textInput, self.dirPlace_toReserve, self.dir_which_reserve, self.calendar_value, count

    # ФУНКЦИЯ ДЛЯ ВЫБОРА ПАПКИ ДЛЯ РЕЗЕРВИРОВАНИЯ ЧЕРЕЗ ДИАЛОГОВОЕ ОКНО
    def open_dirPlace_toReserve(self):
        self.dirPlace_toReserve = filedialog.askdirectory()
        self.label.config(text=self.dirPlace_toReserve)

    # ФУНКЦИЯ ДЛЯ ВЫБОРА ИЗНАЧАЛЬНОЙ ПАПКИ ЧЕРЕЗ ДИАЛОГОВОЕ ОКНО
    def open_dir_which_reserve(self):
        self.dir_which_reserve = filedialog.askdirectory()
        self.label2.config(text=self.dir_which_reserve)


    #ФУНКЦИЯ ОТОБРАЖЕНИЯ ГЛАВНОГО ОКНА
    def windows(self):
        # ЗАПУСКАЕМ ОКНО ВЗАИМОДЕЙСТВИЯ
        root = graphic.Tk()
        root.title("WINDOW")
        root.geometry("800x500")
        x = 15
        y = 200

        def selected_option(event):
            self.selected_value = menu.get()
            self.textInput = self.selected_value
            self.calendar_value = calendarBox.get()
            self.dirPlace_toReserve = self.data[self.selected_value][0]
            self.dir_which_reserve = self.data[self.selected_value][1]
            self.label.config(text=self.dirPlace_toReserve)
            self.label2.config(text=self.dir_which_reserve)
            # menu.set()
            text.insert('1.0', self.textInput)
            calendarBox.set(self.data[self.selected_value][2])

        def selected_calendar(events):
            self.calendar_value = calendarBox.get()

        # ЛЭЙБЛ ПРОВЕРКИ ДОСТАТОЧНОСТИ ДАННЫХ
        def accept():
            self.textInput = text.get("1.0", graphic.END)
            if self.dir_which_reserve == '' or self.dirPlace_toReserve == '' or self.textInput == '':
                label_ERR.pack()
                label_ERR.config(foreground="#ffffff", background='#ff6b6b', text='Информации не достаточно',
                                 font='Courier 13', width=25)

                label_ERR.place(x=15 + labeldata.winfo_width(), y=325)
            else:
                label_ERR.destroy()


        # НАДПИСЬ НАД ПОЛЕМ ВВОДА
        label_nameDir = graphic.Label(root, text='Имя резерва:', width=30)
        label_nameDir.config(foreground="#01579B", background='#B3E5FC', font='Courier 13')
        label_nameDir.pack()
        label_nameDir.place(x=x, y=10)


        # ПОЛЕ ВВОДА НАЗВАНИЯ ПАПКИ РЕЗЕРВА
        text = graphic.Text(root, height=1, width=30)
        text.config(font='Courier 13')
        text.pack()
        root.update_idletasks()
        text.place(x=x, y=10 + label_nameDir.winfo_height())

        # ПОЛЕ ВЫБОРА ИНТЕРВАЛА РЕЗЕРВОРОВАНИЯ
        label_calendar = graphic.Label(root, text="Авто-резервирование every:", width=30)
        label_calendar.pack(side=graphic.LEFT)
        label_calendar.config(foreground="#01579B", background='#B3E5FC', font='Courier 13')
        root.update_idletasks()
        label_calendar.place(x=x, y=10 + text.winfo_height() + 15 + label_nameDir.winfo_height())

        # всплывающе варианты интервала
        calendarBox = ttk.Combobox(root, values=self.calendar_options, width=47)
        calendarBox.pack()
        root.update_idletasks()
        calendarBox.place(x=15,
                          y=10 + text.winfo_height() + 15 + label_nameDir.winfo_height() + label_calendar.winfo_height())
        calendarBox.bind("<<ComboboxSelected>>", selected_calendar)


        # БЛОК С ВЫБОРОМ ПУТИ ПАПКИ, В КОТОРУЮ РЕЗЕРВИРУЕМ -----------------------------------------------------------------------

        button2 = graphic.Button(root, text="Путь резервирования", command=self.open_dirPlace_toReserve)
        button2.pack()
        button2.place(x=x, y=y)

        self.label = graphic.Label(root, text='Место для резервирования')
        self.label.pack(side=graphic.LEFT)
        root.update_idletasks()
        self.label.place(x=x + button2.winfo_width() + 1, y=y)
        self.label.config(foreground="#4CAF50", background='#E8F5E9', font='Courier 13')


        # БЛОК С ВЫБОРОМ ПУТИ РЕЗЕРВИРУЕМОГО ФАЙЛА -------------------------------------------------------------------------------

        button = graphic.Button(root, text="Путь исходных данных", command=self.open_dir_which_reserve)
        button.pack(side=graphic.RIGHT)
        button.place(x=x, y=50 + y)

        self.label2 = graphic.Label(root, text='Файлы, которые резервируем')
        self.label2.pack(side=graphic.LEFT)
        self.label2.config(foreground="#4CAF50", background='#E8F5E9', font='Courier 13')
        root.update_idletasks()
        self.label2.place(x=x + button.winfo_width() + 1, y=50 + y)


        # БЛОК МЕНЮ РЕЗЕРВОВ -----------------------------------------------------------------------------------------------------------

        try:
            self.options[0] == ''
            self.options_var = graphic.StringVar(value='Резервы есть')

        except:
            self.options_var = graphic.StringVar(value='Нет текущих резервов')


        # НАДПИСЬ НАД МЕНЮ
        labeldata = graphic.Label(root, textvariable=self.options_var, width=30)
        labeldata.pack(side=graphic.LEFT)
        labeldata.config(foreground="#01579B", background='#B3E5FC', font='Courier 13')
        labeldata.place(x=15, y=y + 125)


        # МЕНЮ С ВАРИАНТАМИ ПРЕДЫДУЩИХ РЕЗЕРВОВ
        menu = ttk.Combobox(root, text='opkpw', values=self.options, width=47)
        menu.pack()
        root.update_idletasks()
        menu.place(x=15, y=y + 125 + labeldata.winfo_height())
        menu.bind("<<ComboboxSelected>>", selected_option)

        label_ERR = graphic.Label(root)


        #КНОПКА ЗАВЕРШЕНИЯ ВВОДА И ФИКСАЦИИ ДАННЫХ

        button_DONE = graphic.Button(root, text='Выбрать', activeforeground='green',
                                     command=accept)
        button_DONE.pack(side=graphic.LEFT)
        root.update_idletasks()
        button_DONE.place(x=15, y=400)

        root.mainloop()
