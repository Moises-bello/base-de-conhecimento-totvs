---
content_hash: 00e673a0523ee82f8cddcf911461bbd6d3b3828ee6d2695081559e38293f92c8
fetched_at: '2026-06-29T00:08:37.691290+00:00'
page_id: '284881628'
product: rm
source: tdn-rm
title: 1068659 EDUCACIONAL01-1573 DT Datas de Início e Término do Professor na Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284881628
version: 98
---

# DATAS DE INÍCIO E TÉRMINO DO PROFESSOR NA TURMA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | T*****otvs Educacional***** |
| **Função:** | Censo da Educação Básica |
| **Situação/Requisito:** | Estamos na versão 12.1.14.167, sendo que no registro 20 temos os campos de 40 a 65 que valida se a disciplina tem professor. A data do Censo é 31/05/2017 e na preparação do arquivo é validado somente se existe o cadastro de professor e não é validado a data.  Temos casos em que não tínhamos professor na disciplina na data de referência do Censo e mesmo assim está considerando que existe professor. |
| **Solução/Implementação:** | Alteração no Censo para verificar se a data de início e término da turma do professor está de acordo com a data de referência do censo. Somente sairão no censo os professores que possuem a data de início da turma anterior ou igual a data de referência do Censo e não possuem data de término ou a data de término é superior à data de referência. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
