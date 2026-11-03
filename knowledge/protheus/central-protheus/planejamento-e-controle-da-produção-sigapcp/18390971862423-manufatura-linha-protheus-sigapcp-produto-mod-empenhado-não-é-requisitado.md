---
article_id: 18390971862423
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b20ff7c21c64bc11de73a4413ab4246dae772e0f8b8c13fa61913cb6a027633a
fetched_at: '2026-06-28T22:42:45.760982+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Produto MOD empenhado não é requisitado
type: support-article
updated_at: '2023-10-19T11:33:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18390971862423-Manufatura-Linha-Protheus-SIGAPCP-Produto-MOD-empenhado-n%C3%A3o-%C3%A9-requisitado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18390994810519) Tempo aproximado para leitura: **00:01:09 min****Dúvida**O produto do tipo **MOD - Mão de Obra** foi empenhado mas ao apontar a **OP  - Ordem de Produção** ele não foi requisitado  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre quando a **TM - Tipo de Movimento** usada no apontamento está com o campo **F5\_TRANMOD -  Trans Mod** tem o conteúdo **N - Não**.  
Para solucionar essa situação, realize os seguintes passos:  
**1.** Se os apontamentos são realizados pelo **SIGASFC - Chão de Fábrica**, **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2** , consulte o conteúdo do parâmetro **MV\_TMPAD - Tipo de Movimentação Padrão para Produção PCP**  
**2.** Acesse o **MATA230 - Tipos de Movimentação** e consulte essa **TM**  
**3.** Ajuste o campo **F5\_TRANMOD**, mudando seu conteúdo para **S**  
**4.** Estorne e refaça o apontamento
