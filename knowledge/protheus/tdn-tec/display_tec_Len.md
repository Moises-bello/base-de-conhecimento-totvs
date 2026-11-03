---
content_hash: 8875e2d124ba88f4259afe4a2ed4615f677005fe084edde2fab77d37b6a21563
fetched_at: '2026-07-02T19:24:18.913293+00:00'
page_id: '221553723'
product: protheus
source: tdn-tec
title: Len
type: documentation
url: https://tdn.totvs.com/display/tec/Len
version: 2
---

Len

Retorna o tamanho de uma variável.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xParam | qualquer | Variável que será avaliada | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nCount | numérico | Retorna o tamanho de **xParam**. |

## Observações

* Se a cadeia de caracteres especificada for nula (""), a função LEN() retornará o valor zero. Entretanto, o caractere nulo, CHR(0), tem o comprimento de uma (1) posição.
* Deve-se lembrar que no AdvPL cada array multidimensional é composto por vários subarrays. Além disso, estes subarrays não precisam, necessariamente, ter dimensões uniformes.
* A tabela abaixo demonstra os retornos da função LEN para campos criados no SGBD:

  | Tipo | Retorno |
  | --- | --- |
  | C | O tamanho retornado corresponde ao tamanho de string máxima que pode ser armazenado na coluna. |
  | D | É retornado sempre 8 bytes. |
  | L | É retornado sempre 1 byte. |
  | M | É retornado sempre 10 bytes.  Observação: É importante lembrar que, este valor é retornado por compatibilidade e não corresponde a capacidade real de armazenamento da coluna. O tamanho máximo de armazenamento de uma coluna do tipo "M" está condicionada ao driver RDD utilizado. |
  | N | Juntamente com o valor retornado na quarta posição, quantidade de decimais, informa a capacidade de armazenamento de valores numéricos no campo. |

## Exemplos

cppEclipsetruefalse
