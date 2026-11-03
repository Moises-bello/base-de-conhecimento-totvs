---
content_hash: 64fd947ad75df0c9315bf1c68064aad4ced6deb1888fcd6201134cffb4019e9f
fetched_at: '2026-07-02T19:24:25.914872+00:00'
page_id: '514740605'
product: protheus
source: tdn-tec
title: Permitir a leitura de caracteres diferentes de US-ASCII do campo Subject
type: documentation
url: https://tdn.totvs.com/display/tec/Permitir+a+leitura+de+caracteres+diferentes+de+US-ASCII+do+campo+Subject
version: 2
---

|  |  |
| --- | --- |
| Ocorrência | Caracteres Não US não estava corretamente sendo codificados no campo Subject de um email pelas classes de e-mail |
| Correção | Tratado a codificação do campo subject respeitando ao RFC-2045 e codificação quoted-printable. |
| Informações adicionais | * Referente ao chamado: MTEC-3140 * Disponível em builds iguais ou superiores a [13.1.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.45) e [13.2.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.45). |
