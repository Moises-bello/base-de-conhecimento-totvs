---
content_hash: 90ee999a8cb2047c5fb5073c14ce0a6b02a915da8ba16956c4ffbc366abbf80c
fetched_at: '2026-06-29T00:12:02.517295+00:00'
page_id: '901956138'
product: rm
source: tdn-rm
title: Grupo de informações de controle da Fatura (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901956138
version: 19
---

# gFat - Grupo de informações de controle da Fatura

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **gFat** | **[infNFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=900451399)** | **0-1** | **Grupo**de Escolha**** | **Grupo de informações de controle da Fatura**  **Deverá ser gerado somente se o tipo de faturamento for normal tpFat = 0** |
| CompetFat | gFat | 1-1 | Elemento | TMOVFISCAL.DTCOMPETENCIASERVICO |
| dVencFat | gFat | 1-1 | Elemento | FLAN.DATAVENCIMENTO  Gerado com a Data de Vencimento do Lançamento Financeiro  Quando possuir mais de um Lançamento Financeiro, utiliza o do primeiro. |
| **--- x — Sequência opcional do XML: Será gerado somente se ambos os campos estiverem preenchidos** | | | | |
| dPerUsoIni | gFat | 1-1 | Elemento da sequencia | TMOVFISCAL.DATAINICIOCONSUMO  Período de uso inicial |
| dPerUsoFim | gFat | 1-1 | Elemento da sequencia | TMOVFISCAL.DATALEITURA  Período de uso final |
| **Fim da sequência opcional do XML — x ---** | | | | |
| codBarras | gFat | 1-1 | Elemento | FBOLETO.CODIGOBARRA  Existe um serviço utilizado pelo Nucleus para gerar automaticamente o QR Code PIX e o Código de Barras. Podemos utilizar esse mesmo serviço (Imprimir Boleto), porém é necessário ter o TOTVS Techfin. Para os clientes que não possuem o TOTVS Techfin, o campo deve ser gerado preenchido com zeros ou noves.  <https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008995022-Cross-Segmentos-TOTVS-BackOffice-Linha-RM-TOTVS-Gest%C3%A3o-de-Estoque-Compras-e-Faturamento-MOV-Como-Gerar-Boleto-de-Lan%C3%A7amento-Financeiro-ao-Imprimir-Movimento> |
| **--- x — Sequência opcional do XML: Não será gerada** | | | | |
| codDebAuto | gFat | 1-1 | Elemento de Escolha | Não será gerado |
| codBanco | gFat | 1-1 | Elemento | Não será gerado |
| codAgencia | gFat | 1-1 | Elemento | Não será gerado |
| **Fim da sequência opcional do XML — x ---** | | | | |
| **enderCorresp** | **gFat** | **0-1** | **Grupo** |  |
| **gPIX** | **gFat** | **0-1** | **Grupo** |  |

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

eyJpZCI6ICIxNDAyYzQ3NS1lYjQ1LTQ0ZjQtODBmOS0zZDQxNzkyMDljYjYiLCAiYW1vdW50IjogIjEwMDAwIiwgIml0ZW1zIjogW3sidW5pdF9wcmljZSI
]]>
