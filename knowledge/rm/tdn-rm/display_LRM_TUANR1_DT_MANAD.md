---
content_hash: 33aad367d408e8c760f241b1dc819f10241cece26e7b17258acc3ce6966a514e
fetched_at: '2026-06-29T00:06:24.868921+00:00'
page_id: '224126253'
product: rm
source: tdn-rm
title: TUANR1_DT_MANAD
type: documentation
url: https://tdn.totvs.com/display/LRM/TUANR1_DT_MANAD
version: 125
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *MANAD* |
| **Situação/Requisito:** | Ao gerar o MANAD com as datas 01/01/2016 à 31/01/2016 para funcionários que tiveram diferença de 13 salário pagas no mês e tentar validar o arquivo o sistema apresenta a mensagem no validador SVA: Ind, de Base de Cálculo da Prev. Social incompatível com o tipo de folha 2/5(13º Salário) |
| **Solução/Implementação:** | Otimizado geração do MANAD, implementada regra para considerar a diferença de 13 salário como indicador de base de cálculo de 13 salário no registro K300 |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUANR1 TUDWXR |
| **Requisito (ISSUE):** |  |

divs
