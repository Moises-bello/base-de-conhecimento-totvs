---
content_hash: e70c6272af6562a5c7cb47b143beb3051799f7334d547227fc8ba625f3175ba9
fetched_at: '2026-06-29T00:06:15.496571+00:00'
page_id: '210057253'
product: rm
source: tdn-rm
title: TTODQ7_DT_Diferenca_IRRF13o_Zerando_Valores_Negativos_Base
type: documentation
url: https://tdn.totvs.com/display/LRM/TTODQ7_DT_Diferenca_IRRF13o_Zerando_Valores_Negativos_Base
version: 2
---

# DIFERENÇA DE IRRF 13o. QUANDO ZERA VALORES NEGATIVOS QUE COMPOEM A BASE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Diferença de 13o.Salário* |
| **Função:** | *IRRF 13o.* |
| **Situação/Requisito:** | *No cálculo da Diferença de 13o. Salário por Dissídio, com o parâmetro "Zerar evento de diferença quando o valor ficar negativo" marcado, caso a diferença de algum evento que incida em IRRF 13o. fique negativa, a Base de IRRF 13o está ficando incorreta, porque considera o novo valor recalculado a menor, mesmo que esta diferença negativa não seja descontada do funcionário.* |
| **Solução/Implementação:** | *Ajuste na composição da Base de IRRF 13o. na Diferença de 13o. Salário por Dissídio, para considerar o valor original do evento, quando o recálculo retornar um valor menor que o anterior, e o parâmetro "Zerar evento de diferença quando o valor ficar negativo" estiver marcado.* |
| **Conversores e Parâmetros:** | *Zerar evento de diferença quando o valor ficar negativo* |
| **Chamados relacionados:** | *TTODQ7* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
