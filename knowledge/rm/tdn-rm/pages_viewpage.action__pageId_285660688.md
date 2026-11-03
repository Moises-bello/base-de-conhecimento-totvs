---
content_hash: 61d3cbc740290671ef8858ca5556e3bc96c18c54290c5e5b05832ddeb5afbe7f
fetched_at: '2026-06-29T00:08:38.509342+00:00'
page_id: '285660688'
product: rm
source: tdn-rm
title: 977358 MSAU-10136 DT Alteração de Especialidade no Agendamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285660688
version: 101
---

# Alteração de Especialidade no Agendamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Agenda de Atendimentos |
| **Situação:** | Ao realizar a agenda de atendimento e informar uma especialidade que não seja valida o sistema não considerava se o valor inserido era válido ou não, permitindo inserir qualquer tipo de valor no campo. |
| **Solução:** | Adicionada validação ao sair do campo Especialidade do Agendamento, que verifica se a especialidade informada é válida, para não permitir valores incorretos. |

divs
