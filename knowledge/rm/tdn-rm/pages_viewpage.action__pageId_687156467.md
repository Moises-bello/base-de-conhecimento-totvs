---
content_hash: cd1afc07261a8ce607cbcb1702776a192deeba907b0794d4960d9d943a0ff046
fetched_at: '2026-06-29T00:11:20.623502+00:00'
page_id: '687156467'
product: rm
source: tdn-rm
title: Cálculo do DSR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687156467
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esse cálculo será para processar somente os domingos do período global de produção, ou seja, sempre será lançado no domingo. Cálculo do Somatório da produção / Dias de Produção na semana.

Para o cálculo ser efetuado é necessário criar a tarefa DSR, regra DSR com tipo de cálculo sem cálculo interno e prioridade maior que as prioridades das tarefas de produção, finalidade da tarefa DSR e associação de regra para DSR. Por fim informar a tarefa em Parametrizador / Folha Agrária / Parâmetros da Filial / Cálculo.

Será considerado para dias de produção:

* Somatório dos dias da semana anterior ao domingo até a segunda-feira que houve tarefas de prioridade menor que a prioridade da Tarefa do DSR.
* Soma dos dias de férias. **Vide caso 1**
* Soma dos dias de licença maternidade. **Vide caso 2**
* Soma dos dias do primeiro DSR na semana de admissão. **Vide caso 3**
* Soma dos dias na data de demissão. **Vide caso 4**

**Caso 1**: Retorno e saída de férias após segunda feira na semana *que teve produção*.

* Será calculado o valor de um dia das férias através do recibo de férias utilizando o código de cálculo 38 de férias (soma dos valores dividido pela soma das referências).
* Multiplicar o valor de um dia de férias pelos dias de férias da semana.
* Acumula o valor da produção com valor encontrado na semana para valorar o DSR da semana em questão.

**Observação:**

01 - O mesmo cálculo será feito para quando as férias iniciarem no meio da semana, porém com o detalhe de descontar o valor de um dia de férias referente ao domingo da primeira semana das férias. Por exemplo o início do gozo de férias durante a semana (13/05/2021 - quinta feira), então, soma-se a produção daquela semana em questão em que iniciou suas férias (13/05/2021 a 22/05/2021) e encontra-se o valor de um dia das férias (conforme eventos com código de cálculo 38) e esse valor encontrado distribui para 13, 14 e 15, e então, soma-se o total da semana e divide por 6, encontrando assim o DSR do dia 16/05/2021. Como o mesmo encontrava-se férias no dia 16/05 e teve o início das férias fora da segunda-feira, o valor apurado desta primeira semana (DSR) será realizado com a consistência do valor de 1 dia férias subtraindo o DSR apurado, sendo positivo paga o DSR devido desta semana.

02 – Quando o fim do período de gozo for sábado 22/05/2021(conforme exemplo 13/05/2021 a 22/05/2021) deve remunerar o domingo. O procedimento será a soma de um dia referente ao evento de férias com código de cálculo 38 divide pelos dias gozo dentro da semana, de forma a remunerar o domingo 23/05/2021, sem subtrair o valor de um dia de férias porque esse domingo em que é devido DSR não estava no dentro do período gozo de férias.

**Caso 2**: Retorno e saída de licença maternidade dentro da semana que teve produção.

* Será calculado o valor de um dia de Licença Maternidade através da ficha financeira utilizando o código de cálculo 17 de licença maternidade (soma dos valores dividido pela referência).
* Multiplica o valor de um dia de Licença Maternidade pelos dias restantes da semana para cálculo do DSR.
* Acumula o valor da produção com valor encontrado na semana para valorar o DSR da semana em questão.
* Serão obtidos os eventos na ficha financeira pela competência de pagamento.

**Caso 3**: admissão (primeiro DSR a partir da admissão).

* Será calculado o valor dos dias da produção a partir da admissão até o sábado seguinte (somando o valor).
* O valor obtido divide pelo número de dias trabalhados nesta primeira semana.
* Ressalva (havendo ausência entre admissão e sábado) perde o primeiro DSR

**Caso 4**: Demissão.

* Caso a data de demissão do funcionário for sábado e tenha produção, o mesmo terá direito ao DSR desta semana, na qual corresponde ao próximo domingo.
* Caso contrário, ou seja, não tenha produção no sábado da demissão, perde o DSR da semana corrente.

**Caso 5**: Quando o período de cálculo iniciar no meio da semana, deverá ser considerado o DSR desde o início da semana.

* Calcular as produções de segunda a sábado que compreende a semana do DSR (dias anteriores ao DSR) dividindo por 6, exceto os casos específicos de admissão, neste caso soma-se os dias trabalhados até o sábado e divide pela quantidade de dias trabalhados da primeira semana). Mesmo sendo sábado compensado também irá dividir por 6, excetuando admissão na primeira semana.

Casos que perde DSR:

* Ter falta com o campo “Desconta DSR” marcado na PFHSTFALTA na semana.
  + **DESCONTADSR = 1 (Marcado) -** significa que vai descontar o DSR então considera a falta e **perde o DSR**
  + **DESCONTADSR = 0 OU NULL (Desmarcado) -** significa que não vai descontar o DSR então considera que **vai abonar DSR** nesse caso **não perde DSR**
* Rescisão na semana sem produção no sábado.

## **02. EXEMPLO DE UTILIZAÇÃO**

**Exemplo do caso 1:**

Funcionário com Período de gozo de férias de 17/05/2021 a 26/05/2021

Férias - iniciando na segunda-feira e terminando na quarta-feira, será feito o seguinte cálculo para a semana do término das férias:

Semana: 24/05/2021 a 30/05/2021

DATA            TIPO        FORMA       SITUAÇÃO         VALOR

-----------------------------------------------------------------------------------

24/05/2021    Normal    Férias           Normal                257,02

25/05/2021    Normal    Férias           Normal                257,02

26/05/2021    Normal    Férias           Normal                257,02

27/05/2021    Normal    Produção      Normal                  66,31

28/05/2021    Normal    Produção      Normal                  66,31

29/05/2021    Normal    Produção      Normal                  66,31

------------------------------------------------------------------------------------

- Produção - Quantidade: 3 - Total: 198,93

- Férias - Quantidade: 3 - Total: 771,06

DSR: 30/05/2021

Equação: (Total Produção + Total Férias) / (Quantidade Produção + Quantidade Férias)

Cálculo: (198,93 + 771,06) / (3 + 3) = 969,99 / 6 = 161,67

**Observação:**

01 - O mesmo cálculo será feito para quando as férias iniciarem no meio da semana, porém com o detalhe de descontar o valor de um dia de férias referente ao domingo da primeira semana das férias. Por exemplo o início do gozo de férias durante a semana (13/05/2021 - quinta feira), então, soma-se a produção daquela semana em questão em que iniciou suas férias (13/05/2021 a 22/05/2021) e encontra-se o valor de um dia das férias (conforme eventos com código de cálculo 38) e esse valor encontrado distribui para 13, 14 e 15, e então, soma-se o total da semana e divide por 6, encontrando assim o DSR do dia 16/05/2021. Como o mesmo encontrava-se férias no dia 16/05 e teve o início das férias fora da segunda-feira, o valor apurado desta primeira semana (DSR) será realizado com a consistência do valor de 1 dia férias subtraindo o DSR apurado, sendo positivo paga o DSR devido desta semana.

02 – Quando o fim do período de gozo for sábado 22/05/2021(conforme exemplo 13/05/2021 a 22/05/2021) deve remunerar o domingo. O procedimento será a soma de um dia referente ao evento de férias com código de cálculo 38 divide pelos dias gozo dentro da semana, de forma a remunerar o domingo 23/05/2021, sem subtrair o valor de um dia de férias porque esse domingo em que é devido DSR não estava no dentro do período gozo de férias.

**Exemplo do caso 5:**

**Período de Cálculo da Produção Agrária:** 24/04/2021 a 23/05/2021 (Primeiro dia em um sábado)

Semana: 19/04/2021 a 25/04/2021

       DATA      TIPO      FORMA           SITUAÇÃO    VALOR

    --------------------------------------------------------

    19/04/2021   Normal    Produção        Normal     155,96

    20/04/2021   Normal    Produção        Normal     155,96

    21/04/2021   Normal    Produção        Normal     155,96

    22/04/2021   Normal    Produção        Normal     155,96

    23/04/2021   Normal    Produção        Normal     155,96

    24/04/2021   Normal    Produção        Normal      79,75

    --------------------------------------------------------

    - Produção - Quantidade: 6 -  Total: 859,55

    DSR: 25/04/2021

    Equação: Total Produção / Quantidade Produção

    Cálculo: 859,55 / 6 = 143,26

**Observação**: Deve ser considerado o período anterior, mesmo não estando no período local ou global.

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
