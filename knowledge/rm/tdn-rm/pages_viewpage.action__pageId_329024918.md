---
content_hash: 011bc855d4b15727ed2f5754945e79a5915bd860f04b481567f9ee4a02d5cb1a
fetched_at: '2026-06-29T00:08:48.858682+00:00'
page_id: '329024918'
product: rm
source: tdn-rm
title: Formatação Valores - (Expressão)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329024918
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão de como fazer para formatar valores para o formato K (milhar), M (milhões).

       Exemplo:

       O numero 12.000, será mostrado como 12 K, assim como o numero 12.000.000 será mostrado como 12 M.

# Como Funciona:

---

       Como exemplo usaremos o **Relatório TesteFormatação .**Existe apenas um campo da tabela TMOV nesse relatório:

* **VALORBRUTO**

       Os valores retornados por esse campo variam de 0 ate mais de 1 milhão, dessa forma podemos ver a formatação dos valores funcionando corretamente.

       Para isso, adicione um Controle Padrão "Expressão" ao relatório:

***Passo a passo para configurar a expressão:***

falseInstalação em N camadas (App Server)1º Passo:

Clique nos [...] para editar sua expressão:

2º Passo:

Insira uma função lógica "IF"

3º Passo:

Agora iremos estabelecer uma condição para a formatação. Nesse caso, será VALOR BRUTO >= 1.000.000

Para isso, dentro do "IF" selecione o campo do relatório em que se deseja fazer a formatação:

4º Passo:

Informe a condição e digite , (virgula) para indicar o fim da condição.

5º Passo:

Agora iremos informar o que acontecerá caso a condição seja verdadeira.

No caso, o valor será divido por 1.000.000 e será adiciona a letra "M".

Selecione novamente o campo do relatório, informe as modificações e digite , (virgula) para indicar o fim do 'Caso Verdadeiro'.

Não esqueça de adicionar ' (apóstrofo) e + (mais) para concatenar o valor. Conforme exemplo acima.

6º Passo:

Agora iremos informar o 'Caso Falso', que será quando o valor for menor do que 1 milhão.

Nesse caso, iremo verificar se o valor é maior do que 1.000, para adicionarmos o "K".

Para isso, iremos adicionar um novo "IF", seguindo a mesma lógica do anterior. Porém a nova condição será VALOR BRUTO >= 1.000.

7º Passo:

O 'Caso Verdadeiro' do nosso segundo "IF" segue a mesma lógica do primeiro, porém dividindo por 1.000 e adicionando o "K".

8º Passo:

Por fim, informe o 'Caso Falso', que será manter o valor original sem nenhuma modificação.

A expressão ficará conforme o exemplo acima.

# Visualização:

---

       Como exemplo exibimos os valores formatados e sem formatação:

Para exibir somente os valores formatados, basta configurar o outro valor para "Visível: não". Desta forma, ele não será exibido.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Formatação

falsefalse

**Status:** Finalizado

false

**Data:** 04/01/2018

false

**Autores:**

<http://tdn.totvs.com/x/kIcpE>
