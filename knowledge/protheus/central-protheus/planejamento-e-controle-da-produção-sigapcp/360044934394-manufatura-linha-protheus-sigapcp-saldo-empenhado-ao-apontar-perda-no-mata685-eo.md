---
article_id: 360044934394
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4724add2aaa7c8b7a911a031f7e889f44004f688976ca4fd8da3978ac2c147a6
fetched_at: '2026-06-28T22:42:45.921181+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Saldo empenhado ao apontar perda no
  MATA685 e/ou Classificação de Perda
type: support-article
updated_at: '2021-07-29T13:39:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044934394-Manufatura-Linha-Protheus-SIGAPCP-Saldo-empenhado-ao-apontar-perda-no-MATA685-e-ou-Classifica%C3%A7%C3%A3o-de-Perda
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Ao realizar o apontamento de perda através do **Classificação de Perda** e/ou **MATA685 - Apontamento de Perda** o Sistema baixa o saldo empenhado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O Sistema não baixa o saldo empenhado ao realizar o apontamento de perda através do **MATA685** ou ao informar a perda na tela de **Classificação de Perda**.  
  
O comportamento do Sistema é:

* Se tiver uma quantidade empenhada com lote e ainda tiver saldo disponível no lote o Sistema baixa desse saldo excedente e não atualiza nenhuma informação no empenho.
* Se o saldo do produto estiver todo empenhado no lote, ao realizar o apontamento de perda, o Sistema quebra o empenho em duas linhas, uma com a quantidade perdida, deixando esse saldo empenhado sem o lote, e o restante do saldo empenhado na outra linha com o lote.
