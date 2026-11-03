---
content_hash: 1b4b1b3962c1a0bef9e6ea2810fedc26ef22a52e946fb84463408514b63b7355
fetched_at: '2026-06-29T00:12:15.258676+00:00'
page_id: '974806729'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Exemplo - Hierarquias de Centro
  de Custo para Itens de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=974806729
version: 2
---

# **Exemplo dos Agrupamentos de Cliente/Fornecedor e Centro de Custo de Itens de Cobrança**

## **Objetivo**

O objetivo é apresentar diferentes níveis de detalhamento para a consolidação de valores relacionados a clientes/fornecedores, (geração de lançamentos) seus itens de cobrança, bem como subunidades e tipos de cálculos.  
Os agrupamentos permitem analisar desde um panorama geral até um nível mais granular, facilitando a tomada de decisões e o rastreamento de informações financeiras.

---

## **1. Agrupamento por Cliente/Fornecedor e Item de Cobrança**

**Descrição:**  
Neste nível, os dados são consolidados apenas pelos campos:

* **Cliente/Fornecedor**
* **Item de Cobrança**

**Características:**

* Agrupa todos os valores de cada item de cobrança para um determinado cliente.
* Não há distinção por subunidade ou tipo de cálculo.
* É o nível mais simples de visualização, focado no valor agregado por cliente e item de cobrança.

**Exemplo:**

| Cliente | Item de Cobrança | Valor |
| --- | --- | --- |
| C273 | 1 | R$ 21.732,01 |
| C273 | 4 | R$ 6.248,00 |
| C231 | 1 | R$ 25.000,00 |
| C231 | 4 | R$ 4.544,00 |

## **2. Agrupamento por Cliente/Fornecedor, Subunidade e Item de Cobrança**

**Descrição:**  
Neste nível, os dados são consolidados pelos campos:

* **Cliente/Fornecedor**
* **Subunidade**
* **Item de Cobrança**

**Características:**

* Permite detalhar o valor por subunidade, rastreando a origem do contrato.
* Mantém a separação por item de cobrança.
* Útil para identificar quais subunidades geram maior custo ou receita.

**Exemplo:**

| Cliente | Subunidade | Item de Cobrança | Valor |
| --- | --- | --- | --- |
| C273 | LUC 02 | 1 | R$ 15.000,00 |
| C273 | LUC 02 | 4 | R$ 1.704,00 |
| C273 | LUC 03 | 1 | R$ 6.732,01 |
| C273 | LUC 03 | 4 | R$ 4.544,00 |
| C231 | LUC 04 | 1 | R$ 25.000,00 |
| C231 | LUC 04 | 4 | R$ 4.544,00 |

## **3. Agrupamento por Cliente/Fornecedor, Subunidade, Cálculo e Item de Cobrança**

**Descrição:**  
Neste nível, os dados são consolidados pelos campos:

* **Cliente/Fornecedor**
* **Subunidade**
* **Cálculo**
* **Item de Cobrança**

**Características:**

* É o agrupamento mais detalhado.
* Mostra não apenas de qual subunidade vem o valor, mas também o **tipo de cálculo** (Por exemplo: Orçamento, Cobranças Diretas ou Consumos)
* Permite análises mais precisas sobre a composição do valor.

**Exemplo:**

| Cliente | Subunidade | Cálculo | Item de Cobrança | Valor |
| --- | --- | --- | --- | --- |
| C273 | LUC 02 | ORÇAMENTO | 1 | R$ 15.000,00 |
| C273 | LUC 02 | CONSUMO (MEDIÇÕES) | 4 | R$ 1.704,00 |
| C273 | LUC 03 | ORÇAMENTO | 1 | R$ 6.732,01 |
| C273 | LUC 03 | CONSUMO (MEDIÇÕES) | 4 | R$ 4.544,00 |
| C231 | LUC 04 | ORÇAMENTO | 1 | R$ 25.000,00 |
| C231 | LUC 04 | CONSUMO (MEDIÇÕES) | 4 | R$ 4.544,00 |

## **Considerações Gerais**

* **Consistência dos Totais:** Em todos os agrupamentos, o valor total final (R$ 57.524,01) se mantém, pois apenas a forma de distribuição dos valores muda.
* **Uso prático:**

  + **1º agrupamento:** relatórios gerenciais rápidos.
  + **2º agrupamento:** análise de performance por subunidade.
  + **3º agrupamento:** auditorias e rastreamento detalhado dos cálculos.
