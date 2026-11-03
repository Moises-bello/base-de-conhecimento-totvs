---
content_hash: ba0f20a75a4c85e7d1931aa291f93393962e4391f8810eeebdb3416cb444f463
fetched_at: '2026-06-29T00:08:18.605672+00:00'
page_id: '265783753'
product: rm
source: tdn-rm
title: TVTVRW_DT_Geracao_Lancamento_SQL_Customizado_ORACLE
type: documentation
url: https://tdn.totvs.com/display/LRM/TVTVRW_DT_Geracao_Lancamento_SQL_Customizado_ORACLE
version: 115
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Na geração de lançamento financeiro ao utiliza um SQL customizado para identificar os alunos é apresentado o a não conformidade: ORA-00907: parêntese direito não encontrado.  A situação ocorre somente em base de dados ORACLE e somente quando o SQL customizado retorna mais de 999 alunos, no caso do cliente retornava 2843. |
| **Solução/Implementação:** | Ajuste no processo de geração de lançamento financeiro para que não seja apresentada nenhuma não conformidade ao utilizar um SQL customizado para identificar os alunos, este ajuste abrange aos clientes que utilizam base de dados ORACLE, cujo o SQL retorne mais de 999 linhas. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVTVRW |
| **Requisito (ISSUE):** | N/A |

divs
