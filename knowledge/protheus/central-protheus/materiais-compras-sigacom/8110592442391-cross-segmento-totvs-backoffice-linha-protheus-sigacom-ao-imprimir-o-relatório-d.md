---
article_id: 8110592442391
category: Materiais - Compras (SIGACOM)
content_hash: 759623a64236a3d86a22c50d28cf6cac54682c0307ae16c8b3dcfefd780f5aa9
fetched_at: '2026-06-28T22:41:11.560986+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Ao imprimir
  o relatório de Pedido de Compras, é apresentada a mensagem "O pedido de Compras
  chegou ao seu limite de Reemissões"
type: support-article
updated_at: '2022-08-11T18:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8110592442391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ao-imprimir-o-relat%C3%B3rio-de-Pedido-de-Compras-%C3%A9-apresentada-a-mensagem-O-pedido-de-Compras-chegou-ao-seu-limite-de-Reemiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao imprimir o relatório de Pedido de Compras (MATR110), é apresentada a mensagem "O pedido de Compras chegou ao seu limite de Reemissões"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Consulte via Banco de Dados, qual o conteúdo do campo C7\_QTDREEM.

Caso o campo esteja com conteúdo maior ou igual a 99, será apresentada a mensagem:

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8109822524055/imagem2.png)

Dessa forma, sugerimos que insira nos parâmetros, o número do Pedido a ser impresso:

![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8110437685143/imagem3.png)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
