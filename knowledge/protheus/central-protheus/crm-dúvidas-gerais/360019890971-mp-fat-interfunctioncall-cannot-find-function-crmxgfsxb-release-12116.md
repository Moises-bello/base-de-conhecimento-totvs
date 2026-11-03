---
article_id: 360019890971
category: CRM - Dúvidas Gerais
content_hash: eef2453d06adfed867775526f32ad1f18107afbb254fc6482b0d6b1a137337d4
fetched_at: '2026-06-28T22:40:27.597255+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-FAT - InterFunctionCall: cannot find function CRMXGFSXB release 12.1.16'
type: support-article
updated_at: '2021-04-28T14:50:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019890971-MP-FAT-InterFunctionCall-cannot-find-function-CRMXGFSXB-release-12-1-16
---

**Ocorrência**

Ao consultar o cliente na nota de entrada, via consulta F3, gera o erro: **InterFunctionCall: cannot find function CRMXGFSXB in AppMap on CRMXFILSXB(CRMXFUNPERM.PRW)25/10/2017 16:56:54 line : 165**

**Ambiente**

Microsiga Protheus - release 12.1.16  
   
 **Causa**

O erro ocorre, devido a função **CRMXGFSXB** não estar Disponível no RPO.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Efetue o download do pacote do **CRMXFUNGEN**: **[PACOTE\_DE\_CORRECAO\_1273747\_DSERFAT-2099\_12.1.16.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=625387)** ;

2. Via IDE ou TDS, aplique o pacote em questão para atualização da rotina **CRMXFUNGEN**.

Obs: Para aplicação do pacote para atualização do RPO é desejável que seja efetuado um Backup do ambiente e conhecimentos técnicos para efetuar o procedimento.

Em caso de dúvida para aplicação do pacote, consulte a equipe de Frame Work .

Para o erro na release 12.1.17, consulte o artigo: **[MP-FAT - InterFunctionCall: cannot find function CRMXGFSXB in AppMap on CRMXFILSXB(CRMXFUNPERM.PRW)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013488512-MP-FAT-InterFunctionCall-cannot-find-function-CRMXGFSXB-in-AppMap-on-CRMXFILSXB-CRMXFUNPERM-PRW-?source=search)**
