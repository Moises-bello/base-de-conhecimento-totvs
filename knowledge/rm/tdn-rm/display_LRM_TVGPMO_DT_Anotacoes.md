---
content_hash: 1cf65d670571066dab2fb92383e198ad1375ca3762e47084b3bf39de3acbf781
fetched_at: '2026-06-29T00:08:16.316429+00:00'
page_id: '244936787'
product: rm
source: tdn-rm
title: TVGPMO_DT_Anotacoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TVGPMO_DT_Anotacoes
version: 101
---

# ANOTAÇÕES DE SUBORDINADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Gestão de Pessoas.* |
| **Função:** | *Anotações pessoais.* |
| **Situação/Requisito:** | Ao tentar incluir uma nova anotação pessoal em um subordinado através do portal o sistema emite a seguinte mensagem:     Ocorreu um erro buscando os valores do lookup:     The conversion of the varchar value '99997' overflowed an INT2 column. Use a larger integer column.  *.* |
| **Solução/Implementação:** | *Reajustada as consultas SQL responsáveis por listar os chefes.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TVGPMO.* |
| **Requisito (ISSUE):** | N/A |

divs
