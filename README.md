# Grafo Literário

## Requerimentos

	python3

	-NLTK
	-Numpy
	-Pandas
	-Matplotlib
	-Networkx
	-graphviz

## Instalação

	pip3 install numpy
	pip3 install pandas
	pip3 install tqdm
	pip3 install networkx
	pip3 install matplotlib
	pip3 install nltk
	

	**sudo apt install python-dev graphviz libgraphviz-dev pkg-config**\
	pip3 install pygraphviz

## Modo de usar

Dois arquivos são requeridos: Um txt com o livro e um csv com o dicionario de personagens\
O txt do livro é bem simples, é só o texto do livro sem as formatações (Nome de capitulo, pag, etc..)\
O csv (pode ser .txt, mas tem que está no padrão) é no seguinte formato:\
	A primeira linha é o header e deve, obrigatoriamente (por enquanto), ser da seguinte forma:\
		Name;Dic\
	As outras linhas seguem o padrão da primeira\
	Nessa versão do cod só estamos suportando nomes com um token.**(Por Enquanto)**\
	No campos dic os apelidos ou nomes alternativos devem ser separados por espaço\
	O codigo é case sensitive\
	Os nomes não pode se repetir \
	Ex de um personagem:\
		Hermione;hermione Mione mione Amor linda xuxu\
		Harry;harry arry\



Para rodar execute no terminal no diretorio onde o arquivo está\

	python3 geragrafo.py

É bom que os outros dois arquivos estejam no mesmo diretorio\
O programa vai pedir algumas coisas:\
	
	nome do arquivo do livro (o txt com o livro)\
	nome do arquico do dicionario (o csv com o dicionario)\
	janela (o tamanho da janela (quantos tokens ele vai procurar os nomes))\
	overlap (a interseção entre duas janelas)\
	limiar (o valor da conexão alta (se dois nomes tem uma conexão maior ou igual a esse valor a conexão entre eles fica maior na imagem)\
	arquivo de saida (o nome da imagem, ex: grafo.png O .png é bom botar)\


##Trabalho futuro\

-Melhorar o menu (ter que digitar o nome do arquivo não é ideal)\
-Suporte para nomes compostos\
-Melhorar a documentação do cod (lol)\


Valeu!\


Made by Vinicius Sampaio from Boitatá\
vinicius.sampaio@aluno.uece.br 


##Erros comuns

A instalção do graphviz/pygraphviz é um pouco problemática, mas o networkx usa ele para plotar o grafo de forma "legivel"\ então acaba sendo uma dor necessária\

Tem um erro, dependendo da versão do Networkx, em que **G.node()** não existe, a solução é substituir por **G.nodes()**\


