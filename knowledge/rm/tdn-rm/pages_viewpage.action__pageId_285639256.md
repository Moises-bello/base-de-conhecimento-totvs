---
content_hash: d52ed026b6f82283af83b0bec77c3fd2d8953cb3722fa916e2cc950d8d233343
fetched_at: '2026-06-29T00:08:38.198633+00:00'
page_id: '285639256'
product: rm
source: tdn-rm
title: 960875 MSAU-10094 DT Ajuste no Formulário de Agenda de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285639256
version: 101
---

# Ajuste no Formulário de Agenda de Atendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Agenda de Atendimentos |
| **Situação:** | Ao acessar o sistema TOTVS Gestão Hospitalar no menu Atendimento/Agendamento/Agenda de Atendimentos, agendar duas consultas para o mesmo prestador, sendo que a segunda consulta deve no mesmo dia, em unidade de atendimento diferentes e os horários devem estar dentro do intervalo de ambas, nesta configuração, mesmo que  o parâmetro **Permite conflito de horários no agendamento** não estivesse ativo, o sistema permitia a inserção dos registros. |
| **Solução:** | Foram realizados ajustes no formulário, para o sistema iniba o registro de dois agendamentos dentro do mesmo intervalo de tempo com o mesmo prestador. |

divs
