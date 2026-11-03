---
article_id: 16254311902871
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 91750b5e18acbc140488b17a6b23b7444a723beb1daebb73769ce8b253f2ef3e
fetched_at: '2026-06-28T22:38:55.657440+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - array out
  of bounds [1] of [0] on A103XCUSTO(MATA103XEST.PRW)
type: support-article
updated_at: '2023-07-24T19:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16254311902871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-array-out-of-bounds-1-of-0-on-A103XCUSTO-MATA103XEST-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16254343701143) Tempo aproximado para leitura: **00:02:13 min** **Dúvida**Ao incluir/classificar Documento de Entrada ocorre o erro *array out of bounds [1] of [0] on A103XCUSTO(MATA103XEST.PRW).* Como corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Em fontes MATA103XEST de 2023, caso o documento de entrada seja com TES que controle poder de terceiros (F4\_PODER3) sendo R (Remessa) ou D (Devolução), caso esse mesmo TES seja de Transferência entre Filiais (F4\_TRANFIL = 1 - SIM) este erro passa a ocorrer.

Portanto, é recomendável validar internamente a possibilidade de deixar o F4\_TRAMFIL = 2 - Não e, caso necessário, criar outro TES para essa finalidade (desde que o campo de poder de terceiros - F4\_PODER) seja igual à "Não Controla".

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
