---
article_id: 4403743241239
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 02b07ea3ca0929d989a0778fde40979a37d0da39e703c486793bd1ac431918d7
fetched_at: '2026-06-28T22:42:45.713332+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo D3_EMISSAO no
  apontamento via MATA680 ou MATA681, SFCA310 ou SFCA316
type: support-article
updated_at: '2021-07-05T13:11:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403743241239-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-D3-EMISSAO-no-apontamento-via-MATA680-ou-MATA681-SFCA310-ou-SFCA316
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Como é preenchido o campo **D3\_Emissao - Data de emissão** quando o apontamento se dá pelo **MATA680  - Produção PCP Mod 1**, **MATA681 - Produção PCP Mod 2**, **SFCA310 - Apontamento Produção Modelo 1** ou **SFCA316 - Apontamento Produção Modelo 2**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema valida o conteúdo do parâmetro **MV\_DTAPT - Indica a data que será grava na movimentação de estoque** para determinar o preenchimento do campo **D3\_EMISSAO.**Se este parâmetro estiver com o conteúdo **1**, considerada a **data atual**, se estiver como **2** considerada a **database** do Sistema, se estiver como **3** considerada a **data inicial do apontamento** e se estiver como **4** considerada a d**ata final do apontamento**.  
Se o valor for diferente de **1**, **2**, **3** ou **4**, assumirá a **database** do Sistema.
