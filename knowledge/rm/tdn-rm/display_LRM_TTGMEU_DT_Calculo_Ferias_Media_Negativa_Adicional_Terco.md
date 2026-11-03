---
content_hash: d3ac47d28e16e35879a69c0d8a61f55e0c812a34c69c7c9f0e36cc989d787697
fetched_at: '2026-06-29T00:06:15.687782+00:00'
page_id: '211060130'
product: rm
source: tdn-rm
title: TTGMEU_DT_Calculo_Ferias_Media_Negativa_Adicional_Terco
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGMEU_DT_Calculo_Ferias_Media_Negativa_Adicional_Terco
version: 1
---

# CÁLCULO DE FÉRIAS COM MÉDIA NEGATIVA INCIDINDO ADICIONAL DE 1/3

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Cálculo de Férias* |
| **Função:** | *Adicional de 1/3* |
| **Situação/Requisito:** | *No cálculo do recibo de férias, quando existem eventos de desconto que incidem em média, que fazem com que o valor final da média fique negativo, este valor negativo está sendo deduzido na base de cálculo do adicional de 1/3 de férias, mesmo que não ocorra o lançamento do evento negativo no recibo.* |
| **Solução/Implementação:** | *Ajuste no cálculo de férias para não considerar valores de média negativos na base de cálculo do adicional de 1/3 de férias.*  *Eventos de média com valores negativos não são lançados no recibo, portanto não devem compor nenhuma base de cálculo do processo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TTGMEU* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.42* |

divs
