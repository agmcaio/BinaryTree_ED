from BinaryTree import BinaryTree

def readData(nome_do_arquivo: str)->dict:

    try:
        
        dominios = {}
        with open(nome_do_arquivo, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            # alex  = [alex]
            # alex/louise = [alex, louise]
            line_format = line.strip("\n")
            line_format = line_format.split("/")
            if len(line_format) == 1:
                dominios[line_format[0]] = BinaryTree(line_format[0])
            else:
                arvore = dominios.get(line_format[0])
                arvore.addDomain(line_format)

        return  dominios
   
    except FileNotFoundError as fnfe:
        print('ERRO:', fnfe)

# Inicio do Programa Principal

dominios = readData('url_louise.csv')

while(True):
    print("+------Opções de comandos------+")
    print("| 1 - Busca de URL             |")
    print("| #viewtree - percorrer árvore |")       
    print("| #sair - encerrar programa    |")
    print("|______________________________|")
    
    print()
    
    print("Digite a URL de pesquisa ou #sair para encerrar o programa.")
    
    input_url = input("URL: ").lower()
    
    if input_url[0:1] == "#":
        if input_url.lower() == "#sair":
            print("Encerrando o programa...")
            break
        
        elif input_url.lower().split()[0] == "#viewtree":
            arv = dominios[input_url.split()[1]]
            arv.viewtree()

    elif input_url[0:3] == "www" or input_url[0:4] == "http":
            entrada_sites = input_url.split("/")
            site = dominios[entrada_sites[0]].match(entrada_sites)
            print(site)     

            
    #200 OK - Requisição bem-sucedida!
    
    #400 Bad Request - Servidor não atendeu a requisição.