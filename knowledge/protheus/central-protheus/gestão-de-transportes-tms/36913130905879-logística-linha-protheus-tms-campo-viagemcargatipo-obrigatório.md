---
article_id: 36913130905879
category: Gestão de Transportes (TMS)
content_hash: 0b06d5f5632ac3e3351b273d8496803a30d773a8100bf3f4ac1b46d659cdcab7
fetched_at: '2026-06-28T22:45:27.387006+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Campo [viagem.carga.tipo] obrigatório
type: support-article
updated_at: '2025-12-10T15:25:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36913130905879-Log%C3%ADstica-Linha-Protheus-TMS-Campo-viagem-carga-tipo-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36913130890135) Tempo aproximado para leitura: **00:00:35 min**  
  
**Ocorrência**  
No Protheus TMS, ao gravar uma viagem integrando com a operadora de frotas **Pamcard**, ocorre a mensagem **Campo [viagem.carga.tipo] obrigatório.**  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
A mensagem **Campo [viagem.carga.tipo] obrigatório** ocorre na integração com a Pamcard pois o campo **DTQ\_TPOPVG** não foi preenchido na viagem.  
  
**Solução**  
Para resolver, é necessário preencher o campo **DTQ\_TPOPVG - Tp.Oper.Vge**, o qual deve possuir cadastro na tabela **DLO - Tipo de Operação da Viagem**, conforme documentação [DT Tipo de Operação da Viagem](https://tdn.totvs.com/pages/releaseview.action?pageId=425443149)
