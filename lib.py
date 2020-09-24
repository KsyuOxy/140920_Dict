from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox

"""
    Создайте программу «Фирма». Нужно хранить информацию о человеĸе в
    виде ĸарточĸи:
    - ФИО,
    - телефон,
    - рабочий email,
    - название должности,
    - номер ĸабинета,
    - skype.
    Требуется реализовать возможность добавления, удаления, поисĸа,
    замены данных. Используйте словарь для хранения информации.
"""
# -> список сотрудников компании
company_autotrans = {
    'company_employees': {
        1: {'фамилия': 'Иванов', 'имя': 'Иван', 'отчество': 'Иванович', 'телефон': {'рабочий': '0671234567', 'личный':
            '0966542387'}, 'email': 'ivan@gmail.com', 'должность': 'директор', 'кабинет': '10', 'skype': 'ivan.skype'},
        2: {'фамилия': 'Петров', 'имя': 'Пётр', 'отчество': 'Петрович', 'телефон': {'рабочий': '0679421546', 'личный':
            '0666531387'}, 'email': 'petr@gmail.com', 'должность': 'бухгалтер', 'кабинет': '11', 'skype': 'petr.skype'},
        3: {'фамилия': 'Цветок', 'имя': 'Алиса', 'отчество': 'Олеговна', 'телефон': {'рабочий': '0689542163', 'личный':
            '0958882387'}, 'email': 'alisa@gmail.com', 'должность': 'менеджер', 'кабинет': '12', 'skype': 'alis.skype'},
        4: {'фамилия': 'Логик', 'имя': 'Игорь', 'отчество': 'Васильевич', 'телефон': {'рабочий': '0986542589', 'личный':
            '0631141487'}, 'email': 'igor@gmail.com', 'должность': 'логист', 'кабинет': '13', 'skype': 'igor.skype'},
        5: {'фамилия': 'Иванова', 'имя': 'Лора', 'отчество': 'Львовна', 'телефон': {'рабочий': '0975497878', 'личный':
            '0975464943'}, 'email': 'lora@gmail.com', 'должность': 'менеджер', 'кабинет': '14', 'skype': 'lora.skype'},
        6: {'фамилия': 'Рулиев', 'имя': 'Лев', 'отчество': 'Фёдорович', 'телефон': {'рабочий': '0976847456', 'личный':
            '0965554933'}, 'email': 'ruliev@gmail.com', 'должность': 'водитель', 'кабинет': '-', 'skype': 'ruli.skype'},
        7: {'фамилия': 'Водиев', 'имя': 'Яков', 'отчество': 'Вадимович', 'телефон': {'рабочий': '0976112256', 'личный':
            '0505754964'}, 'email': 'vodya@gmail.com', 'должность': 'водитель', 'кабинет': '-', 'skype': 'vodya.skype'}
    },
    'company_car_fleet': {
        1: {'марка': 'MAN', 'номер': 'AA4521АН', 'грузоподъёмность': 18, 'рефрижератор': '-', 'состояние': '-'},
        2: {'марка': 'MAN', 'номер': 'AВ5412УК', 'грузоподъёмность': 12, 'рефрижератор': '+', 'состояние': '+'},
        3: {'марка': 'Volvo', 'номер': 'ВМ5412ОМ', 'грузоподъёмность': 16, 'рефрижератор': '+', 'состояние': '-'}
    },
}

# -> создание корневого окна и его параметры
root = Tk()
root.geometry('335x420+300+150')
root.title('AutoTrans')
root.config(bg='LightSteelBlue')

# -> виджеты корневого окна
button_add_employee = Button(root)  # -> кнопка "Добавить сотрудника"
button_find_by_phone = Button(root)  # -> кнопка "Найти" (по номеру телефона)
button_find_by_last_name = Button(root)  # -> кнопка "Найти" (по фамилии)
button_free_cars = Button(root)  # -> кнопка "Свободные авто"
button_list_of_employees = Button(root)  # -> кнопка "Список сотрудников"

phone_number_root_entry = Entry(root)  # -> поля для ввода номера телефона
last_name_root_entry = Entry(root)  # -> поля для ввода фамилии

Separator(root, orient='horizontal').place(x=0, y=70, relwidth=20)
Separator(root, orient='horizontal').place(x=0, y=225, relwidth=20)
Separator(root, orient='horizontal').place(x=0, y=335, relwidth=20)

Label(root, text='* для управления данными сотрудника\n  сначала выполните поиск', font='Arial 8', bg='LightSteelBlue',
      width=40, justify=RIGHT, fg='white').place(x=80, y=15)
Label(root, text='Поиск сотрудника', width=15, font='Arial 15', bg='LightSteelBlue', fg='white').place(x=40, y=55)
Label(root, text='(по номеру телефона)', font='Arial 8', bg='LightSteelBlue', width=26).place(x=40, y=132)
Label(root, text='(по фамилии)', font='Arial 8', bg='LightSteelBlue', width=26).place(x=40, y=192)


# -> параметры виджетов корневого окна
def root_widget_config():
    button_find_by_phone.config(text='Найти', width=10, font='Arial 9', height=1)
    button_find_by_phone.place(x=220, y=105)

    button_find_by_last_name.config(text='Найти', width=10, font='Arial 9', height=1)
    button_find_by_last_name.place(x=220, y=165)

    phone_number_root_entry.config(width=23, bd=3, relief=RIDGE, font='Arial 10')
    phone_number_root_entry.place(x=40, y=105, height=27)

    last_name_root_entry.config(width=23, bd=3, relief=RIDGE, font='Arial 10')
    last_name_root_entry.place(x=40, y=165, height=27)

    button_free_cars.config(text='Свободные авто', width=20, font='Arial 10')
    button_free_cars.place(x=40, y=360)

    button_add_employee.config(text='Добавить сотрудника', width=20, font='Arial 10')
    button_add_employee.place(x=40, y=250)

    button_list_of_employees.config(text='Список сотрудников', width=20, font='Arial 10')
    button_list_of_employees.place(x=40, y=285)


# -> создаёт окно для добавления сотрудника и добавляет его в словарь
def add_employee():
    card_add = Toplevel()  # -> окно карточки
    card_add.geometry('500x600+500+150')
    card_add.title('Карточка сотрудника')
    card_add.config(bg='LightSteelBlue')

    card_number_label = Label(card_add)  # -> поле номера карточки
    last_name_entry = Entry(card_add)  # -> поле для ввода фамилии
    first_name_entry = Entry(card_add)  # -> поле для ввода имени
    patronymic_entry = Entry(card_add)  # -> поле для ввода отчества
    position_entry = Entry(card_add)  # -> поле для ввода должности
    room_number_entry = Entry(card_add)  # -> поле для ввода номера кабинета
    work_phone_number_entry = Entry(card_add)  # -> поле для ввода рабочего номера телефона
    personal_phone_number_entry = Entry(card_add)  # -> поле для ввода личного номера телефона
    work_email_entry = Entry(card_add)  # -> поле для ввода рабочего email
    skype_entry = Entry(card_add)  # -> поле для ввода skype
    button_save = Button(card_add)  # -> кнопка "Добавить"

    # -> создаёт текстовые Labels и задаёт параметры виджетам
    def widget_and_config():

        Label(card_add, text='Карточка №', bg='LightSteelBlue', font='Arial 15').place(x=180, y=20)

        card_number_label.config(text='000', font='Arial 15', bg='LightSteelBlue')
        card_number_label.place(x=300, y=20)

        Label(card_add, text='Фамилия:', bg='LightSteelBlue', font='Arial 11').place(x=180, y=70)

        last_name_entry.config(bd=3, relief=RIDGE, width=30)
        last_name_entry.place(x=280, y=70)

        Label(card_add, text='Имя:', bg='LightSteelBlue', font='Arial 11').place(x=182, y=100)

        first_name_entry.config(bd=3, relief=RIDGE, width=30)
        first_name_entry.place(x=280, y=100)

        Label(card_add, text='Отчество:', bg='LightSteelBlue', font='Arial 11').place(x=182, y=130)

        patronymic_entry.config(bd=3, relief=RIDGE, width=30)
        patronymic_entry.place(x=280, y=130)

        Label(card_add, text='Должность:', bg='LightSteelBlue', font='Arial 11').place(x=30, y=200)

        position_entry.config(bd=3, relief=RIDGE, width=25)
        position_entry.place(x=120, y=200)

        Label(card_add, text='№ каб.:', bg='LightSteelBlue', font='Arial 11').place(x=325, y=200)

        room_number_entry.config(bd=3, relief=RIDGE, width=12)
        room_number_entry.place(x=385, y=200)

        Label(card_add, text='№ телефона:', bg='LightSteelBlue', font='Arial 11').place(x=30, y=250)

        Label(card_add, text='рабочий', bg='LightSteelBlue', font='Arial 10').place(x=220, y=250)

        work_phone_number_entry.config(bd=3, relief=RIDGE, width=30)
        work_phone_number_entry.place(x=278, y=250)

        Label(card_add, text='личный', bg='LightSteelBlue', font='Arial 10').place(x=220, y=280)

        personal_phone_number_entry.config(bd=3, relief=RIDGE, width=30)
        personal_phone_number_entry.place(x=278, y=280)

        Label(card_add, text='Email (рабочий):', bg='LightSteelBlue', font='Arial 11').place(x=30, y=320)

        work_email_entry.config(bd=3, relief=RIDGE, width=50)
        work_email_entry.place(x=158, y=320)

        Label(card_add, text='Skype (рабочий):', bg='LightSteelBlue', font='Arial 11').place(x=30, y=350)

        skype_entry.config(bd=3, relief=RIDGE, width=50)
        skype_entry.place(x=158, y=350)

        button_save.config(text='Добавить', font='Arial 10', bg='LightSteelBlue', fg='black', width=9)
        button_save.place(x=380, y=390)

    widget_and_config()

    # -> добавляет данные нового сотрудника в словарь
    def save_new_card():
        key_max = 0  # -> будет хранить максимальное значение ключа

        for key in company_autotrans['company_employees']:  # -> поиск максимального значения ключа
            if key_max > key:
                continue
            else:
                key_max = key
        new_key = key_max + 1  # -> новый ключ для добавления

        # -> новое значение для нового ключа
        new_card = {'фамилия': last_name_entry.get(), 'имя': first_name_entry.get(), 'отчество': patronymic_entry.get(),
                    'телефон': {'рабочий': work_phone_number_entry.get(), 'личный': personal_phone_number_entry.get()},
                    'email': work_email_entry.get(), 'должность': position_entry.get(),
                    'кабинет': room_number_entry.get(), 'skype': skype_entry.get()}

        company_autotrans['company_employees'][new_key] = new_card  # -> добавляет новую пару в словарь
        print(company_autotrans)

    button_save.config(command=save_new_card)  # -> привязка функции к кнопке


# -> поиск сотрудника по номеру телефона или фамилии, изменяет, сохраняет изменения и удаляет данные сотрудников
def find_change_delete_employee():
    card_add = Toplevel()  # -> окно карточки
    card_add.geometry('500x600+500+150')
    card_add.title('Карточка сотрудника')
    card_add.config(bg='LightSteelBlue')

    card_number_label = Label(card_add)  # -> поле номера карточки
    last_name_entry = Entry(card_add)  # -> поле для ввода фамилии
    first_name_entry = Entry(card_add)  # -> поле для ввода имени
    patronymic_entry = Entry(card_add)  # -> поле для ввода отчества
    position_entry = Entry(card_add)  # -> поле для ввода должности
    room_number_entry = Entry(card_add)  # -> поле для ввода номера кабинета
    work_phone_number_entry = Entry(card_add)  # -> поле для ввода рабочего номера телефона
    personal_phone_number_entry = Entry(card_add)  # -> поле для ввода личного номера телефона
    work_email_entry = Entry(card_add)  # -> поле для ввода рабочего email
    skype_entry = Entry(card_add)  # -> поле для ввода skype
    button_save = Button(card_add)  # -> кнопка "Сохранить"
    button_change = Button(card_add)  # -> кнопка "Изменить"
    button_delete_employee = Button(card_add)  # -> кнопка "Удалить сотрудника"

    found_employee = {}  # -> будет хранить результат поиска
    state_w = DISABLED  # -> хранит состояние виджета

    # -> находит данные сотрудника по номеру телефона
    def find_by_phone_number():
        number_get = phone_number_root_entry.get().strip()  # -> получает данные из entry (телефон)

        for key in company_autotrans['company_employees']:
            if company_autotrans['company_employees'][key]['телефон']['рабочий'] == number_get or \
                    company_autotrans['company_employees'][key]['телефон']['личный'] == number_get:
                found_employee_by_phone = {key: company_autotrans['company_employees'][key]}
                return found_employee_by_phone

    # -> находит данные сотрудника по фамилии
    def find_by_last_name():

        last_name_get = last_name_root_entry.get().strip()  # -> получает данные из entry (фамилию)

        for key in company_autotrans['company_employees']:  # -> ищет соответствие фамилии среди данных сотрудников
            if company_autotrans['company_employees'][key]['фамилия'] == last_name_get:
                found_employee_by_last_name = {key: company_autotrans['company_employees'][key]}

                return found_employee_by_last_name  # -> данные сотрудника с соотв. фамилией

    by_phone = find_by_phone_number()
    by_last_name = find_by_last_name()

    # -> определяет данные сотрудника в зависимости от выбранного поиска
    if by_phone:
        found_employee = by_phone
    elif by_last_name:
        found_employee = by_last_name

    # -> присваивает виджетам найденные значения, задаёт параметры виджетам, создаёт текстовые Labels
    def widget_and_config():

        try:  # -> выполняет проверку ввода значений для поиска

            Label(card_add, text='Карточка №', bg='LightSteelBlue', font='Arial 15').place(x=180, y=20)

            card_number_label.config(text=list(found_employee.keys())[0], font='Arial 15', bg='LightSteelBlue')
            card_number_label.place(x=300, y=20)

            Label(card_add, text='Фамилия:', bg='LightSteelBlue', font='Arial 11').place(x=180, y=70)

            last_name_entry.place(x=280, y=70)
            last_name_entry.insert(0, found_employee[list(found_employee.keys())[0]]['фамилия'])
            last_name_entry.config(bd=3, relief=RIDGE, width=30, state=state_w)

            Label(card_add, text='Имя:', bg='LightSteelBlue', font='Arial 11').place(x=182, y=100)

            first_name_entry.place(x=280, y=100)
            first_name_entry.insert(0, found_employee[list(found_employee.keys())[0]]['имя'])
            first_name_entry.config(bd=3, relief=RIDGE, width=30, state=state_w)

            Label(card_add, text='Отчество:', bg='LightSteelBlue', font='Arial 11').place(x=182, y=130)

            patronymic_entry.place(x=280, y=130)
            patronymic_entry.insert(0, found_employee[list(found_employee.keys())[0]]['отчество'])
            patronymic_entry.config(bd=3, relief=RIDGE, width=30, state=state_w)

            Label(card_add, text='Должность:', bg='LightSteelBlue', font='Arial 11').place(x=30, y=200)

            position_entry.place(x=120, y=200)
            position_entry.insert(0, found_employee[list(found_employee.keys())[0]]['должность'])
            position_entry.config(bd=3, relief=RIDGE, width=25, state=state_w)

            Label(card_add, text='№ каб.:', bg='LightSteelBlue', font='Arial 11').place(x=325, y=200)

            room_number_entry.place(x=385, y=200)
            room_number_entry.insert(0, found_employee[list(found_employee.keys())[0]]['кабинет'])
            room_number_entry.config(bd=3, relief=RIDGE, width=12, state=state_w)

            Label(card_add, text='№ телефона:', bg='LightSteelBlue', font='Arial 11').place(x=30, y=250)

            Label(card_add, text='рабочий', bg='LightSteelBlue', font='Arial 10').place(x=220, y=250)

            work_phone_number_entry.place(x=278, y=250)
            work_phone_number_entry.insert(0, found_employee[list(found_employee.keys())[0]]['телефон']['рабочий'])
            work_phone_number_entry.config(bd=3, relief=RIDGE, width=30, state=state_w)

            Label(card_add, text='личный', bg='LightSteelBlue', font='Arial 10').place(x=220, y=280)

            personal_phone_number_entry.place(x=278, y=280)
            personal_phone_number_entry.insert(0, found_employee[list(found_employee.keys())[0]]['телефон']['личный'])
            personal_phone_number_entry.config(bd=3, relief=RIDGE, width=30, state=state_w)

            Label(card_add, text='Email (рабочий):', bg='LightSteelBlue', font='Arial 11').place(x=30, y=320)

            work_email_entry.place(x=158, y=320)
            work_email_entry.insert(0, found_employee[list(found_employee.keys())[0]]['email'])
            work_email_entry.config(bd=3, relief=RIDGE, width=50, state=state_w)

            Label(card_add, text='Skype (рабочий):', bg='LightSteelBlue', font='Arial 11').place(x=30, y=350)

            skype_entry.place(x=158, y=350)
            skype_entry.insert(0, found_employee[list(found_employee.keys())[0]]['skype'])
            skype_entry.config(bd=3, relief=RIDGE, width=50, state=state_w)

            button_save.config(text='Сохранить', font='Arial 10', bg='LightSteelBlue', fg='black', width=9)
            button_save.place(x=384, y=390)

            button_change.config(text='Изменить', font='Arial 10', bg='LightSteelBlue', fg='black', width=9)
            button_change.place(x=290, y=390)

            button_delete_employee.config(text='Удалить данные', font='Arial 10', bg='LightSteelBlue', width=14)
            button_delete_employee.place(x=157, y=390)

        except IndexError:
            messagebox.showerror('Ошибка', 'Нет сотрудника с такими данными.')

    widget_and_config()

    # -> изменяет значение переменной, хранящее состояние виджета
    def change_state():
        nonlocal state_w
        if state_w == DISABLED:
            state_w = NORMAL
        else:
            state_w = DISABLED
        return state_w

    # -> вносит изменения в данные сотрудника
    def save_change():
        nonlocal found_employee

        # -> сохраняет в себе новые изменённые данные
        new_values = {'фамилия': last_name_entry.get().strip(), 'имя': first_name_entry.get().strip(),
                      'отчество': patronymic_entry.get().strip(),
                      'телефон': {'рабочий': work_phone_number_entry.get().strip(),
                                  'личный': personal_phone_number_entry.get().strip()},
                      'email': work_email_entry.get().strip(), 'должность': position_entry.get().strip(),
                      'кабинет': room_number_entry.get().strip(), 'skype': skype_entry.get().strip()}

        company_autotrans['company_employees'][list(found_employee.keys())[0]].update(new_values)  # -> обновляет словар
        print(company_autotrans)

        change_state()  # -> изменяет значение переменной состояния entry

        # -> Изменение состояния entries
        last_name_entry.config(state=state_w)
        first_name_entry.config(state=state_w)
        patronymic_entry.config(state=state_w)
        position_entry.config(state=state_w)
        room_number_entry.config(state=state_w)
        work_phone_number_entry.config(state=state_w)
        personal_phone_number_entry.config(state=state_w)
        work_email_entry.config(state=state_w)
        skype_entry.config(state=state_w)

    # -> удаляет текущие данные из словаря
    def delete_employee():
        try:
            nonlocal found_employee
            company_autotrans['company_employees'].pop(list(found_employee.keys())[0])  # -> удаляет данные сотрудника
            button_change.config(state=DISABLED)  # -> изменяет состояние кнопки
            button_save.config(state=DISABLED)  # -> изменяет состояние кнопки
            print(company_autotrans)
        except KeyError:
            messagebox.showwarning('Внимание!', 'Эти данные уже удалены.')

    button_delete_employee.config(command=delete_employee)  # -> привязка функции к кнопке
    button_change.config(command=lambda: (change_state(), widget_and_config()))  # -> привязка двух функций к кнопке
    button_save.config(command=save_change)  # -> привязка функции к кнопке


# -> выводит окно со списком сотрудников(ФИО, раб.тел., должность)
def list_of_employees():
    win_of_employees = Toplevel()  # -> создание окна
    win_of_employees.geometry('550x200+200+300')
    win_of_employees.title('Список сотрудников AutoTrans')

    text = Text(win_of_employees, width=65, height=11)  # -> создание текстового поля
    text.pack(side=LEFT)
    scroll = Scrollbar(win_of_employees, command=text.yview)  # -> создание скроллера
    scroll.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scroll.set)  # -> устанавливает скролер в текстовое поле

    employees = ''  # -> строка, которая будет хранить данные сотрудников, нужные для вывода в текстовое поле

    for key in company_autotrans['company_employees']:  # -> итерируется по ключам в словаре сотрудников
        employees += f'{key}. '  # -> добавляет номер, под которым хранятся данные сотрудника
        for value in company_autotrans['company_employees'][key]:  # -> перебирает знач. ключа, добавляя нужное в строку
            if value == 'фамилия' or value == 'имя' or value == 'отчество':
                employees += f'{company_autotrans["company_employees"][key].setdefault(value)} '
            elif value == 'телефон':
                employees += f', раб. тел.: {company_autotrans["company_employees"][key][value].setdefault("рабочий")}'
            elif value == 'должность':
                employees += f'  ({company_autotrans["company_employees"][key].setdefault(value)})'

        employees += '\n'  # -> вставляет перенос на новую строку в конце отобранных данных каждого сотрудника

    text.insert(1.0, 'Список сотрудников AutoTrans\n\n' + employees)  # -> втавляет текст в текстовое поле
    text.tag_add('title', 1.0, '1.end')  # -> указывает часть текста к которой будут применяться свойства
    text.tag_config('title', font=("Arial", 15, 'bold'), justify=CENTER)  # -> свойства для указанной части текста


# -> выводид окно со списком свободных авто или предупреждение, что их нет
def free_cars():
    win_of_free_cars = Toplevel()  # -> создание окна
    win_of_free_cars.geometry('550x200+200+300')
    win_of_free_cars.title('Список сотрудников AutoTrans')

    text = Text(win_of_free_cars, width=60, height=11)  # -> создание текстового поля
    text.pack(side=LEFT)
    scroll = Scrollbar(win_of_free_cars, command=text.yview)  # -> создание скроллера
    scroll.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scroll.set)  # -> устанавливает скролер в текстовое поле

    free_cars_str = ''  # -> строка, которая будет хранить данные свободных авто для вывода в текстовое поле

    for key in company_autotrans['company_car_fleet']:  # -> итерируется по ключам в словаре авто

        if company_autotrans['company_car_fleet'][key]['состояние'] == '-':  # -> проверяет состояние
            # -> добавляет в строку данные свободных авто
            free_cars_str += f' {company_autotrans["company_car_fleet"][key]["марка"]}, ' \
                             f'{company_autotrans["company_car_fleet"][key]["номер"]} ' \
                             f'{company_autotrans["company_car_fleet"][key]["грузоподъёмность"]} т, '

            if company_autotrans["company_car_fleet"][key]["рефрижератор"] == "+":
                free_cars_str += 'с рефрижератором\n'
            else:
                free_cars_str += 'без рефрижератора\n'

    text.insert(1.0, 'Список свободных авто\n\n' + free_cars_str)  # -> втавляет текст в текстовое поле

    if not free_cars_str:
        messagebox.showwarning('Внимание!', 'Свободных авто нет.')  # -> вызывает сообщ. в случае отсутствия свобод.авто

    text.tag_add('title', 1.0, '1.end')  # -> указывает часть текста к которой будут применяться свойства
    text.tag_config('title', font=("Arial", 15, 'bold'), justify=CENTER)  # -> свойства для указанной части текста


button_add_employee.config(command=add_employee)  # -> привязка функции к кнопке
button_find_by_phone.config(command=find_change_delete_employee)  # -> привязка функции к кнопке
button_find_by_last_name.config(command=find_change_delete_employee)  # -> привязка функции к кнопке
button_list_of_employees.config(command=list_of_employees)  # -> привязка функции к кнопке
button_free_cars.config(command=free_cars)  # -> привязка функции к кнопке
