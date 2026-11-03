---
content_hash: c0bea92a67c6f8c91ce7863334a20e594ad8670036e3cd10493237f1e8509632
fetched_at: '2026-06-29T00:10:06.772154+00:00'
page_id: '452719337'
product: rm
source: tdn-rm
title: Fórmulas / Funções - H (PTO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719337
version: 13
---

**Fórmulas / Funções - H**

* **Função H:** Retorna o número de horas em formato String ( em minutos ).

**Sintaxe: H** (HORA)

**Tipo de Retorno:** String

**Exemplo:**

H (':00')

Resultado da fórmula = 480

* **Função HADNOT:** Retorna o número de horas ou vezes trabalhadas no período de adicional noturno ( 22:00 às 05:00) no período de datas determinado. (0 – horas, 1- total de dias).

**Sintaxe:** HADNOT: (DATA, DATA, STRING)

**Tipo de Retorno:** Valor

**Exemplo:**

1- HADNOT ('01/05/1999', '31/05/1999' , '0') Desse modo, o sistema irá retornar o número de horas de adicional noturno no período.

2- HADNOT ('01/05/1999', '31/05/1999' , '1') Desse modo, o sistema irá retornar o número de dias de adicional noturno no período.

* **Função HOJE:** Retorna a data do dia de hoje.

**Sintaxe:** HOJE

**Tipo de Retorno:** Data

* **Função HORARIOCODDIA:** Retorna o código do horário do funcionário em uma data.

**Sintaxe:** HORARIOCODDIA (DATA)

**Tipo de Retorno:** String

**Exemplo:**

HORARIOCODDIA ('06/01/2002')

Resultado da fórmula = 0001

* **Função HORARIOCODDIAALTER:** Retorna O código do horário do funcionário em uma data considerando horário alternativo.

**Sintaxe:** HORARIOCODDIAALTER (DATA)

**Tipo de Retorno:** String

**Exemplo 1:**

HORARIOCODDIAALTER ('02/08/2025')

                       Horário do Funcionário  –  Código:  0017 -   Descrição : Horário Noturno : 22:00 - 22:59 - 23:59 - 05:00

  Horário Alternativo – Código: ALTNOT  Descrição : Horário Noturno Alternativo : 23:50 - 01:00 - 02:00 - 07:00

  Batidas do funcionário: 02/08/2025 – 23:10E

                                      03/08/2025 -           01:00S - 02:00E - 07:00S

 Fórmula de cálculo: HORARIOCODDIAALTER ('02/08/2025')

 Resultado da fórmula = ALTNOT

**Exemplo 2:**

HORARIOCODDIAALTER ('09/08/2025')

                      Horário do Funcionário –  Código:  0017 -   Descrição : Horário Noturno : 22:00 - 22:59 - 23:59 - 05:00

 Horário Alternativo – Código: ALTNOT  Descrição : Horário Noturno Alternativo : 23:50 - 01:00 - 02:00 - 07:00

 Batidas do funcionário: 09/08/2025 – 21:000E

                                      10/08/2025 -           22:59S - 23:59E - 04:50S

 Fórmula de cálculo: HORARIOCODDIAALTER ('09/08/2025')

Resultado da fórmula = 0017

Importante:

* O sistema verifica a aproximação do horário executado com o horário padrão e Alternativo.
* A função de fórmula HORARIOCODDIAALTER irá retornar o horário padrão se na data o funcionário estiver afastado ou de Férias

* **Função HORARIODIA:** Retorna as batidas do horário do funcionário em uma data.

**Sintaxe:** HORARIODIA (DATA)

**Tipo de Retorno:** String

**Exemplo:**

HORARIODIA ('06/11/2000') = 22:00E 22:59S 23:59E

**Observação:**

A função de fórmula HORARIODIA não verifica a situação do funcionário antes de retornar o horário a ser trabalhado. Caso o funcionário se encontre Afastado, Demitido ou de Férias a variável retornará o horário do funcionário para o dia pesquisado.

**Exemplo:**

Horário do Funcionário: 12:00 às 18:00 Período de férias: 17/03/2003 à 16/04/2003 HORARIODIA('12/03/2003')

Resultado da fórmula = '12:00 - 18:00' HORARIODIA('18/03/2003')

Resultado da fórmula = '12:00 - 18:00'

* **Função HORARIODIAALTER:** Retorna as batidas do horário do funcionário em uma data, considerando também o horário alternativo.

**Sintaxe:** HORARIODIAALTER (DATA)

**Tipo de Retorno:** String

**Exemplo 1:**

HORARIODIAALTER ('02/08/2025')

Horário do Funcionário  –  22:00 - 22:59 - 23:59 - 05:00

  Horário Alternativo –          23:50 - 01:00 - 02:00 - 07:00

  Batidas do funcionário: 02/08/2025 – 23:10E

                                      03/08/2025 -           01:00S - 02:00E - 07:00S

 Fórmula de cálculo: HORARIODIAALTER ('02/08/2025')

 Resultado da fórmula = 23:50 - 01:00 - 02:00 - 07:00

**Exemplo 2:**

HORARIODIAALTER ('09/08/2025')

                     Horário do funcionário   – 22:00 - 22:59 - 23:59 - 05:00

Horário Alternativo  –        23:50 - 01:00 - 02:00 - 07:00

Batidas do funcionário: 09/08/2025 – 21:000E

                                      10/08/2025 -           22:59S - 23:59E - 04:50S

Fórmula de cálculo: HORARIODIAALTER ('09/08/2025')

Resultado da fórmula = 22:00 - 22:59 - 23:59 - 05:00

Importante

* O sistema verifica a aproximação do horário executado com o horário padrão e Alternativo.
* A função de fórmula HORARIODIAALTER irá retornar o horário padrão se na data o funcionário estiver afastado ou de Férias

* **Função HORARIODIASIT:** Retorna o horário do funcionário em uma data verificando a situação do funcionário.

**Sintaxe:** HORARIODIASIT(DATA)

**Tipo de Retorno:** String

**Exemplo:**

HORARIODIASIT ('06/11/2000')

Resultado da fórmula = 22:00E 22:59S 23:59E

**Observação:**

A função de fórmula HORARIODIASIT verifica a situação do funcionário antes de retornar o horário a ser trabalhado. Caso o funcionário se encontre Afastado, Demitido ou de Férias a variável retornará vazio para o dia pesquisado.

**Exemplo:**

Horário do Funcionário: 12:00 às 18:00

Período de férias: 17/03/2003 à 16/04/2003

HORARIODIA('12/03/2003')

Resultado da fórmula = '12:00 - 18:00'

HORARIODIA('18/03/2003')

Resultado da fórmula = ' '

* **Função HORARIOIND:** Retorna o horário do funcionário em um índice específico.

**Sintaxe:** HORARIODIA (ÍNDICE DO HORÁRIO)

**Tipo de Retorno:** String

**Exemplo:**

Horário do funcionário X:

Índice Horário

1 22:00E

2 01:00S 02:00E 05:00S 22:00E

3 01:00S 02:00E 05:00S 22:00E

4 01:00S 02:00E 05:00S 22:00E

5 01:00S 02:00E 05:00S 22:00E

6 01:00S 02:00E 05:00S

7 DESC(00:00 - 24:00)

Teste da fórmula HORARIOIND (5)

Resultado da fórmula = 01:00S 02:00E 05:00S 22:00E

* **Função HORARIOMAISDIATRAB:** Retorna o código do horário que o funcionário mais trabalhou em um intervalo de datas.

**Sintaxe:** HORARIOMAISDIATRAB (DATA, DATA)

**Tipo de Retorno:** String

**Exemplo:** HORARIOMAISDIATRAB (IPM , FPM) Resultado da fórmula = 00016

* **Função HORARIOTURNODIA:** Verifica se no dia o funcionário está fazendo horário de turno de revezamento.

**Sintaxe:** HORARIOTURNODIA (DATA)

**Tipo de Retorno:** Valor No cadastro de horário do funcionário existe um campo chamado "Horário com turno de revezamento", esta função irá verificar no histórico de horário do funcionário se na data escolhida o funcionário estará trabalhando ou não em um horário que esteja com este campo marcado. Se for verdade o sistema retornará 1 (um), se for falso o sistema retornará 0 (zero).

**Exemplos:**

1) Verificar se no dia 06/01/2002 o funcionário está trabalhando em um horário de turno de revezamento.

HORARIOTURNODIA ('06/01/2002')

Resultado da fórmula = 1

2) Contar quantos dias do período atual o funcionário trabalhará no horário de turno de revezamento.

DECL DT, CONT; SETVAR (DT, IPM);

REPITA SE HORARIOTURNODIA (DT) > 0 ENTAO SETVAR (CONT, CONT+1)

FIMSE; SETVAR (DT, DT+1) ATE (DT=FPM+1); CONT

Teste da fórmula = 16

* **Função HORASABONO:** Retorna o número de horas (em minutos) de abono em um determinado dia.

**Sintaxe:** HORASABONO (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

HORASABONO ('/11/2000')

Resultado da fórmula = 480

* **Função HORASABONOADNOT:** Retorna o número de horas (em minutos) de abono dia a dia durante o período de adicional noturno.

**Sintaxe:** HORASABONOADNOT (DATA, DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário: 22:00E 05:00S

Adicional Noturno: 22:00 às 05:00

Batidas do funcionário: 02/08/2004 - 23:00E , 03/08/2004 - 04:00S

HORASABONOADNOT ('/08/2004', '/08/2004').

Desse modo, o sistema irá retornar 120 horas de abono do Adicional Noturno.

* **Função HORASABONOJOR:** Retorna as horas (em minutos) de abono por jornada. Poderão ser definidos os abonos de Atrasos ('), Faltas (') ou Ambos ('')

**Sintaxe:** HORASABONOJOR (DATA, DATA, STRING).

**Tipo de Retorno:** Valor

**Exemplo:** O sistema irá verificar quantas horas de abono o funcionário teve no dia. No dia 26/07/2004 foi cadastrado um abono de falta para o funcionário. Horário do funcionário: 22:00E 05:00S HORASABONOJOR ('/07/2004', '/07/2004', ') Desse modo, o sistema irá retornar 420 horas de abono no dia.

**Observação:** Sempre será considerada a jornada que inicia no dia analisado.

* **Função HORASABONOPORABONO:** Retorna o número de horas que um abono foi utilizado em uma data ou período determinado.

**Sintaxe:** HORASABONOPORABONO (DATA , DATA , STRING , STRING)

**Tipo de Retorno:** Valor 1ª Data = Data do início do período desejado. 2ª Data = Data do fim do período desejado. 1ª String: A – retornar as horas de atrasos abonadas. F – retornar as horas de faltas abonadas. ''– retornar as horas de faltas e atrasos abonadas. 2ª String: Informar o código do abono desejado informado no menu Cadastros |Cálculos | Abonos.

**Exemplo:**

HORASABONOPORABONO('21/02/2006' , '20/03/2006' , 'A' , '0004')

Resultado = 120

* **Função HORASADNOT:** Retorna o número de horas (em minutos ) de adicional noturno do funcionário em uma determinada data.

**Sintaxe:** HORASADNOT (DATA)

**Tipo de Retorno:** Valor

**Exemplos:**

Batidas do funcionário X: Data: 06/11/2000 22:00E 08/11/2000 01:00S 02:00E 05:00S 22:00E

1) HORASADNOT ( '/11/2000')

Resultado da fórmula = 120 2)HORASADNOT ( '/11/2000') Resultado da fórmula = 240

* **Função HORASAFAST:** Retorna o número de horas ( em minutos ) de afastamento ou número de dias de afastamento em um período (0 – Horas, 1 – Total de Dias) .

**Sintaxe:** HORASAFAST (DATA, DATA, STRING)

**Tipo de Retorno:** Valor

**Exemplos:**

1 - HORASAFAST ( '/01/2004', '/02/2004', 0) Desse modo, o sistema irá retornar o número de horas (em minutos) do afastamento de um período.

2 - HORASAFAST ( '/01/2004', '/02/2004', 1) Desse modo, o sistema irá retornar o número de dias de afastamento de um período.

* **Função HORASATRASO:** Retorna o número de horas ( em minutos ) de atraso do funcionário em uma determinada data.

**Sintaxe:** HORASATRASO (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário X:

Data: 01/11/2000 08:00E 12:00S 14:00E 18:00S

Batidas do funcionário X: 01/11/2000 10:00E 12:00S 14:00E 18:00S

Resultado da fórmula: HORASATRASO ( '/11/2000')=120

* **Função HORASATRPERTOT:** Retorna o número de horas totais( em minutos ) de atrasos do funcionário em um determinado período.

**Sintaxe:** HORASATRPERTOT (DATA, STRING, DATA, STRING)

**Tipo de Retorno:** Valor

**Exemplo:**

HORASATRPERTOT (IPM , '00:01' , FPM , '08:00') A função irá retornar as horas de atraso (em minutos) no intervalo de 00:01 às 08:00 horas de cada dia do início do período mensal até o fim do período mensal.

* **Função HORASBASE:** Retorna o número de horas ( em minutos ) base do funcionário em uma determinada data.

**Sintaxe:** HORASBASE (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário X: Data: 12/06/2000 08:00E 12:00S 14:00E 18:00S

Resultado da fórmula: HORASBASE ( '/06/2000') Resultado da fórmula = 480

* **Função HORASFALTA:** Retorna o número de horas ( em minutos ) de falta do funcionário em uma determinada data.

**Sintaxe:** HORASFALTA (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário X:

Data: 17/01/2000 08:00E 12:00S 14:00E 18:00S

Batidas do funcionário X: 17/01/2000 O funcionário não teve batidas neste dia.

Resultado da fórmula: HORASFALTA ( '/01/2000') Resultado da fórmula = 480

* **Função HORASFALTAJOR:** Retorna o número de horas ( em minutos ) de falta de acordo com a jornada do horário do funcionário em uma determinada data.

**Sintaxe:** HORASFALTAJOR (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Horário do funcionário X:

Data: 17/01/2004 - 22:00E 18/01/2004 - 05:00S

Batidas do funcionário X: 17/01/2004

O funcionário não teve batidas neste dia. 18/01/2004

O funcionário não teve batidas neste dia.

Resultado da fórmula: HORASFALTAJOR ( '/01/2004') Resultado da fórmula = 420 HORASFALTAJOR ( '/01/2004') Resultado da fórmula = 0

**Observação:** Neste caso o sistema vai considerar as horas de falta apenas para o dia 17/01/2004, pois é o dia do início da jornada do horário do funcionário. O resultado de 420 minutos equivale a 07:00 horas dos intervalos de 22:00 às 24:00 do dia 17/01/2004 e 00:00 às 05:00 do dia 18/01/2004.

* **Função HORASTRAB:** Retorna o número de horas ( em minutos ) trabalhadas pelo funcionário em uma determinada data.

**Sintaxe:** HORASTRAB (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Batidas do funcionário X:

Data: 17/01/2000 08:00E 12:00S 14:00E 18:00S 18/01/2000

O funcionário não teve batidas neste dia. 20/01/2000 08:00E 12:00S

Teste da fórmula: HORASTRAB ( '/01/2000')

Resultado da fórmula = 480 HORASTRAB ( '/01/2000')

Resultado da fórmula = 0 HORASTRAB ( '/01/2000')

Resultado da fórmula = 240

* **Função HORASTRABDESC:** Retorna o número de horas ( em minutos ) trabalhadas em dia de descanso ou feriado pelo funcionário no período ativo.

**Observação:**Esta função retorna as horas trabalhadas em um dia do período ativo.

**Sintaxe:** HORASTRABDESC (DATA, STRING)

**Tipo de Retorno:** Valor Observação: No campo String deverão ser passados os seguintes valores: '

0' - Retornará as horas trabalhadas considerando descanso, grupo de descanso e feriado;

'1' - Retornará as horas trabalhadas considerando descansos e grupo de descanso;

'2' - Retornará as horas trabalhadas considerando feriados.

''- Retornará as horas trabalhadas considerando apenas os descansos do Grupo de Descanso.

**Exemplo:**

Feriado no dia 30/03/2007 funcionário trabalhou 08:00 neste dia.

HORASTRABDESC ( '30/03/2007' , '2' )

Resultado da fórmula = 480

* **Função HORASTRABJOR:** Retorna o número de horas ( em minutos ) trabalhadas pelo funcionário por jornada em uma determinada data.

**Sintaxe:** HORASTRABJOR (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Batidas do funcionário X:

Data: 17/01/2003 22:00E 18/01/2003 05:00S

Teste da fórmula: HORASTRABJOR ( '/01/2003') Resultado da fórmula = 420

* **Função HORASTRABPER:** Retorna o número de horas ( em minutos ) trabalhadas pelo funcionário em um determinado período.

**Sintaxe:** HORASTRABPER (DATA, STRING, DATA, STRING)

**Tipo de Retorno:** Valor

**Exemplo:**

HORASTRABPER: ('01/02/1999', ':00', '01/03/1999', ':00'), A função irá retornar as horas trabalhadas pelo funcionário do dia 01/02 a partir das 22:00 até o dia 01/03 às 5:00.

* **Função HORASTRABPERTOT:** Retorna o número de horas totais( em minutos ) trabalhadas pelo funcionário em um determinado período.

**Sintaxe:** HORASTRABPERTOT (DATA, STRING, DATA, STRING)

**Tipo de Retorno:** Data

**Exemplo:**

HORASTRABPERTOT (IPM , '00:01' , FPM , '08:00') A função irá retornar as horas trabalhadas (em minutos) no intervalo de 00:01 às 08:00 horas de cada dia do início do período mensal até o fim do período mensal.

* **Função HORCOMPDIA:** Retorna os intervalos de compensação cadastrados em uma data.

**Sintaxe:** HORCOMPDIA (DATA)

**Tipo de Retorno:** String

**Exemplo:** HORCOMPDIA ( '/11/2000') Resultado da fórmula = COMP(00:00 - 24:00)

* **Função HORDESCDIA:** Retorna os intervalos de descanso cadastrados em uma data.

**Sintaxe:** HORDESCDIA (DATA)

**Tipo de Retorno:** String

**Exemplo:** HORDESCDIA ( '/11/2000') Resultado da fórmula = DESC(00:00 - 24:00)

* **Função HORDESCDIAGRUPO:** Retorna os Intervalos de descanso em uma data.

**Sintaxe:** HORDESCDIAGRUPO (DATA,STRING)

**Tipo de Retorno:** String O campo STRING poderá ser preenchido com:

'0' - Retorna o intervalo do descanso considerando somente o horário do funcionário.

'1' - Retorna o intervalo do descanso considerando o horário e o grupo de descanso associado ao funcionário. O descanso do grupo de descanso tem prioridade sobre o descanso do horário.

'2' - Retorna o intervalo do descanso considerando somente o grupo de descanso associado ao funcionário

**Exemplo:**

HORDESCDIAGRUPO ( '/09/2005', 0)

Resultado da fórmula = DESC(00:00 - 24:00)

* **Função HORIREFDIA:** Retorna os intervalos de refeição cadastrados em uma data.

**Sintaxe:** HORIREFDIA (DATA)

**Tipo de Retorno:** String

**Exemplo:**

HORIREFDIA ( '/01/2000')

Resultado da fórmula = IREF(12:00 - 14:00)

* **Função HORNORMDIA:** Retorna as batidas do horário cadastrado em uma data.

**Sintaxe:** HORNORMDIA (DATA)

**Tipo de Retorno:** String

**Exemplo:** HORNORMDIA ( '/01/2000')

Resultado da fórmula = 08:00E 12:00S 14:00E 18:00S

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
