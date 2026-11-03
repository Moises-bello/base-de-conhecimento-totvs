---
article_id: 4413667753111
category: SIGAEST - INVENTÁRIO
content_hash: 8385dd2db661ca9c0d1698971da0b73d481c642225a56078d30b1cd0266f365a
fetched_at: '2026-06-28T22:38:50.330397+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Help: MR287CONTN'
type: support-article
updated_at: '2021-11-22T11:34:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413667753111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-MR287CONTN
---

**Ocorrência**

Ao emitir o relatório divergência de inventário (MATR287), o sistema apresenta o erro - MR287CONTN  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente ocorre quando o parâmetro MV\_CONTINV está desabilitado.

**Solução**Para solucionar essa ocorrência, basta habilitar o parâmetro MV\_CONTINV = .T. Revisar se realmente deseja utilizar o conceito de contagens múltiplas de inventário, pois ao habilitar esse parâmetro muda o fluxo de contagens de inventário.

Caso, o parâmetro MV\_CONTINV = .F. utilize o relatório MATR285 para as conferências de inventário.

![mv_continv.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413667340951/mv_continv.png)

**Saiba mais:**

*[MP - SIGAEST - MATA340 - MV\_CONTINV múltiplas contagens de inventário por seleção de contagem](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061630273-MP-SIGAEST-MATA340-MV-CONTINV-m%C3%BAltiplas-contagens-de-invent%C3%A1rio-por-sele%C3%A7%C3%A3o-de-contagem)*

[Clique aqui e veja mais artigos sobre inventário no estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
