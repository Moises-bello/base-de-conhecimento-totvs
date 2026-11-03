---
content_hash: 6220de41d6680730a24138a5379291c13c60d7760608882af597d6c4e0010ad7
fetched_at: '2026-07-02T19:24:27.776794+00:00'
page_id: '680952944'
product: protheus
source: tdn-tec
title: Correção - Comportamento do sinal negativo na Picture de Formatação com Template
  "9"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680952944
version: 1
---

Correção - Comportamento do sinal negativo na Picture de Formatação com Template "9"

|  |  |
| --- | --- |
| Situação | O template "9" na Picture de Formatação faz com que o campo permita a entrada de qualquer caractere numérico e o sinal de negativo, porém este sinal é permitido em qualquer posição do campo. Por exemplo, a Picture @E 999.999,99 permitiria a entrada de -12.345,67 mas também aceitaria uma entrada incorreta do tipo 1-.3-5,67 |
| Ocorrência | Quando é utilizada a função @R para especificar uma Picture de Formatação que contenha um hífen (o mesmo caractere utilizado como sinal negativo) como por exemplo um CNPJ (@R 99.999.999/9999-99) e utilizado o recurso de copy/paste com um valor formatado (12.345.678/0001-23) ambos os hifens serão exibidos, tanto o próprio hífen da Picture de Formatação como o hífen proveniente do copy/paste, já que este é um caractere válido e aceito pelo Template "9". Então o resultado exibido no campo seria: "12.345.678/0001--2" e o resultado do buffer do campo seria "123456780001-2" pois a função @R elimina os símbolos de formatação mas ainda permite o hífen proveniente do copy/paste. |
| Correção | Foi aplicada uma correção para que o Template "9" da Picture de Formatação permita a entrada (digitação ou copy/paste) do hífen (ou sinal negativo) somente se este for o dígito mais a esquerda do campo. |
| Informações adicionais | * Referente ao chamado: 13661360 * Referente à ocorrência: DTCLIENT01-3263 * Disponível em builds iguais ou superiores a 19.3.1.8 e 20.3.0.3 |
