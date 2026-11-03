---
article_id: 360007359971
category: Gestão de Transportes (TMS)
content_hash: f089fcfc15e640cc3637e4b3d44d371719a5d218081e0aaa825096c424e15b71
fetched_at: '2026-06-28T22:45:33.378329+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Sistema não está transmitindo o cancelamento
  do CT-e
type: support-article
updated_at: '2022-02-02T10:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007359971-Log%C3%ADstica-Linha-Protheus-TMS-Sistema-n%C3%A3o-est%C3%A1-transmitindo-o-cancelamento-do-CT-e
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)**Tempo aproximado para leitura:**00:00:25 min  
  
Dúvida**Por que o Sistema não está transmitindo o cancelamento do CT-e?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**A situação em questão se resume em um **CT-e** - Conhecimento de Transporte Eletrônico, ao qual o prazo para cancelamento já expirou e a **SEFAZ** - Secretaria da Fazenda, não habilita o cancelamento fora do prazo.  
   
Para transmissão do cancelamento do **CT-e**, o **Protheus** considera os seguintes parâmetros:  
  
​**MV\_CTEEXC**- Prazo em dias para cancelamento do **CT-e** após ser autorizado;  
**MV\_CTEEXCH** - Prazo em horas para cancelamento do **CT-e** após ser autorizado.

Realize um teste da transmissão ajustando os parâmetros acima conforme sua operação e veja se possuirá o retorno da **SEFAZ** no Sistema.
