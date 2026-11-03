---
content_hash: e8ce2d5a95ea967b679108ebd3649bd42221a52d4cdaf6037cf32d4fdf1e9d0b
fetched_at: '2026-06-29T00:08:29.742173+00:00'
page_id: '272162173'
product: rm
source: tdn-rm
title: 549818 MRH-8063 DT Diferenca Media 13o Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/549818+MRH-8063+DT+Diferenca+Media+13o+Salario
version: 107
---

# DIFERENÇA DE MEDIA DE 13o. SALÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de 13o.* |
| **Situação/Requisito:** | No cálculo da diferença de 13º em janeiro, a diferença da média é acumulada no evento de diferença da 2a. parcela de 13º salário, informado no momento do processamento.  Quando foi calculada outra diferença de 13º salário em fevereiro por dissídio, o valor da diferença de media foi abatido como diferença salarial, fazendo com que a diferença da 2a. parcela ficasse negativa.. |
| **Solução/Implementação:** | Ajuste no cálculo da diferença de 13º em janeiro para guardar na pasta "Verbas geradas por Diferença" da ficha financeira, os valores originais de media de 13º Salário. |
| **Tickets relacionados:** | MRH-8063 |

divs
