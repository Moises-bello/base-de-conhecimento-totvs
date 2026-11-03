---
article_id: 360003847432
category: Call Center - Telemarketing
content_hash: 6005d2cd377f9dc3a9b363f754ffd2a23842f6bb7bb10cfb41fe631c9cce72d0
fetched_at: '2026-06-28T22:41:29.406045+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - BA1010: There
  is no current index. on MSSEEK'
type: support-article
updated_at: '2021-09-17T19:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003847432-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-BA1010-There-is-no-current-index-on-MSSEEK
---

**Ocorrência**

Ao efetuar um atendimento Call Center, está gerando o erro: **BA1010: There is no current index. on MSSEEK**  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - a partir da versão 11.80

**Solução**

Para solucionar o problema, preencha o parâmetro **MV\_PLORDTM**  com o conteúdo 1.

O parâmetro indica a ordem da tabela **BA1** a ser utilizada, quando o **TMK** for informada a chave de pesquisa direto no campo Entidade, sem usar F3 .
