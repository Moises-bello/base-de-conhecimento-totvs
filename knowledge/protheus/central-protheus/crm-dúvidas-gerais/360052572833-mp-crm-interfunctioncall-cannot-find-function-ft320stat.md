---
article_id: 360052572833
category: CRM - Dúvidas Gerais
content_hash: a9857bbd6b2a9d08b8ae6fe3f8d8d42db7abbbd8741a69e0a611fdac4295edc6
fetched_at: '2026-06-28T22:40:27.578112+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-InterFunctionCall: cannot find function FT320STAT '
type: support-article
updated_at: '2021-04-28T14:49:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052572833-MP-CRM-InterFunctionCall-cannot-find-function-FT320STAT
---

**Ocorrência**Erro ao gerar uma oportunidade de vendas:

**InterFunctionCall: cannot find function FT320STAT in AppMap on {|a,b,c| FWInitCpo(a,b,c),lRet:=(Ft320Stat()),FWCloseCpo(a,b,c,lRet,.T.),lRet }(PROTHEUSFUNCTIONMVC.PRX) 01/04/2020 19:16:48 line : 5471**  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**

O erro ocorre por que o  **x3\_relação (inicializador padrão),x3\_inibrw( inicializador de browser),x3\_when(modo de edição), x3\_valid(Validação do sistema) ou x3\_vlduser (validação de usuário)** do campo **AD1\_STATUS** está chamando a função **FT320STAT** que encontra-se descontinuada.

**Solução**  
 Para solucionar essa ocorrência, reavalie as validações do campo **AD1\_STATUS** deixando conforme o padrão do sistema:

![](https://totvssuporte.zendesk.com/attachments/token/RLx9ITX2D38SEAUuibzelZGTS/?name=inline-1847840772.png)

Inicializador padrão: "1":

Inic.Browse: Vazio

Modo de Edição:**!Empty(FwFldGet("AD1\_FCI")) .OR. !Empty(FwFldGet("AD1\_FCS"))**

![](https://totvssuporte.zendesk.com/attachments/token/B2U1MaVdTIWB9uehTPaYpJNfL/?name=inline1678673744.png)

Validação de Usuário: Vazio

Validação do Sistema: **Ft300VdVis() .AND. Ft300VProp() .AND. Ft300VldFC() .AND. Ft300OpEnc()**
