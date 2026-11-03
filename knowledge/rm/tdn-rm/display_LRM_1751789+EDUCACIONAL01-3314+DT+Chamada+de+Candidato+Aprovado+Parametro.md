---
content_hash: 53efe0d54e457244a37b91ff0459d5c55a231a81e231e867dd3e30e5191327f2
fetched_at: '2026-06-29T00:08:46.670273+00:00'
page_id: '317311147'
product: rm
source: tdn-rm
title: 1751789 EDUCACIONAL01-3314 DT Chamada de Candidato Aprovado Parametro
type: documentation
url: https://tdn.totvs.com/display/LRM/1751789+EDUCACIONAL01-3314+DT+Chamada+de+Candidato+Aprovado+Parametro
version: 95
---

# CHAMADA DE CANDIDATOS APROVADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Chamada de candidatos aprovados* |
| **Situação/Requisito:** | *Foi identificado uma inconsistência na execução do processo de chamada de candidatos aprovados quando utilizado a base de dados Oracle, foi identificado que o problema em questão ocorre pois uma determinada consulta sql utiliza dois parâmetros (CODCOLIGADA e CODFILIAL) duas vezes com o mesmo nome, e assim cada parâmetro é passado duas vezes, porém o sistema identifica que o parâmetro é reutilizado na consulta e informa que estão sendo passados mais parâmetros que o esperado.* |
| **Solução/Implementação:** | *Foi feito o ajuste para que o sistema passe somente os parâmetros necessários e que serão reutilizados na consulta sql.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
