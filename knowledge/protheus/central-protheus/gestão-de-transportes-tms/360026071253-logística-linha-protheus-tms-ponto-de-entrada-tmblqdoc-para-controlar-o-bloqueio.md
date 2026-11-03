---
article_id: 360026071253
category: Gestão de Transportes (TMS)
content_hash: ae814e2bb189f4751114580aa85da157396e02729ce32ba866c2849b230e7691
fetched_at: '2026-06-28T22:45:32.378024+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TMBLQDOC para controlar
  o bloqueio do documento
type: support-article
updated_at: '2022-06-17T18:50:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026071253-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TMBLQDOC-para-controlar-o-bloqueio-do-documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: **00:00:42 min**  
**Dúvida**Como implementar o ponto de entrada **TMBLQDOC**para controlar o **bloqueio do documento**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Este ponto de entrada, localizado no fonte **TMSXFUNB** **- Funções** utilizadas pelo módulo **TMS - Gestão de Transportes**, permite ao usuário controlar o bloqueio do documento no momento do cálculo do frete, mesmo existindo um bloqueio para o cliente na tabela **DV5 - Bloqueio de Cliente.** Se o retorno do ponto de entrada for **.F.** ele ignora os bloqueios para este cliente e gera o documento de transporte.  
  
**Saiba mais**  
Mais informações podem ser verificadas no *link*: [TMBLQDOC - Controla Bloqueio do Documento](http://tdn.totvs.com/display/PROT/TMBLQDOC+-+Controla+Bloqueio+do+Documento)
