import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de texto')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        self.archivo = None
        self.archivo_abierto = False

        self._componentes()
        self._menu()

    def _componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED,
                                 bd=2)
        boton_abrir = tk.Button(frame_botones,text='Abrir',
                                command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones,text='Guardar',
                                  command=self._guardar)
        boton_guardar_como = tk.Button(frame_botones,text='Guardar como...',
                                       command=self._guardar_como)

        boton_abrir.grid(row=0, column=0,
                         sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0,
                         sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0,
                         sticky='we', padx=5, pady=5)

        frame_botones.grid(row=0, column=0, sticky='ns')
        self.campo_texto.grid(row=0, column=1, sticky='nswe')

    def _menu(self):
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)

        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)

        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar como...', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)

    def _abrir_archivo(self):
        self.archivo_abierto = askopenfile(mode='r+')
        self.campo_texto.delete(1.0, tk.END)

        if not self.archivo_abierto:
            return

        with open(self.archivo_abierto.name, 'r+') as self.archivo:
            texto = self.archivo.read()
            self.campo_texto.insert(1.0, texto)
            self.title(f'*Editor Texto - {self.archivo.name}')

    def _guardar(self):
        if self.archivo_abierto:
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                texto = self.campo_texto.get(1.0, tk.END)
                self.archivo.write(texto)
                self.title(f'Editor Texto - {self.archivo.name}')
        else:
            self._guardar_como()

    def _guardar_como(self):
        self.archivo = asksaveasfile(
            defaultextension='txt',
            filetypes=[('Archivos de Texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if not self.archivo:
            return

        with open(self.archivo.name, 'w') as archivo:
            texto = self.campo_texto.get(1.0, tk.END)

            archivo.write(texto)
            self.title(f'Editor Texto - {self.archivo.name}')

            self.archivo_abierto = archivo


if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()