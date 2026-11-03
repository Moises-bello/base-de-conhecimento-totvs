---
content_hash: eb1ca31e851ed64e6dc14b955976dd6940c5e709b6a48c6a33f6a58201f137c8
fetched_at: '2026-06-29T00:09:00.886702+00:00'
page_id: '370607715'
product: rm
source: tdn-rm
title: 734973 FINANCEIRO01-3307 DT Baixa de lançamentos com retenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370607715
version: 2
---

# Baixa de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de lançamento com retenção |
| **Situação/Requisito:** | Na baixa parcial de um lançamento que tem retenção, cuja a base de calculo seja maior que o valor original, sistema aplica o percentual (4,65) sobre o valor baixado, e quando é efetuada a ultima baixa, o valor da retenção fica maior que o valor baixado. |
| **Solução/Implementação:** | Nas situações em que a base de cálculo utilizada para a retenção dos tributos (PIS, COFINS e CSLL) for maior que o valor original do lançamento financeiro, o cálculo utilizado nas baixas parciais segue a lógica abaixo:   * O valor da baixa parcial informada pelo usuário será dividida pelo valor líquido disponível do lançamento (valor líquido disponível já considera a retenção total). * O resultado da divisão será multiplicado pelo valor total da retenção |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-3307> |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
