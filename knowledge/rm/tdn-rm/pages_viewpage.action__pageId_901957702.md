---
content_hash: ee94acda23f2146019b721b8f863dd92f96cb39469103bd400b4ee50cc4c26d6
fetched_at: '2026-06-29T00:12:02.526684+00:00'
page_id: '901957702'
product: rm
source: tdn-rm
title: Endereço de entrega da fatura (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901957702
version: 5
---

# enderCorresp - Endereço de entrega da fatura

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **enderCorresp** | **[gFat](https://tdn.totvs.com/pages/viewpage.action?pageId=901956138)** | **0-1** | **Grupo** | **Endereço de entrega da fatura** |
| xLgr | enderCorresp | 1-1 | Elemento | Tipo de Rua + Endereço do Cliente/Fornecedor |
| nro | enderCorresp | 1-1 | Elemento | Número do endereço do Cliente/Fornecedor |
| xCpl | enderCorresp | 0-1 | Elemento | Complemento do endereço do Cliente/Fornecedor  Se estiver em branco este campo não será gerado |
| xBairro | enderCorresp | 1-1 | Elemento | Tipo de Bairro + Bairro do endereço do Cliente/Fornecedor |
| cMun | enderCorresp | 1-1 | Elemento | Classificação IBGE da município do endereço do Cliente/Fornecedor |
| xMun | enderCorresp | 1-1 | Elemento | Nome do município do endereço do Cliente/Fornecedor |
| CEP | enderCorresp | 1-1 | Elemento | CEP do endereço do Cliente/Fornecedor |
| UF | enderCorresp | 1-1 | Elemento | Estado do endereço do Cliente/Fornecedor |
| fone | enderCorresp | 0-1 | Elemento | Telefone do Cliente/Fornecedor  Se estiver em branco este campo não será gerado |
| email | enderCorresp | 0-1 | Elemento | E-mail do Cliente/Fornecedor  Se estiver em branco este campo não será gerado |

Exemploxml

202509
2025-09-24
2025-09-24
2025-09-25
27595121400000100002233002220070000000000008

rua principal
100
complemento principal
bairro principal
3529005
Teste
30494170
SP
01133333333
email\_principal@totvs.com.br
]]>
