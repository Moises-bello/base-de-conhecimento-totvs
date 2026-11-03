---
content_hash: ab7fa52615aea219c20a4649c39969bf73011beba6d813fa06b93537bb395133
fetched_at: '2026-06-29T00:08:31.096429+00:00'
page_id: '272716502'
product: rm
source: tdn-rm
title: DT_635770_Integração_Bancária-Retorno_de_Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272716502
version: 115
---

# Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Ao importar arquivo de retorno de cobrança o sistema exibe o erro:  Linha 00201 Erro Boleto Ref.:80921- Erro ao salvar dados de lançamentos relativos ao Retorno Bancário  Erro ao atualizar lançamento referente a linha 201 do arquivo de retorno bancário.  Chave duplicada  Possíveis causas:  - inclusão de registro cujo valor da chave primária já existe  - inclusão de registro cujo valor do índice único já existe |
| **Solução/Implementação:** | Melhoria no processo de retorno de cobrança bancária, para quando realizar retorno de cobrança bancária utilizando o parâmetro "Contas a Receber > Integração Bancária > No retorno bancário utilizar os valores (Juros, multa e desconto) do arquivo, sobrepondo os do lançamento" marcado. |
| **Conversores e Parâmetros:** | Contas a Receber > Integração Bancária > No retorno bancário utilizar os valores (Juros, multa e desconto) do arquivo, sobrepondo os do lançamento |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000169 |

divs
