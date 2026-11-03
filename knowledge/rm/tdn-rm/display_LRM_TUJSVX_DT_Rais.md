---
content_hash: 8b8594a20802122c3c75795784e36cbb1310cd96ee421bc93dcef7dc633ea198
fetched_at: '2026-06-29T00:06:30.073824+00:00'
page_id: '235311686'
product: rm
source: tdn-rm
title: TUJSVX_DT_Rais
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJSVX_DT_Rais
version: 117
---

# RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *RAIS* |
| **Situação/Requisito:** | Ao gerar a RAIS para funcionários demitidos e com diferença salarial calculada em competência após a rescisão, os valores dessa diferença (evento com código de cálculo 37) está sendo levado tanto na parte de Remuneração Mensal, quanto na parte de Desligamento > Reajuste Coletivo na GDRais. De acordo com o manual da RAIS, esses valores devem ser levados somente em Desligamento > Reajuste Coletivo |
| **Solução/Implementação:** | Otimizada geração da RAIS, implementada regra para que o evento de diferença salarial (CC37), quando o pagamento do evento for posterior à demissão do funcionário, não componha valores de remuneração mensal do funcionário. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUJSVX |
| **Requisito (ISSUE):** |  |

divs
