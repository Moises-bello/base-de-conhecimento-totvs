---
article_id: 360016583451
category: Materiais - Compras (SIGACOM)
content_hash: 38e9e0d79625b1c8fde1889839f6c757fe5c4c5c0687644c2488fbe36b417db7
fetched_at: '2026-06-28T22:41:08.897833+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A100NITENS ao
  executar um Documento de Entrada
type: support-article
updated_at: '2022-05-12T21:19:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016583451-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A100NITENS-ao-executar-um-Documento-de-Entrada
---

**Dúvida**

Help A100NITENS ao executar Documento de Entrada

Em Documentos de Entrada, o sistema irá apresentar o Help A100NITENS com o alerta que o número máximo de itens foi atingido para que seja alterado o parâmetro ou reduza a quantidade de itens no documento.

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012502672/6.png)  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80

**Solução**

Caso a quantidade que consta no parâmetro MV\_NUMITEN do Documento de Entrada seja distinta do Documento de Saída, é possível utilizar o Ponto de Entrada ***MTAITNFE***: [MTAITNFE - Clique aqui](http://tdn.totvs.com/display/public/PROT/MTAITNFE)

Quanto a quebra automática no documento de entrada não funciona como documento de saída, será apresentado apenas o alerta com impeditivo, sendo necessário confirmar o registro com a quantidade limite estipulada no parâmetro ou ponto de entrada e incluir um novo documento com os demais itens.

Se o documento for Formulário Próprio = NÃO, o sistema não realiza a validação, ou seja, permite incluir o registro independente da quantidade de itens.

***Saiba Mais :***

[MTAITNFE](http://tdn.totvs.com/display/public/PROT/MTAITNFE)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
