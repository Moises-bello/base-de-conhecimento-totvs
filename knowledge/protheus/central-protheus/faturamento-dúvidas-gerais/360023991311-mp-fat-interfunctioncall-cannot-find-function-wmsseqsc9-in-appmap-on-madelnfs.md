---
article_id: 360023991311
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 5db887948b3e9cb52a3148e5481484fcb8790246ef14cf3fbcd148de10d045b9
fetched_at: '2026-06-28T22:38:31.283507+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function WMSSEQSC9 in AppMap on MADELNFS '
type: support-article
updated_at: '2021-04-28T15:54:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023991311-MP-FAT-InterFunctionCall-cannot-find-function-WMSSEQSC9-in-AppMap-on-MADELNFS
---

**Ocorrência**

Ao excluir a nota de saída está gerando o erro:**InterFunctionCall: cannot find function WMSSEQSC9 in AppMap on MADELNFS(MATA521.PRX) 27/12/2018 10:47:30 line : 3807**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorre devido a função **WMSSEQSC9** não ter sido encontrada no RPO.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote atualizado da rotina **WMSXEXP.PRW** (Fonte detentor da função): [**https://suporte.totvs.com/portal/p/10098/download?e=733440**](https://suporte.totvs.com/portal/p/10098/download?e=733440) ;

2. Aplique o pacote via TDS ou antigo IDE para atualização do RPO;

3. Reinicie o Smartclient  e refaça o processo de geração do documento de saída.

**Obs: Para aplicação do pacote é necessário que o analista tenha conhecimentos em estrutura Protheus, em caso de dúvidas no processe, acione a equipe de atendimento de Frame Work.**

**Sempre efetue a aplicação do pacote em ambiente de homologação para validar a atualização, e posteriormente aplique em ambiente de produção.**
