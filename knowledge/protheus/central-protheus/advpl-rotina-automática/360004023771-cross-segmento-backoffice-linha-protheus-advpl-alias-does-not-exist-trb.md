---
article_id: 360004023771
category: ADVPL - Rotina Automática
content_hash: 7a77ec66e318a58b86ee4add1bfbc8f43c2b4d8b0c856d8da5d8fb695fa52556
fetched_at: '2026-06-28T22:40:23.912260+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Alias does not exist _TRB
type: support-article
updated_at: '2021-12-29T13:21:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004023771-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Alias-does-not-exist-TRB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Ocorrência**Ao utilizar a rotina automática FINA450, é retornado o seguinte error.log: Alias does not exist \_TRB on FA450DBEVA(FINA450.PRX)

**Ambiente**Protheus - ADVPL - versão 12.1.17

**Causa**Na função FA450DBEVA são feitas referências ao arquivo/tabela \_TRB, porém este temporário não está aberto ou não existe em tempo de execução.

As demais áreas da rotina fazem referência à tabela TRB (sem o underline no começo)

**Solução**Associar à issue: DSERFINP-11934
