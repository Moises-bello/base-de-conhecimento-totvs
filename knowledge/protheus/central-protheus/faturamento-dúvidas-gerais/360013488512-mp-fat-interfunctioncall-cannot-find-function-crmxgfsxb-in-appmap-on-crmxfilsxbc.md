---
article_id: 360013488512
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ccab8f92d492243bc1345313a12dd0144af14262bf5f6ce9fb3582f4885b14e4
fetched_at: '2026-06-28T22:38:31.125408+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT - InterFunctionCall: cannot find function CRMXGFSXB in AppMap on CRMXFILSXB(CRMXFUNPERM.PRW)  a
  partir da 12.1.17'
type: support-article
updated_at: '2021-04-28T15:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013488512-MP-FAT-InterFunctionCall-cannot-find-function-CRMXGFSXB-in-AppMap-on-CRMXFILSXB-CRMXFUNPERM-PRW-a-partir-da-12-1-17
---

**Ocorrência**

Ao efetuar uma busca via consulta F3 no campo de cliente do pedido de venda,  inclusão de título, nota fiscal de entrada ou qualquer outra rotina que busque o cadastro de clientes, tabela SA1, gera o erro:

**InterFunctionCall: cannot find function CRMXGFSXB in AppMap on CRMXFILSXB(CRMXFUNPERM.PRW) 11/06/2018 16:51:16 line : 166**  
   
 **Ambiente**Microsiga Protheus - a partir da release 12.1.17  
   
 **Causa**O erro ocorre, devido a função **CRMXGFSXB** não estar Disponível no RPO.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Efetue o download do pacote do **CRMXFUNGEN,** de acordo com sua versão:

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=754000> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=753999> ;

2. Via IDE ou TDS, aplique o pacote em questão para atualização da rotina **CRMXFUNGEN**.

Obs: Para aplicação do pacote para atualização do RPO é desejável que seja efetuado um Backup do ambiente e conhecimentos técnicos para efetuar o procedimento.

Em caso de dúvida para aplicação do pacote, consulte a equipe de Frame Work .
