---
article_id: 1500007669221
category: Financeiro - Cadastros
content_hash: 6a7137983b354b48730f3164efa23835c3849eb10e081da18e111efd4775ad3a
fetched_at: '2026-06-28T22:37:53.077700+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA010 - Erro log:
  InterFunctionCall: cannot find function FA010VLD in AppMap'
type: support-article
updated_at: '2026-03-04T17:27:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007669221-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA010-Erro-log-InterFunctionCall-cannot-find-function-FA010VLD-in-AppMap
---

**Ocorrência**

No módulo Financeiro, ao tentar realizar a alteração no cadastro de natureza **-** FINA010, é apresentado o erro.log abaixo:

**InterFunctionCall: cannot find function FA010VLD in AppMap**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA010 - Todas as versões.  
  
**Causa**  
Erro na validação da X3\_VALID  
  
**Solução**  
Correção do campo ED\_DEDPIS, na validação do X3\_VALID para = Pertence("12") 

**Saiba mais**  
[MP - ADVPL - Quais as funções para realizar a leitura das SXs?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025250712-MP-ADVPL-Quais-as-fun%C3%A7%C3%B5es-para-realizar-a-leitura-das-SXs-?source=search)
