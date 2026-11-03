---
article_id: 360019265551
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 69f68352960e4813f7cfcf90ba86612dba93aa0e6c721569a3745596719132d5
fetched_at: '2026-06-28T22:41:03.352551+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010 HELP: CTGNOCAD
  - Calendário Contábil'
type: support-article
updated_at: '2024-09-23T14:59:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019265551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-HELP-CTGNOCAD-Calend%C3%A1rio-Cont%C3%A1bil
---

**Ocorrência**

Ao efetuar um lançamento contábil é apresentado o **HELP**: **CTGNOCAD**

![ctgnocad.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015072471)

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Causa**

Este **HELP** é apresentado, pois o calendário não está amarrado com a moeda contábil.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
  
1º - Acesse o módulo da **Contabilidade Gerencial**;

2º - **Cadastros** > **Amarração** **Moeda X Calendário (CTBA200)**;

3º - Efetue a amarração da **Moeda** com o **Calendário** **Contábil.**

Necessário para o correto funcionamento se faz necessário que as tabelas abaixo estejam com o mesmo compartilhamento

CTE - Moeda X Calendário  
CTG - Calendário Contábil  
CQD - Bloqueio do calendário Contábil  
CTO - Moeda cadastrada  
CTP - Cambio

Para mais detalhes verifique : <https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>

[MP - SIGACTB: Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)

Veja também :

[Tabelas utilizadas](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba010_tabelas.htm)

[MV\_CTBCTG - Bloqueio de Movimentação por Amarração Calendário X Moeda X Tipo de Saldo](http://tdn.totvs.com/pages/releaseview.action?pageId=49283869)

[Calendário contábil P12](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba010.htm)

[Moed. x Cal x Tip. Saldo](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba011.htm)

[Moeda x Calendário](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba200.htm)

[Bloqueio Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=253988018)

[CTBA102 - Permitindo inclusão de lançamentos mesmo com calendário bloqueado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14766971052951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-mesmo-com-calend%C3%A1rio-bloqueado-?source=search)

[CTBA010 - Calendário contábil bloqueado ou fechado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Calend%C3%A1rio-cont%C3%A1bil-bloqueado-ou-fechado)
