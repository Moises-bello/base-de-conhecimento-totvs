---
article_id: 4411554633751
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: b1dfc5f121373c4e270ab7fb6d334bd745a55525e959a95a45c0df472d9adf19
fetched_at: '2026-06-28T22:39:47.707594+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Aumentar o tamanho
  do campo YF_MOEFAT para integração com MV_MOEDA
type: support-article
updated_at: '2021-10-27T17:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411554633751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Aumentar-o-tamanho-do-campo-YF-MOEFAT-para-integra%C3%A7%C3%A3o-com-MV-MOEDA
---

**Dúvida**Cadastrei a moeda 12 no Protheus, e para tanto, preciso "amarrar" a moeda do Parâmetro **MV\_MOEDA12**, com o campo **YF\_MOEFAT** da Tabela **SYF**, porém o campo **YF\_MOEFAT** esta com o tamanho 1, e moeda no meu sistema é a de número 12, isto é, com tamanho 2. Como proceder nesse caso?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*– Todas versões

**Solução**

1) Alterar o conteúdo do parâmetro **MV\_MAXMOEDA** para 12.

![MV_MOEDA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411551629719/MV_MOEDA.png)

2) Ter criado os parâmetros **MV\_SIMB12** e **MV\_MOEDA12** e informado os seus conteúdos.

3) Acessar o configurador na tabela SYF e fazer ao ajuste do tamanho para 2 e o *Picture* do campo **YF\_MOEFAT** para **@E 99.** Depois salve a alteração no configurador.

**![CAMPO_YF_MOEDA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411554482711/CAMPO_YF_MOEDA.png)**
