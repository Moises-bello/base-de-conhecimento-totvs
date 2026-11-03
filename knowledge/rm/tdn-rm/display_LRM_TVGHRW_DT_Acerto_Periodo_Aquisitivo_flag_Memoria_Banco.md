---
content_hash: 887e0a21912ad85380040295bb78b35234ee3ce3a7e7c2e577c4c9ea116bf70c
fetched_at: '2026-06-29T00:08:13.288871+00:00'
page_id: '243661837'
product: rm
source: tdn-rm
title: TVGHRW_DT_Acerto_Periodo_Aquisitivo_flag_Memoria_Banco
type: documentation
url: https://tdn.totvs.com/display/LRM/TVGHRW_DT_Acerto_Periodo_Aquisitivo_flag_Memoria_Banco
version: 115
---

# Acerto de Período Aquisitivo

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Atualizar flag que informar que o Acerto de Período aquisitivo foi processado* |
| **Situação/Requisito:** | A rotina de Acerto de Período Aquisitivo, acionada logo a após de marcar o parâmetro "Acerto de período aquisitivo obrigatório" não atualizava o flag que indica que já acionou o acerto de período aquisitivo. Não permitindo acionar o histórico de provisão. |
| **Solução/Implementação:** | Otimizada a rotina de acerto de período aquisitivo para registrar no banco e no cache em memória o flag que indica que já acionou o Acerto de Período Aquisitivo permitindo acionar o histórico de provisão sem a necessidade de reiniciar o Host. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVGHRW |
| **Requisito (ISSUE):** |  |

divs
