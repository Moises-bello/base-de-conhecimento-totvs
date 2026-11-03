---
content_hash: f64f54ac46e05a8735a33c1daaaa5dab32b0ee6d9204082bfef614de184b3bd0
fetched_at: '2026-06-29T00:06:15.492062+00:00'
page_id: '210057210'
product: rm
source: tdn-rm
title: TTBXQ0_Diferenca_IRRF13o_Zerando_Valores_Negativos_Base
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBXQ0_Diferenca_IRRF13o_Zerando_Valores_Negativos_Base
version: 2
---

# DIFERENÇA DE IRRF 13o. QUANDO ZERA VALORES NEGATIVOS QUE COMPOEM A BASE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de 13o. Salário* |
| **Situação/Requisito:** | *No cálculo da Diferença de 13o. Salário por Dissídio, com o parâmetro "Zerar evento de diferença quando o valor ficar negativo" marcado, caso a diferença de algum evento que incida em IRRF 13o. fique negativa, a Base de IRRF 13o está ficando incorreta, porque considera o novo valor recalculado a menor, mesmo que esta diferença negativa não seja descontada do funcionário.* |
| **Solução/Implementação:** | *Ajuste na composição da Base de IRRF 13o. na Diferença de 13o. Salário por Dissídio, para considerar o valor original do evento, quando o recálculo retornar um valor menor que o anterior, e o parâmetro "Zerar evento de diferença quando o valor ficar negativo" estiver marcado.* |
| **Conversores e Parâmetros:** | *Zerar evento de diferença quando o valor ficar negativo* |
| **Chamados relacionados:** | *TTBXQ0* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.42* |
| **Versão Expedida:** | *11.82.42* |

divs
