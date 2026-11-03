---
article_id: 360020440031
category: Materiais - Compras (SIGACOM)
content_hash: 960084f7edf6a108675bf328b56b26a2f0d6b40ae4fc68c26c952ab0b69eed69
fetched_at: '2026-06-28T22:41:08.995252+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Lançamentos padrão
  para contabilização no Documento de Entrada. (CTBA080)
type: support-article
updated_at: '2023-07-27T15:43:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Lan%C3%A7amentos-padr%C3%A3o-para-contabiliza%C3%A7%C3%A3o-no-Documento-de-Entrada-CTBA080
---

**Dúvida**Lançamentos padrão para contabilização no Documento de Entrada.

**Ambiente**

Protheus - Compras - A partir da versão 12

**Solução**

**Processo - Documento de entrada**

|  |  |
| --- | --- |
| **Lançamento** | **Descrição** |
| **640** | **Contabilização dos Itens do Documento de Entrada - Notas Fiscais de Devolução/Beneficiamento ( Cliente ).**  Estão disponíveis as tabelas:   * Tipo de entrada e saída (SF4) * Cliente (SA1) * Produto (SB1) * Item do documento de Entrada (SD1) |
| **641** | **Contabilização do Rateio dos itens do Documento de Entrada - Notas Fiscais de Devolução/Beneficiamento ( Cliente ).**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Cliente (SA1) * Produto (SB1) * Rateio de Itens (SDE) * Item do documento de entrada (SD1)   **Observação:**  Este lançamento não impede a execução do lançamento 650. |
| **642** | **Contabilização da Devolução de Vendas no Documento de Entrada pelo Total.**  Estão disponíveis as tabelas:   * Cliente (SA1) * Cabeçalho do documento de entrada (SF1) |
| **650** | **Contabilização dos Itens do Documento de Entrada.**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto (SB1) * Item do documento de entrada (SD1) |
| **651** | **Contabilização do Rateio dos Itens do Documento de Entrada para Fornecedor.**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto (SB1) * Rateio de itens (SDE) * Item do documento de entrada (SD1)   **Observação:**  Esse lançamento não impede a execução do lançamento 650. |
| **655** | **Contabilização de Exclusão dos Itens do Documento de Entrada.**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto (SB1) * Item do documento de entrada (SD1) |
| **656** | **Contabilização da Exclusão do Rateio dos Itens do Documento de Entrada.**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto(SB1) * Item do documento de entrada (SD1) * Rateio de itens (SDE)   **Observação:**  Este lançamento não impede a execução do lançamento 651. |
| **660** | **Contabilização do Documento de Entrada pelo Total.**  Estão disponíveis as tabelas:   * Fornecedor (SA2) * Cabeçalho do documento de entrada (SF1) |
| **665** | **Contabilização de Exclusão do Documento de Entrada - Total.**  Estão disponíveis as tabelas:   * Fornecedor (SA2) * Cabeçalho do documento de entrada (SF1) |
| **950** | **Contabilização dos Itens do Documento de Entrada provenientes do Ambiente de Importação (SIGAEIC).**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto (SB1) * Item do documento de entrada (SD1)   **Observação:**  Esse lançamento pode ser executado junto ao lançamento 650. |
| **955** | **Contabilização de Exclusão dos Itens do Documento de Entrada provenientes do Ambiente de Importação (SIGAEIC).**  Estão disponíveis as tabelas:   * Tipo de Entrada e saída (SF4) * Fornecedor (SA2) * Produto (SB1) * Item do documento de entrada (SD1)  **Observação:** Esse lançamento pode ser executado junto ao lançamento 655. |

***Saiba Mais :***

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM)
