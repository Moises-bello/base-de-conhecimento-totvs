---
article_id: 7005722503191
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: cc51a602949fa193f3a9f474511a72ac66c14a80149c3c474deab2b1798f97f8
fetched_at: '2026-06-28T22:39:48.804956+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Cálculo do frete
  na tabela Pré-Cálculo utilizando o Incoterm CFR na fase de desembaraço
type: support-article
updated_at: '2024-06-27T19:37:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7005722503191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-C%C3%A1lculo-do-frete-na-tabela-Pr%C3%A9-C%C3%A1lculo-utilizando-o-Incoterm-CFR-na-fase-de-desembara%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **05:00 min** **Dúvida**O valor do Frete na Tabela Pré-Cálculo utilizando o Incoterm CFR na fase de Desembaraço não segue o mesmo cálculo da Fase de Purchase Order.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**A ocorrência reportada é um problema conceitual.  
Na fase de **Embarque/Desembaraço**, utilizando um Incoterm **CFR** na negociação, o valor do Frete deverá constar na **Invoice** como Incluso no Valor da Mercadoria.  
No momento que for utilizado uma tabela de Pré-Cálculo que contenha a despesa de Frete, será informado ao sistema que além do Frete que consta na negociação (na Invoice ou nas Invoices do processo) o importador terá um custo "**adicional**" de Frete, que será calculado pelo sistema e considerado na composição das bases dos impostos e custos.  
Ou seja, se é o exportador quem paga o frete (**CFR**), tal despesa não deve estar contida na tabela de Pré-Cálculo.  
Reforçando que na fase de **Embarque/Desembaraço** podemos ter várias Invoices, cada uma com um Incoterm diferente.   
  
**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Comportamento do frete da tabela Pré-Cálculo na fase de PO x Embarque/Desembaraço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4859111350551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Comportamento-do-frete-da-tabela-Pr%C3%A9-C%C3%A1lculo-na-fase-de-PO-x-Embarque-Desembara%C3%A7o)
