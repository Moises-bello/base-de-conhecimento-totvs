---
content_hash: 005a69d58bd756e35177734bc88517dd21e2360868b81c09d6c59c0778db780d
fetched_at: '2026-06-29T00:08:17.136853+00:00'
page_id: '253987349'
product: rm
source: tdn-rm
title: TVEIZT_DT_Melhoria_SQL_Executados_Matricula_Online
type: documentation
url: https://tdn.totvs.com/display/LRM/TVEIZT_DT_Melhoria_SQL_Executados_Matricula_Online
version: 114
---

# Matricula Online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Matricula Online |
| **Situação/Requisito:** | Durante o período de matricula foi gerado um log pela ferramenta sentinela para identificar os SQL mais executado e a partir deste log foi solicitado uma revisão. |
| **Solução/Implementação:** | Realizada uma revisão nos SQL apresentado no log e a maioria dos SQL já foram construídos observando as boas práticas, utilizando os índices, join executados pela FK e outros foram ajustados pontualmente através deste chamado.  Uma outra melhoria que realizamos foi a tipagem dos parâmetros do SQL, pois este ajuste evita com que a LIB realize select nas tabelas envolvidas no SQL para identificar os tipos dos parâmetros e com isso ganhamos em performance. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | TVEIZT |
| **Requisito (ISSUE):** |  |

divs
