---
content_hash: f7787b49f18793951207fca5865b7e15cab156f3bc8d1df4723ee009e0a7772b
fetched_at: '2026-06-29T00:12:10.694180+00:00'
page_id: '953003417'
product: rm
source: tdn-rm
title: Grupo UA -  Tributos Devolvidos (para o item da NF-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003417
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo UA -  Tributos Devolvidos (para o item da NF-e)** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Campo de Origem | Campo na Aplicação | Mais Informações |
| 324p | UA01 | impostoDevol | Informação do Imposto devolvido | G | H01 |  | 0-1 |  | O motivo da devolução deverá ser informado pela empresa no campo de Informações Adicionais do Produto (tag:infAdProd). |  |  |  |
| 324q | UA02 | pDevol | Percentual da mercadoria devolvida | E | UA01 | N | 1-1 | 3v2 | O valor máximo deste percentual é 100%, no caso de devolução total da mercadoria. | Tag Calculado |  | Quantidade Nota Referenciada = (Quantidade Itens da Compra \* Fator de Conversão) **SE** a Quantidade Nota Referenciada for igual a zero: pDevol = Quantidade Nota Referenciada **SENÃO** pDevol = (Quantidade Itens da Devolução / Quantidade Nota Referenciada ) \* 100 |
| 324r | UA03 | IPI | Informação do IPI devolvido | G | UA01 |  | 1-1 |  |  |  |  |  |
| 324s | UA04 | vIPIDevol | Valor do IPI devolvido | E | UA03 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  | Totaliza o valor de vTotTrib dos itens. Obs.: Será gerado com o valor do tributo informado nos itens, para correta geração não deve existir a linha do tributo IPI no movimento, apenas nos itens do movimento com o valor a ser devolvido. |
