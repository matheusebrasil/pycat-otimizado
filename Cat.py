import sys
import argparse

def exibir_painel_ajuda():
    """Exibe o manual da ferramenta usando a paleta Skip Gradient."""
    c_roxo = "\033[38;2;132;94;194m"      
    c_ciano = "\033[38;2;79;251;223m"     
    c_v_agua = "\033[38;2;0;194;168m"     
    c_v_escuro = "\033[38;2;0;139;116m"   
    reset = "\033[0m"

    borda_superior = f"{c_roxo}╔══════════════════════════════════════════════════════╗{reset}"
    borda_inferior = f"{c_roxo}╚══════════════════════════════════════════════════════╝{reset}"
    
    print(borda_superior)
    print(f"{c_roxo}║{reset} {c_ciano}PyCat Otimizado - Leitor de Arquivos em Stream{reset}       {c_roxo}║{reset}")
    print(f"{c_roxo}║{reset}                                                      {c_roxo}║{reset}")
    print(f"{c_roxo}║{reset} {c_v_agua}Uso:{reset} python cat.py [arquivo] [flags]                {c_roxo}║{reset}")
    print(f"{c_roxo}║{reset} {c_v_escuro}Flags:{reset}                                              {c_roxo}║{reset}")
    print(f"{c_roxo}║{reset}   -n, --number    Enumera todas as linhas de saida   {c_roxo}║{reset}")
    print(f"{c_roxo}║{reset}   -h, --help      Mostra este painel de ajuda        {c_roxo}║{reset}")
    print(borda_inferior)
    sys.exit(0)

def process_file(file_obj, number_lines=False, start_line=1):
    """Lê e imprime o arquivo iterando linha a linha, protegendo a RAM."""
    line_count = start_line
    for line in file_obj:
        if number_lines:
            sys.stdout.write(f"{line_count:>6}  {line}")
            line_count += 1
        else:
            sys.stdout.write(line)
    return line_count

def main():
    # Intercepta a chamada de ajuda antes do argparse
    if '-h' in sys.argv or '--help' in sys.argv:
        exibir_painel_ajuda()

    # add_help=False impede que o argparse crie o menu chato padrão
    parser = argparse.ArgumentParser(description="Comando Cat otimizado.", add_help=False)
    parser.add_argument('files', nargs='*', help='Caminho dos arquivos para leitura')
    parser.add_argument('-n', '--number', action='store_true', help='Numerar as linhas')
    
    args = parser.parse_args()
    
    if not args.files:
        process_file(sys.stdin, args.number)
        sys.exit(0)

    current_line = 1
    for file_path in args.files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                current_line = process_file(f, args.number, current_line)
        except FileNotFoundError:
            sys.stderr.write(f"cat: {file_path}: Arquivo inexistente\n")
        except PermissionError:
            sys.stderr.write(f"cat: {file_path}: Permissao negada\n")
        except Exception as e:
            sys.stderr.write(f"cat: erro ao ler {file_path}: {e}\n")

if __name__ == '__main__':
    main()