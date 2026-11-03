---
article_id: 360028341392
category: CRM - Dúvidas Gerais
content_hash: 2e14ab3a6e05a65b9c2bcaf363c07b5d6b2f0309ed3733963326b16f3b4258be
fetched_at: '2026-06-28T22:40:27.572489+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-InterFunctionCall -cannot find function FT300NUM
type: support-article
updated_at: '2021-04-28T14:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028341392-MP-CRM-InterFunctionCall-cannot-find-function-FT300NUM
---

**Ocorrência**

Ao clicar no botão incluir da Oportunidade de Vendas (FATA300), ocorre o erro:

**InterFunctionCall: cannot find function FT300NUM in AppMap on {|a,b,c| FWInitCpo(a,b,c),xRet:=(FT300NUM()),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }(PROTHEUSFUNCTIONMVC.PRX) 10/04/2019 14:27:48**  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**

O problema ocorre por que existe uma validação indevida **FT300NUM** está  em das colunas da SX3 (  **X3\_When, x3\_relação, x3\_vlduser ou x3\_valid**) do campo **AD1\_NROPOR** .

**Solução**  
Para correção deste erro, retire a validação**FT300NUM** que encontra-se em uma das colunas da sx3 (  x3\_when, x3\_relação, x3\_vlduser ou x3\_valid) do campo **AD1\_NROPOR**,e desta forma, o erro deixará de ocorrer.

Obs: No padrão do sistema apenas o x3\_valid  e x3\_relação possuem validação**,** conforme abaixo, as demais colunas de validação do sx3 estão em branco:

**x3\_valid (validação de sistema): ExistChav("AD1")                                                                                                                  
x3\_relação(inicializador padrão): GetSxeNum("AD1","AD1\_NROPOR")**
