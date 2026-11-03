---
article_id: 4414744933911
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1a57f1cd175d716886951d9c964cb1662f98502bdb7aa4ff1800d61f49cf4cae
fetched_at: '2026-06-28T22:42:42.197450+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Diferenças entre as tabelas SD3 e a
  SH6
type: support-article
updated_at: '2022-01-06T17:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414744933911-Manufatura-Linha-Protheus-SIGAPCP-Diferen%C3%A7as-entre-as-tabelas-SD3-e-a-SH6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:11 min** **Dúvida**Qual a diferença entre as tabelas **SD3 - Movimentações Internas**, **SH6 - Movimentações da Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Na tabela **SH6** são registrados todos os movimentos com operações realizadas através das rotinas **MATA681 - Produção PCP Mod2** e **MATA680 - Produção PCP Mod1**.  
Já na tabela **SD3** são registrados todos os movimentos de produção e requisição realizadas através de algumas rotinas. Então sempre que realizar o apontamento de produção através do **MATA250 - Produção Simples** é gravado o movimento na tabela **SD3**e também quando realizado apontamento através das rotinas **MATA681** e **MATA680** e houver requisição ou produção de um produto.  
  
**Importante**  
Também há outras rotinas que geram movimentações na tabela **SD3**, porém o exemplo dado acima é para mostrar a diferença entre as tabelas.
