---
article_id: 360017832052
category: Materiais - Compras (SIGACOM)
content_hash: 3d8a8718f5cd13a6caf6252311ce62fe26d3024e3fa130625892c7e83dd55247
fetched_at: '2026-06-28T22:41:22.014103+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Objetivo da Pré-Nota
type: support-article
updated_at: '2022-05-18T21:07:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017832052-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Objetivo-da-Pr%C3%A9-Nota
---

**Dúvida**Qual é o objetivo da Pré-Nota  
   
 **Ambiente**Microsiga Protheus - Compras- A partir da versão 11.80  
   
**Solução**  
 Para checar a ocorrência, realize os seguintes passos:

O pré-documento de entrada é o cadastro prévio dos dados básicos do **Documento** **Fiscal**, que será recebido pela empresa, tais como: **Tipo da Nota, Tipo do Formulário, Número do Documento, Data de Emissão, Fornecedor, Espécie do Documento, Estado Origem, Produtos, Quantidades, Valor Unitário por Item, Valor Total por Item, Valor dos Impostos, Descontos, Valor de Frete, Despesas, Pedidos de Compra Relacionados**, entre outros.

O tratamento realizado na rotina **Pré-nota** (Mata140) para o vínculo com o **Pedido de Compra** é igual ao realizado pela rotina **Documento de Entrada (Mata103)**.

O objetivo deste cadastro é facilitar e agilizar o recebimento de materiais registrados na rotina **Documento de Entrada**. Pois, com os dados previamente cadastrados no Sistema, não é necessário digitar todas as informações relacionadas ao **Documento Fiscal**, basta apenas complementá-las.

Ao registrar um **Pré-documento de Entrada** não é gerado nenhum lançamento fiscal, contábil ou financeiro e nem é atualizado o estoque do produto.

O pré-documento de entrada é utilizado na rotina**Documento de Entrada** e transformado em **Documento** **Fiscal** pela opção de menu **Classificação**, a qual possibilita selecionar o código do **TES** (**Tipo de Entrada e Saída**) da operação. Somente a partir desse procedimento são gerados os lançamentos fiscais, contábeis, financeiros e atualizado o estoque.

Para incluir filtro na rotina**Documento de Entrada** para apresentar somente as notas não classificadas, o campo utilizado deve ser o **F1\_STATUS**.

Quando a nota não foi classificada seu conteúdo é vazio.

Veja o passo de como acessar a rotina

* **Atualizações > Movimentos > Pré-Nota de Entrada** > opção **Incluir**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013211032/mceclip0.png)

Saiba mais
