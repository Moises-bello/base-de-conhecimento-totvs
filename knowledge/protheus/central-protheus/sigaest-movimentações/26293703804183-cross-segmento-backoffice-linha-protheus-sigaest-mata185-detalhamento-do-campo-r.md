---
article_id: 26293703804183
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2abd91fac56fe27ee98caec82e2da3f4b7c6629cfba2084c4c2603aa13ba708f
fetched_at: '2026-06-28T22:38:56.851418+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Detalhamento
  do campo "Reservas PV/OP"
type: support-article
updated_at: '2025-03-12T12:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26293703804183-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Detalhamento-do-campo-Reservas-PV-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26293703785239) Tempo aproximado para leitura: **00:02:41 min** **Dúvida**Como saber a que se refere os possíveis empenhos e reservas englobados no campo Reservas PV/OP da rotina de Baixa de Pré-Requisição (MATA185)?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26293663679127)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O conteúdo do campo Reservas de PV/OP é a somatória de vários campos do arquivo SB2(nQtRes) que são:

Reservas de pedidos de venda, empenhos de Solic. armazém, notas de entrada a classificar e ordem de produção (DTP não trabalha)  
   
nQAtu := SB2->B2\_QATU  
nQtRes:= SB2->B2\_RESERVA+SB2->B2\_QEMP+SB2->B2\_QEMPSA+SB2->B2\_QACLASS-If(mv\_par03==1.And.!Empty(SCP->CP\_OP),SCP->CP\_QUANT,0)  
nQtSal:= nQAtu - nQtRes  
   
SALDO ATUAL (B2\_QATU)  
RESERVAS (B2\_RESERVA)  
SOMA DE EMPENHOS NO SD4 (B2\_QEMP)  
QTDE NÃO ENDEREÇADA NA PRÉ-NOTA (B2\_QACLASS)  
EMPENHOS DE PRÉ-REQUISIÇÃO (B2\_QEMPSA)

**Como saber, da totalizado, o quanto se refere a cada empenho?**

Na rotina Cadastro do Produto - MATA010, basta pressionar o F4 em cima do produto que deseja ter mais informações de cada empenho do mesmo. Para ter mais detalhes da composição de cada empenho e reserva no F4, verifique nossa documentação deste tema: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](Cross%20Segmento%20-%20Backoffice%20(Linha%20Protheus)%20-%20SIGAEST%20-%20MATA185%20-%20Detalhamento%20do%20campo%20"Reservas%20PV/OP")
