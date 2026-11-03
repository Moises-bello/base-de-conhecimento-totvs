---
article_id: 4403754224023
category: Financeiro - Baixas a Receber
content_hash: b37a4fc907095a31575af60d817ec1718793c14f2bb7513fcde9866eaec83766
fetched_at: '2026-06-28T22:37:43.732922+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Não é possível alterar
  o campo valor do título a receber desdobrado em aberto
type: support-article
updated_at: '2025-07-30T17:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403754224023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-N%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-campo-valor-do-t%C3%ADtulo-a-receber-desdobrado-em-aberto
---

**Ocorrência**Ao tentar alterar um título desdobrado a receber que se encontra em aberto, o campo *Valor* não é habilitado para alteração  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro - Todas as versões.   
  
**Causa**Esse problema ocorre porque o parâmetro ***MV\_BLVLDES*** está configurado como "**.T.".**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403759893399)

**Solução**

Para solucionar essa ocorrência, realize o seguinte procedimento:

Ajuste o parâmetro **MV\_BLVLDES** para **'.F.'**. Com essa configuração, o campo **E1\_VALOR** será habilitado para edição.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403759853207)

**Saiba mais**

[Geração de Títulos por Desdobramento (FINA040 -](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119) [SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=306856119)
