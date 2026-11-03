---
content_hash: 044fcf7164f86932844b146a0ec2a92df7e43efc9b35ff6c7559da74130d9cd9
fetched_at: '2026-06-29T00:09:25.462287+00:00'
page_id: '423938158'
product: rm
source: tdn-rm
title: Faturamento / Recebimento do Item de Movimento (Integração Gestão de Construção
  e Projetos x Gestão de Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938158
version: 9
---

O Faturamento / Recebimento é um processo que permite avançar uma solicitação de compra ou de cotação e assim permitir que uma Compra seja realmente efetivada. Uma requisição de materiais chega ao TOTVS Gestão de Estoque, Compras e Faturamento como uma Solicitação de Compra ou solicitação de Cotação.   
A Solicitação de Compras deverá ser faturado para um movimento de Pedido de Compra e uma Solicitação de Cotação poderá ser faturado para um movimento de Solicitação de Compras , ou diretamente para um Pedido de Compras.   
O novo movimento gerado, se estiver parametrizado para fazer apropriação, incluirá o valor dos itens faturados no cronograma da tarefa.

**Pré-Condições**

Ter incluído o tipo de movimento para Pedido de Compra  
**Passo 1**- Selecione o movimento de Solicitação de Compras ou Solicitação de Cotação e acesse: Processos/ Faturar-Receber   
**Passo 2**- Selecione o movimento criado para Pedido de Compra e clique em [Executar]   
**Passo 3**- Preencha os campos do Pedido e acesse a aba [Itens].   
**Passo 4**- A quantidade do pedido é a mesma que foi informada na Solicitação de Compra ou de Cotação. Clique em [Ok]

* Se deseja Faturar parcialmente informe uma quantidade menor.
* Se esta ação for feita o sistema executará um faturamento parcial e permitirá ao usuário faturar novamente a Solicitação de Compras ou de Cotação para receber o restante dos materiais, ou então será possível Estornar os Itens não Recebidos.
* Se deseja fazer um faturamento total, a quantidade do item não deve ser alterada.

***Observação***: A alteração da quantidade dos itens no Pedido de Compra não gera estorno, pois o mesmo é gerado apenas se a quantidade for alterada nas   
Solicitações de Compra ou de Cotação.

**Passo 5**- Selecione o projeto e acesse: Projetos/ Construção e Projetos/ Planejamento/ Cronograma/ Planilha de Atividades.   
**Passo 6**- Clique sobre a tarefa qual a solicitação pertencia para visualizar a apropriação do valor do Pedido de Compras.
