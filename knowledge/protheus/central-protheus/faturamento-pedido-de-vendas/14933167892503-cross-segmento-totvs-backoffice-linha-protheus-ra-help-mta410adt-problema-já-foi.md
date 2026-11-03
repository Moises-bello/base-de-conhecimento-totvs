---
article_id: 14933167892503
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1ae89b87cd70f38b790ce9f561081950854787aa0e482128ce6941648be7a629
fetched_at: '2026-06-28T22:38:38.404467+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - RA - Help: MTA410ADT
  Problema: Já foi realizada uma baixa do Adiantamento para este pedido'
type: support-article
updated_at: '2025-01-10T20:05:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14933167892503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-RA-Help-MTA410ADT-Problema-J%C3%A1-foi-realizada-uma-baixa-do-Adiantamento-para-este-pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao realizar um Faturamento parcial com Vinculo de Recebimento Antecipado **(Adiantamento)**, e tentar desvincular o saldo para utilizar em outro Pedido ou Titulo no Financeiro(Do mesmo Cliente) é apresentado o **Help: MTA410ADT** no Faturamento e no Financeiro **Help:** **ADTXPED.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.17;

**Solução**

A mensagem é apresentada pois foi realizada a vinculação TOTAL do valor Antecipado ao Pedido de Venda e foi Faturado parcialmente, com isso o sistema realiza o vinculo do saldo restante no Pedido através da "FIE".

Conforme o Help apresentado, para utilizar o valor corretamente em outros títulos(deste Cliente), é necessário que realize a exclusão da nota fiscal para voltar o saldo e realizar a liberação correta em caso de Faturamento Parcial.

**Help:** MTA410ADT

**Problema:** Já foi realizado uma baixa do adiantamento para esse pedido. A amarração com o adiantamento não pode ser desfeita.

**Solução:**Exclua as Notas Fiscais que utilizam este adiantamento.

Caso não possa excluir a nota fiscal devido ao prazo de cancelamento, e queira usar o restante do valor do "RA", é necessário excluir os itens que não foram Faturados ou realizar a eliminação de resíduo, que o restante do saldo, pode ser usado em um novo pedido de venda, para este cliente.

[9010718 DSERFAT-17010 DT Pedido de Venda - Encerramento do PV faturado parcialmente com Adiantamento](https://tdn.totvs.com/display/public/PROT/9010718+DSERFAT-17010+DT+Pedido+de+Venda+-+Encerramento+do+PV+faturado+parcialmente+com+Adiantamento)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14933071080599)

**Saída contorno para utilizar o "RA" em um Faturamento parcial**

Ao realizar a inclusão de um Pedido de Venda que tenha RA, não vincular o mesmo no momento da inclusão, pois caso seja vinculado com o valor TOTAL, ao realizar o Faturamento parcial, o sistema vai apresentar os helps, caso queira desvincular o restante do valor em outro pedido de venda.

Aconselhamos que ao realizar a inclusão do pedido de venda, salve sem realizar o relacionamento do Adiantamento ao pedido e no momento do Faturamento parcial, informe o saldo do RA que queira usar para abater do valor deste Faturamento parcial que esta realizando.

Saiba Mais;

[9010718 DSERFAT-17010 DT Pedido de Venda - Encerramento do PV faturado parcialmente com Adiantamento](https://tdn.totvs.com/display/public/PROT/9010718+DSERFAT-17010+DT+Pedido+de+Venda+-+Encerramento+do+PV+faturado+parcialmente+com+Adiantamento)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Como vincular ou Desvincular RA no Pedido de Vendas pela Rotina MATA410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017422212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-vincular-ou-Desvincular-RA-no-Pedido-de-Vendas-pela-Rotina-MATA410)

[Webinar | MP - SIGAFAT - Adiantamento (RA) em Pedidos de Venda](https://www.youtube.com/watch?v=zXZxJ8DknQM)
