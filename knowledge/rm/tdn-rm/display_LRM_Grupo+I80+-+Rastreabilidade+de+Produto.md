---
content_hash: 3c63d3951a2e4817885ed3911df177e150c9473ffe4ec7ac62e0f8e2cff885f6
fetched_at: '2026-06-29T00:12:10.300849+00:00'
page_id: '953002036'
product: rm
source: tdn-rm
title: Grupo I80 - Rastreabilidade de Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+I80+-+Rastreabilidade+de+Produto
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo I80 - Rastreabilidade de Produto** | | | | | | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo da Aplicação** | **Mais Informações** |
| 128q | I80 | rastro | Detalhamento de produto sujeito a rastreabilidade | G | I01 |  | 0-500 |  | Informar apenas quando se tratar de produto a ser rastreado posteriormente |  | Gerado quando o código NCM for igual a 3003 / 3004. | Informar apenas quando se tratar de produto a ser rastreado posteriormente, |
| 128r | I81 | nLote | Número do Lote do produto | E | I80 | C | 1-1 | 1-20 |  | TLOTEPRD.NUMLOTE | Número do lote |  |
| 128s | I82 | qLote | Quantidade de produto no Lote | E | I80 | N | 1-1 | 8v3 |  | TITMLOTEPRD.QUANTIDADE2 | Quantidade física 2 da mov. do lote |  |
| 128t | I83 | dFab | Data de fabricação/ Produção | E | I80 | D | 1-1 |  | Formato: “AAAA-MM-DD” | TLOTEPRD.DATAFABRICACAO | Data de fabricação do lote |  |
| 128u | I84 | dVal | Data de validade | E | I80 | D | 1-1 |  | Formato: “AAAA-MM-DD” Informar o último dia do mês caso a validade não especifique o dia. | TLOTEPRD.DATAVALIDADE | Data de validade do lote | Informar o último dia do mês caso a validade não especifique o dia. |
| 128v | I85 | cAgreg | Código de Agregação | E | I80 | N | 0-1 | 1-20 |  | TLOTEPRD.CODAGREGACAO |  |  |
