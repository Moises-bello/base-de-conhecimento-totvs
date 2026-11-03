---
article_id: 4418619287575
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c4fe05ae83503be6b2cf03607e79ba06f55155d1e8b12c6e90e5f5d3664940d8
fetched_at: '2026-06-28T22:42:43.615735+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A680NAOSF5
type: support-article
updated_at: '2022-01-20T10:48:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418619287575-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A680NAOSF5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Ao realizar o apontamento de produção pelo **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção - PCP Mod 2** o usuário recebe a mensagem **A680NAOSF5 - Não foi encontrado o tipo de movimentação no cadastro de tipo de movimentação**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa situação ocorre quando o **TM - Tipo de movimento**, definido no parâmetro **MV\_TMPAD - Tipo de movimentação padrão para produção PCP**, não está cadastrado no **MATA230 - Tipos de movimentação**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Consulte o conteúdo do parâmetro **MV\_TMPAD**;  
2. Cadastre o **TM** no **MATA230** com o código determinado no parâmetro **MV\_TMPAD** e com o campo **F6\_TIPO - Tipo de TM** com o conteúdo **Produção**.
