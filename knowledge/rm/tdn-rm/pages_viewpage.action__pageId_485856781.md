---
content_hash: 85c563597ce6407fcce544d982eaf0b921cab78624df03477847992aa9f8e20e
fetched_at: '2026-06-29T00:10:20.076202+00:00'
page_id: '485856781'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Grupo de Condições"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485856781
version: 5
---

## **ÍNDICE**

1. **Visão Geral**
2. **Descrição dos Campos da****Atividade**

**01. VISÃO GERAL**

A atividade "Grupo de Condições" é uma atividade que engloba outras atividades em seqüência. As atividades dentro do grupo de condições serão executadas enquanto a sua condição de qualquer atividade do grupo for verdadeira ou até que a condição Until do grupo seja verdadeira. Essa atividade não possui propriedades, ela agrupa e executa as atividades arrastadas para dentro dela. A ordem de execução será da esquerda pra direita.

É preciso muita cautela no uso desta atividade, pois a definição incorreta das condições das atividades e/ou da condição Until do grupo poderá causar travamentos no sistema por causa de loops infinitos na execução da atividade.

**02. DESCRIÇÃO DOS CAMPOS DA ATIVIDADE**

Descrição dos campos da atividade "Grupo de Condições":

**Atividade:**

* **Name:** Nome da atividade
* **Description:** Descrição da atividade
* **Enabled:** Define se a atividade estará em uso ou não.

**Condições:**

**UntilCondition:**

* **Condição de Regra Declarativa**
  + **ConditionName:** Nome da Condição
  + **Expression:**Condição de regra a ser atribuída à condição da atividade

* **Condição de Código**
  + **Condition:** Associação da condição para a propriedade de uma atividade
