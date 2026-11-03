---
content_hash: 83a4c717988fb0582b6e6367b550500c154fc741799ded99aab1f4c67039342d
fetched_at: '2026-06-29T00:08:08.969963+00:00'
page_id: '239018117'
product: rm
source: tdn-rm
title: TVABC3_DT_Agrupamento_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVABC3_DT_Agrupamento_Salarial
version: 113
---

# Agrupamento Salarial

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Agrupamento Salarial* |
| **Situação/Requisito:** | Para o chamado TURRW3 foi implementado, especificamente para a ASAV, uma mudança no filtro que retorna os períodos letivos em integração com o classis (Vide chamado TURRW3).  A partir da 12.1.12 a mudança realizada para a ASAV passará a ser geral para todos os clientes, pois o produto Classis irá preparar um script que fará com que o parâmetro " Período Letivo Encerrado para folha de pagamento " (presente no classis), seja específico para a regra de retornar os períodos letivos no labore, no Agrupamento Salarial |
| **Solução/Implementação:** | Ajuste para retirar a verificação específica para o cliente ASAV, transformando a regra para todos os clientes |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVABC3,TURRW3 |
| **Requisito (ISSUE):** |  |

divs
