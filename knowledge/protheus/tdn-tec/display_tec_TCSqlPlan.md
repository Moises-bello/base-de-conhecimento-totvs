---
content_hash: b280896e56c12f9ddf4d9a009c72cf2c8e8e3448385152806ba2b1271fda7e98
fetched_at: '2026-07-02T19:24:27.809904+00:00'
page_id: '682438912'
product: protheus
source: tdn-tec
title: TCSqlPlan
type: documentation
url: https://tdn.totvs.com/display/tec/TCSqlPlan
version: 2
---

Permite obter junto ao banco de dados o plano de execução de um statement SQL.

##### Sintaxe

```
TCSqlPlan( < cQuery >, < aResult >, [ nLevel ] )
```

##### Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cQuery | caractere | String contendo a instrução SQL para gerar o plano de execução. | X |  |
| aResult | vetor | Array por referencia, onde será retornado o plano de execução da instrução SQL. | X |  |
| nLevel | numérico | Nivel de detalhamento do plano de execução. Default=1 ( básico ). Os demais valores dependem do banco de dados da conexão atual. |  |  |

##### Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | 0 (zero) em caso de sucesso, ou um numero negativo em caso de falha. Detalhes da falha podem ser obtidos com a função TCSqlError(). |

##### Observações

O array de retorno, com os detalhes do plano de execução, retornam basicamente um array multi-dimensional com dois elementos. O primeiro elemento contém um array com a descrição dos campos com as informações que serão retornadas pelo plano de execução, e o segundo elemento contém um array multi-dimensional contendo as informações do plano de execução obtidas junto ao banco de dados.

Ambos os arrays retornados, dependem do fornecedor do banco de dados conectado, e do nível de detalhamento do plano de execução solicitado. Veja abaixo um exemplo de retorno do mesmo statement, retornado primeiro pelo MSSQL, e depois pelo POSTGRES:

```
aPlan -> ARRAY (    2) [...]
     aPlan[1] -> ARRAY (    1) [...]
          aPlan[1][1] -> ARRAY (    4) [...]
               aPlan[1][1][1] -> C (    8) [STMTTEXT]
               aPlan[1][1][2] -> C (    1) [C]
               aPlan[1][1][3] -> N (   15) [       144.0000]
               aPlan[1][1][4] -> N (   15) [         0.0000]
     aPlan[2] -> ARRAY (    2) [...]
          aPlan[2][1] -> ARRAY (    1) [...]
               aPlan[2][1][1] -> C (  144) [  |--Sort(ORDER BY:([P12133MNTDBEXP].[dbo].[TSTQRY].[CPOC] ASC))                                                                                ]
          aPlan[2][2] -> ARRAY (    1) [...]
               aPlan[2][2][1] -> C (  144) [       |--Clustered Index Scan(OBJECT:([P12133MNTDBEXP].[dbo].[TSTQRY].[TSTQRY_PK]), WHERE:([P12133MNTDBEXP].[dbo].[TSTQRY].[CPOD]='        ')) ]
```

```
aPlan -> ARRAY (    2) [...]
     aPlan[1] -> ARRAY (    1) [...]
          aPlan[1][1] -> ARRAY (    4) [...]
               aPlan[1][1][1] -> C (    7) [CFIELD1]
               aPlan[1][1][2] -> C (    1) [C]
               aPlan[1][1][3] -> N (   15) [      4096.0000]
               aPlan[1][1][4] -> N (   15) [         0.0000]
     aPlan[2] -> ARRAY (    4) [...]
          aPlan[2][1] -> ARRAY (    1) [...]
               aPlan[2][1][1] -> C ( 4096) [Sort  (cost=18.79..18.80 rows=4 width=67)]
          aPlan[2][2] -> ARRAY (    1) [...]
               aPlan[2][2][1] -> C ( 4096) [  Sort Key: cpoc]
          aPlan[2][3] -> ARRAY (    1) [...]
               aPlan[2][3][1] -> C ( 4096) [  ->  Seq Scan on tstqry  (cost=0.00..18.75 rows=4 width=67)]
          aPlan[2][4] -> ARRAY (    1) [...]
               aPlan[2][4][1] -> C ( 4096) [        Filter: (cpod = '        '::bpchar)]
```

**Atenção**

Esta função está disponivel em builds de Totvs Application Server iguais ou superiores a 20.3.1.0, e requer um DBACcess atualizado, com build igual ou superior a 22.1.1.0

##### Exemplos

```
USER FUNCTION TEST()

RETURN
```

##### Veja também

* [TCSetField](https://tdn.totvs.com/TCSetField)
* [TcGenQry](https://tdn.totvs.com/TcGenQry)
* [TcGenQry2](https://tdn.totvs.com/TcGenQry2)
* [DBStruct](https://tdn.totvs.com/DBStruct)
