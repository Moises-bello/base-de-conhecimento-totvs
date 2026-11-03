---
content_hash: 3d03e6ffc0dbb1a8ffda024e15ca530dd28de63a2d004395225d88f05e1c4cee
fetched_at: '2026-06-29T00:11:12.638113+00:00'
page_id: '655883912'
product: rm
source: tdn-rm
title: Folha de Pagamento - Gerar integração com Backoffice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655883912
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Após gerar a folha de pagamento é possível integrá-la com o BackOffice, informando o tipo de movimento, a condição de pagamento e dependendo do BackOffice, a natureza financeira.

Com isso, pode ser gerado um lançamento financeiro a pagar.

## **02. EXEMPLO DE UTILIZAÇÃO**

O tipo de movimento é preenchido com a seguinte regra:

* **Se o valor líquido for positivo**:
  + Se o prestador é pessoal física:
    - Movimento a pagar
  + Se o prestador for pessoa jurídica
    - Movimento a pagar
* **Se o valor líquido for negativo:**
  + Se o prestador for pessoa jurídica
    - Movimento a receber
  + Se o prestador é pessoal física:
    - Movimento a receber

## **03.****TABELAS UTILIZADAS**

* SZFOLHAPAGTOPREST
