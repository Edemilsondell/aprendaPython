""" import tkinter as tk
from tkinter import messagebox, Entry

# Função para exibir a caixa de diálogo
def show_dialog():
    # Cria uma caixa de diálogo de informação
    messagebox.showinfo("Primeiro Text.", "Hello!")

# Cria a janela principal
window = tk.Tk()
website_entry = Entry(width=100)
#website_entry = Entry(height=35)
window.title("Gerador de Código QR")
window.config(padx=10, pady=100)



# Cria um botão para exibir a caixa de diálogo
button = tk.Button(window, text="Exibir Caixa de Diálogo", command=show_dialog)
button.pack()

# Inicia o loop principal da janela


window.mainloop()
 """

import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button


def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n "
                    f"Endereço: {url} \n "
                    f"Pronto para salvar?")

        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save('qrExport.png')


if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Código QR")
    window.config(padx=10, pady=100)

    # Labels
    website_label = Label(text="URL:")
    website_label.grid(row=2, column=0)

    # Entries
    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()
    add_button = Button(text="Gerar QR Code", width=36, command=gera_qr_code)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()