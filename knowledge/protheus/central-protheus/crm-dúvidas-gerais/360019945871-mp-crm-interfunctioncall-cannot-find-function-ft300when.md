---
article_id: 360019945871
category: CRM - Dúvidas Gerais
content_hash: 027cdd02e1c0ae1f98544895ebd0adaea602bd197ab1af317e6548769845180f
fetched_at: '2026-06-28T22:40:27.575162+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-InterFunctionCall- cannot find function FT300WHEN
type: support-article
updated_at: '2021-04-28T14:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945871-MP-CRM-InterFunctionCall-cannot-find-function-FT300WHEN
---

**Ocorrência**

Ao tentar realizar uma inclusão na rotina de oportunidade de venda e apresentado o seguinte erro:

InterFunctionCall: cannot find function FT300WHEN in AppMap on {|a,b,c| FWInitCpo(a,b,c),lRet:=(Ft300When()),FWCloseCpo(a,b,c,lRet,.T.),lRet }(PROTHEUSFUNCTIONMVC.PRX)

**Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**

O erro ocorrer devido a chamada do **FT300WHEN()** no **X3\_WHEN** do campo **AD1\_PROSPE**, por padrão da versão 12, X3\_WHEN não possui esta validação.  
   
 **Solução**

Retire a validação do **X3\_WHEN** -> **FT300WHEN()** do campo **AD1\_PROSPE**.

Obs: se caso os  campos **AD1\_LOJPRO**, **AD1\_CODCLI** E **AD1\_LOJCLI** , também tiverem a validação  em questão no X3\_WHEN, é importante que também sejam retirados, pois se estes campos estiverem com a validação, acabará gerando erro  também.
