import os

def gerar_arquivo_massivo(nome_arquivo="dataset_gigante.txt", tamanho_alvo_gb=5):
    """Gera um arquivo massivo com feedback visual de progresso."""
    bytes_alvo = tamanho_alvo_gb * 1024 * 1024 * 1024
    
    linha_log = "INFO: [2026-03-05 08:00:00] Processo disparado. Memoria estavel. CPU nominal.\n"
    bloco = linha_log * 10000
    tamanho_bloco = len(bloco.encode('utf-8'))
    
    print(f"Iniciando geracao de {tamanho_alvo_gb}GB. Isso vai exigir do seu disco...")
    print("Mantenha o terminal aberto. Progresso de gravacao:")
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        bytes_escritos = 0
        gb_atual = 0
        while bytes_escritos < bytes_alvo:
            f.write(bloco)
            bytes_escritos += tamanho_bloco
            
            # Avisa no terminal a cada 1 Gigabyte gravado
            if bytes_escritos // (1024**3) > gb_atual:
                gb_atual = bytes_escritos // (1024**3)
                print(f" > {gb_atual} GB consolidados no disco...")
                
    print(f"\nOperacao concluida com sucesso! {nome_arquivo} finalizado.")

if __name__ == "__main__":
    gerar_arquivo_massivo()