---
content_hash: 00ec277112d4ea347bf26c331033ae9b018d22f9f74dfaef98d070386426d6fa
fetched_at: '2026-06-29T00:11:36.887788+00:00'
page_id: '773518860'
product: rm
source: tdn-rm
title: TCGI - Comissão - Desconto Comissão na Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518860
version: 4
---

### Regras para Comissão de Clientes e Financiamento

1. **Desconto da Comissão no Financiamento**

   * Quando um cliente paga comissão sobre uma venda, esse valor será descontado do total da venda, do item da venda e dividido entre as partes do financiamento (entrada, principal, etc.).
   * Antes de gerar o plano de financiamento, a comissão deve estar cadastrada, pois o desconto será aplicado nesse momento.
2. **Edição da Comissão**

   * Após o desconto da comissão no financiamento, a edição não será mais permitida, desde que a comissão tenha sido paga pelo cliente.
   * Se não houver esse tipo de comissão, a edição será liberada, pois nesse caso a empresa paga a comissão e isso não altera o valor da venda.
3. **Exclusão do Financiamento**

   * Se o financiamento for excluído, o desconto da comissão será desfeito no valor da venda, no item da venda e nas regras do financiamento.
   * Isso garante que o sistema esteja sempre sincronizado e sem falhas.
4. **Regras para o Tipo de Cálculo da Comissão**

   * Todos os comissionados devem seguir um único tipo de cálculo: **desconto decrescente, proporcional ou parcelas iguais**.
   * Não será permitido alterar o tipo de cálculo do cliente ou quais componentes serão descontados na tela do PVI.
   * Esse cálculo deve ser definido previamente conforme as regras da empresa, sem intervenção do corretor.

Formas de cálculo de desconto da comissão paga pelo cliente com o seguinte exemplo:

* Tenho no plano dois componentes:
  + Entrada: Valor : R$5.000,00 em 5X = R$1000,00 por parcela; - Prioridade 1 (modelo de cálculo)
  + Mensal Valor: R$ 100.000,00 em 50X = R$2.000,00 por parcela;  - Prioridade 2
  + Valor Comissão pagamento cliente: R$8.000,00

1. Decrescente: Determina a prioridade dos componentes geradores de parcelas para realizar o pagamento da comissão;
   * O sistema terá que  descontar R$8.000,00, sendo:
     + 5000 da entrada, ou seja, não terá entrada no plano
     + 3000 do mensal, pois usei a prioridade definida no castrado do modelo de cálculo
2. Parcelas Iguais: Determina que valor da comissão será descontado na forma proporcional de cada componente sobre o valor total;
   * O sistema terá que  descontar R$8.000,00, sendo que o total de parcelas é 50 + 5 = 55:
     + entrada são 5 parcelas: 5 /55 \*   R$8.000,00 = R$727,28
     + mensal  são 50 parcelas: 50 /55 \*   R$8.000,00 = R$7272,72
3. Proporcional: Determina que valor da comissão será descontado na forma proporcional de cada componente sobre o valor total
   * O sistema terá que  descontar R$8.000,00, sendo que o total  do plano é 5.000+100.000 = 105.000:
     + entrada com valor de 5.000:  5000/105.000 \*   R$8.000,00 = R$400,00
     + mensal  com valor de 100.000 parcelas: 100000/105.000 \*  R$8.000,00 = R$7.600,00
