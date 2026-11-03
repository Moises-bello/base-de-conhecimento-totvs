---
content_hash: 508c8b2f213359330d26dd846b0a966208e47dabf47a09a3bac7fb874bf78322
fetched_at: '2026-06-29T00:09:18.140683+00:00'
page_id: '421388682'
product: rm
source: tdn-rm
title: Baixar créditos/devoluções vinculados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388682
version: 11
---

O processo de baixa de lançamentos financeiros com créditos/devoluções vinculados, permite ao usuário baixar somente o valor vinculado entre o lançamento financeiro e o lançamento financeiro de devolução ou o lançamento financeiro de crédito de adiantamento. Desta forma somente será efetuada a baixa do valor vinculado.

Campos da Tela de Baixa 

Os campos da tela de baixa de créditos/devoluções são os mesmos presentes na tela de baixa manual.

Regras da Tela de Baixa  

As regras da tela de baixa de crédito/devoluções são as mesmas presentes na tela de baixa manual.

Lançamento selecionado

Somente lançamentos que possuem vínculo(s) do tipo "Crédito de Adiantamento", "Devolução" ou "Nota de Crédito" em aberto (ainda não baixado) poderão ser selecionados para execução do processo. Para qualquer outro lançamento selecionado para execução desse processo será emitida mensagem de erro. O objetivo do processo é permitir baixas parciais do lançamento sem a necessidade de informar um valor, o que será baixado, serão os valores dos créditos/devoluções.

Valores da baixa

Para o(s) lançamento(s) baixado(s) por esse processo o Valor da Baixa será sempre zero e o Status será "Parcialmente baixado" até zerar o valor pendente para baixa, quando o Status irá assumir "Baixado". Como a baixa é zerada o campo "Valor Baixado" do lançamento não é afetado. Podem ser usados o tipo de Baixa Completa (a forma de pagamento será sempre "Dinheiro") ou a Simplificada (necessário informar a forma de pagamento). Os lançamentos do tipo "Crédito de Adiantamento", "Devolução" ou "Nota de Crédito" vinculados ao que está sendo baixado seguem as regras normais do processo de baixa.

Obs.: Em caso de baixas parciais o modo de cálculo utilizado é sempre por Prioridade independente da parametrização utilizada no sistema.

Dados do Lançamento 

Os dados dos lançamentos na tela do processo de baixa não poderão ser alterados já que o lançamento será baixado com valor zero.

Outras Baixas 

O processo poderá ser executado N vezes para o mesmo lançamento desde que após a baixa anterior, novos créditos de adiantamento tenham sido vinculados. O lançamento também poderá sofrer outras baixas do tipo "normal", e nesse caso os valores serão gerados de acordo com a regra desse tipo de baixa. 

**Processamento de Baixa com Créditos/Devoluções Vinculados**

Item de Baixa

Geração do item de baixa  
Define o valor da baixa do item de baixa igual a zero

Retenção

Calcula base de cálculo do tributo para a baixa

**Baixa Créditos/Devoluções Vinculados**

Base de cálculo do tributo menor que o valor original do lançamento financeiro e lançamento de adiantamento, onde em sua baixa, foi gerado o lançamento de crédito de adiantamento, sem tributo. O cálculo será:

(Valor do adiantamento / valor original) \* base de cálculo restante do tributo

Base de cálculo do tributo igual ou maior que o valor original do lançamento financeiro, o cálculo será:

Valor do adiantamento – Valor total do vínculo quando o lançamento de adiantamento, gerador do crédito de adiantamento, possui tributos. Caso contrário, será o valor do adiantamento.
