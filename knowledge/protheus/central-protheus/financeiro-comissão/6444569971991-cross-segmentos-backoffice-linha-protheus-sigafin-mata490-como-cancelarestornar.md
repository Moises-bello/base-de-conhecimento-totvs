---
article_id: 6444569971991
category: Financeiro - Comissão
content_hash: c7b80804f844e1bffb327dfbefa360c01e2c03d78a0f8e2bf12e8f9e3b6db04c
fetched_at: '2026-06-28T22:37:50.825081+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA490 - Como cancelar/estornar
  uma baixa de um título que já foi pago a comissão
type: support-article
updated_at: '2025-07-30T17:23:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6444569971991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA490-Como-cancelar-estornar-uma-baixa-de-um-t%C3%ADtulo-que-j%C3%A1-foi-pago-a-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33826019915159) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como cancelar/estornar uma baixa de um título que já foi pago a comissão?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**

Para cancelar a comissão já paga se faz necessário cancelar a **baixa** pela **Rotina FINA070**, mesmo que tenha pago a comissão ao cancelar será gerado um movimento negativo abatendo o valor pago.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444337070103)

Se a **comissão** estiver 100% na emissão, no caso precisa excluir a **NF** para gerar um movimento negativo para o **vendedor**.
