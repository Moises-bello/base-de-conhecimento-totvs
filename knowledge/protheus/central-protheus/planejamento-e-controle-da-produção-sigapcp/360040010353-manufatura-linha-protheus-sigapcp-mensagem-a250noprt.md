---
article_id: 360040010353
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9f533407c0a4569df73961ba62f895aecb3cb3a15158d67414e0a0d99bcc987b
fetched_at: '2026-06-28T22:42:43.588448+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A250NOPRT
type: support-article
updated_at: '2022-02-16T18:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040010353-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A250NOPRT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:45 min**  
 **Ocorrência**Ao tentar realizar um apontamento de uma **OP - Ordem de Produção** através da rotina **MATA250 - Produção Simples** a mensagem **A250NOPRT** é apresentada.   
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
 **Causa**Essa mensagem é apresentada quando se tenta apontar uma **OP** indicada como **Total**, porém o Sistema encontra registros de requisição com data posterior ao do apontamento em questão.  
  
 **Solução**Para solucionar essa situação avalie se as requisições registradas estão com data superior ao do apontamento que está sendo realizado, por meio do campo **D3\_EMISSAO - Data de Emissão**.
