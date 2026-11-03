---
content_hash: 19d4fe4cc4dfa19d927a7cd08640362aef76ee4a41260b8d8bb317d12d48a795
fetched_at: '2026-06-29T00:10:50.620769+00:00'
page_id: '561869781'
product: rm
source: tdn-rm
title: Validação dos Gastos sem liberação do Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561869781
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. Exemplo com maior número de lançamentos que autorizações (diárias)
   2. Exemplo com maior número de autorizações que lançamentos (diárias)
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Se o convênio estiver parametrizado para a exigência de liberação dos gastos com (honorários, diárias, SADT, taxas / serviços e Matmed) e **caso nem todos os lançamentos possuam autorização**, não é possível encerrar a parcial, como nesse exemplo com diárias:

Mensagem: 'Número de diárias lançadas na conta do paciente superior ao número de autorizações lançadas no atendimento'.

Além disso, se o **número de autorizações é maior que o número de lançamentos** desse tipo de gasto, também não é possível encerrar a parcial:

Mensagem: 'Número de autorizações lançadas para o procedimento superior ao número de diárias lançadas na conta do paciente'.

Se o número de autorizações e lançamentos forem iguais, a parcial é encerrada sem problemas:

Para mais informações sobre o parâmetro que exige a liberação do convênio, acesse a documentação de Condições Contratuais com Convênio, na parte de Restrições do Contrato, disponível [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=531022960).

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

childrensExemplo com maior número de lançamentos que autorizações (honorários)

### **2.1 Exemplo com maior número de lançamentos que autorizações (honorários):**

Os códigos da mensagem são, respectivamente: código da especialidade, código do grupo de itens e código do item.

Exemplo com maior número de autorizações que lançamentos (honorários)

### **2.2 Exemplo com maior número de autorizações que lançamentos (honorários):**

Os códigos da mensagem são, respectivamente: código da especialidade, código do grupo de itens e código do item.

## **03. TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDTAXASERV
* SZATENDDIARIAS
* SZATENDSADT
* SZATENDMATMED
]]>
