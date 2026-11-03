---
article_id: 360021325292
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: aadf5b6324cb73b7259f23b3a7f8b05502585e8366b3ccc8aeda636ef925fba2
fetched_at: '2026-06-28T22:37:20.084361+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ocorrência do erro
  na Revisão de Contrato: InterFunctionCall: cannot find function CN010RETBX in AppMap
  on X3CBOX(AP5TRANSLATE.PRW)'
type: support-article
updated_at: '2022-05-19T20:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021325292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ocorr%C3%AAncia-do-erro-na-Revis%C3%A3o-de-Contrato-InterFunctionCall-cannot-find-function-CN010RETBX-in-AppMap-on-X3CBOX-AP5TRANSLATE-PRW
---

**Ocorrência**Ocorrência do erro na Revisão de Contrato: **InterFunctionCall: cannot find function CN010RETBX in AppMap on X3CBOX(AP5TRANSLATE.PRW)**

**Ambiente**

Microsiga Protheus - Gestão de Contratos -  A partir da versão 12  
  
**Causa**

Esse incidente ocorre, devido a existência uma validação na tabela no campo X3\_CBOX do Dicionário de Dados da tabela CN0 no ambiente em questão, porém, esta validação não é utilizada na versão 12 do Protheus.

**Solução**  
Para solucionar essa ocorrência, realize o seguinte passo.  
1. Com o auxilio e realização por um analista especialista em loco, deve-se verificar no Dicionário de Dados (SX3) realizando filtro para a tabela **CN0** e pesquisando por ***X3\_CBOX = CN010Retbx*** e apagar esta validação.
