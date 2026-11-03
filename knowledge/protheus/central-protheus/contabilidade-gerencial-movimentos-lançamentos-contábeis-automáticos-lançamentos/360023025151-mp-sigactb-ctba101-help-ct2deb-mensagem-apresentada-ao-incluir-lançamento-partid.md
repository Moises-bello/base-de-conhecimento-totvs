---
article_id: 360023025151
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: f5f2d26a865e7d005770692647d7293957dab0c71760297fd425054671f6d7c3
fetched_at: '2026-06-28T22:40:32.624021+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'MP - SIGACTB : CTBA101 HELP: CT2DEB: MENSAGEM APRESENTADA AO INCLUIR LANÇAMENTO
  PARTIDA SIMPLES '
type: support-article
updated_at: '2021-04-28T22:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023025151-MP-SIGACTB-CTBA101-HELP-CT2DEB-MENSAGEM-APRESENTADA-AO-INCLUIR-LAN%C3%87AMENTO-PARTIDA-SIMPLES
---

**Ocorrência**

Ao incluir lançamento de partida simples através da rotina de Lançamento Contábil (CTBA101) sistema apresenta mensagem

HELP: CT2DEB

Problema : Debito e Credito não Conferem !!

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020382671/mceclip6.png)  
   
 **Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80  
   
 **Causa**

F12 :Ao informar o "Verif. Lanc. 1/2 ? = Sim" o sistema realiza validação impedindo que o lançamento de partida simples seja gravado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020489832/mceclip4.png)

Para mais detalhe sobre o conceito do parâmetro  **[CLIQUE AQUI](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba101_validando_valores_bra.htm)**   
 **Solução**

* Ao informa "Sim"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020382191/mceclip5.png)

* É apresentada mensagem impedindo que o lançamento seja realizado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020490292/mceclip7.png)

* Ao Informar "Não"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020490432/mceclip8.png)

* O sistema apresenta mensagem , porem permite prosseguir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020490692/mceclip10.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020384291/mceclip12.png)

* Diante disso caso deseje incluir lançamento de partida simples deve informe "Verif. Lanc. 1/2 ? = Não"
