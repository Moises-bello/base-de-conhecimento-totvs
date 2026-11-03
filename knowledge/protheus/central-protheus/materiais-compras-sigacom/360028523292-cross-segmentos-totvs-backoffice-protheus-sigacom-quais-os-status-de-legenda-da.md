---
article_id: 360028523292
category: Materiais - Compras (SIGACOM)
content_hash: 2263c29883d1caa7ee5e83712fb6a03ab0d2f50e485597d9af6123d881a92d34
fetched_at: '2026-06-28T22:41:10.363461+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais os status de
  legenda da Solicitação de Compras?
type: support-article
updated_at: '2026-05-06T13:47:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028523292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-os-status-de-legenda-da-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**

Quais as Legendas das Solicitação de Compras ?  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029455052)

Quantidade disponível para ser utilizado no pedido de compras.

***C1\_QUJE = 0 e C1\_COTACAO = vazio e C1\_APROV = L***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029455472)

A quantidade foi totalmente utilizada no vínculo com pedido de compras e posteriormente no documento de entrada.

***C1\_QUANT = C1\_QUJE*****.**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029456312)

É utilizada parte da quantidade no vínculo com pedido de compras.

***C1\_QUJE > 0 AND C1\_QUJE < C1\_QUANT***

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15355763935895)

**C1\_QUJE > 0 AND C1\_QUJE < C1\_QUANT AND C1\_COTACAO = 'XXXXXX'**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029456051)

A partir da solicitação pode-se gerar a cotação gerando o pedido de compras nesse caso a solicitação ficara em processo de cotação.

***C1\_COTACAO*** **diferente de branco**.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029456131)

Quando a solicitação de compras é encerrada através da rotina eliminação de resíduo ( MATA235 ).

***C1\_RESIDUO = S***.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029456751)

Quando existe alçada configurada, aguardando a liberação da  solicitação.

***C1\_QUJE = 0 e (C1\_COTACAO = branco ou  C1\_COTACAO = IMPORT) e C1\_APROV = B***

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029457932)

Quando a solicitação é incluída com o produto importando cujo campo B1\_IMPORT - sim ficando a legenda de solicitação importado.

***C1\_IMPORT = S***

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029457291)

Ocorre quando a solicitação é bloqueada por alçada e rejeitada.

***C1\_QUJE = 0 e (C1\_COTACAO = branco ou  C1\_COTACAO = IMPORT) e C1\_APROV = R***

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029457951)

É quando é incluindo um contrato e vinculado a  esta solicitação de compra ela fica com a legenda integração GCT.

***C1\_FLAGGCT = 1 e C1\_QUJE menor C1\_QUANT***

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029459211)

No módulo 87 Gestão de Licitações (SIGAGCP), ao incluir uma solicitação de compras no edital ela fica com a legenda de gestão de licitação.

***C1\_TPSC = 2 e C1\_QUJE = 0 e C1\_CODED diferente de branco***

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029459531)

A compra centralizada é a necessidade de comprar onde centraliza o processo de compra em uma matriz e uma filial para integra gerando a compra centralizada.

***C1\_RESIDUO igual a 'S' e C1\_COMPRAC igual a'1'***

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029460912)

É uma solicitação de compras direcionado a compra de materiais importados.

***C1\_TIPO = 2***

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029459851)

É uma solicitação de compras que foi encaminhada para o portal Marketplace.

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029461252)

Para que o sistema não apresente a legenda com triangulo amarelo nas solicitações de compras quando não houver integração com MARKET PLACE.

***C1\_ACCPROC diferente de branco*****.**

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029462932)

Solicitação para licitação refere-se ao controle de licitações ao modulo SIGAGCP.

***C1\_QUJE = 0 e C1\_APROV = L e  (C1\_COTACAO =branco ou C1\_COTACAO for igual ANALIS) e C1\_TPSC = 2.***

**Observações:**

**1)**Em qual momento do processo o sistema define o valor 'B' (Bloqueado) no campo C1\_APROV ?E como é preenchido o campo C1\_STATUS nessa situação?

**R:**O campo C1\_APROV da SC é gravado com B quando a SC está  com status "bloqueada" aguardando a sua liberação de alçada.E o campo C1\_STATUS é preenchido com 2.

**2)**Como é prenchido o campo C1\_APROV ao rejeitar o documento de uma solicitação Bloqueada e como é preenchido o campo C1\_STATUS?

**R:**Ao rejeitar o documento de aprovação de uma SC bloqueada , o campo C1\_APROV é atualizado com R e o campo CR\_STATUS é atualizado com  06.

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001545042)
