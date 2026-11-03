---
content_hash: 40b194d45131bfbbeb0cee0e0f43be5a42a746ed4dca4bc7a5d34531256b56fa
fetched_at: '2026-06-29T00:06:29.476384+00:00'
page_id: '234609848'
product: rm
source: tdn-rm
title: TTOUPG_DT_Sala_Reserva_Instalacao_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOUPG_DT_Sala_Reserva_Instalacao_Portal
version: 120
---

# RESERVA DE INSTALAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Reserva de Instalação (Portal)* |
| **Situação/Requisito:** | *Ao informar os campos para reserva de instalação pelo Portal, não informar a sala e clicar em "salvar", O sistema exibe a mensagem abaixo:*  *"ORA - 12899: valor muito grande para a coluna "RM"."SRESERVAINSTALACAO"."CODSALA" (real: 13, máximo: 10)"* |
| **Solução/Implementação:** | *Ajustado comportamento do campo código sala para não tentar salvar o texto "Carregando..." na tabela.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
