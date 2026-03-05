import tkinter as tk
from tkinter import filedialog, messagebox
import sys

def processar_arquivo_eficiente(file_path):
    """Lê o arquivo em stream para evitar sobrecarga de RAM."""
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            yield chunk

def atualizar_file_view(args):
    """Atualiza o conteúdo do simulador com o arquivo selecionado."""
    file_path = args.get()
    if not file_path:
        messagebox.showwarning("Aviso", "Por favor, selecione um arquivo primeiro.")
        return

    # Correção aplicada: uso de notação de ponto em vez de dicionário
    window.text_area.delete('1.0', tk.END)
    window.text_area.insert(tk.END, f"[Lendo {file_path}...]\n\n", "filename")

    line_count = 1
    for chunk in processar_arquivo_eficiente(file_path):
        lines = chunk.splitlines()
        for line in lines:
            window.text_area.insert(tk.END, f"{line_count:>5}  {line}\n")
            line_count += 1
            window.update_idletasks()

def main():
    """Constrói a interface gráfica baseada no layout Skip Gradient."""
    global window
    window = tk.Tk()
    window.title('Simulação de Execução do Comando Cat')
    window.geometry('500x350')
    window.configure(bg='#F0F0F0')

    c_roxo = "#845EC2"
    c_cian = "#4FFBDF"
    c_v_agua = "#00C2A8"
    c_v_escuro = "#008B74"

    header = tk.Frame(window, bg=c_roxo)
    header.pack(fill=tk.X)
    title_lbl = tk.Label(header, text="Leitura de Arquivo em Tempo Real", bg=c_roxo, fg="white", font=("Arial", 14, "bold"), pady=10)
    title_lbl.pack()

    selection_frame = tk.Frame(window, pady=10)
    selection_frame.pack()
    
    file_label = tk.Label(selection_frame, text="Selecione o arquivo:")
    file_label.pack(side=tk.LEFT, padx=(0, 5))
    
    file_options = ['teste.txt']
    selected_file = tk.StringVar(window)
    selected_file.set(file_options[0])
    file_dropdown = tk.OptionMenu(selection_frame, selected_file, *file_options)
    file_dropdown.pack(side=tk.LEFT, padx=5)

    simulate_btn = tk.Button(selection_frame, text="Simular Leitura", bg="#FFFFFF", fg=c_v_escuro, relief="solid", borderwidth=1, font=("Arial", 10), command=lambda: atualizar_file_view(selected_file))
    simulate_btn.pack(side=tk.LEFT, padx=(5, 0))

    text_frame = tk.Frame(window, pady=10)
    text_frame.pack(fill=tk.BOTH, expand=True)
    
    text_area = tk.Text(text_frame, height=10, width=50, bg="white", font=("Monospace", 9), relief="solid", borderwidth=1)
    text_area.tag_config("filename", foreground=c_v_agua)
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
    
    scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    
    status_bar = tk.Frame(window, pady=5)
    status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    status_lbl = tk.Label(status_bar, text="✓ Estado: Concluído.", anchor=tk.W, pady=5, padx=10)
    status_lbl.pack(fill=tk.X)

    # Correção aplicada: definindo o atributo no objeto da janela
    window.text_area = text_area

    window.mainloop()

if __name__ == '__main__':
    main()