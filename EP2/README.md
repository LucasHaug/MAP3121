# Exercício Programa 2 de MAP3121

Repositório do exercício programa de Cálculo Numérico (MAP3121).

Para se resolver o exercício programa foram feitos scripts em python 3, utilizando-se a versão 3.7.7 para se interpretar os scripts.

O código está dividido em 5 arquivos `.py`,  scripts em python. O plotter.py contém uma função para se plotar os gráficos do problema. O arquivo crank_nicolson.py contém as rotinas relacionadas à resolução pro problema direto pelo método de Crank-Nicolson (retirado e ligeiramente alterado do EP1). O arquivo mmq.py contém funções relacionadas ao método dos mínimos quadrados, incluindo resolução de sistemas lineares necessárias para o método. Já o arquivo tests.py contém funções que retornam os dados específicos de cada um dos testes a, b, c e d. E por fim, o arquivo main.py é feita a interação com o usuário, sendo então feita a escolha de qual teste se irá rodar, além de serem feitas todas as chamadas de funções necessárias para os cálculos das intensidades ak e o erro quadrático.

O usuário pode escolher visualizar os gráficos e também pode escolher salvá-los alterando o valor de duas variáveis públicas que se encontram no começo do arquivo main.py. Se a variável `ENABLE_GRAPHS_VIEW` for `True`, os gráficos gerados serão mostrados e se a variável `SAVE_GRAPHS_IMAGE` for `True`, os gráficos serão salvos no computador. Todos os resultados dos valores calculados das intensidades e dos erros, além dos gráficos, são guardados dentro da pasta "results", que se não existir previamente será criada pelo programa.

Para rodar o exercício programa, deve-se ter python3 instalado no computador onde se irá executar. Além disso, os scripts  possuem dependências, as quais estão listadas no arquivo "requirements.txt" e podem ser instaladas ao se rodar no terminal:

```bash
pip3 install -r requirements.txt

```

Por fim, para se rodar o exercício programa, estando no mesmo diretório do arquivo main.py, deve-se rodar no terminal:

```bash
python3 main.py

```
