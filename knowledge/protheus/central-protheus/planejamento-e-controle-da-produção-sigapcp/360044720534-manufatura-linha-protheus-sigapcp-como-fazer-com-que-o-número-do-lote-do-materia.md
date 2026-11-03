---
article_id: 360044720534
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a911367d7b5b0d8242f288ff1b8a1502c82b649f8bb403af48990bf71a66c8b2
fetched_at: '2026-06-28T22:42:41.996753+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como fazer com que o número do lote
  do material consumido seja preenchido na tabela SD3
type: support-article
updated_at: '2022-01-31T17:57:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044720534-Manufatura-Linha-Protheus-SIGAPCP-Como-fazer-com-que-o-n%C3%BAmero-do-lote-do-material-consumido-seja-preenchido-na-tabela-SD3
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:06 min**  
**Dúvida**Ao apontar uma **OP - Ordem de Produção** que requisitou material com controle de lote, como fazer para que o lote consumido também seja preenchido na tabela **SD3 - Movimentações internas**, nos campos **D3\_LOTECTL - Lote** e **D3\_NUMLOTE - Sub-Lote**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para que ocorra o preenchimento desses campos, é necessário que o empenho já tenha definido o lote a ser consumido, para isso verifique o conteúdo do parâmetro **Sugere Lote End a Empenhar** do **MATA650 - Ordem de Produção**, que deve estar com o conteúdo igual a **Sim**, ou pode-se fazer o ajuste manual dessa informação no empenho já gerado através das rotinas **MATA380 - Empenho Simples** e/ou **MATA381 - Empenho Múltiplo**, indicando o **Lote** e **Sub-lote**, se existir, a ser consumido.
