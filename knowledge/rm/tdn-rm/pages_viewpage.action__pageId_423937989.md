---
content_hash: f0c9be1146bed62b0b35b300b3a5575281605113895b5fbf076c5d74462157af
fetched_at: '2026-06-29T00:09:24.669186+00:00'
page_id: '423937989'
product: rm
source: tdn-rm
title: Lançamento Financeiro por Item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937989
version: 2
---

***Atenção!***  
 Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

**Conceito**  
  
 O Parcelamento permite ao usuário gerar lançamentos financeiros personalizados a partir de dois  parâmetros: Data de Vencimento e o Valor da Parcela, que poderão ser informados manualmente ou automaticamente, usando a data de entrega do item do movimento como base para o vencimento dos lançamentos financeiros a serem gerados.  
  
**Processo**  
  
 O lançamento financeiro originado do movimento pode ser gerado de três formas:

* **Condição de Pagamento**, que consiste em um cadastro prévio das composições das parcelas;
* **Meio de Pagamento** que são as formas de pagamentos possíveis para um documento (dinheiro, cheque, cartão de débito, cartão de crédito, etc.) associado a composição de cada parcela.
* **Parcelamento** que permite a geração das parcelas de forma manual ou automática com base na data de entrega dos itens e na condição de pagamento selecionada.

**Parametrização**

Nos parâmetros de Tipo de Movimento, etapa <Fin – Condições de Pagamento>, a opção Parcelamento é utilizada para indicar a forma de operação do Parcelamento. Neste parâmetro esta disponível três opções: "Não Usa", "Usa" e "Usa com data de Entrega do Item".   
Esta ultima opção implica na utilização obrigatória do Parâmetro "Data de Entrega do item", disponível em <Item – Identificação 1 /2>.  
Na inclusão de um movimento o sistema disponibilizará a aba Integrações Financeiras, onde os dados do parcelamento serão informados, quando parametrizado:

* Parcelamento sem quebra por data de entrega do item (Parâmetro do Parcelamento = "Usa"): O usuário informa a composição das parcelas manualmente. Nesta interface será possível informar uma Condição de Pagamento para facilitar a geração das parcelas, com base na data de vencimento do lançamento financeiro. Se o usuário tiver permissão, ele poderá editar a composição das parcelas.. O valor a ratear continua sendo o valor definido na fórmula de valor a ratear dos parâmetros do tipo de movimento.

* Parcelamento com quebra por Data de Entrega do Item (Parâmetro do Parcelamento = "Usa com data de Entrega do Item"): O valor a ratear para o financeiro definido na 'Fórmula de Valor a Ratear' nos parâmetros do Tipo de Movimento deve retornar valores por item e não por movimento.. O Parcelamento poderá ser gerado automaticamente pelo sistema, gerando lançamentos financeiros para cada item, considerando como valor original o valor calculado conforme a Fórmula do Valor a Ratear e o vencimento de cada parcela com base na Data de Entrega do respectivo item de movimento.

Caso a data de vencimento da parcela de um item coincida com a data de vencimento de outro item, os valores destas serão somados e apenas uma parcela com o valor total será gerado.  
Tendo o usuário permissão, ele poderá editar a composição das parcelas geradas pelo sistema.  
**O tratamento das opções**: 'Efeito na 1ª. parcela', 'Distribuição do Valor Opcional' e 'Valor na 1ª. Parcela' não sofrem alterações quando se usa o parcelamento.
