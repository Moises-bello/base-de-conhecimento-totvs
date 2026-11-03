---
content_hash: c3f0a673fc2c9fa4cdb56d6bd63f6c79d257601b3a0935578e599c5bd054df15
fetched_at: '2026-06-29T00:08:46.266015+00:00'
page_id: '315908347'
product: rm
source: tdn-rm
title: 1203351 FINANCEIRO01-2638 Retorno bancário cobrança a maior gera adiantamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315908347
version: 94
---

# GERAÇÃO DE LANÇAMENTO DE ADIANTAMENTO PARA RETORNO BANCÁRIO A MAIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Retorno bancário de cobrança. |
| **Situação/Requisito:** | Sistema emitia mensagem de consistência de complemento de histórico da contabilização não preenchido (parametrizado como obrigatório). Evento contábil estava parametrizado para buscar complemento do histórico e mesmo em lançamentos com o campo preenchido nos lançamentos. |
| **Solução/Implementação:** | O lançamento de adiantamento criado, quando o valor a maior retornado ultrapassar o máximo parametrizado, terá um default no histórico com a seguinte informação: **Adiantamento referente ao recebimento a maior do retorno bancário Documento Número XXX**, onde XXX terá o Número do Documento do lançamento lido no arquivo e baixado. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1203351. |
| **Requisito:** | FINANCEIRO01-2638. |

divs
