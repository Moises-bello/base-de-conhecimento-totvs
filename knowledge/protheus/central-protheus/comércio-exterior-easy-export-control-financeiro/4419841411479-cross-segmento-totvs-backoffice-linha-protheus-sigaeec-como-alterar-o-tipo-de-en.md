---
article_id: 4419841411479
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 31ac05a62b183f622cdf7c3da77569d62ad21f29fd7f800b3f4d7c27b948d1d3
fetched_at: '2026-06-28T22:36:58.108690+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Como alterar o
  tipo de entrada e saída TES quando for fazer a nota fiscal complementar de embarque?
type: support-article
updated_at: '2022-01-21T11:55:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419841411479-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-alterar-o-tipo-de-entrada-e-sa%C3%ADda-TES-quando-for-fazer-a-nota-fiscal-complementar-de-embarque
---

**Dúvida**Como alterar o tipo de Entrada e Saída TES quando ao fazer a Nota Fiscal Complementar de Embarque?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução** No padrão não é possível esta alteração, a nota complementar de embarque será gerada, com tipo de entrada e saída TES informada no pedido de exportação.  
A rotina de complemento de preços na exportação é executada em modelo de rdmake padrão, ou seja, é um programa que pode ser alterado conforme a necessidade ou regras de negócio do cliente.  
Para efetuar a alteração, pode ser  pelo programa EECFATCP\_RDM e alterando o tipo de entrada e saídaTES e o código fiscal de operação CFOP utilizados na integração de notas complementares de acordo com a sua  necessidade.

[EEC0010\_Nota\_Fiscal\_Complemento\_Preço](https://tdn.totvs.com/pages/releaseview.action?pageId=273975975)

Obs.: O Rdmake é disponibilizado no pacote de expedição continua do Comex.

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-MP-SIGAEIC-Pacote-acumulado-do-Comex-no-Portal-de-Cliente)
