---
content_hash: 2408b1c455cc636c2cdbcf3690753b011935bc1856760718f9f576a02e84c49f
fetched_at: '2026-06-29T00:09:16.294558+00:00'
page_id: '421385506'
product: rm
source: tdn-rm
title: Rastrear Movimentos do Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/Rastrear+Movimentos+do+Estoque
version: 4
---

Esta funcionalidade de rastreabilidade permite o acompanhamento do desdobramento de um movimento gerado no BackOffice a partir do Totvs Obras e Projetos.

**Passos:**

Após a execução do processo "Gerar integração com Suprimento e Faturamento", gerando um movimento é possível rastrear o movimento clicando no processo do anexo de período de contrato "Rastrear Movimentos do Estoque".

**Exemplo:**

Quando uma SA (Solicitação de Armazém) é gerada a partir do TOP esta pode gerar uma BX (Baixa de Estoque) ou SC's (Solicitação de Compra) que por sua vez podem gerar COT (Cotação) um PC (Pedido de Compra) e por fim uma NF (Nota Fiscal).

 O Totvs Obras e Projetos possui a funcionalidade de rastreabilidade disponível em três dos seus módulos:

**Contratos**

No módulo de contrato a rastreabilidade está disponível no menu "Rastrear Movimentos do Estoque" e pode ser feita a partir de PC's (Pedidos de Compra) ou PV's (Pedidos de Venda) gerados pelas rotinas "Gerar integração com o suprimento/faturamento" e "Liberação de Retenção" onde são liberados os períodos medidos ou de insumos liberados e as retenções respectivamente.

**Requisição de Materiais**

No módulo de Requisição a rastreabilidade está disponível através do menu Anexos> Movimento e pode ser feita a partir de PC's (Pedidos de Compra),  SA's (Solicitações de Armazém) ou SC's (Solicitações de Compra).

**Requisição Extra**

No módulo de Requisição Extra a rastreabilidade está disponível através do menu Anexos> Movimento e pode ser feita a partir de PCs (Pedidos de Compra),  SAs (Solicitações de Armazém) ou SCs (Solicitações de Compra) gerados pela rotina "Rastreamento de Movimentos".

Obs.

 A exibição da rastreabilidade de um movimento será feita através de um diagrama onde cada entidade representara um movimento. Selecionando um movimento, no diagrama, serão exibidas as demais informações do mesmo de acordo com o tipo de movimento selecionado.
