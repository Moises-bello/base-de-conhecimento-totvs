---
article_id: 360058981613
category: Financeiro - Contas a Receber
content_hash: 64272892cb8f9263ba77432f305edd6113f428c227461993243cdb51bcef1a7f
fetched_at: '2026-06-28T22:38:12.838577+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA330 - Help: FA440COMISBX
  na compensação com NCC/RA'
type: support-article
updated_at: '2023-01-04T19:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058981613-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Help-FA440COMISBX-na-compensa%C3%A7%C3%A3o-com-NCC-RA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:06:00 min**

**Ocorrência** Help: **FA440COMISBX** ao realizar uma compensação com NCC/RA.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**O Help: **FA440COMISBX** é apresentado em ambiente onde o parâmetro **MV\_COMIDEV** está configurado com o conteúdo T e o motivo de baixa (Ex.: CMP) está configurado para não calcular comissões (Comissão = N).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096941874/mceclip0.png)

**Solução**Para que a mensagem não seja mais apresentada o motivo de baixa deverá ser configurado para calcular a comissão **(Comissão = S)**.

**Saiba mais**[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
