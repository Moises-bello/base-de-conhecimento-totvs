---
content_hash: 820b16232d4c2c4c134b03ac4888a5c6deb6b0673fc191e4795e239797673964
fetched_at: '2026-06-29T00:10:08.865785+00:00'
page_id: '452719598'
product: rm
source: tdn-rm
title: Fórmulas / Funções - N
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719598
version: 13
---

**Fórmulas / Funções - N**

---

* **Função N:** Retorna o número de horas ( em minutos ) de um evento.

**Sintaxe:** N(CÓDIGO DO EVENTO)

**Tipo de Retorno:** Valor

**Exemplo:** N ( '') = 1200

* **Função NCOMP:** Retorna o número de horas ( em minutos ) do evento no banco de horas do funcionário do período atual.

**Sintaxe:** NCOMP(CÓDIGO DO EVENTO)

**Tipo de Retorno:** Valor

**Exemplo:** NCOMP ( '') = 1200

* **Função NCOMPER:** Retorna o número de horas ( em minutos ) do evento em um determinado período.

**Sintaxe:** NCOMPER(CÓDIGO DO EVENTO, DATA, DATA)

**Tipo de** **Retorno:** Valor

**Exemplo:** NCOMPER(CÓDIGO DO EVENTO, DATA, DATA)

* **Função NDIASDESC:** Retorna o total de dias de descansos vinculados ao funcionário dentro de um período determinado, tomando como base o horário do funcionário e/ou o grupo de descanso.

**Sintaxe:** NDIASDESC (DATA, DATA, STRING).

O campo string, pode ser preenchido com as informações: 0 - Todos descansos, 1 - Somente descanso do horário, 2 - Somente descanso do Grupo de  Descanso.

**Tipo de** **Retorno:** Valor

**Exemplo:** NDIASDESC ('01/07/2023', '31/07/2023', 1) = 5  

**Observação:**

Nesse exemplo o funcionário tem os descansos somente aos domingos, no período de  01/07/2023 a 31/07/2023 existem 5 domingos.  Esta função não considera se existem férias, afastamento ou demissão.

* **Função NDFERIAS:** Retorna o número de dias de férias em um período.

**Sintaxe:** NDFERIAS (DATA, DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

NDFERIAS ( '/03/2004', '/03/2004') = 30

* **Função NDFERIASPER:** Retorna o número de dias de férias em um período.

**Sintaxe:** NDFERIASPER (DATA, DATA)

**Tipo de Retorno:** Valor

**Observação:**

Para usar a função de fórmula as férias tem que estar lançadas, pois o sistema buscará os dados do histórico de férias do funcionário.

**Exemplo:**

Funcionário de férias no período: 15/03/2007 até 03/04/2007. Período do Ponto: 01/03/2007 até 31/03/2007 (NDFERIASPER(IPM,FPM) Resultado da fórmula = 17

* **Função NDFERMES:** Retorna o número de dias de férias no mês.

**Sintaxe:** NDFERMES

**Tipo de Retorno:** Valor

**Exemplo:**

Funcionário X período de férias = 16/04/2001 a 15/05/2001. Mês competência = 4

**Observação:**

O sistema irá verificar o mês competência informado no módulo OPÇÕES | PARÂMETROS DO SISTEMA. Ele não irá verificar o período mensal, quinzenal ou semanal.

**Execução da fórmula:** NDFERMES = 15

* **Função NDFERPROX:** Retorna o número de dias de férias do próximo mês.

**Sintaxe:** NDFERPROX

**Tipo de Retorno:** Valor

**Exemplo:**

Funcionário X período de férias = 16/04/2001 a 15/05/2001. Mês competência = 4

**Observações:**

O sistema irá verificar o mês competência informado no módulo OPÇÕES | PARÂMETROS DO SISTEMA. Ele não irá verificar o período mensal, quinzenal ou semanal.

**Execução da fórmula:** NDFERMES = 15

* **Função NFICOMP:** Retorna o número de horas ( em minutos ) do evento do banco de horas em um determinado mês e ano.

**Sintaxe:** NFICOMP(MES, ANO, CÓDIGO DO EVENTO)

**Tipo de Retorno:** Valor

**Exemplo:** NFICOMP ( 10, 2000 , '') = 120

* **Função NFIFIN:** Retorna o número de horas ( em minutos ) do evento da ficha financeira em um determinado mês e ano.

**Sintaxe:** NFIFIN(MES, ANO, CÓDIGO DO EVENTO)

**Tipo de Retorno:** Valor

**Exemplo:** NFIFIN ( 1, 2000 , '') = 1200

* **Função NMOVDIADIA:** Retorna o número de horas ou valor de um evento da Movimentação Dia a Dia em uma determinada data do período ativo.

**Sintaxe:** NMOVDIADIA(CÓDIGO DO EVENTO,DATA,STRING)

**Tipo de Retorno:** Valor

**Observação:**

'0' retorna número de horas do evento e '1' retorna valor do evento.

**Exemplo :**

NMOVDIADIA('0082', '22/09/2005', '0')

**Teste da Fórmula:**  50  O sistema vai retornar o número de horas do evento 0082 para o funcionário no dia 22/09/2005.

* **Função NPER:** Retorna o número de horas ( em minutos ) do evento em um determinado período.

**Sintaxe:** NPER(CÓDIGO DO EVENTO, DATA, DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

NPER( '','/10/2000', '/10/2000') = 13.200

* **Função NUMBATIDA:** Retorna o número de batidas e um data.

**Sintaxe:** NUMBATDIA (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

No dia 01/10/2000 o funcionário X teve as seguintes batidas: 08:00E 12:00S 14:00E 18:00S

**Teste da fórmula:** NUMBATDIA('/10/2000') = 4

* **Função NUMBATHOR:** Retorna o número de batidas cadastradas no horário do funcionário em uma data.

**Sintaxe:** NUMBATHOR (DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

No dia 26/04/2001 o funcionário X tem o seguinte horário cadastrado: 08:00E 12:00S 14:00E 18:00S

**Teste da fórmula:** NUMBATHOR('/04/2001') = 4

* **Função NUMDESCJOR:** Retorna o número de dias de descanso considerando a jornada em um período, podendo este descanso ser do horário ou do grupo de descanso.

**Sintaxe:** NUMDESCJOR(DATA, DATA, STRING)

**Tipo de Retorno:** Valor

**Observação:** O campo string pode ser preenchido com as seguintes informações: 0 - Todos descansos, 1 - Somente descanso do horário, 3 - Somente descanso do Grupo de Descanso.

**Exemplo:** No dia 26/10/2007 o funcionário X tem o seguinte horário: 22:00E 22:59S 23:59E 05:00S Descanso cadastrado: 26/10/2007 - 22:00 ás 24:00 27/10/2007 - 00:00 ás 05:00

**Teste da Fórmula:** NUMDESCJOR(26/10/2007, 27/10/2007, '') Resultado da fórmula = 1

* **Função NUMJOR:** Retorna o número de jornadas a serem trabalhadas em um intervalo de datas, considerando afastamento, férias e demissão.

**Sintaxe:** NUMOR(DATA, DATA)

**Tipo de Retorno:** Valor

**Exemplo:**

Funcionário afastado do dia 12/04/2007 a 27/04/2007. NUMJOR (IPM, FPM).

Retornará o número de jornadas (dias) a serem trabalhados pelo funcionário dentro do período mensal. Resultado da fórmula = 9.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funções Específicas do TOTVS Automação de Ponto
