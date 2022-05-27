import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import requests
from core.default_values import BACKGROUND_PATH
from core.default_values import BACKEND_URL

def upload_new():
    def back2main():
        window_upload_new.destroy()

    def select_file(filetype, entry_photo):
        def upload_archive():
            print(filetype)
            if filetype==1:
                with open(entry_photo.get(), "rb") as f:
                    chunk = f.read(15 * 1024 * 1024)  # 50 MB
                    print(entry_photo.get())
                    extension=entry_photo.get().split('.')[1]

                    res = requests.post(
                        f"{BACKEND_URL}/user",
                        params={"fio":entry_fio.get(),"extention":  extension,"info":entry_role.get()},
                        files={"file_data": chunk},
                    )
                    print(res.status_code)


        if filetype == 1:
            filetypes = [
                ("all files", ".*"),
                ("text files", ".txt"),
                ("image files", ".png"),
                ("image files", ".jpeg"),
                ("image files", ".jpg"),
            ]
        if filetype == 2:

            filetypes = [("zips", ".zip")]

        filename = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )

        entry_photo.insert(0, filename)
        btn_upload = tk.Button(
            window_upload_new, text="Загрузить файл",width=15, height=3, command=upload_archive
        )
        btn_upload.place(x=600, y=150)

        showinfo(title="Selected File", message=filename)

    def package():
        entry_photo = tk.Entry(window_upload_new, width=30)
        open_button = ttk.Button(
            window_upload_new,
            text="Открыть файл",
            command=lambda: select_file(2, entry_photo),
        )
        entry_photo.place(x=150, y=350)
        open_button.place(x=450, y=350)


    def oneandonly():

        fio_label = tk.Label(window_upload_new, text="ФИО")
        role_label = tk.Label(window_upload_new, text="Должность")

        entry_photo = tk.Entry(window_upload_new, width=30)
        open_button = ttk.Button(
            window_upload_new,
            text="Открыть файл",
            command=lambda: select_file(1, entry_photo),
        )
        fio_label.place(x=150, y=150)
        role_label.place(x=150, y=200)
        entry_photo.place(x=250, y=250)
        open_button.place(x=550, y=250)
        entry_fio.place(x=250, y=150)
        entry_role.place(x=250, y=200)

    window_upload_new = tk.Toplevel()
    window_upload_new.title("Добавление новых пользователей")
    window_upload_new.resizable(False, False)
    window_upload_new.geometry("800x300")
    img = tk.PhotoImage(file=BACKGROUND_PATH)
    limg = tk.Label(window_upload_new, image=img)
    entry_fio = tk.Entry(window_upload_new, width=30)
    entry_role = tk.Entry(window_upload_new, width=30)
    limg.place(x=0, y=0)
    btn_back = tk.Button(window_upload_new, text="Назад", command=back2main)
    btn_package = tk.Button(
        window_upload_new, text="Пакетная загрузка", width=15, height=3, command=package
    )
    btn_one = tk.Button(
        window_upload_new, text="По одному", width=15, height=3, command=oneandonly
    )
    btn_package.place(x=400, y=80)
    btn_one.place(x=150, y=80)
    btn_back.place(x=0, y=0)
    window_upload_new.mainloop()
