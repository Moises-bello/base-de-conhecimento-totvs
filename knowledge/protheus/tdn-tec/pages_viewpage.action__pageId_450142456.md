---
content_hash: 0e474cd9d5a013dc8c76a4a416df322f9d5803eff73de6db99d6366e62216634
fetched_at: '2026-07-02T19:24:23.447954+00:00'
page_id: '450142456'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave LogMaxFileSizeBytes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450142456
version: 2
---

Define o tamanho máximo de um arquivo de log gerado pelo Agent da AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 5 MB (5 \* 1024 \* 1024 bytes) (Padrão) | Define como 5 MB (5 \* 1024 \* 1024 bytes) o tamanho máximo de um arquivo de log gerado pelo Agent da AppDynamics. |
| <número\_de\_bytes> | Define como <número\_de\_bytes> o tamanho máximo de um arquivo de log gerado pelo Agent da AppDynamics. |

## Observações

* Após atingido o tamanho máximo estabelecido, o arquivo de log será rotacionado, fazendo com que um novo arquivo seja criado e, se atingido a quantidade máxima no rotacionamento, o mais antigo seja apagado;
* A quantidade de arquivos rotacionados é definida em .

## Exemplo

Define como **5000000** o tamanho máximo de um arquivo de log gerado pelo Agent da AppDynamics:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
