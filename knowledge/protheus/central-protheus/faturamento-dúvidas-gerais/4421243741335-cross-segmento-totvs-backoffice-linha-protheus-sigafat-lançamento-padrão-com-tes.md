---
article_id: 4421243741335
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1e97f803cdce7f406666edb936e1222d584d8c6d4572ac98df3f55f44268f070
fetched_at: '2026-06-28T22:38:32.981980+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) SIGAFAT - Lançamento padrão
  com Tes
type: support-article
updated_at: '2025-01-10T19:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421243741335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Lan%C3%A7amento-padr%C3%A3o-com-Tes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Lançamento padrão quando a nota fiscal tem TES diferente

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) SIGAFAT - Lançamento padrão com Tes

**Solução**

A contabilização ocorre com base no lançamento padrão configurado para a nota e não com base na tes, É possível avaliar a query de contabilização se na comparação existe a chamada por CFOP.

Exemplo : , IF(SF4$ "6118", SD2->D2\_TOTAL,0), para que desta forma, o sistema valide nas notas de saída, se há o CFOP que desejo contabilizar, qualquer informação que não esteja de acordo com a query, o sistema não contabiliza.  
Lembrando que o suporte não orienta na configuração do lançamento padrão do cliente, a configuração do lançamento padrão deve ser efetuado por um programador com conhecimento em advpl mais um contador.

**Saiba mais em : [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Contabilização no Modulo Faturamento Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056039034-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Contabiliza%C3%A7%C3%A3o-no-Modulo-Faturamento-Protheus?source=search)**
