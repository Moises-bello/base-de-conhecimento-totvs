---
content_hash: 50f3a10f31bc879004c011f164a461c044ced514e15c02315947b940f46c0e5b
fetched_at: '2026-06-29T00:08:36.000706+00:00'
page_id: '283401540'
product: rm
source: tdn-rm
title: EDUCACIONAL01-1431 DT Inclusao Candidato Atualizar Lista Excedentes
type: documentation
url: https://tdn.totvs.com/display/LRM/EDUCACIONAL01-1431+DT+Inclusao+Candidato+Atualizar+Lista+Excedentes
version: 102
---

# INCLUSÃO DE INSCRIÇÕES - ATUALIZAR LISTA DE EXCEDENTES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Nova inscrição* |
| **Situação/Requisito:** | *No TOTVS Processo Seletivo foi identificado que caso exista alguma inscrição excedente no processo seletivo que não se tornou inscrição e o usuário criar uma nova inscrição, o sistema não valida o excedente e permite criar um novo candidato como inscrito, não respeitando a ordem de excedentes, principalmente se for feito um cancelamento de matrícula no educacional no processo seletivo RM e não selecionar o parâmetro para atualizar a lista de excedentes.* |
| **Solução/Implementação:** | *F*oi feito um ajuste para que o sistema identifique o processo seletivo que permite excedentes e antes de incluir um novo candidato, atualize a lista de excedentes pela quantidade de vagas disponíveis e inclua este novo candidato como excedente ou até mesmo como inscrito, dependendo das vagas disponíveis.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
