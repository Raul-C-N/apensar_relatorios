# #
# caminho_usuario = os.path.expanduser("~")  # Retorna a pasta do usuário
# caminho_pasta = os.path.join(caminho_usuario,"Downloads","Repositorios_GIT","apensar_relatorios","dados")  # Cria caminho relativo
# caminho_ipsum = os.path.join(caminho_usuario,"Downloads","Repositorios_GIT","apensar_relatorios","dados", "ipsum_lorem.txt")  # Cria caminho relativo
# print(caminho_pasta)
# # ADICIONAR EM DADOS DEPOIS
# Seccionais = []
# chave_quebrar_texto = ")(*"
# Texto_Seccional=""
import os
from funcoes import *


#caminhos da pasta
# caminho_pasta = os.path.expanduser("~")+"\\Downloads\\Repositorios_GIT\\apensar_relatorios"
# caminho_ipsum = os.path.join(caminho_pasta, "dados", "ipsum_lorem.txt")

def main():
    print("Executando pacote como script...")
    devolver_texto_com_contagem(Quebrar_texto_em_lista(Importar_docx_apenas_nome("7.docx"),"**¨¨"))
    # print("Resultado da soma:", Importar_txt(caminho_pasta))

if __name__ == "__main__":
    main()
