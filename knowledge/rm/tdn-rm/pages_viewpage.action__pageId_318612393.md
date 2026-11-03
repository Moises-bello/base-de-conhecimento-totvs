---
content_hash: 9ee91cb7f46a7e166077f73bfebedaf8220f362f7e056ce022fc34d2bbfb8ae0
fetched_at: '2026-06-29T00:08:47.164171+00:00'
page_id: '318612393'
product: rm
source: tdn-rm
title: 1736479 FINANCEIRO01-4133 DT Retorno de cobrança bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318612393
version: 94
---

# RETORNO DE COBRANÇA BANCÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Retorno de cobrança bancária |
| **Situação/Requisito:** | Ao importar arquivo de retorno bancário, pago a menor, para dois lançamentos no mesmo boleto, o sistema está enviando a diferença para o campo de Desconto normalmente, entretanto o valor original do Item de Baixa está ficando incorreto e o lançamento parcialmente baixado. Na parametrização de diferença para baixa parcial, está preenchido com 0,00. Observação: Se o parâmetro para não gerar boleto na baixa parcial estiver desmarcado, o sistema gera um boleto com o valor 0,00 em aberto. |
| **Solução/Implementação:** | Otimizado o processo de retorno bancário de cobrança para fazer a proporção do pagamento a maior/menor entre os lançamentos associados ao boleto. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1744020 |

divs
