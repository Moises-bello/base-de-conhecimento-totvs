---
content_hash: 12dd81298ced2a53e0e0dfd0dc755fd2f9ac7488259ba5b8a7f565c4e6c868ee
fetched_at: '2026-06-29T00:05:58.264929+00:00'
page_id: '185747796'
product: rm
source: tdn-rm
title: Geração de Planilhas em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185747796
version: 20
---

# Índice:

---

.\*ndice:

# Introdução

---

          Os parâmetros solicitados pela Consulta SQL são dados de uma visão do RM. O processo de Geração de Planilha em Lote possibilita a exportação do resultado de uma Consulta SQL em uma planilha.

         Desta forma, para cada registro selecionado na visão, serão retornados dados como resultado, seguindo a condição da consulta SQL utilizada na planilha.

         Entre as exigências do processo, está a necessidade de uma planilha "Template".   
Esta planilha template deverá possuir uma consulta SQL que exija um valor como parâmetro.   
Este parâmetro por sua vez será o valor de uma coluna da visão do RM.

         O usuário pode ainda salvar resultado em disco, como uma planilha do Excel ou na base de dados, como uma Planilha .Net.

# Exemplos:

---

**Abaixo segue 2 exemplos:**

Fonte de Dados1Exemplo 1

***Passo a passo:***

false.1° Passo:

         Insira uma Consulta SQL utilizando a sintaxe como exemplo abaixo:

         Esta consulta possibilitará visualizar dados do funcionário em planilha selecionando a chapa.

sql2° Passo:

         Em seguida inclua uma planilha.NET informando um nome. Esta será a planilha "TEMPLATE" (modelo a qual será gerada as outras).

false

 *Somente planilhas do **tipo Excel** são utilizadas neste processo..*

3° Passo:

         Ao acessar a planilha siga os procedimentos abaixo para inclusão da consulta SQL informando o parâmetro (*conforme exemplo abaixo*). Ao final clique em "*Salvar*" e depois "*Fechar*".

4° Passo:

         Acesse a tela respectiva a informação que serão geradas as planilhas em lote. Lembre-se: Esta tela deverá conter em sua visão a mesma coluna utilizada na consulta SQL. Siga os passos descritos na figura abaixo.:

5° Passo:

         No Wizard apresentado siga a ordem de preenchimento dos campos informados na figura abaixo:

6° Passo:

         No Wizard apresentado informe o parâmetro da coluna:

7° Passo:

         Observe que o processo será iniciado até concluir. Clique em Fechar para finalizar.

8° Passo:

         Acesse o cadastro de planilhas e clique em atualizar, em seguida visualize as planilhas geradas para cada registro selecionado na visão.

2Exemplo 2

Visualizar dados em planilhas do cadastro de Cliente/ Fornecedor selecionando o registro.

Consulta para utilizar no exemplo:

sqlfalsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Geração de Planilhas em Lote

falsefalse

**Status:** Finalizado

false

**Data: 09/07/2018**

false

**Autores:**
