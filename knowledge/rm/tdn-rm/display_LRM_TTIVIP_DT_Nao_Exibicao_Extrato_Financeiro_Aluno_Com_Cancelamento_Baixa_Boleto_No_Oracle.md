---
content_hash: ec7efb0546409087d3bf2e5eeabab54ddcbf7013762ec3ca4e4490d5d202fff3
fetched_at: '2026-06-29T00:06:12.539731+00:00'
page_id: '205917554'
product: rm
source: tdn-rm
title: TTIVIP_DT_Nao_Exibicao_Extrato_Financeiro_Aluno_Com_Cancelamento_Baixa_Boleto_No_Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIVIP_DT_Nao_Exibicao_Extrato_Financeiro_Aluno_Com_Cancelamento_Baixa_Boleto_No_Oracle
version: 1
---

# EXTRATO FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Extrato financeiro.* |
| **Situação/Requisito:** | *Não exibição de extrato financeiro do aluno quando há boletos com baixas canceladas no Oracle. Isto ocorre devido inconsistência na consulta*  *que recupera os boletos, fazendo com que traga também o registro da baixa cancelada.* |
| **Solução/Implementação:** | *Adicionar o filtro "AND FLANBAIXA.STATUS <> 1" no JOIN com a tabela FLANBAIXA. Com isto, os registros virão filtrados e não será mais*  *necessária a utilização da função agregada MAX para SQL Server, bem como o GROUP BY para SQL Server e Oracle.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.40.* |
| **Versão Corrigida:** | *11.82.40.* |
| **Versão Expedida:** | *11.82.40.* |

divs
