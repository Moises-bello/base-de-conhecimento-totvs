---
content_hash: b3130edc150c0130c6adc5a16575c0d990ff4c8ae0c87b3bf95c88844995b4a6
fetched_at: '2026-06-29T00:08:54.893221+00:00'
page_id: '347444027'
product: rm
source: tdn-rm
title: 2039440 FINANCEIRO01-5055 DT Geração de Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=347444027
version: 1
---

# Geração de Acordo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Geração e Acordo |
| **Situação/Requisito:** | Na tela de geração do Acordo, existe uma inconsistência no preenchimento do campo Opções de Acordo, onde se informa o Template desejado para a operação. O usuário digita o código do template e tecla Enter ou TAB, mas o sistema não acata a informação. É preciso que o usuário clique no lookup do campo e navegue entre a lista de templates possíveis |
| **Solução/Implementação:** | Foi feito tratamento para que no lookup do template de acordo, permita que ao digitar o primeiro caractere seja feito a busca do registro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2039440 |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-5055> |
| **Documento de Referência:** | N/A |
