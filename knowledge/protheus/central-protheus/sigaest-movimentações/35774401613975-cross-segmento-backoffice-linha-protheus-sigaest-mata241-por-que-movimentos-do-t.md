---
article_id: 35774401613975
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 15a4406e15692ce953d64688394e968e434b3eb29106ba25b8ae0d4228626ed6
fetched_at: '2026-06-28T22:38:56.982346+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Por que
  movimentos do tipo Devolução não gravam o campo Endereço (D3_LOCALIZ)?
type: support-article
updated_at: '2025-10-21T12:29:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35774401613975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Por-que-movimentos-do-tipo-Devolu%C3%A7%C3%A3o-n%C3%A3o-gravam-o-campo-Endere%C3%A7o-D3-LOCALIZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35774362851479) Tempo aproximado para leitura: **00:01:14 min**  
  
**Dúvida**  
Por que movimentos do tipo Devolução não gravam o campo Endereço (D3\_LOCALIZ)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Movimentos do tipo "Devolução" (ou seja, está entrando saldo no armazém), realmente não permite a inserção do endereço, pois este é feito através da sua rotina própria (Endereçamento - MATA265). Este comportamento é compreendido como correto, uma vez que o endereçamento não é feito via rotina de movimentação, mas sim via rotina de Endereçamento.  
  
A exceção fica por conta da rotina MATA261 - Transferência que permite transitar produto entre endereços, delegando o endereço destino, mas por ser uma rotina de transferência, esta é permitida a inserção do saldo no endereço de destino por meio da movimentação.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35774401613975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Por-que-movimentos-do-tipo-Devolu%C3%A7%C3%A3o-n%C3%A3o-gravam-o-campo-Endere%C3%A7o-D3-LOCALIZ)
