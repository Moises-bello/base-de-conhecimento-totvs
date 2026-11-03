---
content_hash: fefd4649e7ebbd9570283c08add53d4b8db983721eb1fd786d569378aafa4267
fetched_at: '2026-06-29T00:10:00.324746+00:00'
page_id: '452718487'
product: rm
source: tdn-rm
title: Código de Cálculo 48 - 13º Salário Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718487
version: 3
---

Este evento será utilizado para os cálculos das rescisões, e é um provento do tipo valor.   
 O cálculo será feito da seguinte forma:

(SALARIO MES \* No. MESES TRABALHADOS NO ANO) / 12

O sistema buscará o salário-mês, multiplicará pelo número de meses trabalhados durante o ano corrente e dividirá por 12.

Este evento é considerado na soma dos eventos que "incidem IRRF". Você poderá optar por efetuar o cálculo de 13º salário com ou sem média:

**Com média**

O sistema buscará o salário-mês e somará a média dos eventos que incidem 13º salário, considerando o número de meses para média, conforme informado em Cadastros | Sindicatos | pasta Médias.

**Sem média**

O sistema buscará o salário-mês, que equivale ao salário normal. Se existirem eventos que "incidem salário", o sistema irá acrescentá-los para cálculo do 13º salário.

**Observação**

O usuário deverá estar atento para o fato de o salário-mês incluir o salário cadastrado, somado a todos os eventos que "incidem salário".

**Importante:**

Para o perfeito funcionamento do cálculo de 13º rescisão, o usuário deverá deixar os eventos de código de cálculo 48 e 71 sem fórmula, para que o RM Labore calcule o 13º salário e proporcionalize este valor entre o 13º salário rescisão(CC48) e o 13º salário indenizado (CC71). Se for incluída uma fórmula em algum destes eventos o outro evento deverá obrigatoriamente ter fórmula para que o sistema faça os cálculos.

Particularidades do cálculo por fórmula

No cálculo de 13º salário indenizado a variável C,valor de evento no movimento atual, não poderá ser usada, porque o envelope não é calculado antes deste evento e portanto não existe o evento com CC48 para ser utilizado em fórmula.

**Exemplo:**

CC48 - fórmula = ( (RC + 100.00) / 12 ) \* NROAVOS13

CC71 - fórmula = C('0048') / NROAVOS13 = ERRADO

CC71 - fórmula = ( (RC + 100.00) / 12 ) \* NROAVOS13/ NROAVOS13 = CORRETO
