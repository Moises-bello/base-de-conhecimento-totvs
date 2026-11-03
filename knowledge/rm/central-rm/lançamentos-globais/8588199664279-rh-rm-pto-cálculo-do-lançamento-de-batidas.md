---
article_id: 8588199664279
category: Lançamentos Globais
content_hash: baf67529c185d1598ea451930456d826de5aa4335257c23ea8be13d716da2f4f
fetched_at: '2026-06-28T22:46:35.205615+00:00'
product: rm
section_id: 6045394476951
source: central-rm
title: RH - RM - PTO - Cálculo do lançamento de batidas
type: support-article
updated_at: '2025-02-19T00:47:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8588199664279-RH-RM-PTO-C%C3%A1lculo-do-lan%C3%A7amento-de-batidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981951768727) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Como é realizado o cálculo, no processo de lançamento de batidas ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Versão 12.1 e superiores.  
  
**Solução**O  cálculo do lançamento de batidas considera a proximidade das batidas já existentes no espelho com as batidas do horário planejado do funcionário.

**Regra Principal**

Serão consideradas as batidas faltantes para lançamento aquelas que restarem do horário planejado após validação das marcações importadas por **aproximação**.

Demais Regras:

1. Caso a primeira batida coletada seja de hora inferior à primeira hora do horário planejado, ela será associada à esta primeira batida do horário planejado.
2. As demais batidas coletadas serão verificadas por proximidade das batidas planejadas e feito o lançamento das demais conforme planejado.
3. Caso uma batida possua a mesma distância entre duas batidas planejadas, será associada à primeira das duas batidas.

Acesse o link abaixo para ter acesso a mais informações e a exemplos de calculo:  
**[Cálculo do lançamento de batidas](https://tdn.totvs.com/pages/viewpage.action?pageId=574885134)  
  
Saiba Mais:  
[Lançamento de horários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719844)**
