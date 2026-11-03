---
article_id: 360046892374
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5330b51b4c3133aa23b558926b0c38bac48280f51e2a1517ffbac4413ad8f2f0
fetched_at: '2026-06-28T22:42:45.869886+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisição automática no apontamento
type: support-article
updated_at: '2021-06-04T11:11:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046892374-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%A3o-autom%C3%A1tica-no-apontamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:01 min**  
**Dúvida**Por que ao realizar apontamento de produção no **MATA250 - Produção Simples** não está requisitando o material empenhado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para que a requisição ocorra de forma automática, ou seja, ao realizar o apontamento o Sistema requisite proporcionalmente os materiais empenhos é necessário que o parâmetro **MV\_REQAUT - Verifica se o Sistema deve ou não gerar requisitado no empenho na produção A -> Gera automático, D -> Digita requisições** esteja igual a **A**.  
Se o parâmetro estiver configurado igual a **D**, a requisição não ocorrerá de forma automática. Sendo necessário realizar manualmente através das rotinas de **Estoque**, **MATA240 - Movimentação Simples** ou do **MATA241 - Movimentação Múltipla**.
