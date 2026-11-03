---
content_hash: 21e81ffb2f011569fbaec00767c2b517a8ff4fa2cd32a4bce50d5db21ff9aa5c
fetched_at: '2026-06-29T00:10:07.034220+00:00'
page_id: '452719359'
product: rm
source: tdn-rm
title: Fórmulas / Funções – D
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719359
version: 13
---

**Função D**

Retorna número de dependentes de IRRF cadastrado em Funcionário l Folha de pagamento l Dependente pasta incidências.  
   
**Função DA**  
Retorna total de dependentes de assistência medica cadastrado em Funcionário l Folha de pagamento l Dependente pasta incidências.  
   
**Função DATANULA**  
Retorna a data mínima do sistema 01/01/0001.  
   
**Exemplo:**  
SE DATANULA<>'00/00/0000' ENTAO 5 SENAO 10 FIMSE  
Neste exemplo o sistema retorna 10.  
Entendendo que 01/01/0001 e igual '00/00/0000'.  
Ou seja, '00/00/0000', ' ', DATANULA, para o sistema é como se não existe data.   
   
**Função DECANO**  
Subtrai um número de meses de um Mês\Ano e retorna o ano do resultado.  
DECANO (VALOR, VALOR, VALOR)  
Onde: Decano (Mês, Ano, Quantidade de Meses)  
   
**Exemplo:**  
DECANO (10, 2013, 30) = 2011  
   
**Função DECMES**  
Deduz do mês o número do meses e retorna o mês correspondente. Esta função deve ser utilizada seguida do mês atual e do número de meses a deduzir.  
DECMES (MÊS, NÚMERO DE MESES)   
   
**Função DI**  
Retorna número de dependentes de INSS cadastrado em Funcionário l Folha de pagamento l Dependente pasta incidências.  
   
**Função DIADIRFER**  
Retorna os dias de direito de férias em real.  
DIADIRFER (VALOR)  
No campo VALOR deverá ser informado: 0,1 ou 2 (0 - Férias Proporcionais, 1- Férias Vencidas e 2 - Soma de Férias Proporcionais + Vencidas)  
   
**Exemplo:**  
Funcionário com 30 dias de férias vencidas + 7,5 dias de férias proporcionais  
DIADIRFER (0) = 7,5  
DIADIRFER (1) = 30  
DIADIRFER (2) = 37,50  
   
**Observação:**  
Se for informado na fórmula um parâmetro diferente de 0,1 ou 2 o valor de retorno será a soma de Férias Proporcionais + Férias Vencidas  
   
**Função DIADIRFERPER**  
Dias de Direito de Férias até a data informada.  
Esta função de fórmula é semelhante à variável DIADIRFER(valor), retorna a quantidade de dias de direito de férias até a data informada.   
DIADIRFERPER (VALOR, DATA)  
No parâmetro VALOR, deve informar:   
0 - Férias Proporcionais,   
1 - Férias Vencidas ou  
2 - Soma de Férias Proporcionais + Vencidas  
   
**Atenção:**  
Se informar um parâmetro diferente de 0,1 ou 2 o valor de retorno é a soma das Férias Proporcionais + Férias Vencidas.  
**Exemplo:**  
Necessita de uma fórmula que retorne a quantidade total de dias de férias sempre no dia 18 do mês, deve criar a fórmula:  
DIADIRFERPER (2, MTDATA (18, MES, ANO)).  
No exemplo acima, quando calcular a rescisão para o próximo mês, o sistema verifica a competência da rescisão.  
   
**Função DIADT**  
Esta fórmula retorna o dia de uma data

Sintaxe: DIADT(data)  
**Exemplo:**  
MTDATA (DIADT(HOJE), MESDT(HOJE), ANODT(HOJE))  
   
**Função DIAFERPER**  
Retorna número de dias de férias que o funcionário tem nesse período.    
DIAFERPER (DATA, DATA)  
   
**Exemplo:**  
DIAFERPER ('17/12/2013','31/12/2013')  
   
**Função DIASAFT**  
Retorna o número de dias de afastamento.  
DIASAFT (Data Inicial, Data Final, Tipo de Afastamento)  
   
**Exemplos:**  
-Funcionário afastado pela previdência (P), no período de 01/10/2001 a 30/10/2001.  
Função:  
DIASAFT ('10/10/2001' , '30/10/2001' , 'P')  
Retorno = 21 dias  
   
-Funcionário afastado pela previdência (P), no período de 01/10/2001 a 30/10/2001 e afastado por Licença Remunerada (R), no período de 10/11/2001 a 20/11/2001  
Função:  
DIASAFT ('01/10/2001' , '15/11/2001' , 'PR')  
Retorno = 45 dias

**Função DIASAFT****PAG**  
Retorna o número de dias de afastamento de acordo com o tipo do afastamento e se o pagamento é devido pela empresa ou pela previdência.  
DIASAFTPAG (Data Inicial, Data Final, Tipo de Afastamento, Pagamento)

Tipo de Afastamento:

P – Previdência

T – Acidente de Trabalho

O – Doença Ocupacional

Pagamento:

E – Empresa

P - Pervidência  
   
**Exemplos:**  
- Funcionário afastado pela previdência (P), no período de 01/10 a 30/10, estando na competência 10.  
Função:  
**DIASAFTPAG**(**MTDATA**(01,MES,ANO),**MTDATA**(31,MES,ANO),'P','E')  
Retorno = 15 dias

**DIASAFTPAG**(**MTDATA**(01,MES,ANO),**MTDATA**(31,MES,ANO),'P','P')  
 Retorno = 15 dias

-Funcionário afastado pela previdência (P), no período de 01/10 a 30/10 e afastado por Acidente de Trabalho (T), no período de 10/11 a 19/11, estando na competência 10.  
Função:

**DIASAFTPAG**(**MTDATA**(01,MES,ANO),**MTDATA**(30,11,ANO),'PTO','E')  
Retorno = 25 dias

**DIASAFTPAG**(**MTDATA**(01,MES,ANO),**MTDATA**(30,11,ANO),'PTO','P')  
 Retorno = 15 dias

Observação: A Função de fórmula DIASAFT2 foi descontinuada e esta nova função DIASAFTPAG é a substituta.

**Função DIASATESTADO**  
DIASATESTADO (VALOR)  
No parâmetro VALOR, deve informar:   
**DIASATESTADO(1)**  
Retorna os dias ÚTEIS, verificando o histórico de horário do funcionário  
Na rescisão para o próximo mês verifica os dias de atestado da competência da rescisão.  
**DIASATESTADO(2)**  
Retorna os dias NÃO ÚTEIS, verificando o histórico de horário do funcionário  
Na rescisão para o próximo mês verifica os dias de atestado da competência da rescisão.  
**DIASATESTADO(3)**   
Retorna os dias de feriados no período de atestado.  
Na rescisão para o próximo mês verifica os dias de atestado da competência da rescisão.  
**DIASATESTADO(4)**  
Retorna os dias de descanso no período de atestado.  
Na rescisão para o próximo mês verifica os dias de atestado da competência da rescisão.  
**DIASATESTADO(5)**   
Retorna a quantidade de sábados no período de atestado, independente do horário.  
Na rescisão para o próximo mês verifica os dias de atestado da competência da rescisão.  
   
**Observação:**  
É observado o limite de 15 dias e os parâmetros de carência pelo mesmo afastamento informado nos parâmetros do Folha de Pagamento.  
   
**Função DIASEMANA**  
Retorna o dia da semana correspondente a determinada data.  
DIASEMANA (DATA, STRING)  
   
**Exemplo:**  
-DIASEMANA (DTA, 'V')    
/\* Dia da semana da data de admissão do funcionário \*/

* DIASEMANA (DTA, 'V') SETVAR (data, MTDATA(1,MES,ANO) ); /\* Primeiro dia do mês \*/   
  SETVAR (primdia,MTDATA(1,INCMES(MES,1), INCANO(MES,ANO,1))); /\* Primeiro dia do próximo mês \*/   
  REPITA    
  SE DIASEMANA(data, 'S') = 'DOM'   
  ENTAO SETVAR (cont, cont+1)    
  SENAO 0   
  FIMSE;  
  SETVAR (data, data+1)  
  ATE data = primdia;  
  Cont  
  /\* Esta fórmula verifica quantos domingos tem no mês atual \*/

**Função DIASTRAB**  
Retorna a quantidade de dias dentro de uma carga hora diária que o funcionário deve trabalhar em uma determinada situação**.**  
DIASTRAB(DATAINICIO, DATAFIM, MINUTOS1(INT), MINUTOS2(INT), SITUACAO(STRING), PARAMGERAIS(STRING))   
   
**Atenção:**

01 - O sistema verifica o horário e seção do histórico do funcionário, caso não exista nenhum histórico é utilizado do cadastro do funcionário.  
DATAINICIO e DATAFIM: Informar o período que o sistema deve considerar para calcular a de dias.

02 - Quando houver dias compensados não serão considerados na fórmula, porque esses dias não tem horas cadastradas no cadastro de horário.

**Exemplo:**  
O usuário precisa saber a quantidade de dias que o funcionário deve trabalhar entre o dia 01 e    30/04/2013.  
Deve informar 01/04/2013 a 30/04/2013  
MINUTOS1 e MINUTOS2: Informar em minutos a quantidade de horas diárias que o funcionário deve ter.  
Pode ser informado um intervalo que o sistema deve considerar para calcular a quantidade de dias. Lembrando que deve ser informado em minutos.  
   
**Exemplo:**   
O usuário precisa saber a quantidade de dias que o funcionário deve trabalhar mais de 6 horas.  
Deve informar:  
MINUTOS1       361 = 06:00 ((6  x 60minutos) + 1) 'maior que 6 horas'  
MINUTOS2       0 ou -1 = sempre que informar 0(zero) ou -1(menos 1) o sistema considera até o fim da jornada diária do funcionário  
   
**Exemplo:**   
O usuário precisa saber a quantidade de dias que o funcionário deve trabalhar entre 6 e 8 horas.  
Deve informar   
MINUTOS1       360   = 06:00 (6  x 60minutos) 'maior ou igual a 6 horas'  
MINUTOS2       480  = 08:00 (8  x 60minutos) 'menor ou igual a 8 horas'  
   
SITUAÇÃO: Informar qual situação o sistema deve considerar, conforme valores abaixo:  
T          = Trabalhadas  
F          = Férias  
AT        = Atestado Médico  
AF        = Afastado (todos os tipos)   
AF\_X    = Afastado do tipo específico. Exemplo 'P'

PARAMGERAIS: Atualmente contém dois parâmetros, sendo eles:  
Considera feriado  
Informe 'S' para que o sistema considere os feriados do calendário da seção do funcionário.   
Caso contrário informe 'N' para que os feriados não sejam considerados.  
   
**Observação**   
Quando no Automação de Ponto o funcionário utiliza cartão de ponto, este parâmetro somente tem efeito caso esteja parametrizado no funcionário para considerar feriados.  
   
Considera intervalo de refeição  
Informe 'S' para que o sistema considere o intervalo de refeição cadastrado no horário do funcionário.   
Caso contrário informe 'N' para que o intervalo não seja considerado.  
**Exemplo:**  
Funcionário XX tem o horário de 08:00 às 15:00 com 1 hora de intervalo para almoço. Total de horas trabalhadas = 6horas.  
Funcionário ZZ tem o horário de 07:00 às 13:00 sem intervalo para almoço. Total de horas trabalhadas = 6horas.  
Com o parâmetro igual S, o sistema retorna 7horas para o Funcionário XX e 6horas para o Funcionário ZZ. Caso contrário o sistema retorna 6horas para os dois funcionários.  
   
**Atenção:**  
Ao utilizar a variável DIASTRAB para retornar a quantidade de dias que o funcionário tem e informar a quantidade de horas diária maior que 6horas, e o parâmetro for igual S, o sistema deve considerar somente o Funcionário XX.  
   
**Exemplo:**  
O usuário deseja saber a quantidade de dias que o funcionário trabalhou mais de 6 horas no período de 01/06 a 30/06 sem considerar os feriados e sem considerar o intervalo de refeição, a fórmula deve ser:  
DIASTRAB('01/06/2010','30/06/2010','361','0','T','NS')  
   
**Atenção:**  
O sistema em geral só trabalha em minutos, para retornar o valor correto, para não ocorrer perdas no arredondamento. Caso o usuário deseje que retorne em horas é de responsabilidade do usuário a multiplicação por 60.  
   
**Exemplo:**  
O usuário deseja saber a quantidade de dias que o funcionário trabalhou mais de 6 horas no período de 01/06 a 30/06 sem considerar os feriados e sem considerar o intervalo de refeição, a fórmula deve ser:  
DIASTRAB('01/06/2010','30/06/2010','361','0','T','NS') ou   
DIASTRAB('01/06/2010','30/06/2010','361','-1','T','NS')

**Atenção:**

Usando a situação AF - Afastado (todos os tipos) os dias cadastrado no cadastro de horário em que as horas estão zeradas (Compensado/Descanso) não serão contados, sendo considerados somente dias úteis.

A função é DIASTRAB que retorna de acordo com cadastro de horário a carga hora diária do funcionário.

**Função DISSIDIO**  
DISSIDIO  
Variável utilizada para Diferença por Dissídio.

**Atenção:**

Será retornado valor  1 sempre que for  executada dentro de algum processo de diferença por Dissídio(Rescisão Complementar,Diferença Salarial, Diferença de Férias, Diferença de 13 Salário) quando  confirmada a flag  "Dissídio Sim" , caso contrário retornará 0.

**Função DNASCIM**  
Retorna data de nascimento. Retorno Data.  
DNASCIM  
   
**Função DP**  
Retorna número de dependentes de Pensão Alimentícia. Retorno Valor.  
   
**Função DSR**  
Retorna o valor total dos eventos que incidem em DSR.  
DSR (VALOR, VALOR, VALOR)   
Onde os parâmetros correspondem ao mês, ano e período respectivamente. Se o período informado for zero, serão considerados todos os períodos do mês e ano informados como parâmetros.  
   
**Atenção:**

* + DSR (MES, ANO, PERIODO)  
    O Sistema irá calcular o valor total dos eventos que incidem em DSR do mês e ano da competência atual no período atual.

DSR (0,0,0)  
Com todos os parâmetros iguais 0 (zero) e ao ser lançados simultaneamente, através de Lançamento de Grupos Eventos, eventos que incidem em DSR e eventos com fórmula utilizando esta função, o sistema irá buscar dentro do período atual o total dos eventos que incidem DSR.  
 **Função DTA**  
DTA  
Retorna data de admissão.  
   
**Função DTD**  
 DTD  
Retorna a data de demissão do funcionário demitido no mês atual.  
   
**Função DUTEISMES**  
DUTEISMES  
Retorna nº de dias úteis no mês conforme cadastramento do calendário e o horário do funcionário.  
   
**Função DV**  
Retorna valor a deduzir por dependente.
