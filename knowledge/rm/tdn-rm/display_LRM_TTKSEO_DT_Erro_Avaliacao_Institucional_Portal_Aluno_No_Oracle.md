---
content_hash: c9d2d146c660b2e5d009f02eba4e1d0bbb254814ab711c57310925746d9f0e56
fetched_at: '2026-06-29T00:06:13.396047+00:00'
page_id: '208340158'
product: rm
source: tdn-rm
title: TTKSEO_DT_Erro_Avaliacao_Institucional_Portal_Aluno_No_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKSEO_DT_Erro_Avaliacao_Institucional_Portal_Aluno_No_Oracle
version: 1
---

# AVALIAÇÃO INSTITUCIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Avaliação institucional.* |
| **Situação/Requisito:** | *Erro ao acessar a avaliação institucional pelo portal do aluno. Isto ocorre somente no Oracle devido utilização de função ISNULL do SQL Server*  *na consulta que recupera os registros para a tela.* |
| **Solução/Implementação:** | *Inclusão de validação do banco (Oracle ou SQL Server) para adicionar a função de atribuição de valor nulo para o campo (ISNULL para SQL Server*  *e NVL para Oracle).* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
| **Versão Corrigida:** | **12.1.8*.* |
| **Versão Expedida:** | **12.1.8*.* |

divs
