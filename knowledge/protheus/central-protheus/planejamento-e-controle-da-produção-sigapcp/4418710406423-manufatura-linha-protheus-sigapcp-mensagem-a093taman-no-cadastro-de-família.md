---
article_id: 4418710406423
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 698c44c08f948b6112c47f37729fa8194fbef9471e1f200a7e45fd52f9aa4f70
fetched_at: '2026-06-28T22:42:43.575569+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A093TAMAN no cadastro de família
type: support-article
updated_at: '2022-01-20T10:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418710406423-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A093TAMAN-no-cadastro-de-fam%C3%ADlia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No **MATA093 - Configurador de produtos**, ao tentar salvar ou mover o cursor entre as linhas do *grid* das características ocorre a mensagem **A093TAMAN - Tamanho final do código de produto com tamanho superior ao tamanho do código de produto**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem ocorre quando o tamanho do código da família preenchido no campo **BP\_BASE - Conteúdo** somado aos tamanhos de todas as características, informados no campo **BQ\_TAMANHO - Tamanho** é maior do que o tamanho do campo **B1\_COD - Código**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique o tamanho do campo **B1\_COD - Código**;  
2. No **MATA093**, ajuste o tamanho do campo **BP\_BASE** ou reveja as características e os tamanhos informados no campo **BQ\_TAMANHO** de modo que a soma desses valores seja menor ou igual ao tamanho do campo **B1\_COD.**
