---
content_hash: ef41b04354436d7a97db3a45e591d1ec5509d4fff4d45d1613c2613df8c50cc6
fetched_at: '2026-07-02T19:24:28.621296+00:00'
page_id: '801315591'
product: protheus
source: tdn-tec
title: tUnicode
type: documentation
url: https://tdn.totvs.com/display/tec/tUnicode
version: 9
---

A classe tUnicode, tem o objetivo de realizar conversões em strings UTF-8 para outros formatos de encoding além de realizar normalização delas.

Strings UTF-8 podem ser representadas em várias formas diferentes, chamadas de **formas normais**. As formas normais são importantes para garantir a comparação e ordenação corretas de strings UTF-8.

Existem três formas normais de strings UTF-8:

* **Forma normalizada NFD** (Normal Form Composed): é a forma mais compacta, pois combina todos os caracteres com diacríticos em um único caractere. Por exemplo, a string "café" é representada como um único caractere com código U+00E9 na forma normalizada NFD.
* **Forma normalizada NFC** (Normal Form Canonical): é a forma mais comumente usada, pois é a forma de composição de caracteres mais eficaz. É semelhante à forma normalizada NFD, mas os caracteres com diacríticos são representados separadamente. Por exemplo, a string "café" é representada como os caracteres "c", "a", "f", "é" na forma normalizada NFC.
* **Forma normalizada NFKD** (Normal Form Decomposed): é a forma mais detalhada, pois descompõe todos os caracteres com diacríticos em seus componentes básicos. Por exemplo, a string "café" é representada como os caracteres "c", "a", "f", "e", "´" na forma normalizada NFKD.
* **Forma normalizada NFKC** (Normal Form Canonical Composition) é uma forma de normalização de strings UTF-8 que combina os caracteres com diacríticos em um único caractere, se possível. A forma normal NFKC é semelhante à forma normal NFD, mas ela também elimina as combinações de caracteres compatíveis.

A forma normalizada NFC é geralmente a melhor escolha para comparação e ordenação de strings UTF-8. Isso ocorre porque é a forma mais comumente usada e é a forma de composição de caracteres mais eficaz.

Além disso, a função ConvertEncoding é equivalente as DecodeUTF e EncodeUTF utilizadas originalmente no AdvPL.

# Referências

[Unicode® Standard Annex #15](https://unicode.org/reports/tr15/)

# Observação

**Essa classe é apenas compatível com o uso em TLPP e não disponível para uso em ADVPL.**

# Métodos da Classe

Atualmente, temos os seguintes métodos disponíveis para realizar normalização de strings UTF-8 de um formato para um outro desejado:
