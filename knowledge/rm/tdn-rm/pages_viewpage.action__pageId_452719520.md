---
content_hash: def601382a8fbea169afed970b1a1a870581a5c87ddaa01067b3e6f31449edd7
fetched_at: '2026-06-29T00:10:08.472087+00:00'
page_id: '452719520'
product: rm
source: tdn-rm
title: Fórmulas / Funções - E
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719520
version: 6
---

**Fórmulas / Funções - E**

* **Função EXECSQL:** Executa uma consulta SQL previamente cadastrada.

**Sintaxe:** EXECSQL ('CÓD. DA CONSULTA')

**Tipo de Retorno:** Valor

* **Função EXTRAAUTO:** Retorna o número de extras autorizadas ( em minutos ) em uma data.

**Sintaxe:** EXTRAAUTO (DATA )

**Tipo de Retorno:** Valor

**Exemplo:** EXTRAAUTO('/04/2001') = retornar as horas extras realizadas no dia 26/04/2001.

* **Função EXTRAEXEC:** Retorna o número de extras autorizadas ( em minutos ) em uma data.

**Sintaxe:** EXTRAEXEC(DATA )

**Tipo de Retorno:** Valor. A função terá diferente comportamento se executada diretamente pela fórmula ou executada pelo cálculo;

Pela Fórmula - Calculará de acordo com a tabela AAFHTFUN, retornando as extras executadas.

Pelo cálculo - Calculará de acordo com as ocorrências do dia, retornando as extras executadas. Isso deve, a tabela AAFHTFUN que pode não conter valores para um determinado tipo de extra.

**Exemplo:** EXTRAEXEC('26/04/2001') = retornar as horas extras executadas no dia 26/04/2001.

* **Função EXTRAFORAHOR:** Retorna as horas extras efetuadas em um dia, antes do horário, depois do horário, ou todas as extras efetuadas no dia

**Sintaxe:** EXTRAFORAHOR (DATA , STRING)

**Tipo de Retorno:** Valor O campo String deve ser preenchido com as seguintes opções:

0 - Para retornar todas as horas extras efetuadas na data.

1 - Para retornar todas as horas extras efetuadas antes do horário do funcionário. As extras têm que estar em intercessão com o horário do funcionário.

2 - Para retornar todas as horas extras efetuadas depois do horário. As extras têm que estar em intercessão com o horário do funcionário.

3 - Para retornar o número de extras efetuadas em dia que o funcionário não tem jornada a ser cumprida. Exemplo: Dias de descanso, compensado, ou feriado.

**Exemplos:**

Período atual: 01/03 à 31/03 Horário do Funcionário: 22:00 às 05:00

Batidas: 31/05 QUA - 06:00S 21:00 EEXTRAFORAHOR ('31/03/2004' , '0') 0

- Total Resultado = 120 EXTRAFORAHOR ('31/03/2004' , '1')

1 - Antes Resultado = 60 EXTRAFORAHOR ('01/03/2004' , '2')

2 - Depois Resultado = 60 EXTRAFORAHOR ('01/03/2004' , '3')

3 - Sem jornada Resultado = 0

* **Função EXTRAFORAHORJOR:** Retorna as horas extras efetuadas na jornada, antes do horário, depois do horário, ou todas as extras efetuadas na jornada.

**Sintaxe:** EXTRAFORAHORJOR (DATA,STRING)

**Tipo de Retorno:** Valor O campo String deve ser preenchido com as seguintes opções: 0 - Para retornar todas as horas extras efetuadas na jornada que inicia na data informada.

1 - Para retornar todas as horas extras efetuadas antes da jornada que inicia na data informada.. As extras têm que estar em intercessão com o horário do funcionário.

2 - Para retornar todas as horas extras efetuadas depois da jornada que inicia na data informada.. As extras têm que estar em intercessão com o horário do funcionário.

3 - Para retornar o número de extras efetuadas em dia que o funcionário não tem jornada a ser cumprida. Exemplo: Dias de descanso, compensado, ou feriado.

**Exemplo:**

Horário do funcionário: 22:00 às 05:00

Período atual: 01/03/04 à 31/03/04

Batidas do funcionário: 30/03 TER - 05:30S 20:00E 31/03 QUA - 06:00S 07:00E 10:00S 20:30E EXTRAFORAHORJOR ( FPM-1 , '0')

Resultado = 180 EXTRAFORAHORJOR ( FPM-1 , '1')

Resultado = 120 EXTRAFORAHORJOR ( FPM-1 , '2')

Resultado = 60 EXTRAFORAHORJOR ( FPM , '0') Resultado = 270 EXTRAFORAHORJOR ( FPM , '1')

Resultado = 90 EXTRAFORAHORJOR ( FPM , '2')

Resultado = 0

* **Função EXTRAPARCIALINTREF:** Retorna o número de extras realizadas no início, no final ou em todo o intervalo de refeição.

**Sintaxe:** EXTRAPARCIALINTREF (DATA', STRING, DATA, STRING)

**Tipo de Retorno:** Valor O campo String deve ser preenchido com as seguintes opções: Primeira String: Número do intervalo de refeição desejado Segunda String:

1 - Extras realizadas no Início do intervalo de refeição.

2 - Extras realizadas no Fim do intervalo de refeição.

3 - Extras realizadas durante todo o intervalo de refeição.

**Observação:**

A função de fórmula EXTRAPARCIALINTREF somente apura valores dos horários que possuem Intervalo de Refeição (Ausência Planejada) cadastrados. Não deve ser utilizada caso o horário seja flexível.

**Exemplo:**

Horário: 02:00ent1 - 04:00sai1 - 05:00ent2 - 08:00sai2 - 09:00ent3 - 12:00sai3 - 13:00ent4 - 16:00sai4 - 17:00ent5 19:00sai5

Intervalo de refeição: 04:00 - 05:00 | 08:00 - 09:00 | 12:00 - 13:00 | 16:00 - 17:00

Batidas:

Data                 Dia        ent1        sai1        ent2        sai2        ent3        sai3        ent4        sai4        ent5        sai5

16/05/2008      SEX     02:00      04:10     04:50      08:15       08:45     12:20      12:40      16:05      16:55     19:00

17/05/2008      SAB    02:00      04:20      05:00      08:15       09:00      12:05     13:00       16:10      17:00    19:00

18/05/2008     DOM    02:00      04:00      04:55      08:00       08:50      12:00      12:45      16:00      16:40    19:00

**Sintaxe da Fórmula:**

EXTRAPARCIALINTREF ('16/05/2008', 4, '18/05/2008',

1) Retorna as extras realizadas no quarto intervalo de refeição cadastrado no horário no início do intervalo de refeição, ou seja verifica as batidas do horário do dia 16/05/2008 sai4 16:05 = 00:05 minutos de extra e 17/05/2008 sai4 16:10 = 00:10 minutos de extra. Resultado: 15,0000

* **Função EXTRAPER:** Retorna o número de extras ( em minutos ) em um período determinado.

**Sintaxe:** EXTRAPER (DATA,INICIO,FIM )

**Tipo de Retorno:** Valor

**Exemplo:** EXTRAPER('/10/2000',1080,1320) = retornar as horas extras efetuadas no dia 26/10/2000 no período de 18:00 às 22:00 horas.

**Observação:** O Início e o Fim devem ser informados em minutos.

* **Função EXTRAPERAUTO:** Retorna o número de extras autorizadas ( em minutos ) em uma data dentro de um intervalo de horas.

**Sintaxe:** EXTRAPERAUTO (DATA,INICIO,FIM )

**Tipo de Retorno:** Valor

**Exemplo:**

Funcionário trabalhou em um dia de descanso de 08:00 as 12:00 realizou 04:00 horas extras, porém foram autorizadas somente 02:00 extras. EXTRAPERAUTO ('07/04/2007', 480, 720). Resultado da fórmula = 120.(minutos)

**Observação:** O Início e o Fim devem ser informados em minutos.

* **Função EXTRAPERINTREF:** Retorna o número de extras realizadas no intervalo de refeição em um período.

**Sintaxe:** EXTRAPERINTREF (DT,INTREF,DT)

**Tipo de Retorno:** Valor

**Observação:** A função de fórmula EXTRAPERINTREF somente apura valores dos horários que possuem Intervalo de Refeição (Ausência Planejada) cadastrados. Não deve ser utilizada caso o horário seja flexível.

**Exemplo:** EXTRAPERINTREF (IPM ,1, FPM) Extras realizadas no período do primeiro intervalo de refeição cadastrado no dia (do primeiro ao último dia do período) EXTRAPERINTREF (IPM ,2 , FPM) Extras realizadas no período do segundo intervalo de refeição cadastrado no dia (do primeiro ao último dia do período)

* **Função EXTRAJORDIANOT**: Retorna a quantidade de horas extras diurnas e noturnas realizadas durante a jornada de trabalho. As horas extras diurnas correspondem às realizadas fora do período de adicional noturno, enquanto as horas extras noturnas são aquelas realizadas dentro do período do adicional noturno.

  Importante

  Se o período de adicional noturno não for configurado, a fórmula não calculará as horas extras, tanto diurnas quanto noturnas, e o resultado será 0.

  Ao associar a função de fórmula a eventos do movimento ou banco de horas, as ocorrências de extras toleradas e extras compensadas são desconsideradas no cálculo do total de horas. Não recomendamos comparar os resultados da função de fórmula executada manualmente com aqueles obtidos quando a função está associada a esses eventos, visto que as ocorrências de extras toleradas e extras compensadas são montadas na etapa de cálculo.

**Sintaxe**: EXTRAJORDIANOT(DATA, STRING)  
**Tipo de Retorno**: Valor das horas extras executadas na jornada, em minutos.

### **Parâmetros:**

* + - **DATA**: Data da jornada de trabalho.
    - **STRING**: Deve ser preenchido com '1' ou '2':
      * **'1'** - Retorna a quantidade de horas extras diurnas, em minutos.
      * **'2'** - Retorna a quantidade de horas extras noturnas, em minutos.

### **Exemplos de utilização:**

* + - **Horas extras diurnas**:
      * **Horário do funcionário**: 07:00-11:00 / 13:00-17:00
      * **Adicional noturno**: Início às 22:00 e fim às 05:00
      * **Batidas realizadas**: 06:00-11:00 / 13:00-18:00
      * **Intervalo de horas extras:** 06:00-07:00 / 17:00-18:00

**EXTRAJORDIANOT('Data da jornada', '1')**Resultado = 120

* + - **Horas extras noturnas**:
      * **Horário do funcionário**: 07:00-11:00 / 13:00-17:00
      * **Adicional noturno**: Início às 22:00 e fim às 05:00
      * **Batidas realizadas**: 22:00-23:00
      * **Intervalo de horas extras:** 22:00-23:00

**EXTRAJORDIANOT('Data da jornada', '2')**Resultado = 60

* + - **Horas extras diurnas e noturnas**:
      * **Horário do funcionário**: 22:00-02:00 / 03:00-04:00
      * **Adicional noturno**: Início às 22:00 e fim às 05:00
      * **Batidas realizadas**: 21:00-02:00 / 03:00-04:45
      * **Intervalo de horas extras:** 21:00-22:00 / 04:00-04:45

**EXTRAJORDIANOT('Data da jornada', '1')**Resultado = 60

**EXTRAJORDIANOT('Data da jornada', '2')**Resultado = 45

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
