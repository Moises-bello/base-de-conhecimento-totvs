---
article_id: 360016361432
category: Materiais - Compras (SIGACOM)
content_hash: 7a38c122fcfce842e81dc206a03d459f8accf304e6f83ec4fb15a4678586888b
fetched_at: '2026-06-28T22:41:08.713683+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar outra
  Moeda em Pedido de Compra com PA e realizar sua Compensação ?
type: support-article
updated_at: '2022-05-12T21:08:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361432-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-outra-Moeda-em-Pedido-de-Compra-com-PA-e-realizar-sua-Compensa%C3%A7%C3%A3o
---

**Dúvida**Como utilizar outra Moeda em Pedido de Compra com PA e realizar sua Compensação ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
  
**Solução**

O sistema permite realizar a baixa do PA em outra moeda que está vinculado ao Pedido de Compra, quando vinculado ao Documento de Entrada.

No título gerado a partir do vínculo do Pedido de Compra com o Documento de Entrada é necessário ajustar a moeda e a taxa na aba Duplicata, isto pois o cliente pode realizar o pagamento em outra moeda.

Por default a moeda do Documento de Entrada será 1 (Real) e a taxa zerada.

Ex.:

Pedido de Compra – 200,00 reais, na moeda 4 com taxa 4,00 o valor convertido em reais é 800,00

Quando criado um PA, gera um título de Adiantamento com Saldo no financeiro.

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519511/6.png)

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519531/7.png)

Quando vinculado o Pedido de Compras a um Documento de Entrada e ajustada a moeda na aba Duplicata, o sistema abate o valor da compensação (tipo PA) e gera o outro título do Documento (tipo NF).

![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012510652/8.png)

![9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012510692/9.png)

![10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519571/10.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
