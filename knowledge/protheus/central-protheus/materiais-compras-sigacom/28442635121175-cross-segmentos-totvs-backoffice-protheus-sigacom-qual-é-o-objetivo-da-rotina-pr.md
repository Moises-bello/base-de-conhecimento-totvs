---
article_id: 28442635121175
category: Materiais - Compras (SIGACOM)
content_hash: a67a9e0983c01565da99e2becefd076e44a66bae9adbc03f6e2ebe68fc5ac156
fetched_at: '2026-06-28T22:41:24.283312+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual é o objetivo da
  rotina Pré Nota de Entrada (MATA140) ?
type: support-article
updated_at: '2024-12-11T13:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28442635121175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-%C3%A9-o-objetivo-da-rotina-Pr%C3%A9-Nota-de-Entrada-MATA140
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28442651782167) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Qual é o objetivo da rotina Pré Nota?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**

O pré-documento de entrada é o cadastro prévio dos dados básicos do **Documento** **Fiscal**, que será recebido pela empresa, tais como: **Tipo da Nota, Tipo do Formulário, Número do Documento, Data de Emissão, Fornecedor, Espécie do Documento, Estado Origem, Produtos, Quantidades, Valor Unitário por Item, Valor Total por Item, Valor dos Impostos, Descontos, Valor de Frete, Despesas, Pedidos de Compra Relacionados**, entre outros.

O tratamento realizado na rotina **Pré-nota** para o vínculo com o **Pedido de Compra** é igual ao realizado pela rotina **Documento de Entrada**.

O objetivo deste cadastro é facilitar e agilizar o recebimento de materiais registrados na rotina **Documento de Entrada**. Pois, com os dados previamente cadastrados no Sistema, não é necessário digitar todas as informações relacionadas ao **Documento Fiscal**, basta apenas complementá-las.

Ao registrar um **Pré-documento de Entrada** não é gerado nenhum lançamento fiscal, contábil ou financeiro e nem é atualizado o estoque do produto.

O pré-documento de entrada é utilizado na rotina**Documento de Entrada** e transformado em **Documento** **Fiscal** pela opção de menu **Classificação**, a qual possibilita selecionar o código do **TES** (**Tipo de Entrada e Saída**) da operação. Somente a partir desse procedimento são gerados os lançamentos fiscais, contábeis, financeiros e atualizado o estoque.

Para incluir filtro na rotina**Documento de Entrada** para apresentar somente as notas não classificadas, o campo utilizado deve ser o **F1\_STATUS**.

Quando a nota não foi classificada seu conteúdo é vazio.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
