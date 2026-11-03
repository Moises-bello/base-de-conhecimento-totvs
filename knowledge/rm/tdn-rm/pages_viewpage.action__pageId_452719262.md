---
content_hash: 61e3188f0af7350bd5a3f1a083063e18000661bc2084b47861a349b20d65834a
fetched_at: '2026-06-29T00:10:04.848881+00:00'
page_id: '452719262'
product: rm
source: tdn-rm
title: Fórmulas / Funções - H
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719262
version: 4
---

**Função H**  
Retorna salário-hora. Tipo do retorno Valor.   
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a **H**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
**Função HANT**  
Retorna salário-hora em uma data determinada.  
HANT ('DATA')  
   
**Função HC**  
Retorna salário-hora nominal. Tipo de retorno Valor.  
HC  
   
**Função HISTCOMPRAVT**  
Retorna valor de um Campo do Histórico de Compra de Vale Transporte.  
HISTCOMPRAVT (VALOR,VALOR,STRING,DATA,VALOR,STRING)  
Onde:  
Valor - Ano comp   
Valor- Mês comp   
String –Código Linha   
Data – Data Inicio  
Valor –Viagem Diarias  
String - Campo da Tabela PFHSTFCOMPRAVT  
   
**Sugestão de Fórmula**  
DECL (TOTVALES);  
DECL (STRAUX);  
   
SETVAR (TOTVALES, HISTCOMPRAVT  ( ANO , MES, LINHAVTCORRENTE ('CODLINHA') , DATANULA, -1, 'TOTALVALESENTREGUE') );  
SETVAR (TOTVALES, ARRED(TOTVALES / 20 \* 22));  
   
SETVAR (STRAUX, '');  
SETVAR (STRAUX, CONCATVT (STRAUX , 'TOTALVALESENTREGUE', TOTVALES));  
SETVAR (STRAUX, CONCATVT (STRAUX, 'DIASPERIODO',  22));  
   
STRAUX  
   
**Função HOJE**  
Retorna a data corrente. Tipo de retorno Data.  
HOJE  
   
**Função HORDESCDIA**  
Retorna os intervalos de descanso cadastrados em uma data. Tipo de retorno String.  
HORDESCDIA(DATA)  Verificar   
   
**Exemplo:**  
HORDESCDIA ('05/01/2014') = DESC (00:00 - 24:00)  
   
   
**Função HORNORMDIA**  
Retorna Batidas de um  horário cadastrado em um data.  
HORNORMDIA (DATA) String   
   
**Exemplo:**  
HORNORMDIA ('01/04/2013') = 08:30E 12:30S 14:00E 18:00S  
   
   
**Função HR**  
Retorna os minutos de um Evento no movimento atual.  
HR ('Codevento ') String  
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a HR, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
   
   
**Função HORASTRAB**  
Retorna a quantidade de horas que o funcionário deve trabalhar em uma determinada situação**.**  
HORASTRAB(DATAINICIO, DATAFIM, INICIOINTERVALO, FIMINTERVALO, SITUACAO, PARAMGERAIS**)**  
ONDE:  
**DATAINICIO e DATAFIM:** Informar o período que o sistema deve considerar para calcular a quantidade de horas.  
   
**INICIOINTERVALO e FIMINTERVALO:** Informar o intervalo que o sistema deve considerar para calcular a quantidade de horas. Lembrando que deve ser informado em minutos.  
   
**Exemplo:**  
O usuário necessita saber separadamente a quantidade de horas no período diurno (de 05:00 as 22:00), e noturno (de 22:00 as 05:00), deve criar duas fórmulas informando o intervalo abaixo:  
**Horário Diurno**  
**INICIOINTERVALO        300       = 05:00 (5  x 60minutos)**   
**FIMINTERVALO           1320     = 22:00 (22 x 60 minutos)**   
   
**Horário Noturno**  
**INICIOINTERVALO       1320    = 22:00 (22 x 60 minutos)**   
**FIMINTERVALO             300   = 05:00 (5  x 60minutos)**  
   
**OBSERVAÇÃO**   
Caso o usuário deseje que o sistema considere o dia inteiro deve passar -1 nos parâmetros **INICIOINTERVALO e FIMINTERVALO.**  
   
**Exemplo:**  
O usuário deseja saber a quantidade de horas trabalhadas no período de 01/08/2009 a 31/08/2009 sem intervalo de horário e sem considerar os feriados, a fórmula deve ser:  
HORASTRAB('01/08/2009', '30/08/2009','-1','-1','T','NN')  
   
**SITUAÇÃO**: Informar qual situação o sistema deve considerar, conforme valores abaixo:  
T         = Trabalhadas  
F         = Férias  
AT       = Atestado Médico  
AF       = Afastado (todos os tipos)  
AF\_X   = Afastado do tipo específico. Exemplo 'P'  
   
   
**PARAMGERAIS:** Atualmente contém dois parâmetros, sendo eles:  
Considera feriado  
Informe 'S' para que o sistema considere os feriados do calendário da seção do funcionário.   
Caso contrário informe 'N' para que os feriados não sejam considerados.  
   
**OBSERVAÇÃO:**   
Quando no Automação de Ponto o funcionário utilizar cartão de ponto, este parâmetro somente tem efeito caso esteja parametrizado no funcionário para considerar feriados.  
   
Considera intervalo de refeição  
Informe 'S' para que o sistema considere o intervalo de refeição cadastrado no horário do funcionário.   
Caso contrário informe 'N' para que o intervalo não seja considerado.  
   
**Exemplo:**  
Funcionário XX tem o horário de 08:00 às 15:00 com 1 hora de intervalo para almoço. Total de horas trabalhadas = 6horas.  
Funcionário ZZ tem o horário de 07:00 às 13:00 sem intervalo para almoço. Total de horas trabalhadas = 6horas.  
   
Com o parâmetro igual S, o sistema retorna 7 horas para o Funcionário XX e 6horas para o Funcionário ZZ. Caso contrário o sistema retorna 6horas para os dois funcionários.  
   
   
**AtençãoI:**  
O sistema em geral só trabalha em minutos, para retornar o valor correto, para não ocorrer perdas no arredondamento. Caso o usuário deseje que retorne em horas é de responsabilidade do usuário a multiplicação por 60.  
   
**AtençãoII:**  
Atualmente a variável só funciona para quem utiliza o Automação de Ponto.  
        Deve estar configurado para bater ponto no Automação de Ponto (Existir na APARFUN);  
        Deve estar com o parâmetro 'utiliza horário do Automação de Ponto para professor' definir para TRUE, quando o   funcionário for professor;  
   
**Exemplo:**  
O usuário deseja saber a quantidade de dias que o funcionário trabalhou mais de 6 horas no período de 01/06 a 30/06 sem considerar os feriados e sem considerar o intervalo de refeição, a fórmula deve ser:  
HORASTRAB('01/06/2010','30/06/2010','361','0','T','NS') ou   
HORASTRAB('01/06/2010','30/06/2010','361','-1','T','NS')  
   
**Função HORACODCALCULO**  
Retorna a hora do código de cálculo informado.  
HORACODCALCULO(valor)  
   
**Exemplo:**  
HORACODCALCULO(1)  
O sistema retornou 13200 =220\*60.  
   
**Atenção:**  
Na rescisão para o próximo mês verifica os dias trabalhados da competência da rescisão.
