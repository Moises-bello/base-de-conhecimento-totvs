---
content_hash: 92c7a1976ea6f77f98b03f92e302f066f1dd810de2067ae2fbf8de4bb7a05902
fetched_at: '2026-06-29T00:06:06.358918+00:00'
page_id: '201730430'
product: rm
source: tdn-rm
title: TTCPH3_DT_ERRO_Renovacao_Emprestimo_Hora_Zerada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCPH3_DT_ERRO_Renovacao_Emprestimo_Hora_Zerada
version: 1
---

# RENOVAÇÃO DE EMPRESTIMO - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS - Gestão Bibliotecária* |
| **Função:** | *Renovação de Emprestimo* |
| **Situação/Requisito:** | *Ao realizar uma renovação de empréstimo , o campo Data de Devolução deve estar no formado (DD/MM/AAAA HH:MM), o resultado que está sendo informado está no formato (DD/MM/AAAA)* |
| **Solução/Implementação:** | *Remover o trecho de código que formata a data de devolução, para permitir que as informações de hora e minutos se mantenham independemente do tipo de prazo de empréstimo selecionado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
