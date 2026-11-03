---
content_hash: f855083501ae06760b43f3624a2d93c0fe8823279785e6560f30e680095dfc4b
fetched_at: '2026-07-02T19:24:28.717536+00:00'
page_id: '816906154'
product: protheus
source: tdn-tec
title: ConvertEncoding
type: documentation
url: https://tdn.totvs.com/display/tec/ConvertEncoding
version: 6
---

Converte o encoding the um determinado tipo de conjunto de caracteres, fornecido pela a string sInput por referência, para um outro formato. Atualmente, os seguintes formatos são suportados e homologados para realizar conversões:

* Big5
* Big5-HKSCS
* CP949
* EUC-KR
* GB18030
* HP-ROMAN8
* IBM 850
* IBM 866
* IBM 874
* ISO 8859-1 até 10
* ISO 8859-13 até 16
* Iscii-Bng, Dev, Gjr, Knd, Mlm, Ori, Pnj, Tlg, e Tml
* KOI8-R
* KOI8-U
* Macintosh
* Shift-JIS
* TIS-620
* TSCII
* UTF-8
* Windows-1250 até o 1258

## Parâmetros

| Parâmetro | Tipo | Obrigatório | Referência | Descrição |
| --- | --- | --- | --- | --- |
| sInput | C | X | X | String de entrada para ser convertida, passada por referência, sendo esta a ser convertida para o formato desejado |
| sEncodingInput | C | X |  | String Encoding de entrada da string no primeiro parâmetro |
| sEncodingOutput | C | X |  | String Encoding de saída da string para ser convertido |

## Exemplo

 UTF8: [" + cEncodeUTF8 + "]"
cMensagem += "UTF8 -> Texto: [" + cDecodeUTF8 + "]"
ConOut(cMensagem)
Return]]>
