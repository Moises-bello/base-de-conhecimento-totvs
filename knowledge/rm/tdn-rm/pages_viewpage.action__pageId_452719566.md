---
content_hash: ed77157b7bc242ff0e41ad68d89c875fd95c2a7ae4ac11686e88361029ea0336
fetched_at: '2026-06-29T00:10:08.722376+00:00'
page_id: '452719566'
product: rm
source: tdn-rm
title: Fórmulas / Funções - D
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719566
version: 2
---

**Fórmulas / Funções - D**

* **Função DECANO:** Deduz do mês o número do meses e retorna o mês correspondente. Esta função deve ser utilizada seguida do mês atual e do número de meses a deduzir.

**Sintaxe:** DECANO (MÊS, ANO, NÚMERO DE MESES)

**Tipo de Retorno:** Valor

**Exemplo:** DECANO (10, 1997, 20) = 1996

* **Função DECMES:** Deduz do mês o número do meses e retorna o mês correspondente. Esta função deve ser utilizada seguida do mês atual e do número de meses a deduzir.

**Sintaxe:** DECMES (MÊS, NÚMERO DE MESES)

**Tipo de Retorno:** Valor

**Exemplo:** DECMES(10,20) = 2

* **Função DIADT:** Retorna o dia de uma data.

**Sintaxe:** DIADT ( DATA ) **Tipo de Retorno:** Valor **Exemplo:** 1) DIADT ( 15/11/2000 ) = 15 2) (MTDATA(1,INCMES(MESDT(HOJE),1)INCANO(MESDT(HOJE),ANODT(HOJE) Esta fórmula calcula quantos dias tem o mês atual,e retorna o primeiro dia do próximo mês e diminui um dia. Este será o último dia do mês atual. Desta data é utilizado somente o último dia para identificarmos a quantidade de dias do mês.

* **Função DIAFER:** Irá verificar se o dia é feriado

**Sintaxe:** DIAFER ( DATA )

**Tipo de Retorno:** Valor

**Exemplo:** O sistema irá verificar se o dia 25/12/2001 é feriado de acordo com o calendário associado a seção do funcionário. Se o dia 25/12/2001 for feriado, o resultado da fórmula será 1,00 ( verdade ), mas se não for feriado irá retornar 0,00 ( falso ). DIAFER('/12/2001')

**Execução da fórmula:** Constante literal  25/12/2001 Chamada a função DIAFER  25/12/2001 Resultado da função DIAFER  1,00 Resultado da fórmula  1,00

* **Função DIAFOLGA:** Irá verificar se o dia é folga. Esta folga é determinada no Grupo de descanso associado no cadastro do funcionário.

**Sintaxe:** DIAFOLGA ( DATA )

**Tipo de Retorno:** Valor

**Exemplo:** O sistema irá verificar se o dia 31/10/2002 é uma folga de acordo com o Grupo de Descanso associado ao cadastro do funcionário. Se o dia 31/10/2002 for uma folga, o resultado da fórmula será 1,00 ( verdade ), mas se não for uma folga irá retornar 0,00 ( falso ). DIAFOLGA('/10/2002')

**Execução da fórmula:** Constante literal  31/10/2002 Chamada a função DIAFOLGA  31/10/2002 Resultado da função DIAFOLGA  1,00 Resultado da fórmula  1,00

* **Função DIASABONO:** Retorna o número de Abonos no dia. Poderão ser definidos abonos de Atraso ('), Faltas (') ou Ambos ('').

**Sintaxe:** DIASABONO ( DATA, DATA, STRING)

**Tipo de Retorno:** Valor O sistema irá verificar quantos abonos o funcionário teve no dia. Para serem considerados abonos diferentes eles deverão ter códigos diferentes ou estarem em jornadas diferentes

**Exemplo:** No dia 30/07/2004 foram cadastrados dois abonos de atrasos diferentes para o funcionário. Horário do funcionário: 08:15E 12:30S 14:30E 18:15S Batidas do funcionário: 09:00E 12:30S 14:30E 18:00S DIASABONO ('/07/2004', '/07/2004', ') Desse modo, o sistema irá retornar 2 abonos no dia.

**Observação:** Será definido como abono de falta somente quando toda a falta estiver abonada, senão será considerado abono de atraso.

* **Função DIASBONOJOR:** Retorna o número de Abonos por jornada. Poderão ser definidos abonos de Atraso ('), Faltas (') ou Ambos ('')

**Sintaxe:** DIASBONOJOR ( DATA, DATA, STRING)

**Tipo de Retorno:** Valor O sistema irá verificar quantos abonos o funcionário teve na jornada. Para serem considerados abonos diferentes eles deverão ter códigos diferentes ou estarem em jornadas diferentes. Sempre será considerada a jornada que inicia no dia analisado.

**Exemplo:** No dia 03/08/2004 foram cadastrados dois abonos de atrasos diferentes para o funcionário. Horário do funcionário: 22:00E 05:00S Batidas do funcionário: 02/08/2004 - 22:00E 03/08/2004 - 04:00S - 23:00E DIASBONOJOR ('/08/2004', '/08/2004', '). Desse modo, o sistema irá retornar 2 abonos, pois os atrasos estão em jornadas diferentes.

**Observação:** Será definido como abono de falta somente quando toda a falta estiver abonada, senão será considerado abono de atraso.

* **Função DIASABONOPORABONO:** Retorna o número de dias que um abono foi utilizado em um período determinado.

**Sintaxe:** DIASABONOPORABONO (DATA , DATA , STRING , STRING)

**Tipo de Retorno:** Valor 1ª Data = Data do início do período desejado. 2ª Data = Data do fim do período desejado. 1ª String: A – retornar os dias de atrasos abonados. F – retornar os dias de faltas abonados. ''– retornar os dias de faltas e atrasos abonados. 2ª String Informar o código do abono desejado informado no menu Cadastros | Cálculos | Abonos.

**Exemplo:** DIASABONOPORABONO ('/02/2006', '/03/2006', ', '') Resultado = 3

* **Função DIASEM:** Retorna o dia da semana de uma data.

**Sintaxe:** DIASEM ( DATA )

**Tipo de Retorno:** String

**Exemplo:** DIASEM ( 08/11/2000 ) = QUA

* **Função DTSIST:** Retorna o dia do sistema operacional.

**Sintaxe:** DTSIST

**Tipo de Retorno:** Data

|  |  |
| --- | --- |
|  | Informações Complementares |

[  
Funções Específicas do TOTVS Automação de Ponto|Fórmulas - PTO]
