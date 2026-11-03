---
article_id: 360027352952
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7b89a5d3b8a8f56e0f167cf6d81c322573a3df5ff13fa1a6b2f6f2f8187542b9
fetched_at: '2026-06-28T22:42:47.136697+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Vários registros na tabela SD4 para
  o mesmo componente
type: support-article
updated_at: '2021-10-08T18:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027352952-Manufatura-Linha-Protheus-SIGAPCP-V%C3%A1rios-registros-na-tabela-SD4-para-o-mesmo-componente
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min****Dúvida**Por que em algumas ocasiões há mais de um registro na tabela**SD4 - Requisições empenhadas** para o mesmo componente?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o parâmetro **MV\_CONSEST - Considera estoque na geração de Ordem de Produção** está com o valor **Sim**, o Sistema verifica a disponibilidade de estoque do**PI - Produto intermediário**, reservando a quantidade disponível e abrindo uma **OP - Ordem de produção** intermediária para o saldo necessário, se houver.  
  
**Exemplo**  
Uma **OP** que necessite de 9 unidades de um **PI**, porém para esse **PI** o estoque disponível é de 7 unidades.  
Neste caso o Sistema fará um registro na **SD4** de 7 unidades e outro de 2 unidades para as quais abrirá uma **OP** intermediária para produção.
