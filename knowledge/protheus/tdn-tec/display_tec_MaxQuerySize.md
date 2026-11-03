---
content_hash: 93c0ea1f35ab017ed19e59aa87db1f63fa01be7b2b39dc1f322d718ab9a1099b
fetched_at: '2026-07-02T19:24:23.301460+00:00'
page_id: '41353992'
product: protheus
source: tdn-tec
title: MaxQuerySize
type: documentation
url: https://tdn.totvs.com/display/tec/MaxQuerySize
version: 5
---

MaxQuerySize

Permite alterar a validação do limite de tamanho de query, em bytes, executada através de uma aplicação true.

Este limite foi estabelecido na concepção da linguagem true, baseado em uma restrição de tamanho de query dos primeiros bancos relacionais homologados e foi mantido até hoje como um paradigma da linguagem.

A configuração MaxQuerySize está disponível no true a partir da versão 13.2.0.0.

Os valores padrão e limites, em bytes, para essa configuração são:

| Versão | Padrão | Mínimo | Máximo |
| --- | --- | --- | --- |
| Até a versão 13.2.3.34 | 15960 | 1024 | 31960 |
| a partir da versão 12.2.3.35 e supeiores | 32768 | 1024 | 65536 |

Oriente o programador a buscar alternativas que não usem queries tão longas.

## Exemplo

Veja a seguir um exemplo de configuração da chave MaxQuerySize.

## Observações

 Esta configuração pode ser especificada diretamente na seção do ambiente (environment) em uso, atuando unicamente sobre ele.
