---
content_hash: 7f41b77a7e16bb5332f07386c437705e3b863aa35fbe4c5c566a8790b1fa2c5e
fetched_at: '2026-06-29T00:08:37.086286+00:00'
page_id: '284870282'
product: rm
source: tdn-rm
title: 659347 FINANCEIRO01-1223 DT Pagamento Eletrônico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284870282
version: 101
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Retorno Bancário de Pagamentos |
| **Situação/Requisito:** | Ao importar arquivo de retorno de pagamento do santander 240 posições, com o código de ocorrência para retorno "03 - Débito Autorizado pela Agência - Efetuado" O sistema está alterando o status CNAB dos lançamentos para Recusado, quando deveria baixá-los. |
| **Solução/Implementação:** | Quando o retorno bancário padrão CNAB-240 retornar um código de ocorrência "03", deve ser tratado como uma baixa do lançamento. |
| **Conversores e Parâmetros:** | N/D |
| **Tickets relacionados:** | N/D |
| **Requisito:** | FIN000173 |

divs
