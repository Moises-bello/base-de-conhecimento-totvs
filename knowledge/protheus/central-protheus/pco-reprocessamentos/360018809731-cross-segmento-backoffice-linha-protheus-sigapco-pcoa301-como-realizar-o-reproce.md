---
article_id: 360018809731
category: PCO - Reprocessamentos
content_hash: 9a29a2dc5f4164645719f941522892434069de3deb43b0ec9f9583eb58c9cbcf
fetched_at: '2026-06-28T22:37:07.017367+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA301 Como realizar
  o reprocessamento multi-thread dos saldos do cubo
type: support-article
updated_at: '2024-07-01T20:41:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018809731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA301-Como-realizar-o-reprocessamento-multi-thread-dos-saldos-do-cubo
---

**Dúvida**

Como realizar o reprocessamento multi-thread dos saldos do cubo?

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

O reprocessamento é realizado através da rotina Cubos Multi-Threads (PCOA301), que dividirá o processo considerando a quantidade de threads a serem utilizadas, que deverá ser informada no parâmetro MV\_PCOTHRD. Podem ser utilizadas entre 2 e 9 threads.

Para utilização desta rotina, além da configuração do parâmetro acima é necessário que os cubos estejam configurados e que haja movimentações no período selecionado.

Seu acesso é realizado através do SIGAPCO em Miscelânea/reprocessamento/cubos Multi-Threads (PCOA301).
