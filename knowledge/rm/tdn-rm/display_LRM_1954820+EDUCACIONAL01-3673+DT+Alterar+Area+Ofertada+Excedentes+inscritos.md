---
content_hash: f85227742f90660d43e0af499cba260e9441983d3609cfb7e0f10e608329ca91
fetched_at: '2026-06-29T00:08:48.837684+00:00'
page_id: '329023500'
product: rm
source: tdn-rm
title: 1954820 EDUCACIONAL01-3673 DT Alterar Area Ofertada Excedentes inscritos
type: documentation
url: https://tdn.totvs.com/display/LRM/1954820+EDUCACIONAL01-3673+DT+Alterar+Area+Ofertada+Excedentes+inscritos
version: 92
---

# INSCRIÇÃO DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Processo Seletivo |
| **Função:** | Inscrição do candidato |
| **Situação/Requisito:** | Em um determinado processo seletivo com controle de vagas, uma das áreas ofertadas tem mais candidatos inscritos que o número de vagas permitido. |
| **Solução/Implementação:** | Foi identificado que a inconsistência foi causada por uma alteração indevida na consulta sql que carrega a lista de excedentes, pois sempre ao salvar uma nova inscrição o sistema busca candidatos excedentes e altera para inscritos caso existam vagas na área de interesse que o candidato está se cadastrando, assim estava trazendo excedentes de outras áreas e alterando-os para inscrito indevidamente, foi feito o ajuste na consulta para que a busca sempre seja pela área de interesse que o candidato está se inscrevendo e a alteração de excedentes para inscritos só ocorra na área corrente do usuário. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
