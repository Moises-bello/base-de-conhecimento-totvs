---
article_id: 15317983680023
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 272e831523610957027b3090c29f19a20632f3b13e0f8d7cdac09d263285fa2e
fetched_at: '2026-06-28T22:38:54.327959+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - B8_EMPENHO - Quais
  movimentações atualizam/estornam o campo B8_EMPENHO?
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15317983680023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-B8-EMPENHO-Quais-movimenta%C3%A7%C3%B5es-atualizam-estornam-o-campo-B8-EMPENHO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15318029077911) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Quais as movimentações que atualizam o campo ***Empenho do Lote** **(B8\_EMPENHO)***?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O campo ***Empenho do Lote (B8\_EMPENHO)*** é atualizado juntamente com o campo **B2\_QEMP**, nas seguintes situações:   
   
**- Empenhos a partir de Ordens de Produção (OP's),**

**- Lote vencido (tabela SDD). Conferir pelo relatório MATR425.**

**- Na rotina Solicitação de transferência (MATA311) ainda não efetivada.**

**- Ao incluir um Pedido de Venda informando o Lote e efetuar a reserva (B2\_RESERVA).**

[- Clique aqui e veja a FAQ dos Saldos em Estoque da Consulta F4.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto-?source=search)

Para remover o empenho do deferido lote, dependerá do processo que originou o empenho. Por exemplo, no caso do Empenho a partir de Ordem de Produção, este empenho deixará de existir quando o saldo empenhado for consumido na Produção ou caso o operador desista e estorne esta Ordem de Operação. Já no caso do Lote Vencido, o que tira o empenho é se houver uma [Manutenção de Lote (MATA390)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030246893-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes) que deixe o lote com uma data de validade que ainda não foi atingida.

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
