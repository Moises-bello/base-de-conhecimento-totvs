---
content_hash: 820a7982b88cd3e4aed66e1a06b42b3fb5e5548f77a683ef6a48e90f59242ad4
fetched_at: '2026-06-29T00:11:27.575807+00:00'
page_id: '727910869'
product: rm
source: tdn-rm
title: Atualizar registros de uma tabela dinâmica usando fórmula visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727910869
version: 8
---

## Objetivo:

---

Este documento tem por objetivo especificar como atualizar um registro de uma tabela dinâmica.

## Especificação:

---

Será criada uma formula visual com atividade para ler registros de uma tabela dinâmica usando o Data Server GlbItemDinamData.   
Em seguida utilizaremos uma atividade para informar a coluna e seu novo valor a ser alterado.  
Posteriormente o registro será salvo na base.

Para mais informações sobre criar a tabela dinâmica e a fórmula visual, acesse o link:

## Criando o fluxo e atividades na Fórmula Visual

---

* **Atividades**Será necessário adicionar as seguintes atividades e seguindo o fluxo conforme a imagem abaixo.  
  → CodeActivity(Codigo) → RMSReadRecordActivity(Leitura) → RMSExpressionActivity(Alterar) → RMSSaveRecordActivity(Salvar)

* **Atividade CodeAcivity**Com um duplo clique sobre esta atividade será apresentado o texto de código para criar um filtro.  
  Deverá ser criado um filtro informando a Tabela([Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=701684268#Lerregistrosdeumatabeladin%C3%A2micausandof%C3%B3rmulavisual-Finalidade)) e as condições, conforme o exemplo abaixo:

Deverá ser informado o filtro para a atividade de Leitura e Salvar registro.

c#RDark

* **Atividade RMSReadRecordActivity**Nesta atividade será informado o Data Server GlbItemDinamData, ele possui uma particularidade dos demais onde não traz todos os campos chave da tabela, portanto é necessário utilizar a atividade CodeActivity, para criar um filtro e informar o valor em cada coluna necessária.   
  Apenas o campo Codigo é apresentado e se refere ao CodCliente na tabela. Conforme destacado na imagem abaixo:

* **Atividade RMSExpressionActivity**Nesta atividade vamos informar o campo que deve ser alterado e o novo valor.  
  Na propriedade Expressões deve ser informado o novo valor, Exemplo: 'ALTEREI A DESCRICAO'  
  Em Valor Calculado deve ser informada a atividade RMSReadRecordActivity, a Tabela e o campo, Exemplo: Activity=Leitura, Path=Tables[0].Item["DESCRICAO"].AsString

* **Atividade RMSSaveRecordActivity**Esta atividade será responsável por salvar a alteração na base.  
  Na propriedade Atividade Ler Registro, deve ser informada a atividade RMSReadRecordActivity.  
  Em Nome do Data Server, deve ser informado o GlbItemDinamData.
