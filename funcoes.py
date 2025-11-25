import os
caminho_usuario = os.path.expanduser("~")  # Retorna a pasta do usuário
caminho = os.path.join(caminho_usuario,"Downloads","Repositorios_GIT","apensar_relatorios","dados", "ipsum_lorem.txt")  # Cria caminho relativo
print(caminho)

def mostrar_pasta_atual():
    """
    Mostra a pasta atual de trabalho.
    """
    pasta_atual = os.getcwd()
    print("Pasta atual de trabalho:", pasta_atual)
    return pasta_atual  # Opcional

def mudar_pasta(proxima_pasta:str):
    """
    Muda a pasta atual de trabalho para o caminho especificado.
    """
    os.chdir(os.getcwd()+"\\"+proxima_pasta)
    print("Pasta alterada para:", proxima_pasta)

def listar_arquivos_pasta(caminho_pasta):
    """
    Lista os arquivos na pasta especificada.
    """
    arquivos = os.listdir(caminho_pasta)
    print("Arquivos na pasta", caminho_pasta, ":", arquivos)
    return arquivos  # Opcional

def Importar_txt(caminho_arquivo):
    """
    importa o texto dentro de um arquivo txt e devolve a string do texto.
    """
    # Bloco de código (corpo da função)
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)
    return conteudo  # Opcional

def caminho_pasta_dados():
    """
    Retorna o caminho relativo da pasta 'dados' dentro do diretório atual.
    """
    return mostrar_pasta_atual()+"\\dados"

def Importar_txt_apenas_nome(nome_arquivo:str):
    """
    importa o texto dentro de um arquivo txt e devolve a string do texto.
    """
    # Bloco de código (corpo da função)
    with open(caminho_pasta_dados()+"\\"+nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)
    return conteudo  # Opcional

#### FUNÇÕES DOCX - MICROSOFT WORD ####
def Importar_docx_apenas_nome(nome_arquivo:str):
    """
    importa o texto dentro de um arquivo docx e devolve a string do texto.
    """
    from docx import Document
    doc = Document(caminho_pasta_dados()+"\\"+nome_arquivo)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    conteudo = '\n'.join(fullText)
    print(conteudo)
    return conteudo  # Opcional

#### FUNÇÕES DE MANIPULAÇÃO DE TEXTO ####
def Quebrar_texto_em_lista(texto:str, chave_quebrar:str):
    """
    Quebra o texto em uma lista de strings, usando a chave especificada como delimitador.
    """
    lista_texto = texto.split(chave_quebrar)
    print("Texto quebrado em lista:", lista_texto)
    return lista_texto  # Opcional

def devolver_texto_com_contagem(lista):
    """
    Devolve o texto com contagem de itens na lista.
    """
    for i in lista:
        print (lista.index(i) + 1)
        print(i)

def devolver_texto_com_contagem_movel(lista:str,contador_inicial:int=1):
    """
    Devolve o texto com contagem de itens na lista.
    """
    contador_inicial 
    for i in lista:
        print (lista.index(i) + contador_inicial+1)
        print(i)

###AREA DE TESTES DAS FUNÇÕES###
texto_7 = Importar_docx_apenas_nome("7.docx")
lista_texto7 = Quebrar_texto_em_lista(texto_7,"**¨¨")
devolver_texto_com_contagem(lista_texto7)
devolver_texto_com_contagem_movel(lista_texto7,33)