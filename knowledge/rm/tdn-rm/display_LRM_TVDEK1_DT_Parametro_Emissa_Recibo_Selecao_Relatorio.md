---
content_hash: ec4fa1094d5cf9a6f9d15e66296e142c1604bd5bd0adc0593cb8b05498cd2577
fetched_at: '2026-06-29T00:08:11.439159+00:00'
page_id: '243008483'
product: rm
source: tdn-rm
title: TVDEK1_DT_Parametro_Emissa_Recibo_Selecao_Relatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDEK1_DT_Parametro_Emissa_Recibo_Selecao_Relatorio
version: 110
---

# PARÂMETRO - EMISSÃO DE RECIBOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Parâmetro - Emissão de recibos* |
| **Situação/Requisito:** | **Na tela de parâmetros para emissão de recibos, a seleção de relatórios não permite a alteração de nenhum relatório pois sempre alerta que está faltando relatórios, mesmo com estes preenchidos.** |
| **Solução/Implementação:** | *Foi identificado que se um relatório for alterado (empréstimo ou devolução) for alterado para o novo gerador ou para o antigo, o sistema continua validando a opção anterior, que como tem o código do relatório removido, o sistema alerta que está faltando. Foi inserido uma validação para que o sistema identifique o tipo de relatório utilizado e valide se o relatório foi definido somente para o tipo selecionado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
