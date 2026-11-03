---
article_id: 360024696894
category: Gestão de Transportes (TMS)
content_hash: 072b05b4d17ad92e4d1bd5840dbf423938ecc66f4a744f8896e91496589da5cd
fetched_at: '2026-06-28T22:45:29.491752+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Parâmetro MV_RTCTEID - Retorno de Status
  de CT-e
type: support-article
updated_at: '2021-07-26T20:52:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024696894-Log%C3%ADstica-Linha-Protheus-TMS-Par%C3%A2metro-MV-RTCTEID-Retorno-de-Status-de-CT-e
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como retornar o Status de um **CT-e - Conhecimento de Transporte Eletrônico** com rejeição de Cancelamento?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Implementada a nova funcionalidade, por meio do botão **Ret. Status** criado na rotina  **TMSAE70 - Monitor de CT-e.**Será possível retornar o status do CT-e para **autorizado**, quando a **SEFAZ - Secretaria da Fazenda**retornar rejeição para a solicitação de cancelamento.  
  
Após realizar as parametrizações para essa nova funcionalidade, na rotina Monitor de CT-e, será apresentado o botão **Ret. Status, conforme imagem abaixo:**

**![ret_status.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4405035730199/ret_status.jpg)**

**Saiba mais**Mais informações poderão ser acessadas no *link*: [Utilizar processo de retorna status CTe na rotina TMSAE70 - Monitor de CT-e](http://tdn.totvs.com/pages/viewpage.action?pageId=490968416)
