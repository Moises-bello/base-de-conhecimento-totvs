---
article_id: 4411771556119
category: Contabilidade Gerencial - Relatórios Razões
content_hash: ab4845efce4c84c9a356b94b981eafb74d11d3b8af63872955c057c886539ba1
fetched_at: '2026-06-28T22:40:41.147664+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBR400 Lançamento de
  partida Simples não apresenta o C/Partida  mesmo com o parâmetro MV_IMPCPAR  configurado '
type: support-article
updated_at: '2023-08-23T11:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411771556119-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-Lan%C3%A7amento-de-partida-Simples-n%C3%A3o-apresenta-o-C-Partida-mesmo-com-o-par%C3%A2metro-MV-IMPCPAR-configurado
---

**Ocorrência**

Ao emitir o relatório Razão CTBR400  sistema não apresenta  a "C/Partida"  para os lançamento de partida simples , mesmo com o parâmetro  MV\_IMPCPAR = .T.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS  Contabilidade Gerencial- Todas as versões  
  
**Causa**

Issue [DSERCTR1-11875](https://tdn.totvs.com/pages/releaseview.action?pageId=385859271) aberto para tratar a mesma questão , não foi liberado patch e sim a orientação abaixo :

" Para impressão da informação referente a contrapartida é necessário que o parâmetro MV\_IMPCPAR esteja habilitado, e que no lançamento seja informado esta informação.

Para lançamentos de partida simples a informação da contrapartida é apenas informativa, não sendo considerada nos saldos das contas." 

[http://tdn.totvs.com/x/E\_MlE](https://tdn.totvs.com/x/E_MlE)

Help Online (<https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/sigactb.htm>): Contabilidade Gerencial -> atualizações -> Movimentos -> Lançamento Contábil Automático -> Dicas "

**Solução**

Com base na posição da Issue ,para o relatório CTBR400 apresente a "C/Partida" é necessário que no lançamento contabil (CTBA102) seja informado as duas conta debito e credito ,no lançamento de partida simples

* [LANÇAMENTO DE PARTIDA DOBRADA E PARTIDA SIMPLES COM DUAS CONTAS INFORMADAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018884032--MP-SIGACTB-CTBA102-LAN%C3%87AMENTO-DE-PARTIDA-DOBRADA-E-PARTIDA-SIMPLES-COM-DUAS-CONTAS-INFORMADAS?source=search)
* [PERMITE CONTRA CREDITO EM LANÇAMENTO A DÉBITO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013678371-MP-SIGACTB-CTBA102-CTBA101-PERMITE-CONTRA-CREDITO-EM-LAN%C3%87AMENTO-A-D%C3%89BITO-?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411771439895/mceclip0.png)

**Exemplo :**

**1º TESTE**

* parâmetro configurado :

![](https://totvssuporte.zendesk.com/attachments/token/IXaTqXivTfguRxvLqaDxLF6My/?name=inline-1928175140.png)

* Lançamento partida simples somente com uma conta

![](https://totvssuporte.zendesk.com/attachments/token/iDE3GYNfFkmJPsW4mofZY56sC/?name=inline1530332115.png)

* lançamento partida dobrada

![](https://totvssuporte.zendesk.com/attachments/token/0ptfXSxGOcb7H1cq5OIu1hNOX/?name=inline-762419690.png)

* O sistema só apresentou "C/PARTIDA "para os lançamentos de partida dobrada

![](https://totvssuporte.zendesk.com/attachments/token/0zf5cR1SPIMNbBygdIsPxTK3j/?name=inline1302867971.png)

**2º Teste**

* Lançamento de partida dobrada

![](https://totvssuporte.zendesk.com/attachments/token/PIkKtel7ZBi5pl8bikz7EjnH9/?name=inline-1932631968.png)

* Veja que no lançamento de partida simples foi informado as duas contas Debito e credito

![](https://totvssuporte.zendesk.com/attachments/token/56asH2xfCwlpKnxPxFqZRC3Pi/?name=inline-1138513569.png)​​

* parâmetro configurado

![](https://totvssuporte.zendesk.com/attachments/token/3XPcZaURQtAx6jwJOmeHrs5IP/?name=inline936109837.png)

* a contra partida não é apresentada

![](https://totvssuporte.zendesk.com/attachments/token/1L9UNMF8tRRjQVte8obWMkqlC/?name=inline301069330.png)

* parâmetro configurado :

![](https://totvssuporte.zendesk.com/attachments/token/IXaTqXivTfguRxvLqaDxLF6My/?name=inline-1928175140.png)​

* o sistema passou a apresentar a "C/ PARTIDA" para os lançamentos de partida simples e partida dobrada

![](https://totvssuporte.zendesk.com/attachments/token/aG49kDkgkjNnCsO2cJ59tLe0h/?name=inline-1871374157.png)
