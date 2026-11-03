---
content_hash: 1211952f279605c1861b94df792f5e4acd4bddd4fdf4a49ba0229b0e1e93ee59
fetched_at: '2026-07-02T19:24:25.062937+00:00'
page_id: '496371131'
product: protheus
source: tdn-tec
title: Comando TCQUERY
type: documentation
url: https://tdn.totvs.com/display/tec/Comando+TCQUERY
version: 1
---

### Sintaxe completa

```
TCQUERY <cSqlExpr> ALIAS <cAlias> [ NEW ]
```

### Include

```
#include 'topconn.ch'
```

### Parâmetros

| Cláusula | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| <cSqlExpr> | C | S | Expressão caractere, constante ou variável, que contém uma Query a ser executada em um banco de dados relacional através da RDD TOPCONN. |
| ALIAS <cAlias> | C | N | Expressão caractere, constante ou variável, que contém o nome do *Alias* – ou apelido – que a query será aberta. |
| NEW |  | N | Caso especificado, indica que uma nova área de trabalho (WorkArea) deve ser criada para a abertura da tabela. Caso não especificado, a área de trabalho atual será usada, e se houver uma tabela aberta na área de trabalho atual, a mesma será fechada. |

* A sintaxe mínima do comando TCQUERY apenas poderia suprimir a cláusula NEW, que recomendamos utilizar sempre ao abrir qualquer tabela ou Query em AdvPL, para evitar fechamentos indesejados da WorkArea atual.
* Como a chamada do comando é traduzida em tempo de compilação para a função , em conjunto da Função , com os parâmetros necessários para a abertura de uma Query.
* Veja as outras formas de abertura da mesma Query em AdvPL, usando sintaxes distintas ou mesmo a chamada direta de funções. Sem dúvida usar o comando TCGENQRY é mais fácil.

### Exemplos
