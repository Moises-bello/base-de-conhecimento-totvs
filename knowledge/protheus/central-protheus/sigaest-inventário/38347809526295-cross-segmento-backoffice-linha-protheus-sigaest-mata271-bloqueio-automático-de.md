---
article_id: 38347809526295
category: SIGAEST - INVENTÁRIO
content_hash: 92037f820eafbc04d0006e263d14b56b7d21aa5b17ef010f1d2317b897701ef9
fetched_at: '2026-06-28T22:38:50.298705+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio
  automático de movimentações de produtos para inventário (MV_BLQINVA)
type: support-article
updated_at: '2026-06-17T19:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347809526295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-autom%C3%A1tico-de-movimenta%C3%A7%C3%B5es-de-produtos-para-invent%C3%A1rio-MV-BLQINVA
---

No TOTVS Backoffice (Protheus), ao habilitar o parâmetro MV\_BLQINVA = T, o sistema atualiza automaticamente a data do parâmetro MV\_DATAINV no primeiro acesso diário, bloqueando as movimentações dos produtos em inventário. As datas de bloqueio são atualizadas automaticamente, mas o desbloqueio deve ser feito manualmente pela rotina MATA271.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38347809522327) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como bloquear as movimentações de produtos que estão em período de inventário de forma automática  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Quando o parâmetro estiver habilitado - MV\_BLQINVA = T, o sistema passa a atualizar a data que consta no parâmetro MV\_DATAINV automaticamente no primeiro acesso do sistema**(a data desse parâmetro não deve ser alterada manualmente)**. Ao fazer essa validação diária, ele verifica todos os produtos do sistema e bloqueia suas movimentações automaticamente.

Dessa forma, os campos "Data Inicial Bloq. de Inventário" (B2\_DTINV) e "Data Final Bloq. de Inventário" (B2\_DINVFIM) são atualizados automaticamente com a data do parâmetro MV\_DATAINV.

**OBS:** O desbloqueio desses produtos devem ser realizados manualmente pela rotina MATA271 - Bloqueio de produtos para inventário.

**Saiba mais:**

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search)

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data informada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada?source=search)

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
