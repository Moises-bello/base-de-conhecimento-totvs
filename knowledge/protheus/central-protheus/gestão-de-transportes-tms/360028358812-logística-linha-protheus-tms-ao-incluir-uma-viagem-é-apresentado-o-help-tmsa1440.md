---
article_id: 360028358812
category: Gestão de Transportes (TMS)
content_hash: dfb4070e086c90807fbac39a5f1d141d58a86cdacc1b66bf8e482dd792909716
fetched_at: '2026-06-28T22:45:27.255215+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ao incluir uma viagem é apresentado o help
  TMSA14404
type: support-article
updated_at: '2022-05-31T19:56:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028358812-Log%C3%ADstica-Linha-Protheus-TMS-Ao-incluir-uma-viagem-%C3%A9-apresentado-o-help-TMSA14404
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como proceder para corrigir o *help* **TMSA14404** na inclusão da viagem?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**O *help* **TMSA14404** **- Rota não pertence a região de origem**, é apresentado ao incluir uma viagem. O mesmo ocorre pois no cadastro da rota utilizada na viagem, o campo **Cod.Reg.Ori.** - **DA8\_CDRORI** está preenchido incorretamente.  
  
Este campo deve sempre ser preenchido com a região que está localizado sua filial, ou seja, igual ao parâmetro **MV\_CDRORI**.   
  
Já no campo **Cod.Ori.MDF-e - DA8\_CDOMDFE**, deve ser informado a região onde irá iniciar a prestação de serviço. Lembrando também de preencher a aba **Percurso MDFe**, com a sequência de **Estados** que o veículo irá passar. Esta aba deve ser preenchida em ordem de fronteiras.

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029032292/Capturar3.PNG)
