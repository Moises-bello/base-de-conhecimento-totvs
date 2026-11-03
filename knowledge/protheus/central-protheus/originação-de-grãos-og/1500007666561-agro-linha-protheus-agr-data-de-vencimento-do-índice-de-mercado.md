---
article_id: 1500007666561
category: Originação de Grãos (OG)
content_hash: d9f722eb6d1943bc7a84f8223735efeb6faf597ebc1dfaa63824eb0aaf202d62
fetched_at: '2026-06-28T22:45:38.979268+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Data de Vencimento do Índice de Mercado
type: support-article
updated_at: '2025-06-18T17:00:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007666561-Agro-Linha-Protheus-AGR-Data-de-Vencimento-do-%C3%8Dndice-de-Mercado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20350924534423)***Tempo aproximado para leitura:**00:00:50 min**  
**Dúvida**Como atualizar a data de vencimento do índice de mercado?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Na rotina **Índices de Mercado - OGA080** no campo **NK0 - Índices de Mercado -** **NK0\_DATVEN** - **dt.venc** deverá ser informado a data de vencimento do índice igual data enviada pela integração **API REST - Transferência Representacional de Estado do M2M**.  
Quando informado a data de vencimento para o **Índice**, na execução da integração com a **API REST do M2M**, o índice será salvo com a data da integração e o valor do índice receberá o valor do vencimento.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011143801)
