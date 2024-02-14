import tkinter as tk
from ply import lex


tokens = ('RESERVADO', 'IDENTIFICADOR', 'DELIMITADOR', 'OPERADOR', 'NUMERO', 'NO_DEFINIDO')

t_RESERVADO = r'static|void|int|public|base|altura'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DELIMITADOR = r'\(|\)|\{|\}|\;'
t_OPERADOR = r'[+\-*/=<>]'
t_NUMERO = r'\d+(\.\d+)?'
t_NO_DEFINIDO = r'[^()=\s]+'
t_ignore='\t'

lexer = lex.lex()

def analizar(entrada):
    tokens = []
    lexer.input(entrada)

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append((tok.type, tok.value))

    return tokens

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    lineas_codigo = codigo.split("\n")

    resultado_frame.config(state=tk.NORMAL)
    resultado_frame.delete("1.0", tk.END)
 
    resultado_frame.insert(tk.END, f"{'Token':^30} {'Lexema':^30} {'Linea':^30}\n")
    resultado_frame.insert(tk.END, '-'*85 + '\n')

    for numero_linea, linea in enumerate(lineas_codigo, start=1):
        tokens_linea = analizar(linea)
        for token, lexema in tokens_linea:
            resultado_frame.insert(tk.END, f"{token:^26} {lexema:^26} {numero_linea:^35}\n")

    resultado_frame.config(state=tk.DISABLED)

def borrar_contenido():
    entrada_texto.delete("1.0", tk.END)
    resultado_frame.config(state=tk.NORMAL)
    resultado_frame.delete("1.0", tk.END)
    resultado_frame.config(state=tk.DISABLED)

ventana = tk.Tk()
ventana.geometry('1000x500')
ventana.title("Analizador")
ventana.config(bg='##33FF42 ')  

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="#F9EBEA", fg="black", height=15, width=50)
entrada_texto.grid(row=0, column=0, padx=25, pady=50)

boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_codigo)
boton_analizar.place(x=10, y=5, width=100, height=30)


boton_borrar = tk.Button(ventana, text=" Borrar ", command=borrar_contenido)
boton_borrar.place(x=900, y=5, width=100, height=30)

resultado_frame = tk.Text(ventana, font=("Arial", 12), bg="#FFFFFF", fg="black", height=15, width=50)
resultado_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
resultado_frame.config(state=tk.DISABLED)  # Configura la ventana como desactivada para que no se pueda editar

if _name_ == '_main_':
   ventana.mainloop()