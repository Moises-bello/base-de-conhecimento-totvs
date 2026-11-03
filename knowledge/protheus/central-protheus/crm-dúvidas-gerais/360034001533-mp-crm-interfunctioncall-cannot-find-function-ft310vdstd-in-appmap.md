---
article_id: 360034001533
category: CRM - Dúvidas Gerais
content_hash: 6cad821afb1e80215eb16d07c264516e71edf015af9dd9b69b36ac7f8ff776a9
fetched_at: '2026-06-28T22:40:27.535154+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM- InterFunctionCall: cannot find function FT310VDSTD in AppMap '
type: support-article
updated_at: '2021-04-28T14:50:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034001533-MP-CRM-InterFunctionCall-cannot-find-function-FT310VDSTD-in-AppMap
---

**Ocorrência**

Ao acessar a rotina fata010 - cadastro de processo de vendas, gera o error.log:

**InterFunctionCall: cannot find function FT310VDSTD in AppMap on {|a,b,c,d| FWInitCpo(a,b,c),lRet:=((FT310VdStd())),FWCloseCpo(a,b,c,lRet),lRet }(PROTHEUSFUNCTIONMVC.PRX) 15/02/2019 09:01:30**

**Ambiente**

Microsiga Protheus - a partir da versão 12.1.17.  
   
 **Causa**

O erro ocorre, devido a função **FT310VDSTD**não estar disponível no RPO ou  rotina pai da função  não estar atualizada .

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote do **FATA010,**mais atual:

<https://suporte.totvs.com/portal/p/10098/download?e=680004>

2. Via IDE ou TDS, aplique o pacote em questão para atualização da rotina **FT310VDSTD**.

Obs: Para aplicação do pacote para atualização do RPO é desejável que seja efetuado um Backup do ambiente e conhecimentos técnicos para efetuar o procedimento.

Em caso de dúvida para aplicação do pacote, consulte a equipe de Frame Work .
