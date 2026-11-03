---
content_hash: 54117de49ace415c3f9e06a03621e2ea833df2bae5b458f8105384ac1c5df041
fetched_at: '2026-06-29T00:08:13.280946+00:00'
page_id: '243660471'
product: rm
source: tdn-rm
title: Planilha RM com parâmetros das consultas SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243660471
version: 23
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é demonstrar como utilizar parâmetros nas Consultas SQL para a Planilha RM, de forma que será definida na consulta, em qual célula da planilha, o valor do parâmetro deve ser consultado.

# Introdução:

---

          A Planilha RM permite que sejam criadas Consultas SQL que definam as células da planilha que serão associadas aos parâmetros da consulta. Dessa forma, não é preciso criar várias Consultas SQL com parâmetros diferentes. Neste documento estão descritos os passos para sua criação.

**Exemplo de Consulta SQL a ser utilizada na Planilha RM**

         Foi criada a Consulta SQL abaixo, no menu **'Gestão | Visões de Dados'** como exemplo. Veja:

Essa consulta retornará dados de Funcionários cujo salário seja maior do que o valor informado na célula 'A1', página 'Sheet1', da planilha onde a consulta for associada.

Atualmente, a planilha suporta os seguintes padrões de parâmetros, que podem ser utilizados na consulta:

1. **:PLN\_<nome da página>$<coluna>#\_<tipo>** – Nesse formato, informe o nome da página da planilha e a coluna para qual deseja fazer referência. O símbolo # representa a linha.   
   *Exemplo  :PLN\_SHEET1\_$A#\_S*, indica que o valor do parâmetro está na página “SHEET1”, na coluna “A”, na mesma linha da célula que a consulta está vinculada e que o tipo de dado é String.
2. **:PLN\_$<coluna>#\_<tipo>** – Nesse formato, informe a coluna para qual deseja fazer referência. O símbolo # representa a linha.   
   *Exemplo :PLN\_$AB#\_S*, indica que o valor do parâmetro está na coluna “AB”, na mesma linha e página da célula que a consulta está vinculada, e que o tipo de dado é String.
3. **:PLN\_<nome da página>#$<linha>\_<tipo>** – Nesse formato, informe o nome da página da planilha e a linha para qual deseja fazer referência. O símbolo # representa a coluna.   
   *Exemplo :PLN\_SHEET1\_#$5\_S*, indica que o valor do parâmetro está na página “SHEET1”, na linha “5”, na mesma coluna da célula que a consulta está vinculada e que o tipo de dado é String.
4. **:PLN\_#$<linha>\_<tipo>** – Nesse formato, informe o nome da página da planilha e a linha para qual deseja fazer referência. O símbolo # representa a coluna.   
   *Exemplo :PLN\_#$12\_S*, indica que o valor do parâmetro está na linha “12”, na mesma coluna e página da célula que a consulta está vinculada, e que o tipo de dado é String.

Informações

O tipo de dado pode ser omitido. Para isso, basta remover do parâmetro a parte \_<tipo>. Exemplo **:PLN\_<nome da página>$<coluna>#**.

O padrão antigo (**:PLN\_<nome da página>$<coluna>$<linha>\_<tipo>**) continua sendo suportado.

Dica

Variáveis dinâmicas, que são variáveis de contexto também podem ser utilizadas para montar consultas a serem vinculadas na planilha. [Clique aqui](http://tdn.totvs.com/x/RoLFAw) e saiba quais são essas variáveis.

# Exemplo:

---

           Seguindo os passos abaixo, será possível criar uma Planilha RM com parâmetros da Consulta SQL.

falseExemploPasso 1Passo 1

Crie a Consulta SQL desejada, que utilize o parâmetro da Planilha.

Para realizar o cadastro, acesse o menu**'Gestão | Visões de Dados'** e clique no botão Incluir (Ctrl + Ins). Veja a imagem a seguir:

Neste exemplo, essa consulta retornará dados de Funcionários cujo salário seja maior do que o valor informado na célula 'A1', página 'Sheet1', da planilha onde a consulta for associada.

Passo 2Passo 2

Após a criação da Consulta SQL no sistema, vamos criar a planilha RM.

Acesse o menu **'Gestão > Planilha Net'** e clique no botão Incluir (Ctrl + Ins). Em seguida, preencha os campos como ilustrado na imagem abaixo:

Passo 3Passo 3

Após criar a planilha, clique duas vezes sobre ela e será apresentada a sua tela de edição.

Agora, vamos associar a sentença SQL na planilha. Selecione a célula da planilha que executará a Consulta SQL. Lembre que a célula deve ser diferente da célula definida na Consulta SQL, pois esta deve conter o valor do parâmetro (célula 'A1', página 'Sheet1', deste exemplo).

Acesse o menu **'Planilha | Visões de Dados | Associar Consulta SQL à Célula'**.

Selecione a Consulta SQL e em seguida clique no botão 'OK'.

Passo 4Passo 4

Existem três tipos de Parâmetros. São eles:

Expressão, Valor e Referência.

Expressão: É quando o parâmetro é feito direto na consulta. (Verifique **Exemplo de Consulta SQL a ser utilizada na Planilha RM)**

Valor: É o valor absoluto do parâmetro.

Referência: Referência de uma célula, você apontar para a célula que deseja exibir.

Passo 5Passo 5

Informe na célula A1 da página 'Sheet' o valor que o parâmetro receberá. Neste exemplo, o valor mínimo dos salários que devem ser pesquisados.

Em seguida, execute a Consulta SQL associada à célula.

Ao observar a planilha será possível visualizar o resultado, como na figura a seguir:

false

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Planilha RM

false

**Subprocesso:** Planilha RM com parâmetros das Consultas SQL

falsefalse

**Status:** Finalizado

false

**Data:**

**Autores:**
