---
article_id: 9324451218839
category: Materiais - Compras (SIGACOM)
content_hash: 90cb217e497c6470cc2f7892eb270dbc4b25eb201788ac895ad39e2bdab939c3
fetched_at: '2026-06-28T22:41:11.672225+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Help NAOMVMOD
  ao incluir um Documento de Entrada
type: support-article
updated_at: '2024-10-23T22:18:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9324451218839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Help-NAOMVMOD-ao-incluir-um-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27287479839255) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao incluir um Documento de Entrada é apresentado o Help NAOMVMOD

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9324178392471)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

O Help NAOMVMOD é apresentado ao incluir um Documento de Entrada vinculando um produto de mão-de-obra.

Os produtos MOD são identificados quando:

* O código (B1\_COD) é iniciado pela sigla "MOD" + o código do Centro de Custo;
* Se os campos B1\_CCCUSTO e/ou B1\_GCCUSTO estiverem preenchidos.

A rotina não aceita esse tipo de produto devido seu custo ser obtido somente através do rateio dos movimentos vinculados a ordem de produção (SD3).  
  
Caso seja necessário que a informação de Centro de Custo esteja no cadastro de Produto, informe na Aba Cadastrais, no campo Centro de Custo (B1\_CC) e no campo Conta Contábil (B1\_CONTA).

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
