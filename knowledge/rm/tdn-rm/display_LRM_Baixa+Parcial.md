---
content_hash: 3de74131242dfa30ad99587a9688ad359b57d87f5f42e0c530ac04a37a522831
fetched_at: '2026-06-29T00:09:18.130482+00:00'
page_id: '421388678'
product: rm
source: tdn-rm
title: Baixa Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+Parcial
version: 5
---

Ao baixar um Lançamento parcialmente, não será gerado um novo lançamento com o valor pendente de pagamento ou recebimento. O valor quitado parcialmente ficará registrado como Item de Baixa(Anexos/Baixas do Lançamento). O valor original do lançamento não será alterado. O valor líquido do Lançamento será recalculado considerando o valor original, os acréscimos, os descontos iniciais e o valor baixado parcialmente.   
No processo de baixa parcial:

* Não será gerado lançamento com a diferença do valor; . Você poderá usar "N" meios de pagamento; . Cada valor baixado fica gravado no lançamento de origem; . O lançamento fica com o status de baixado parcialmente; . O processo de baixa poderá ser executado novamente para a diferença; . Não tem limites para a quantidade de baixas parciais  de um lançamento.

Aplicar Desconto Total

A opção Aplicar Desconto Total, somente será habilitada caso o parâmetro de baixa por proporcionalização estiver selecionada em Contas à pagar/receber| Baixas | Manutenção de baixa | Baixa 3/5;  
Na baixa parcial do lançamento financeiro, ao marcar a opção "Aplicar desconto Total", o sistema aplica o valor total do desconto informado no lançamento, independente se o sistema está parametrizado para baixa por proporcionalização.

**Observações**:

Os lançamentos criados por prioridade, ao realizar a baixa parcial do lançamento, a opção "Aplicar desconto Total" não será exibida.

Cálculo dos valores proporcionais dos campos opcionais, com a opção Aplicar desconto Total marcada:  (Valor do campo \* (Valor Baixado + Valor do desconto)) / (Valor original + (Valor Opcional Acrescentar – Valor opcional a Descontar)

Cálculo dos valores proporcionais de todos campos, com a opção Aplicar desconto Total desmarcada:   
Calculo da proporcionalidade = (Valor do campo \* Valor Baixado) /valor líquido.

Com a opção selecionada, ao realizar a alteração do valor do desconto na baixa, automaticamente o cálculo será feito sobre o valor informado no campo "Desconto" e o restante do valor será desconsiderado, caso o valor seja à menor.

**Base de Cálculo dos Tributos**

Este campo ficará  disponível quando o parâmetro, "[Informar base de cálculo dos tributos de lançamentos a pagar](http://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)", for marcado.

No processo de Baixa será permitido informar o valor base que será utilizado no cálculo dos tributos do lançamento para geração de tributos. Informando o valor base o sistema realiza o cálculo dos tributos Pis, Cofins e Csll, considerando o valor informado no campo, caso contrário considera o valor da baixa"

**Observação**:

Se este parâmetro estiver marcado e o usuário não informar a base de cálculo,  o sistema fará o cálculo já existente.
