---
content_hash: c89fc3d1cf8bdd98bdc3e1d625b7baee604134a3d5ca57b2c119886f5cf30065
fetched_at: '2026-07-02T19:24:28.640870+00:00'
page_id: '804036871'
product: protheus
source: tdn-tec
title: Normalize
type: documentation
url: https://tdn.totvs.com/display/tec/Normalize
version: 6
---

Este método realiza a normalização de uma string UTF-8 para uma outra Forma Normal selecionada.

Atualmente, na normatização da Unicode Consortion, temos 4 diferentes tipos de formas normais para a UTF-8 que são: NFD,NFC, NFKC e NFKD.

## Sintaxe:

, ,  )]]>

```
A entrada desta função aceita a seguinte parametrização:
```

| Parâmetro de Entrada | Referência | Obrigatório | Descrição |
| --- | --- | --- | --- |
| sInput |  | X | String, no formato UTF-8 para ser normalizada |
| sConvStr | X | X | Variável string passada por referência para armazenar o a string normalizada |
| CONVMODE\_FLAG |  | X | Flags para configuração da normalização |

O parâmetro CONVMODE\_FLAG, pode ser utilizada as seguintes constantes numéricas

| Constante | Valor Numérico |
| --- | --- |
| NORMALFORM\_TONFC | 0 |
| NORMALFORM\_TONFD | 1 |
| NORMALFORM\_TONFKC | 2 |
| NORMALFORM\_TONFKD | 3 |

## Retorno

Em caso de sucesso, se a string de entrada for válida, o retorno será 0 e caso houver uma string de entrada inválida, o retorno será -1.

## Exemplo

 sExpected)
Conout("##### Conversão FALHA")
Return -1
ELSE
Conout("##### Conversão OK")
Return 0
ENDIF
Return]]>

```

```
