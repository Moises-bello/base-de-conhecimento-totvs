---
content_hash: fef43b2bbab5a301236a9810753836009ecf21f83c64c07c872032c72f6eb1ad
fetched_at: '2026-06-29T00:10:11.128627+00:00'
page_id: '452719947'
product: rm
source: tdn-rm
title: Fórmulas / Funções - P
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719947
version: 2
---

**Fórmulas / Funções - P**

* **Função PAR:** Esta variável é utilizada para retornar um parâmetro utilizado na fórmula.

**Sintaxe:** PAR

**Tipo de Retorno:** Indefinido

**Exemplo:** Se PAR > 30 e PAR < 50 Entao verdade Senao falso Fimse

* **Função PARMQRY:** Retorna o valor de um campo da query de um relatório.

**Sintaxe:** PARMQRY(STRING)

**Tipo de Retorno:** Indefinido

**Exemplos:**

1) PARMQRY(DATA) = 01/08/2002

**Observação:** DATA é um campo da base que está no relatório do gerador de relatórios que vamos incluir a fórmula.

2) Para imprimir no gerador de relatório as batidas do funcionário em uma data será utilizado uma fórmula para trazer a data (PARMQRY) e outra para retornar as batidas do dia (BATDIA). Esta fórmula colocaremos no gerador de relatórios. A DATA utilizada será o campo data da tabela de Movimentos diários dos funcionários que está em uma LD de um relatório. Fórmula criada para incluir na mesma LD do gerador de relatórios: BATDIA(PARMQRY(DATA)) = 08:15E 12:30S 14:01E 19:12

* **Função POS:** Esta função irá retornar a posição de uma substring em uma string.

**Sintaxe:** POS ( STRING , STRING )

**Tipo de Retorno:** Valor

**Exemplos:**

1) POS ('T' , TABFUNC ('NOME' , 'S')) Nome do Funcionário = ADALBERTO DE JESUS LIMA

**Execução da fórmula:**

Constante literal    T

Constante literal    NOME

Constante literal    S

Chamada a funcao TABFUNC

NOME S

Resultado da funcao TABFUNC  ADALBERTO DE JESUS LIMA Chamada a funcao POS  T ADALBERTO DE JESUS LIMA Resultado da funcao POS   8,00 Resultado da formula   8,00

2) POS ('M' , TABFUNC ('NOME' , 'S'))

Nome do Funcionário = ADALBERTO DE JESUS LIMA

**Execução da fórmula:**

Constante literal    M

Constante literal    NOME

Constante literal    S

Chamada a funcao TABFUNC  NOME S

Resultado da funcao TABFUNC  ADALBERTO DE JESUS LIMA

Chamada a funcao POS  M ADALBERTO DE JESUS LIMA

Resultado da funcao POS   22,00 Resultado da formula   22,00

* **Função PROXREGSQL:** Esta variável avança para o próximo registro da sentença SQL

**Sintaxe:** PROXREGSQL (CÓDIGO DA CONSULTA SQL)

**Tipo de Retorno:** Indefinido

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
