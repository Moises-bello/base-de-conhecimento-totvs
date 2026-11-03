---
content_hash: 4ec787f953b14f9e9dd49520b10a8891a4360ffc7910ca44a47b261949b568b8
fetched_at: '2026-06-29T00:09:13.354882+00:00'
page_id: '419548186'
product: rm
source: tdn-rm
title: 830316 EDUCACIONAL01-827 DT Parâmetro para restrição de casas decimais no CR
  e média global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=419548186
version: 3
---

# RESTRIÇÃO DE CASAS DECIMAIS NA EXIBIÇÃO DOS VALORES DE CR E MEDIA GLOBAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Parâmetros do sistema |
| **Situação/Requisito:** | Ao incluir o valor do CR e da média global, via fórmula, o valores não obedecem uma restrição de casas decimais. |
| **Solução/Implementação:** | Para a solução do problema, foi incluso um novo parâmetro, na tela de parametrização da secretaria, a fim de restringir a quantidade de casas decimais dos campos de CR (coeficiente de rendimento) e da média global.  Parâmetro: 15.01 - Secretaria | Geral 5/7 | Casas Decimais | CR/Média global  A definição desse parâmetro irá afetar os campos:   * Coeficiente de rendimento   + Tela de histórico, no cadastro de curso/habilitação do aluno   + Tela de matrícula no período letivo do aluno   + Tela de análise curricular * Média global   + Tela de histórico, no cadastro de curso/habilitação do aluno   + Tela de análise curricular * As funções de fórmula: "***BuscaCampoCursoAluno***", "***GravaCampoPL***", "***GravaCampoCursoAluno***", também, irão refletir a quantidade de casas decimais parametrizada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
