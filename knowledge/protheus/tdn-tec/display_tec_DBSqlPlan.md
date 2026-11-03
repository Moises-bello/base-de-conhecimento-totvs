---
content_hash: 831e537de6d7e6cc6050fa607413e30bc7e4d64f160b749e2241c4c51ef71f70
fetched_at: '2026-07-02T19:24:27.814896+00:00'
page_id: '682440818'
product: protheus
source: tdn-tec
title: DBSqlPlan
type: documentation
url: https://tdn.totvs.com/display/tec/DBSqlPlan
version: 1
---

Permite obter junto ao banco de dados SQLITE, o plano de execução de um statement SQL.

##### Sintaxe

```
DBSqlPlan( < cQuery >, < cRDD >, < aResult >, [ nLevel ], [ cError ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cQuery | caractere | String contendo a instrução SQL para gerar o plano de execução. | X |  |
| cRDD | caractere | String contendo a RDD SQLITE a ser considerada ( SQLITE\_SYS, SQLITE\_TMP, SQLITE\_MEM ). | X |  |
| aResult | vetor | Array por referencia, onde será retornado o plano de execução da instrução SQL. | X |  |
| nLevel | numérico | Nivel de detalhamento do plano de execução. 1= básico (default), 2 = detalhado. |  |  |
| cError | caractere | String por referencia, para recuperar detalhes em caso de erro na obtenção do plano de execução. |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna .T. em caso de sucesso, .F. em caso de falha ao obter o plano de execução. |

##### Observações

O plano de execução é retornado como um array de múltiplas dimensões, onde o primeiro elemento contém um array de strings, que identifica as informações retornadas, e a partir do segundo elemento, arrays contendo os detalhes do plano de execução, vide exemplo abaixo:

```
aPlan -> ARRAY (    3) [...]
     aPlan[1] -> ARRAY (    4) [...]
          aPlan[1][1] -> C (    2) [id]
          aPlan[1][2] -> C (    6) [parent]
          aPlan[1][3] -> C (    7) [notused]
          aPlan[1][4] -> C (    6) [detail]
     aPlan[2] -> ARRAY (    4) [...]
          aPlan[2][1] -> N (   15) [         3.0000]
          aPlan[2][2] -> N (   15) [         0.0000]
          aPlan[2][3] -> N (   15) [         0.0000]
          aPlan[2][4] -> C (   17) [SCAN TABLE TSTQRY]
     aPlan[3] -> ARRAY (    4) [...]
          aPlan[3][1] -> N (   15) [        16.0000]
          aPlan[3][2] -> N (   15) [         0.0000]
          aPlan[3][3] -> N (   15) [         0.0000]
          aPlan[3][4] -> C (   28) [USE TEMP B-TREE FOR ORDER BY]
```

**Atenção**

Esta função está disponivel em builds de Totvs Application Server iguais ou superiores a 20.3.1.0.

##### Exemplos

```
USER FUNCTION TEST()

RETURN
```

##### Veja também

* [TCSqlPlan](https://tdn.totvs.com/TCSqlPlan)
* [TCSetField](https://tdn.totvs.com/TCSetField)
* [TcGenQry](https://tdn.totvs.com/TcGenQry)
* [TcGenQry2](https://tdn.totvs.com/TcGenQry2)
* [DBStruct](https://tdn.totvs.com/DBStruct)
