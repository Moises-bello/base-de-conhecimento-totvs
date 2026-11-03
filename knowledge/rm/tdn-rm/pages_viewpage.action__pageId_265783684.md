---
content_hash: 5127442e45abd31908e71b709412ff3f38af90828340156e25917cfb9380dd85
fetched_at: '2026-06-29T00:08:18.602293+00:00'
page_id: '265783684'
product: rm
source: tdn-rm
title: TVTVRW_DT_Geração_Lançamento_SQL_Customisado_ORACLE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=265783684
version: 114
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Na geração de lançamento financeiro ao utiliza um SQL para identificar os alunos é apresentado o a mensagem de não conformidade: ORA-00907: parêntese direito não encontrado.  O situação ocorre somente em base de dados ORACLE e quando o SQL customizado retorna mais de 999 alunos, no caso do cliente retornava 2843 alunos. |
| **Solução/Implementação:** | Ajuste no processo de geração de lançamento financeiro para que não seja apresentada nenhuma não conformidade ao utilizar um SQL customizado para identificar os alunos, este ajuste abrange aos clientes que utilizam base de dados ORACLE, cujo o SQL retorne mais de 999 linhas. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVTVRW |
| **Requisito (ISSUE):** | *N/A* |

divs
