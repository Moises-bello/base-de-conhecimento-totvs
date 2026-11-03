---
content_hash: d954aebd61030725ed7a37338e2b48fd8972740518975cac17e85506edb06fc7
fetched_at: '2026-06-29T00:09:01.555164+00:00'
page_id: '373491969'
product: rm
source: tdn-rm
title: 2759486 FISCAL01-4606 DT Escrituração - Lançamento com ICMS Diferido e IPI
  Tributado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=373491969
version: 1
---

# Escrituração - Lançamento com ICMS Diferido e IPI Tributado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Escrituração - Lançamento com ICMS Diferido e IPI Tributado |
| **Situação/Requisito:** | Ao realizar a escrituração de um determinado movimento é apresentando o seguinte erro:  Erro na Inclusão do Registro: Documento 00144264 - Série 4 - Data 24/04/2018 - Parcela 2:  Deduções (Materiais/Sub-Empreitada) não poderão ser maiores que Valor Contábil. |
| **Solução/Implementação:** | Foi modificado o processo que calcula o valor contábil das parcelas para não apresentar problema de fechamento de valores. |
