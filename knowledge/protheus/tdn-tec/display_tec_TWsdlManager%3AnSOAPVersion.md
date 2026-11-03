---
content_hash: 2208c42b1b6d07b2b46a3bff70f3c871c18ce0f86e8fbb703285dd28fcfc93ec
fetched_at: '2026-07-02T19:24:24.974374+00:00'
page_id: '493630744'
product: protheus
source: tdn-tec
title: TWsdlManager:nSOAPVersion
type: documentation
url: https://tdn.totvs.com/display/tec/TWsdlManager%3AnSOAPVersion
version: 2
---

TWsdlManager:nSOAPVersion

Define ou recupera a versão do protocolo SOAP utilizado.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| numérico | 1 | N |

## Observações

Valores válidos:

|  |  |
| --- | --- |
| 0 | Força a utilização da versão SOAP 1.1 |
| 1 | Força a utilização da versão SOAP 1.2 |
| x | O programa tenta descobrir a versão do protocolo (comportamento default na ausência de definição desta propriedade). |

## Exemplos

cppEclipseExemplo 1truefalse
