---
content_hash: 29c814ccc0ba67c8290361c249673e6a8f3884d8aa47a4caf25ece1414cfe6db
fetched_at: '2026-06-29T00:11:03.407048+00:00'
page_id: '622217661'
product: rm
source: tdn-rm
title: Máscara
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=622217661
version: 4
---

Máscara é uma sequência de dígitos que determinam como os dados deverão ser informados em campos pré-definidos nos Parâmetros do Sistema (Código Seção, Chapa, CEP, etc.) Esta sequência consiste basicamente na definição do número de dígitos, bem como seus respectivos tipos (letras, números e símbolos).

A máscara é formada pelos seguintes caracteres:  
Símbolo - Significado

# - Para números

L ou l - Para campo alfabético

A ou a - Para campo alfanumérico

Q - Para qualquer caractere, menos os separadores ( : . , ; / )

Observação: Por exemplo, se a máscara de um patrimônio for L#.##, o código poderá ser: A1.01, sendo que se digitado a1.01, o sistema passará "a" (minúsculo) para "A" (maiúsculo).

Qualquer outro caractere ou letra colocado na máscara fora deste padrão, não será aceito pelo sistema.
