---
content_hash: 71eb584996bf1e0bc036b88cb7c1eefe785a0a7feb40d000452e97f618316736
fetched_at: '2026-06-29T00:09:11.648936+00:00'
page_id: '415105210'
product: rm
source: tdn-rm
title: 3812335 EDUCACIONAL01-6430 DT Impressão de relatório da análise curricular
  com entrada de parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415105210
version: 2
---

# IMPRESSÃO RELATÓRIO COM ENTRADA DE PARÂMETROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Impressão de relatório com entrada de parâmetros |
| **Situação/Requisito:** | Ao utilizar um relatório customizado o sistema não apresenta a tela de entrada de parâmetros |
| **Solução/Implementação:** | Foi realizado um tratamento no sistema para que seja apresentada a tela de entrada de valores, caso o relatório não tenha como parâmetros de entrada:   * Código da coligada - CODCOLIGADA\_N * Id. matriz aplicada - IDHABILITACAOFILIAL\_N * RA do aluno - RADE\_S * RA do aluno - RAATE\_S * Código da filial - CODFILIAL\_N * Código do tipo de curso - CODTIPOCURSO\_N   Esses parâmetros são disponibilizados quando é utilizado o provider da análise curricular.  Caso seja identificado que o relatório tenha os parâmetros citados, o sistema irá passar os valores em segundo plano e será executado sem a exibição da tela de entrada de valores. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
