---
article_id: 360026051371
category: Call Center - Telemarketing
content_hash: d1cdb14da0daa482f378ff2f0fc59e892643271eab5bd1587b6078fbc4208aef
fetched_at: '2026-06-28T22:41:29.427869+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Variable does not
  exist X - AtCorWh(x,"AAG_COR")
type: support-article
updated_at: '2022-06-22T18:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026051371-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Variable-does-not-exist-X-AtCorWh-x-AAG-COR
---

**Ocorrência**

Ao gerar uma integração do atendimento call center (**Tmka271**) com o chamado técnico do gestão de serviços (**Teca300**), ocorre o erro:**variable does not exist X on {|a,b,c| FWInitCpo(a,b,c),lRet:=(AtCorWh(x,"AAG\_COR")),FWCloseCpo(a,b,c,lRet,.T.),lRet }(PROTHEUSFUNCTIONMVC.PRX)**  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-  a partir da versão 11.

**Causa**

O erro ocorre por que a validação **(AtCorWh(x,"AAG\_COR"))** está  em das colunas da SX3 (  **X3\_When, x3\_relação, x3\_vlduser ou x3\_valid**) do campo **AAG\_COR** .

**Solução**  
Para correção deste erro, retire a validação****(AtCorWh(x,"AAG\_COR"))**** que encontra-se em um dos campos da sx3 (  X3\_When, x3\_relação, x3\_vlduser ou x3\_valid) do campo **AAG\_COR** ,e desta forma, o erro deixará de ocorrer.

Obs: No padrão do sistema apenas o x3\_valid possui informação **AtCorVal("AAG\_CORDES")**, os demais tem que estar em branco.
