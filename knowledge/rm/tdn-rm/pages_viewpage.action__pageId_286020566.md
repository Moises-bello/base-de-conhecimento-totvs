---
content_hash: e1e752a3d80d801e075570d629659c313d3dda5da1c03655e0aa7f524bf3b553
fetched_at: '2026-06-29T00:08:39.429648+00:00'
page_id: '286020566'
product: rm
source: tdn-rm
title: Formatação de campos do Cubo (Nome de exibição, Total, Subtotal, Ordenação,
  etc.)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286020566
version: 14
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é explicar as funcionalidades disponibilizadas no menu de Formatação de Campos do Cubo, onde é possível realizar as configurações de:

* Alterar nome de exibição do campo;
* Selecionar o tipo de subtotal dos valores;
* Ordenar de acordo com um campo;
* Máscara de colunas calculadas;
* Agregar valores por;
* Exibir valores por;

# Introdução

---

       Após criar um Cubo (), o menu de Formatação de campos do cubo pode ser acessado através do ícone destacado na imagem abaixo:

No menu de formatação dos campos, é possível selecionar, na listagem à esquerda, qual campo se deseja configurar:

# Alterar nome de exibição do campo

---

Na opção "Texto", é possível alterar o nome de exibição do campo no Cubo:

**Texto padrão:**

**Texto modificado:**

Texto modificado no Cubo:

# Totalizar Valores (Subtotal)

---

Na opção "Totalizar valores", é possível selecionar o tipo de totalizador (Subtotal) a ser exibido para os campos aninhados, conforme mostrado na imagem abaixo:

As opções de totalizar são:

* + ***Total:*** Soma todos os valores
  + ***Média:*** Seleciona o valor médio dos valores.
  + ***Quantidade:*** Conta quantos registros de valores existem.
  + ***Nenhum:***Não exibe nenhum totalizador.

Observação

Se o campo selecionado para totalizar os valores não possuir mais de um campo aninhado à ele, o subtotal correspondente não é mostrado, por default. 

Na imagem anterior, o campo CODSECAO foi configurado para ser totalizado como "Quantidade". Com isso, no exemplo abaixo, nas linhas onde esse campo possui mais dados aninhados (CODSECAO 1.02 e 1.03), são exibidos os subtotais de quantidade de ocorrência do campo. Já na linha onde não possui nenhum dado aninhado (CODSECAO 1.05), o subtotal não é exibido.

Além disso, o campo NOMEFANTASIA foi configurado para ser totalidade como "Total", realizando uma soma dos valores das colunas:

O resultado final é exibido abaixo:

# Ordenar de acordo com um campo

---

Nessa opção é possível ordenar as linhas de acordo com os totais gerais de um campo que esteja na área de dados ou de uma coluna calculada:

Desvincular ordenação

Para desvincular um campo selecionado, basta clicar sobre a opção e pressionar a tecla **DELETE** do teclado.

Nesse exemplo, os campos CHAPA e SALARIO estão na área de dados SALCORRIG é uma coluna calculada. Na imagem abaixo, o Cubo está sem nenhuma ordenação;

Configurando o campo DATAADMISS, que está na área de registros (linhas), para ser ordenado de acordo com o campo SALARIO DO FUNC, conforme mostrado abaixo, a tabela passaria a ser organizada pelo total desse campo.

Resultado da ordenação:

A opção de Ordenar de acordo com um campo só é disponível para campos que não estejam na área de dados ou que não sejam do tipo coluna calculada, já que esses campos são justamente as opções oferecidas para ordenação.

# Máscara

---

Nessa opção é possível selecionar a máscara a ser aplicada nos valores das coluna calculadas incluídas no Cubo, conforme mostrado abaixo:

Desvincular ordenação

Para desvincular uma máscara selecionada, basta clicar sobre a opção e pressionar a tecla **DELETE** do teclado.

Com a máscara "Monetário" selecionado:

A opção de Máscara só é disponível para campos do tipo coluna calculada.

 

# Agregar valores por

---

Nessa opção é possível selecionar a forma de agregar os valores para os campos que estejam na área de dados e que, consequentemente, são exibidos em "Total Geral":

As opções de agregar são:

* + ***Total:*** Soma todos os valores
  + ***Média:*** Seleciona o valor médio dos valores.
  + ***Quantidade:*** Conta quantos registros de valores existem.
  + ***Máximo:*** Exibe o maior valor registrado.
  + ***Mínimo:*** Exibe o menor valor registrado.

Observação

Para que funcione corretamente, é necessário que o campo colocado na área de dados contenha valores numéricos.

A opção de Agregar valores por é disponível apenas para campos que estejam na área de dados ou que sejam do tipo coluna calculada.

No exemplo abaixo, o campo CHAPA foi configurado para agregar valor por **Quantidade** e o campo SALARIO foi configurado para agregar valor por **Máximo**. A imagem abaixo mostra o resultado dessa configuração:

# Exibir valores como

---

Nessa opção é possível selecionar a forma como os valores serão exibidos em "Total Geral":

As opções de agregar são:

* ***Padrão:*** Exibe os valores sem modificações.
* ***Percentual da coluna:*** Exibe a porcentagem que aquele valor representa em relação a sua coluna.
* ***Percentual da linha:*** Exibe a porcentagem que aquele valor representa em relação sua a linha

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** Formatação de campos do Cubo

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
