---
article_id: 360020029891
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d8ead40f322a4a66a9ddd2c784e0df9302d46706780df2fb47495c8fc40b88b3
fetched_at: '2026-06-28T22:38:31.250669+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-InterFunctionCall- cannot find function ATUINFOFRT in AppMap on A512MANUT
type: support-article
updated_at: '2021-04-28T15:55:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020029891-MP-FAT-InterFunctionCall-cannot-find-function-ATUINFOFRT-in-AppMap-on-A512MANUT
---

**Ocorrência**

O sistema passou a apresentar error.log na rotina Expedição/Manutenção no módulo faturamento(MATA512): **InterFunctionCall: cannot find function ATUINFOFRT in AppMap on A512MANUT(MATA512.PRW) 09/03/2018 09:24:00 line : 216**  
  
   
 **Ambiente**

Microsiga Protheus- a partir da versão 12.  
   
 **Causa**

O  RPO não possui a função **AtuInfoFrt** que o **mata512** está chamando no momento de utilizar a rotina.

**Solução**

Para solucionar o problema:

1-Baixe o pacote do portal de cliente: **[PACOTE\_DE\_CORRECAO\_3017518\_DLOGGFE-5297\_12.1.17.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=695087);**

2- Aplique o pacote via TDS ou Ide antigo para atualização do RPO.

3- Reinicie o smartclient e efetue o processo novamente.

Obs... Os procedimentos devem ser realizados por uma analista com conhecimento de estrutura Protheus.

Sempre efetuar os procedimentos primeiro em base de homologação para validar e posteriormente, aplique em base de produção.
