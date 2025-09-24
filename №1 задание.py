import platform
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

    if text == 'cd':  # Показывает путь где мы
        text = os.getcwd()

    elif text == "os.chdir('..')":  # шаг назад
        os.chdir('..')
        text = os.getcwd()

    elif text == "$home":  # шаг назад
        text = platform.node()


    elif text == 'ls':  # выводит какие файлы в папке
        text = os.listdir()
        for i in range(len(text)):
            text2.append(text[i] + '\n')
        text = ''.join(text2)

    elif text=='exit':
         root.destroy()
         
    else:
        text='такой команды нет'
        
    if history == "":
        history = str(text)
    
    else:
        history += "\n" + str(text)

    cmd_label.config(text=history)
    canvas.update_idletasks()
    canvas.yview_moveto(1)  # автоматически скроллим вниз
    enter.delete(0, END)

# Параметры окна
root.geometry('600x400')
root.title('VFS')
root.iconbitmap('gd.ico')
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
