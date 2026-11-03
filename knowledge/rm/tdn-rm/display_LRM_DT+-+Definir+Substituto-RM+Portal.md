---
content_hash: cb8c40221f3a4fd529e25d4b2285d48f4576a20dc2e340654b535e0b1d29ca81
fetched_at: '2026-06-29T00:11:06.433207+00:00'
page_id: '634831219'
product: rm
source: tdn-rm
title: DT - Definir Substituto-RM Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Definir+Substituto-RM+Portal
version: 12
---

## ****01. DADOS GERAIS****

Linha RM​

**Patches:**12.1.29.287 12.1.32.140 12.1.31.204

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - Portal - Substituto |
| Função: |  |
| País: | Brasil |
| Ticket: | 11977292 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-885 |

## **02. SITUAÇÃO/REQUISITO**

 Ao acessar o portal e selecionar uma chapa para substituto o sistema apresenta o erro abaixo:

|  |
| --- |
| Chave duplicada |

Possíveis causas:

* inclusão de registro cujo valor da chave primária já existe
* inclusão de registro cujo valor do índice único já existe|

## **03. SOLUÇÃO**

  Ao definir um substituto foi retirada a trava do lookup de chapa, permitindo que o sistema liste todos os funcionários da coligada.

  Antes deste ajuste o sistema filtrava somente funcionários da mesma seção onde o supervisor estava inserido.
