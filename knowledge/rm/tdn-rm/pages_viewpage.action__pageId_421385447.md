---
content_hash: d243823d0b98e1f7f83baf0442cb2c9b80db5fa747ac02cc02bd6593114aadb0
fetched_at: '2026-06-29T00:09:16.037515+00:00'
page_id: '421385447'
product: rm
source: tdn-rm
title: Insumo Receita com Derivação - Aba Insumo Derivado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385447
version: 4
---

---

Com o objetivo de derivar receita do(s) contrato(s) de venda do projeto, sendo possível associar contratos de outras revisões ou até mesmo outros projetos foi criado o Insumo Derivado de Receita, que possui características do Insumo Receita combinado com as características do Insumo Derivado, assim é possível criar um Insumo associado a uma regra de derivação que possa calcular automaticamente a receita. Para insumos Receita com Derivação é possível associar apenas o tipo de derivação Tarefa X Cronograma. A regra de derivação permite que sejam associados diferentes contratos de diferentes projetos de uma mesma coligada.

**Funções de Fórmulas**

As funções de fórmula auxiliam no cálculo de valores relacionados com os períodos do contrato que estão em equivalência com os períodos do cronograma. As funções retornam valores de acordo com:

* Valor Planejado do Contrato: Retorna o valor definido no campo Valor Previsto na edição do período do contrato para o período do cronograma.
* Valor Medido: Retorna o valor definido no campo Valor Medido do Contrato para o período do Cronograma.
* Valor Liberado: Retorna o valor definido no campo Valor Liberado do Contrato para o período do Cronograma.

Foram inseridas no sistema as fórmulas abaixo que resgatam valores de acordo com o parâmetro de busca:

* VLRPDOCNTPLAN (0) – Valor planejado do Contrato por número de periodo;
* VLRPDOCNTPLAN (1) – Valor planejado do Contrato por dias corridos;
* VLRPDOCNTMED (0) – Valor medido do contrato por número de período;
* VLRPDOCNTMED (1) - Valor medido do contrato por dias corridos;
* VLRPDOCNTREAL (0) – Valor liberado do contrato por número de período;
* VLRPDOCNTREAL (1) - Valor liberado do contrato por dias corridos;

**Parâmetros de Busca**

O parâmetro de busca define como será a busca do valor no período do contrato, sendo 0 (zero) para a busca por Número do Período e 1 (um) para a busca por Dias Corridos.

* **Número do período(0):**

Considera que os períodos do cronograma do projeto do contrato são idênticos aos períodos do cronograma do projeto corrente, portanto os valores das funções de fórmula serão definidos a partir dos períodos do contrato associados aos períodos do cronograma.

**Exemplo:**

PROJETO CORRENTE

Cronograma: 3 períodos mensais com início em 01/01/2011 e fim em 31/03/2011.

Pdo 01            Pdo 02            Pdo 03

01/01/2011      01/02/2011      01/03/2011 31/01/2011

28/02/2011      31/03/2011

PROJETO DO CONTRATO 1

Contrato 1: 3 períodos quinzenais começando em 1/01/2011 e terminando em 15/02/2011.

Pdo 0001         Pdo 0002        Pdo 0003

01/01/2011      16/01/2011     01/02/2011

15/01/2011      31/01/2011     15/02/2011

250,00            120,00            50,00

Depois de associar os períodos do contrato aos períodos do cronograma, ficará da seguinte maneira:

* Pdo 01 – Pdo 0001
* Pdo 01 – Pdo 0002
* Pdo 02 – Pdo 0003

De acordo com o exemplo, o período 01 do cronograma compreende 100% dos períodos 0001 e 0002 do contrato e o período 02 do cronograma compreende 100% do período 0003 do contrato. Logo, o cálculo utilizará valores completos dos períodos 0001, 0002 e 0003 do contrato.

O resultado será a soma dos períodos:

Custo Unitário/ Valor Unitário = 250,00 + 120,00 + 50 = 420,00

* **Dias corridos(1):**

Quando isto não for verdadeiro. Neste caso as datas do período do contrato serão consideradas para calcular o valor de cada período do cronograma.

**Exemplo:**

PROJETO CORRENTE

Cronograma: 3 Períodos mensais com início em 01/01/2011 e fim em 31/03/2011.

Pdo 01            Pdo 02             Pdo 03

01/01/2011      01/02/2011       01/03/2011

30/01/2011      28/02/2011       30/03/2011

PROJETO DO CONTRATO 2

Contrato 2: 3 períodos personalizados como 20 com início em 01/01/2011 e fim em 01/03/2011.

Pdo 0001        Pdo 0002         Pdo 0003

01/01/2011     21/01/2011      10/02/2011

20/01/2011     09/02/2011      01/03/2011

200,00               350,00            150,00

Depois de associar os períodos do contrato aos períodos do cronograma, ficará da seguinte maneira:

* Pdo 01 – Pdo 0001
* Pdo 01 – Pdo 0002
* Pdo 02 – Pdo 0002
* Pdo 03 – Pdo 0002
* Pdo 03 – Pdo 0003

De acordo com o exemplo, os períodos 01, 02 e 03 do cronograma são parcialmente equivalentes aos períodos 0001, 0002 e 0003 do contrato. Levando em consideração o percentual de equivalência temos:

* O período 0001 do Contrato é 100% equivalente ao período 01 do Cronograma > (100% = 200,00);
* O período 0002 do Contrato é 55% equivalente ao período 01 do Cronograma (55% = 192,50);
* O período 0002 do Contrato também é 45% equivalente ao período 02 do Cronograma (45% = 157,50);
* O período 0003 do Contrato é 90% equivalente ao período 02 do Cronograma (90% = 135,00);
* O período 0003 do Contrato também é 10% equivalente ao período 03 do Cronograma (10% = 15,00);

O cálculo deve ser efetuado de acordo com cada período do cronograma. Assim teremos:

* Período 01 = 200,00 + 192,50 = 392,50
* Período 02 = 157,50 + 135,00 = 292,50
* Período 03 = 15,00 Custo Unitário/ Valor Unitário = 700,00

**Observação**

* Os valores resgatados pela derivação deverão incidir sobre a quantidade da tarefa no momento do calculo do projeto, assim como o tipo de derivação Tarefa X Cronograma permite para o insumo do tipo derivado;
* Permitir somente contratos de serviço;
* As tarefas com esse tipo de insumo associado não devem influenciar no valor do projeto, seguindo o mesmo comportamento do insumo de receita. Os períodos do cronograma devem estar associados aos períodos do cronograma.
