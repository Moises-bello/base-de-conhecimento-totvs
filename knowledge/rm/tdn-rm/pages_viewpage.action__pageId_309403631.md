---
content_hash: 909f152b23a7ce27dc5486f0c65763829be340a2985c6a50532183dbc27c0197
fetched_at: '2026-06-29T00:08:44.838020+00:00'
page_id: '309403631'
product: rm
source: tdn-rm
title: 1244202 EDUCACIONAL01-2887 Campo Aulas Dadas na digitação de nota e frequência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309403631
version: 92
---

# NOTAS E FALTAS POR ETAPA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Notas e faltas por etapa* |
| **Situação/Requisito:** | *Ao acessar o Menu de "Digitação de Notas e faltas por etapa e digitação de frequência diária", o sistema bloqueia a digitação das Notas mas permite a digitação das aulas dadas. Configurado acesso a campos para somente consultar a tabela SNOTAETAPA e SFREQUENCIA.* |
| **Solução/Implementação:** | Otimização do campo “Número de aulas dadas” nos menus “Digitação Frequencia diária”, “Digitação de notas e faltas por aluno” e “Digitação de notas e faltas por etapa” para obedecerem à permissão de acesso a campos do perfil do usuário, quando as tabelas SFREQUENCIA e SNOTAETAPA estão configuradas para somente consultar o campo AULASDADAS. Para a tabela SFREQUENCIA, somente será permitido alterar o campo Aulas dadas, se o usuário tiver permissão ao campo SFREQUENCIA.PRESENCA. |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
