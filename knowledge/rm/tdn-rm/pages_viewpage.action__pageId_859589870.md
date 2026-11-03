---
content_hash: d2e7cc7f60a1a24df5e5570ef8c0c1ddcffe645c99e2a6aaaeb2db47e65238c2
fetched_at: '2026-06-29T00:11:55.007866+00:00'
page_id: '859589870'
product: rm
source: tdn-rm
title: 'FISCAL01-23402- Erro no documento XML .. Erro de validação de instância: não
  é um valor válido para TNFeInfNFePagDetPagTPag.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859589870
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerador de saídas |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | FISCAL01-23402 |

## **02. SITUAÇÃO/REQUISITO**

Ao importar a XML apresenta o erro, Mensagem Original: Erro no documento XML (195, 10).. Erro de validação de instância: '21' não é um valor válido para TNFeInfNFePagDetPagTPag.

## **03. SOLUÇÃO**

O tipo da tag tPag foi alterado de enumerado para string. A modificação foi feita para aderir a novos meios de pagamento.

Disponível a partir da biblioteca 12.1.2310
