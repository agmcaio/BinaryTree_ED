class NodeException(Exception):
    """Classe base que implementa as exceções"""
    def __init__(self, msg):
        super().__init__(msg)

class PosicaoNaoVazia(NodeException):
    pass

class ArvoreVaziaException(Exception):
    pass


'''
Classe para instanciação de nós que vão ficar na memória
'''
class Node:
    """Classe que implementa os nós da Árvore Binária"""
    def __init__(self,data:str):
        """Construtor padrão que inicializa o Nó"""
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->str:
        """Método que retorna o dado da árvore binária"""
        return self.__data

    @data.setter
    def data(self, newData:str):
        """Método que insere um novo dado na árvore binária"""
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        """Método que retorna o nó esquerdo da árvore binária"""
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        """Método que insere um nó esquerdo na árvore binária"""
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        """Método que retorna o nó direito da árvore binária"""
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        """Método que insere um nó direito na árvore binária""" ##corrigir##
        self.__rightChild = newRightChild

    def insertLeft(self, data:'Node'):
        """Método que insere um nó esquerdo na árvore binária"""
        if self.__leftChild == None:
            self.__leftChild = data	

    def insertRight(self,data:'Node'):
        """Método que insere um nó direito na árvore binária"""
        if self.__rightChild == None:
            self.__rightChild = data

    def __str__(self):
       """Método que retorna a representação de string de um objeto"""
       return str(self.data)

    def hasLeftChild(self)->bool:
        """Método que retorna se tem um nó esquerdo na árvore binária"""
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        """Método que retorna se tem um nó direito na árvore binária"""
        return self.__rightChild != None
	    
'''
Classe para a instanciação de Árvores Binárias
Autor: Alex Sandro
'''
class BinaryTree:
    # constructor that initializes an empty Tree 
    def __init__(self, data_root):
        """Construtor padrão que inicializa a Árvore vazia"""
        self.__root = Node(data_root)
        # O cursor é um apontador usado para navegar na árvore (sem mexer no root)

    def getRoot(self)->'Node':
        """Método que obtem a referência para o nó 'root'"""
        return self.__root

    def getNode(self, key): 
        """"Método que obtem a referência para os nós"""
        return self.__getNode(key, self.__root)

    def __getNode(self, key, node:Node) -> 'Node':
        """"Método privado que obtem a referência para os nós"""
        if node == None:
            return None
        if node.data == key:
            return node
        elif self.__getNode(key, node.leftChild):
            return self.__getNode(key, node.leftChild)
        else:
            return self.__getNode(key, node.rightChild)
    
    def addDomain(self, key: list) -> None:
        """Método que adiciona os nós da árvore binária"""
        if self.__root is None:
            self.__root = Node(key[0])
        else:
            self.__addDomain(key, self.__root)

    def __addDomain(self, key: list, node: 'Node'):
        """Método privado que adiciona os nós da árvore binária"""
        if node.data == key[0]:
            key = key[1:]
            #tem que procurar o proximo no para ir 
            # a esquerda e a direita
            if node.leftChild is not None and node.leftChild.data == key[0]:
                # desce recursivamente para o lado esquerdo
                self.__addDomain(key, node.leftChild)
               
            elif node.rightChild is not None and node.rightChild.data == key[0]:
                # desce recursivamente para o lado direito
                self.__addDomain(key, node.rightChild)
                
            else:
                # já encontrou o nó pai de inserção.
                # entao verifica se vai adicionar a direita
                # ou a esquerda return True
                newNode = Node(key[0])
                if node.leftChild == None:
                    print(self.addLeft(node,newNode))
                    self.__addDomain(key, node)
                
                else:
                    print(self.addRight(node,newNode))
                    self.__addDomain(key, node)

        # (a) Se a url a adicionar é louise/alex/fernando
        #     para poder inserir fernando é necessário que
        #     haja uma raiz 'louise' e que 'louise' tenha
        #     um filho esquerdo ou direito 'alex'
        # (b) Entao, acessa o nó raiz (louise) e caminha
        #     para o nó 'alex'
        # (c) nesse caminhamento, a cada nó visitado, a 
        #     carga do nó tem que corresponder à parte
        #     da url verificada
    
    def addLeft(self, root, newNode):
        """Método que adiciona um nó esquerdo na árvore binária"""

        if root is None:
            return False

        if root.leftChild == None:
            root.insertLeft(newNode)
            return True
        else:
            return False
    
    def addRight(self, root, newNode):
        """Método que adiciona um nó direito na árvore binária"""
        
        if root is None:
            return False

        if root.rightChild == None:
            root.insertRight(newNode)
            return True
        else:
            return False

    def search(self, key:object )->bool:
        '''Realiza uma busca na árvore pelo nó cuja carga é igual à chave
           passada como argumento.
           Returns
           ---------
           True: caso a chave seja encontrada na árvore
           False: caso a chave não esteja na árvore
        '''
        return self.__searchData(key, self.__root)
    
    def __searchData(self, key, node):
        """"Método privado que realiza busca na árvore pelo nó cuja carga é igual à chave passada como argumento"""
        if (node == None):
            return False # Nao encontrou a chave
        if ( key == node.data):
            return True 
        elif ( self.__searchData( key, node.leftChild)):
            return True
        else:
            return self.__searchData( key, node.rightChild)

    def preorderTraversal(self):
        """Método que exibe os nós da árvore com percurso em pré-ordem"""
        self.__preorder(self.__root)
        
    def __preorder(self, node):
        """Método privado que exibe os nós da árvore com percurso em pré-ordem"""
        if( node == None):
            return
        print(f'{node.data} ',end='')
        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)
    
    def viewtree(self):
        """Método que exibe a árvore binária através do comando especial #viewtree"""
        ancestral = []
        self.__viewtree(self.__root, ancestral)

    def __viewtree(self, node, ancestral):
        """Método privado que exibe a árvore binária através do comando especial #viewtree"""
        # louise
        # louise/fernando
        # louise/fernando/alex
        # louise/caio
        # str = ''
        '''
                           louise
                         //      \\
                   fernando        caio
                    //     \\         \\
               damires      Alex        tsi
        '''     
        if(node == None):
            return
        
        urls = ""
        
        if ancestral != []:
            for i in ancestral:
                urls = urls + i + "/"

        print(f"{urls}{node.data}")
        ancestral.append(node.data)
        self.__viewtree(node.leftChild, ancestral)
        self.__viewtree(node.rightChild, ancestral)
        ancestral.pop()

    def match(self, key):
        return self.__match(self.__root, key)

    def __match(self, node, key):
        """Método que compara os nós da árvore binária com o input do usuário"""
        paths = key
        site = False
        for path in paths:
            site = self.search(path)
            if not site:
                break

            if node.hasLeftChild():
                if node.leftChild.data == path:
                    return self.__match(node.leftChild, paths)
            
            if node.hasRightChild():
                if node.rightChild.data == path:
                    return self.__match(node.rightChild, paths)

        return site        