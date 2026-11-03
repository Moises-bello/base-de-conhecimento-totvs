---
content_hash: 0aec95b43a70d5cc3d325edc745a78d3346e1a3452e6a23fde32699847d0ccc9
fetched_at: '2026-06-29T00:06:12.667680+00:00'
page_id: '205919626'
product: rm
source: tdn-rm
title: TTJXOW_DT_Erro_Avaliacao_Institucional_Portal_Aluno_No_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJXOW_DT_Erro_Avaliacao_Institucional_Portal_Aluno_No_Oracle
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
| **Versões/Release:** | *11.82.41.* |
| **Versão Corrigida:** | *11.82.41.* |
| **Versão Expedida:** | *11.82.41.* |

divs
