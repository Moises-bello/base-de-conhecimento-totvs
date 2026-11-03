---
content_hash: 85918bb4f28516e75b53307eb09fd08a338adfc8cb82d88b2b1f3aea07acbdb6
fetched_at: '2026-06-29T00:06:15.705149+00:00'
page_id: '211060473'
product: rm
source: tdn-rm
title: TTOKU6_DT_Calculo_Ferias_Media_Negativa_Adicional_Terco
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOKU6_DT_Calculo_Ferias_Media_Negativa_Adicional_Terco
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
| **Chamados relacionados:** | *TTOKU6* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
