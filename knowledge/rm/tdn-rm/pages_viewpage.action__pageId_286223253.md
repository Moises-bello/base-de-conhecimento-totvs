---
content_hash: 7a1ce416ba768b02b1b702d6a8bbb8129a10a07f0d4d74528b5b1f24606511df
fetched_at: '2026-06-29T00:08:40.524934+00:00'
page_id: '286223253'
product: rm
source: tdn-rm
title: 1052353 CONTROLADORIA01-324 DT Depreciação Acumulada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286223253
version: 106
---

# Depreciação acumulada na inclusão de patrimônio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Patrimonial |
| **Função:** | Depreciação acumulada na inclusão de patrimônio |
| **Situação/Requisito:** | O cliente informa que ao realizar a inclusão de um patrimônio, com data de aquisição anterior ao período de cálculo, a depreciação acumulada está sendo calculada incorretamente. O dia de aquisição não está sendo sendo considerado.  Exemplo para cota proporcional:  Data de aquisição - 26/05/2017 Período atual de cálculo - 06/2017 Taxa depreciação - 20% Valor de aquisição - 641.666,67  Para este cenário está sendo calculada uma depreciação acumulada de 1.425,93, porém o correto seria 1.782,41. |
| **Solução/Implementação:** | Durante a inclusão de um patrimônio, se a data de aquisição for inferior ao período de cálculo, é possível marcar a opção "Informar depreciação acumulada corrigida". Com esta opção selecionada é possível realizar o cálculo automático da depreciação acumulada, clicando no botão que possui a imagem de uma calculadora. Este cálculo foi alterado para que o dia de aquisição seja considerado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
