---
content_hash: 929cdacbd5cab1723e13e3d4405e116f5658314fb1883ddd368077df5637593d
fetched_at: '2026-06-29T00:12:10.286606+00:00'
page_id: '953001187'
product: rm
source: tdn-rm
title: Grupo I03 - Produtos e Serviços / Grupo de Exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953001187
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo I03 - Produtos e Serviços / Grupo de Exportação** | | | | | | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo da Aplicação** | **Mais Informações** |
| 128.f | 150 | detExport | Grupo de informações de exportação para o item | G | I01 |  | 0-500 | - | Informar apenas no Drawback e nas exportações. |  | Número Ato Concess. Regime Drawback | Será criado um registro para cada movimento relacionado ao item. |
| 128.g | 151 | nDraw | Número do ato concessório de Drawback | E | I50 | C | 0-1 | 1-20 | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10). | TMOVFISCAL.DRAWBACK | Número Ato Concess. Regime Drawback | No movimento, pasta Integrações | aba Fiscal. |
| 128.h | 152 | exportInd | Grupo sobre exportação indireta | G | I50 |  | 0-1 | - | - |  | Natureza de Exportação | Será gerado somente se a Natureza de Exportação da pasta Informações Adicionais | aba Exportação, for igual a Exportação Indireta ou Exportação Indireta Simplificada. Também será necessário que o movimento e seus itens estejam relacionados ao movimento de origem da exportação. |
| 128.i | 153 | nRE | Número do Registro de Exportação | E | I52 | N | 1-1 | 12 |  | TITMMOV.REGISTROEXPORTACAO | Núm. Registro de Exportação | Item do movimento, pasta Informações Adicionais | aba Exportação. |
| 128.j | 154 | chNFe | Chave de Acesso da NF-e recebida para exportação | E | I52 | N | 1-1 | 44 | NF-e recebida com fim específico de exportação. No caso de operação com CFOP 3.503, informar a chave de acesso da NF-e que efetivou a exportação. | TMOV.CHAVEACESSONFE ou TNFEESTADUAL.CHAVEACESSO | Chave de acesso da NF-e Referenciada | - |
| 128.k | 155 | qExport | Quantidade do item realmente exportado | E | I52 | N | 1-1 | 11v4 | A unidade de medida desta quantidade é a unidade de comercialização deste item. No caso de operação com CFOP 3.503, informar a quantidade de mercadoria devolvida. | TITMMOVRELAC.QUANTIDADE | Relac. Mov. Exportação | Quantidade do movimento relacionado no item do movimento, pasta Informações Adicionais | aba Relac. Mov. Exportação. |
