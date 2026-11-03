---
content_hash: 053c1fc335a9196682ec9b34a1c03827787aa0147cf72414aec5e9961ea615cc
fetched_at: '2026-06-29T00:08:18.099617+00:00'
page_id: '263192690'
product: rm
source: tdn-rm
title: TVUPPC_DT_Faixa_Etaria_Area_Ofertada_Validacao_Responsavel_Varios_Candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUPPC_DT_Faixa_Etaria_Area_Ofertada_Validacao_Responsavel_Varios_Candidatos
version: 110
---

# INSCRIÇÃO DE CANDIDATOS - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Inscrição de candidatos - Portal* |
| **Situação/Requisito:** | *Quando o responsável acessa o portal e tem dois ou mais candidatos vinculados para fazer inscrição, com idades diferentes e o processo seletivo utiliza faixa etária, o sistema sempre considera a idade do primeiro candidato, independente de qual candidato for selecionado, assim independente da faixa etária, impedindo a inscrição.* |
| **Solução/Implementação:** | **Foi identificado que ao tentar excluir um recurso que é utilizado no processo seletivo, o sistema não permite pois existe um outro local referenciando este recurso e mostra a mensagem não tratada, foi feito o tratamento da mensagem alertando que não é possível excluir pois o registro é utilizado em outro local.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
