# MAP3121
Repositório do exercício programa de Cálculo Numérico (MAP3121).

Para se resolver o exercício programa foram feitos scripts em python 3, utilizando-se a versão 3.6.9 para se interpretar os scripts.

O código está dividido em 5 arquivos `.py`,  scripts em python. O plotter.py contém funções para se plotar os gráficos em duas e três dimensões. O arquivo task_one.py contém a rotina relacionada à primeira parte do exercício programa, enquanto o arquivo task_two.py contém as rotinas relacionadas à segunda parte do exercício programa. O arquivo problems.py contém as fontes de calor, as condições de contorno, as condições iniciais e a soluções exatas para cada problema a ser testado, além de uma função que retona uma matriz U já inicializada para a solução aproximada. Já no arquivo main.py é feita a escolha de qual parte do exercício programa se irá rodar, escolhendo também qual a fonte de calor, além de criar o diretório onde es resultados dos testes serão guardados.

Todos os resultados são guardados dentro da pasta "results" e dentro dessa pasta há outras para cada tarefa e fontes de calor diferentes.

Para rodar o exercício programa, deve-se ter python3 instalado no computador onde se irá executar. Além disso, os scripts  possuem dependências, as quais estão listadas no arquivo "requirements.txt", as quais podem ser instaladas ao se rodar no terminal: 

```bash
pip3 install -r requirements.txt
```

Por fim, para se rodar o exercício programa, estando no mesmo diretório do arquivo main.py, deve-se rodar no terminal:

```bash
python3 main.py
```
