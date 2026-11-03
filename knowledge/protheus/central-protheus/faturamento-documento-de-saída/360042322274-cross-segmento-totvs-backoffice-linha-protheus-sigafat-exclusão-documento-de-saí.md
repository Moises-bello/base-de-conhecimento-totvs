---
article_id: 360042322274
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 427355ee8468c615d9f240965351fb6cb831cb2bfb18aad0a2a964336f1502e7
fetched_at: '2026-06-28T22:38:43.867354+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Exclusão Documento
  de Saída apresentado:HELP FECHTO
type: support-article
updated_at: '2023-03-13T18:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042322274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Exclus%C3%A3o-Documento-de-Sa%C3%ADda-apresentado-HELP-FECHTO
---

**Ocorrência**Ao tentar excluir uma nota fiscal através da rotina **MATA521A - Exclusão Documento de Saída**, é apresentado: HELP FECHTO

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057324473/mceclip0.png)**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**Essa mensagem ocorre quando o período está fechado.  
  
**Solução**Quando é apresentada essa mensagem é necessário verificar com a equipe de **Estoque e Custos** se há procedimento de reabertura do mês, para que seja possível realizar o estorno. Caso contrário não terá como estornar o registro**.**Se a nota fiscal é de um período já fechado, não é possível excluir pois afetaria o resultado do período.  
Os parâmetro **MV\_ULMES** (Data do ultimo fechamento do estoque) e **MV\_DBLQMOV** (Data de bloqueio de movimentos) impedem movimentos que manipulem as tabelas **SF2** / **SF1** / **SF3** (independente se a TES gera movimento de estoque/financeiro).
