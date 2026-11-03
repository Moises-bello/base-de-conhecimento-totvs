---
content_hash: f279d1113b3f2e84646514f82d5e52688d85c9b6cb14470569671067a7da17a9
fetched_at: '2026-06-29T00:08:27.443503+00:00'
page_id: '271412393'
product: rm
source: tdn-rm
title: 433934 MEDU-2371 DT Geração de aulas obedecendo horários cadastrados no feriado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271412393
version: 111
---

# GERAÇÃO DE AULAS OBEDECENDO HORÁRIOS CADASTRADOS NO FERIADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de Plano de Aula* |
| **Situação/Requisito:** | *Sistema não está considerando os horários cadastrados no feriado. Com isso o dia 01/03/2017 que está marcado para ser feriado até as 14:30, considera que a aula que acontecerá no dia 01/03/2017 às 19:00 também é um feriado.* |
| **Solução/Implementação:** | *Validar se o horário da aula está dentro ou não do período (hora inicial e hora final) cadastrado no feriado. Se estiver, é feriado e será DESCONSIDERADA na geração do plano de aula. Caso contrário, é uma aula normal e será CONSIDERADA para a geração do plano de aula.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
