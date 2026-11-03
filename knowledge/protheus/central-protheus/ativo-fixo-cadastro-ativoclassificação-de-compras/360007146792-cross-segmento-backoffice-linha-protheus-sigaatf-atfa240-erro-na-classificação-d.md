---
article_id: 360007146792
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: a9ebc5c0247fb0792df03df0986455fa05c09944e2be005814425c2cc81905ca
fetched_at: '2026-06-28T22:41:48.196785+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -  SIGAATF - ATFA240 - Erro na
  Classificação do bem Ao incluir informação no campo Conta, N3_CCONTAB:  Cannot find
  function AFA010CTA in AppMap'
type: support-article
updated_at: '2021-09-15T14:09:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007146792-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Erro-na-Classifica%C3%A7%C3%A3o-do-bem-Ao-incluir-informa%C3%A7%C3%A3o-no-campo-Conta-N3-CCONTAB-Cannot-find-function-AFA010CTA-in-AppMap
---

**Ocorrência**

Ao incluir informação no campo "Conta(N3\_CCONTAB)" dentro da Classificação de ativo ocorre o error.log cannot find function AFA010CTA in AppMap on {|a,b,c,d| FWInitCpo(a,b,c),lRet:=((AFA010CTA( ))),FWCloseCpo(a,b,c,lRet),lRet }(PROTHEUSFUNCTIONMVC.PRX).

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Ativo Fixo - 12.1.17

**Causa**

Esse incidente ocorre, pois X3\_VALID do campo N3\_CCONTAB estar tentando utilizar a função AF010CTA(), porém a partir da versão 12.1.17 a função correta é AF012CTA().

**Solução**Para solucionar será necessário corrigir o dicionário de dados, link referente a atualização do ambiente: [MP -SIGACTB - Como realizar a atualização do ambiente no Microsiga Protheus 12?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006655452-MP-SIGACTB-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ambiente-no-Microsiga-Protheus-12-)

**Saiba mais**

[Atfa240 Error log](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007823351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Erro-na-Classifica%C3%A7%C3%A3o-do-bem-InterFunctionCall-cannot-find-function-AF010VALOR-in-AppMap-on-) [-cannot-find-function-AF010VALOR-in-AppMap-on-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007823351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Erro-na-Classifica%C3%A7%C3%A3o-do-bem-InterFunctionCall-cannot-find-function-AF010VALOR-in-AppMap-on-)

[ATFA240 - Cancelamento da classificação do bem](https://totvssuporte.zendesk.com/knowledge/articles/360006848432/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360006848432)

[Classificação do Bem não gatilha conta contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006575352-MP-SIGAATF-Ao-classificar-um-bem-o-sistema-n%C3%A3o-carrega-a-conta-cont%C3%A1bil)
