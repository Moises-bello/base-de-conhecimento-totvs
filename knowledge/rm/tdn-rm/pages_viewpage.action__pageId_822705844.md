---
content_hash: 982b2c38443eb5a135fdc9de7dda2d92833f452dbbe3b1bf6d1d897746f23a85
fetched_at: '2026-06-29T00:11:46.593816+00:00'
page_id: '822705844'
product: rm
source: tdn-rm
title: Integração Fluxo de Aprovação com TAA - Faturamento direto - Portal de Medições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822705844
version: 7
---

Para habilitar a integração do TAA (TOTVS Aprovações e atendimentos) com o Faturamento Direto é necessário habilitar o seguinte parâmetro:

Menu: Integração → TOTVS Aprovações e atendimentos

**Status para Aprovação:**

Status que indica que o Workflow foi aprovado no TAA.

**Status para Reprovação:**

Status que indica que o Workflow foi reprovado no TAA.

**Tipo do Contrato:**

Define o tipo de contrato que devem ser aprovados via Workflow de aprovação:

* Ambos
* A Pagar
* A Receber

**Tipo do Atendimento:**

Workflow de aprovação criado no TAA para aprovar ou reprovar o pedido de faturamento direto.

Exemplo:

**Etapa "Aprovado" do Workflow:**

**Ação a ser realizada nessa etapa:**

Deve ser configurado o mesmo status configurado nos parâmetros de projeto "Status para aprovação".

E para a etapa "reprovada" deve ser configurado o mesmo status configurado nos parâmetros de projeto "Status para reprovação".

**Observação:**

É necessário agendar o  para que o status dos pedidos de faturamento direto sejam aprovados ou reprovados no portal de medição do fornecedor após a aprovação ou reprovação do Workflow no TAA.

Ao habilitar a integração do Faturamento Direto com TAA, devem aparecer os 2 processos na visão de pedido de faturamento direto do contrato:

* **Gerar Workflow de Aprovação**
  + Será criado um atendimento de aprovação no TAA vinculado ao pedido de faturamento direto.
* **Cancelar Workflow de Aprovação**
  + Será excluído o atendimento de aprovação no TAA vinculado ao pedido de faturamento direto.

O pedido de faturamento direto só poderá ser enviado para Suprimentos/Faturamento caso o atendimento seja "aprovado" no TAA.

**Observação:**

* Caso a integração do Faturamento Direto não esteja habilitada no projeto, ao arrastar o pedido de faturamento direto para a coluna "em aprovação", o sistema deverá aprovar automaticamente o pedido de faturamento direto.
* No portal de medição, o usuário poderá arrastar o pedido de faturamento "aprovado" para a coluna "pedido entregue".
* Caso o atendimento associado ao pedido de faturamento direto seja "aprovado", o pedido deverá estar na coluna "aprovado" (após a execução agendada do processo de atualização de histórico do contrato).
* Caso o atendimento associado ao pedido de faturamento direto seja "reprovado", o pedido deverá estar na coluna "reprovado" (após a execução agendada do processo de atualização de histórico do contrato).
