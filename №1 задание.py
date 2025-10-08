from pathlib import Path
import os
from tkinter import *

root = Tk()
history = ""

# Функция отображающая изменения в консоли
def logcmd():
    global history
    text2 = []
    text = enter.get()

    # раскрываем переменные окружения
    text = os.path.expandvars(text)

    if 'cd' in text:  # Показывает путь где мы
        t=text+' '
        t=t[3:-1]
        text=f"команда 'cd' аргумент '{t}'"

    elif text == "$home":  # имя устройства
        text = Path.home()


    elif 'ls' in text:# выводит какие файлы в папке
        t=text+' '
        t=t[3:-1]
        text=f"команда 'ls' аргумент '{t}'"

    elif text=='exit': #выход из cmd
         root.destroy()

    elif text=='':
        text='\n'
         
    else:
        text='такой команды нет' #ошибка в команде
        
    if history == "":
        history = str(text)
    
    else:
        history += "\n" + str(text) #Выводит текс

    cmd_label.config(text=history)
    canvas.update_idletasks()
    canvas.yview_moveto(1)  # автоматически скроллим вниз
    enter.delete(0, END)

# Параметры окна
root.geometry('600x400')
root.title('VFS')
root.config(bg='#808080')
root.resizable(False, False)

# Canvas + Scrollbar для Label
frame = Frame(root, bg='#A5A5A5')
frame.place(x=10, y=10, width=580, height=330)

canvas = Canvas(frame, bg='#A5A5A5')
scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

# прокручиваться
cmd_label = Label(canvas, bg='#A5A5A5', font='Consolas', justify='left', anchor='nw')
canvas.create_window((0, 0), window=cmd_label, anchor='nw')

# Обновление scrollregion при изменении размера Label
def update_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

cmd_label.bind("<Configure>", update_scroll)

# Кнопка
btn = Button(root,
             text='↵',
             command=logcmd,
             font='Consolas',
             bg='#A5A5A5',
             activebackground='#293133'
             )
btn.place(x=565, y=350)

# Ввод
enter = Entry(root, width=90)
enter.place(x=10, y=360)

root.mainloop()
