# MAP3121
Repositório do exercício programa de Cálculo Numérico (MAP3121).

Para se resolver o exercício programa foram feitos scripts em python 3, utilizando-se a versão 3.6.9 para se interpretar os scripts.

O código está dividido em 5 arquivos ".py",  scripts em python. O plotter.py contém funções para se plotar os gráficos em duas e três dimensões. O arquivo task_one.py contém a rotina relacionada à primeira parte do exercício programa, enquanto o arquivo task_two.py contém o necessário pra segunda parte do exercício programa. O arquivo problems.py contém com as fontes de calor, as condições de contorno, as condições iniciais e a soluções exatas para cada problema a ser testado. Já no arquivo main.py se faz a leitura dos parâmetros de entrada, além de permitir a escolha de qual parte e qual item se irá rodar.

Todos os resultados são guardados dentro da pasta "results" dependendo de qual tarefa se está falando e de qual item.

Para rodar o exercício programa, deve-se ter python3 instalado no computador onde se irá executar. Além disso, os scripts  possuem dependências, as quais estão listadas no arquivo "requirements.txt", podendo serem instaladas ao se rodar no terminal: 

```bash
pip3 install -r requirements.txt
```

Por fim, para se rodar o exercício programa, estando no mesmo diretório do arquivo main.py, deve-se rodar no terminal:

```bash
python3 main.py
```
