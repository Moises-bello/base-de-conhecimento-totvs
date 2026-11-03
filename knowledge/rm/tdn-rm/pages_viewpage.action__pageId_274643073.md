---
content_hash: d8f99cc684c2a583263dcf7c6a46237efee4dfa3d7cfe1bc5115a09934becef5
fetched_at: '2026-06-29T00:08:34.064741+00:00'
page_id: '274643073'
product: rm
source: tdn-rm
title: 659347 FINANCEIRO01-314 Integração Bancária - Retorno de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274643073
version: 108
---

# Integração Bancária - Retorno de Pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Pagamento |
| **Situação/Requisito:** | Ao importar arquivo de retorno de pagamento do santander 240 posições, com o código de ocorrência para retorno "03 - Débito Autorizado pela Agência - Efetuado"  O sistema está alterando o status CNAB dos lançamentos para Recusado. |
| **Solução/Implementação:** | Ajuste no processo de retorno de pagamento (padrão febraban 240) para considerar o código de ocorrencia '03 - Débito Autorizado pela Agência - Efetuado' como registrado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000171 |

divs
