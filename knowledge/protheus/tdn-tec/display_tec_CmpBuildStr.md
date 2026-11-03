---
content_hash: 8a04678f3930b749155aa40eafb8e4d8e2f17fa3a1f610c6b07d6d2db48a1544
fetched_at: '2026-07-02T19:24:27.916090+00:00'
page_id: '696118096'
product: protheus
source: tdn-tec
title: CmpBuildStr
type: documentation
url: https://tdn.totvs.com/display/tec/CmpBuildStr
version: 1
---

Compara duas strings em formato nnn.nnn.nnn.nnn, considerando os quatro primeiros blocos numéricos

##### Sintaxe

```
CmpBuildStr( < cLeft >, < cRight > )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cLeft | caractere | Primeira string para comparação | X |  |
| cRight | caractere | Segunda string para comparação | X |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nEq | numérico | Retorna 0 se ambas são iguais, 1 se a primeira build é maior que a segunda, e -1 se a primeira build for menor que a segunda. |

##### Observações

* Caso a string informada tenha menos de quatro blocos de numeros, os blocos posteriores serão considerados com o valor 0 (zero)

##### Exemplos

```
#include "TOTVS.ch"

user function combuild()
  Local cLeft := GETSRVVERSION()
  Local cRight := '20.3.0.0'
  Local nCmp

  nCmp := CmpBuildStr(cLeft ,cRight )
  If nCmp > 0
     MsgStop("Build AppServer atual ['+cLeft+'] MAIOR QUE "+cRight ,"Totvs")
  ElseIf nCmp < 0
     MsgStop("Build AppServer atual ['+cLeft+'] MAIOR QUE "+cRight ,"Totvs")
  Else
     MsgInfo("Build AppServer atual ['+cLeft+'] IGUAL A "+cRight ,"Totvs")
  Endif

return
```

##### Abrangência

Application Server 19.3.1.11, 20.3.0.11, 20.3.1.0

##### Veja também

* [GetSrvVersion](https://tdn.totvs.com/GetSrvVersion)
* [TCVersion](https://tdn.totvs.com/TCVersion)
* [GetRmtVersion](https://tdn.totvs.com/GetRmtVersion)
