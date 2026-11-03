---
content_hash: 70d886b5eec3fd7576de74ba3d9e1aa37efb8d93218e70663722afaa5d730123
fetched_at: '2026-06-29T00:10:05.478454+00:00'
page_id: '452719295'
product: rm
source: tdn-rm
title: Fórmulas / Funções – N
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719295
version: 16
---

**Função N**  
Retorna número de horas de um evento, que é procurado no movimento atual do funcionário (mês/ano de competência). N ('CÓD. DO EVENTO')  
   
**Exemplo:**  
N ('CÓD. DO EVENTO')  
(N('001') /N('002'))  
O número de horas do evento de código 001 será dividido pelo número de horas do evento de código 002.   
   
   
**Função NCFIX**  
Retorna número de vezes de um código fixo.  
NCFIX (STRING)  
   
**Exemplo:**  
NCFIX ('0096')   
Irá retornar o valor do campo "número de vezes do lançamento" do evento cadastrado no Códigos Fixos do funcionário.   
   
**Função ND**  
Retorna número de dias trabalhados, considerando data de admissão, afastamento e demissão.  
ND- retorno valor   
   
   
**Função NDDSRPER**  
Retorna a quantidade de domingos, sábados e feriados conforme calendário da seção, verificando admissão, férias, afastamento e demissão.  
(DATA, DATA, STRING)  
 Onde:  
 **Data** = Data Inicio   
 **Data** = Data Fim   
 **Parâmetros Gerais(String**)= Para considerar os sábados deverá informar 1, caso contrário deverá informar 0.  
   
**Exemplo:**  
NDDSRPER (01/01/2013, 31/01/2013, 1) =8  
   
NDDSRPER (01/01/2013, 31/01/2013, 0) =4  
 

**Função NDEP**  
Retorna o número de dependentes que tem determinada incidência marcada  
NDEP  
   
**Exemplo:**  
A incidência 2 – "**Presentes de Natal**" está marcada para 3 dos 4 dependentes de um funcionário e na fórmula está pedindo o seguinte - NDEP (2) - o resultado será 3.  
   
   
   
**Função NDDIRFERIAS**  
Retorna o número de dias de direito de férias.  
NDDIRFERIAS  
   
   
**Função NDEPCORRENTE**  
NDEPCORRENTE  
   
É uma variável que retorna o número do dependente corrente. Esta variável só deverá ser usada em fórmulas que serão executadas no "movimento | cálculo da pensão alimentícia", pois somente neste cálculo é passado o parâmetro para determinar o dependente corrente. Como no cálculo de pensão o sistema está analisando cada dependente, então faz sentido querer saber qual o dependente corrente, o que não acontece em outros lugares do sistema.  
   
   
**Função NDEPIDADE**  
Esta função retorna a idade do dependente.  
NDEPIDADE (VALOR, DATA)  
Onde  
**Valor** =Número do Dependente   
**Data**= Data Referencia  
   
**Exemplo:**  
Funcionário: João da Silva  
Dependente 1: Data de nascimento 10/01/1990  
Dependente 3: Data de nascimento 15/05/1928  
Fórmulas   
A) NDEPIDADE (1,'22/06/2013') Resultado = 23 anos  
B) NDEPIDADE (1,'01/01/2013') Resultado = 22 anos  
C) NDEPIDADE (3,'14/05/2013') Resultado = 14 anos  
D) NDEPIDADE (3,'15/05/2013') Resultado = 15 anos  
   
   
   
**Função NDEPIDINT**  
Retorna o número de dependentes de um determinado grau de parentesco em um determinado intervalo de idade.  
NDEPIDINT (STRING, VALOR, VALOR)  
   
Onde   
**String** =Grau  
**Valor** =Idade Inicial  
**Valor**=Idade Final  
   
**Exemplo:**  
NDEPIDINT ('1', 10, 50)  
O funcionário testado tem 4 dependentes com as seguintes idades 33,27,85,80.  
Ao testar a formula foi retornado 2, indicando que o funcionário tem 2 dependente com idades   entre 10 e 50.  
   
   
   
**Função NDEPLIQUIDO**  
Esta função retorna o rendimento líquido do funcionário para um dependente específico, ou seja, o somatório de todos os proventos subtraído do somatório de todos os descontos, excluindo aqueles que foram indicados na pasta "eventos não considerados" da ficha do dependente. O número do dependente é o único parâmetro utilizado nesta função.  
NDEPLIQUIDO(Valor )  
   
**Exemplo:**  
Sugestão de fórmula para cálculo de pensão sobre o rendimento líquido mensal.  
   
DECL VALOR,CONT;   
DECL RB, CP, PERC;  
   
SETVAR (RB, NDEPBRUTO (NDEPCORRENTE) );   
SETVAR (CP, TI(A('01')));  
SETVAR (PERC, TABDEP('PERCENTUAL' , 'V', NDEPCORRENTE) / 100 );   
   
REPITA   
SETVAR (VALOR, PERC \* (RB - CP – TR (RB - CP - VALOR)));   
SETVAR (CONT, CONT+1)  
ATE CONT = 7;  
SE PERC > 0 ENTAO  
VALOR / PERC  
SENAO  
0  
FIMSE  
   
   
   
**Função NDEPBRUTO**  
Esta função retorna o rendimento bruto do funcionário para um dependente específico, ou seja, o somatório de todos os proventos excluindo aqueles que foram indicados na pasta "eventos não considerados" da ficha do dependente. O número do dependente é o único parâmetro utilizado nesta função.  
NDEPBRUTO (Valor)  
   
   
**Função NDEPIR**  
Número de dependentes de IRRF em uma determinada data.  
NDEPIR(Data)  
   
**Exemplo:**  
NDEPIR ('01/01/2013')  
De acordo com esta fórmula o sistema irá retornar a quantidade de dependentes de IRRF em   01/01/2013, verificando o Histórico de Dependentes no cadastro do Funcionário.  
   
   
   
   
**Função NDEPSF**  
Número de dependentes de Salario Família em uma determinada data.  
NDEPIR(Data)  
   
**Exemplo:**  
 NDEPIR ('01/01/2013')  
De acordo com esta fórmula o sistema irá retornar a quantidade de dependentes de SALÁRIO FAMÍLIA em 01/01/2013, verificando o Histórico de Dependentes no cadastro do Funcionário.  
   
   
   
**Função NDEPSFAMRET**  
Número de dependentes de Salário Família.  
NDEPSFAMRET (PARÂMETRO)  
Onde  
Parâmetro 0 - retorna o total de dependentes com direito ao salário família.  
Parâmetro 1 - retorna o valor monetário relativo ao pagamento devido de salário família dos dependentes que não entregaram o cartão de vacina e/ou atestado de frequência escolar.  
   
**Observação:**  
Para funcionários que recebem acima do teto para pagamento de salário família o tratamento pode ser feito na fórmula.   
Para ambos os parâmetros, será considerado as regras do salário família.  
   
   
   
   
**Função NDFERIAS**  
Retorna o número total de dias de férias.  
NDFERIAS  
   
   
   
**Exemplo:**   
O sistema se encontra na competência janeiro no ano de 2014, o funcionário tem registrado no cadastro de férias o seguinte período de gozo: 15/01/2014 a 15/02/2014. Ao executar a fórmula para este funcionário o sistema irá retornar "30" que equivalem a soma dos dias de férias do mês com os dias de férias do próximo mês. Nesta mesma competência outro funcionário tem registrado no cadastro de férias o seguinte período de gozo: 02/01/2014 a 31/01/2014. Ao executar a fórmula para este funcionário o sistema irá retornar "30" que equivalem a quantidade de dias de férias do mês.  
   
   
   
**Função NDFERIASAQ**  
Retorna o número de dias de Férias no período Aquisitivo.  
NDFERIASAQ  
   
   
   
**Função NDFERMES**  
Retorna o número total de dias de férias no mês.  
NDFERMES  
   
**Exemplo:**  
O sistema se encontra na competência janeiro no ano de 2014, o funcionário tem registrado no cadastro de férias o seguinte período de gozo: 20/01/2014 a 18/02/2014. Ao executar a fórmula para este funcionário o sistema irá retornar "12" que equivalem aos números de dias de férias do mês.  
Caso no histórico de férias do funcionário tenha registro de férias gozadas dentro do mês da competência atual, estes dias somarão aos dias de férias do mês informados no cadastro de férias no funcionário.  
   
   
   
   
**Função NDFERPROX**  
NDFERPROX  
   
**Exemplo:**  
O sistema se encontra na competência janeiro no ano de 2014, o funcionário tem registrado no cadastro de férias o seguinte período de gozo: 20/01/2014 a 18/02/2014. Ao executar a fórmula para este funcionário o sistema irá retornar "18" que equivalem aos números de dias de férias do próximo mês.  
   
   
   
   
**Função NDIASDESC**  
Esta variável retorna o total de dias de descanso do funcionário dentro de um período pré -determinado, tomando como base o horário do funcionário.  
NDIASDESC (DATA, DATA)

**Exemplo:**  
NDIASDESC ('01/07/2013', '31/07/2013')  
Esta fórmula retorna o total de dias de descanso dentro do período  
   
   
   
**Função NDIASDESCGRP**  
NDIASDESCGRP (DATA, DATA)  
Esta variável retorna o total de dias de descanso do funcionário dentro de um período pré- determinado, tomando como base o grupo de descanso associado ao mesmo, no Automação de Ponto.  
   
**Exemplo:**  
NDIASDESCGRP('01/01/2014','31/01/2014')  
Cadastrando no Chronus 3 dias de descanso no período de 1/01/2014 a 31/01/2014   e associando o funcionário a este Grupo de Descanso a formula retornará 3.  
   
   
**Função NDIASCALEND**  
NDIASCALEND(DATA1,DATA2,PARAMETRO)  
Retornar o número de dias úteis ou não úteis do período informado.  
Para contagem dos dias uteis e não úteis, serão considerados os feriados e domingos do calendário da seção do funcionário.  
São considerados dias não úteis: feriados, domingos e, os sábados dependendo da parametrização informada no parâmetro específico desta variável.  
**Atenção:** Não será considerada a jornada do horário do funcionário.  
   
DATA1 e DATA2: Informe o período desejado. Formato DD/MM/AAAA.  
PARÂMETRO: A primeira posição define se o retorno será em quantidade de dias úteis ou em quantidade de dias não úteis. Informe **U** ou **N**.  
Informe **U** para retornar a quantidade de dias úteis  
Informe **N** para retornar a quantidade de dias não úteis.  
A segunda posição determina se o sábado será considerado como dia ÚTIL ou NÃO ÚTIL. Informe **S**(sim) ou **N**(não).  
   
**Observação:** Quando o sábado for feriado, mesmo o parâmetro estando 'S', este sábado será considerado como NÃO ÚTIL.  
**Exemplos:**  
NDIASCALEND('01/07/2014', '31/07/2014', 'US') retorna o total de dias úteis no mês 07/2014, e o 'S' determina que os sábados serão contados.  
NDIASCALEND('01/07/2014', '31/07/2014', 'UN') retorna o total de dias úteis no mês 07/2014, e o 'N' determina que os sábados não devem ser contados, ou seja, sábado é dia não útil.  
NDIASCALEND('01/07/2014', '31/07/2014', 'NS') retorna o total de dias NÃO úteis no mês 07/2014, e o 'S' determina que os sábados não devem ser contados, porque é um dia útil.  
NDIASCALEND('01/07/2014', '31/07/2014', 'NN') retorna o total de dias NÃO úteis no mês 07/2014, e o 'N' determina que os sábados serão contados, ou seja, sábado é dia não útil.  
   
**Função NDIASCOMP**  
Esta variável retorna o total de dias de compensado do funcionário dentro de um período pré - determinado, tomando como base o horário do funcionário.  
NDIASCOMP (DATA, DATA)  
   
**Exemplo:**   
NDIASCOMP ('01/01/2014', '31/01/2014')  
Ao executar a fórmula o sistema irá retornar "4" que equivalem ao número de dias de compensado do horário associado no funcionário.   
   
   
   
**Função NDIASMES**  
Retorna o número de dias do mês e ano informado  
NDIASMES (Mês, Ano)  
   
**Exemplo:**  
NDIASMES (02, 2013),  
O sistema verificará o mês de fevereiro de dois mil e treze retornando a quantidade de 28 dias. Observando sempre o calendário.  
   
   
   
**Função NDTRAB**  
Retorna número de dias que o funcionário deverá trabalhar no mês de competência conforme calendário, afastamento, horário e histórico do funcionário.  
NDTRAB

**Função NEPRG**  
Retorna meses restantes do Evento Programado.  
NEPRG('Cod Evento')   
   
   
**Função NJTRAB**  
Retorna número de dias que o funcionário deverá trabalhar no mês de competência, verificando a jornada existente no horário cadastrado para o funcionário, calendário, afastamento e históricos.  
NJTRAB  
   
   
   
**Função NJTRABPXMES**  
Retorna número de dias que o funcionário deverá trabalhar no mês seguinte à competência atual, verificando a jornada existente no horário cadastrado para o funcionário, calendário, afastamento e históricos.  
NJTRABPXMES  
   
   
**Função NDTRABPER**  
Esta função calcula o número de dias que o funcionário deveria trabalhar considerando o seu horário, feriados, férias e afastamentos. Verifica o histórico conforme data informada na variável.  
NDTRABPER (DATA, DATA)  
   
   
**Exemplo:**  
NDTRABPER ('21/04/2013', '20/05/2013') O sistema retornará o número de jornadas trabalhadas do funcionário considerando o seu horário, feriados, férias e afastamentos ocorridos entre 21/04/2013 a 20/05/2013.  
   
   
  
   
   
   
**Função NDUTEIS**  
Retorna o número de dias úteis no mês conforme o que foi cadastrado em Administração Pessoal| funcionário | Parâmetros no campo Dias Úteis do Mês.  
   
**Observação:**  
Verifica o histórico de seção.  
Na rescisão para o próximo mês verifica os dias trabalhados do mês da rescisão.  
   
   
**Função NDUTPROX**  
Retorna o número de dias úteis no próximo mês conforme o que foi cadastrado em Administração Pessoal| funcionário | Parâmetros no campo Dias Úteis do Mês.  
   
   
**Função NHORACUM**  
Retorna número de horas de acumulador.  
NHORACUM ('COD. DO ACUMULADOR).'  
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a **NHORACUM,** não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
   
**Função NMESES**  
Retorna o número de meses de casa do funcionário  
NMESES  
   
**Função NREFACUM**  
Retorna o total da referência dos eventos, no período atual, que incidem em um determinado Acumulador.  
NREFACUM ('STRING')  
   
 **Exemplo:**  
NREFACUM('4')  
Onde 4 é o código de um acumulador registrado na Tabela Dinâmica (INT34)  
   
**Atenção:**  
As variáveis de fórmula que são relativas a movimentação do funcionário, como a TOTPROV, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do  funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".  
   
**Função NROAVOS13**  
Retorna o número de avos de 13º salário que o funcionário tem direito.  
NROAVOS13.  
   
**Observação:**  
Está variável também considera as faltas e os afastamentos do funcionário. Os tipos de afastamentos que estão sujeitos à redução de avos durante o afastamento no ano corrente são: **P** (Afast.Previdência), **L** (Licença s/venc ), **M** (Serv.Militar) e **U** (Outros). Os funcionários afastados por **T** (Af.Ac.Trabalho) só terão avos reduzidos caso o parâmetro "Meses de afastamentos por acidente de trabalho reduz avos de 13º" esteja marcado no Parametrizador l 13 Salario l Calculo.

**Função NROAVOSPER**  
Retorna o número de avos do funcionário.O usuário quem irá definir o mês de referência para a contagem dos avos.

NROAVOSPER.

Para maiores informações veja em: [NROAVOSPER .](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519716424)  
   
   
**Função NROAVOSPROP**  
Esta variável retorna o número de avos de férias proporcionais que o funcionário tem direito.  
NROAVOSPROP(DATA)  
   
**Observação:**  
Em (DATA) deverá ser informado a data limite para a contagem dos avos.  
   
   
**Função NROFALTASAVOS**  
Retorna os avos proporcionais de férias de acordo com o número de faltas existentes no período aquisitivo do funcionário.  
NROFALTASAVOS  
   
**Exemplo:**  
Funcionário tem o período aquisitivo: 06/08/2012 à 05/08/2013  
No mês 09/2012 ele teve 10 faltas   
Fórmula: NROFALTASAVOS  
Resultado: 9  
   
**Observações**:  
O sistema irá retornar a quantidade de avos de acordo com a tabela:  
0 a 5 faltas = 12 avos de férias  
6 a 14 faltas = 9 avos de férias  
15 a 23 faltas = 7 avos de férias  
24 a 32 faltas = 4 avos de férias

O sistema verifica em Administração Pessoal | Sindicatos | pasta Férias o parâmetro **Ignora falta em férias normais.**  
   
   
**Função NUMDIASEM**  
NUMDIASEM (STRING, Data1, Data2)  
Esta função calcula o total de dias de um determinado dia da semana (domingo, segunda, terça, quarta, quinta, sexta, sábado) que existem entre duas datas.  
Onde  
String-Dia da Semana    
Data1-Data Inicio   
Data2-Data Fim  
   
**Exemplo:**  
NUMDIASEM ('DOM', 01/03/2013, 31/03/2013)  
Total de número de domingos entre o dia 01/03/2013 e 31/03/2013.  
   
   
**Função NVD**  
Retorna número de viagens diárias, do registro cujo o período de uso está dentro da competência e período atual.  
NVD ('CÓD. DA LINHA')  
   
   
**Exemplo:**  
   
**Nº de Viagens    Nº de viag M. Exp     Cod linha       Nome Linha     Valor            Inicio Uso         Ter Uso**   
      2                            2                                  2210                     Rio                    2,10                  01/01/2010            31/12/2010  
      3                            3                                  2210                     Rio                    2,10                  01/01/2011            31/12/2011  
      4                            4                                  2210                     Rio                    2,10                  01/01/2012            31/10/2012  
      5                            5                                  2210                     Rio                    2,10                  01/11/2012            30/11/2012  
      8                            8                                  2210                     Rio                    2,10                  01/12/2012  
   
Comp: Dez/2012 - Cx: Dez - Per: 1  
Resultado: 8,0000  
   
   
**Função NVDME**  
Retorna o número de viagens diárias em meio expediente, do registro cujo período de uso está dentro da competência e período atual.  
NVDME ('Cod Linha' )  
   
   
   
**Exemplo:**  
**Nº de Viagens    Nº de viagens M. Exp      Cod linha    Nome Linha     Valor         Inicio Uso     Termino Uso**   
        2                               2                                   2210                  Rio                   2,10              01/01/2010        31/12/2010  
        3                               3                                   2210                  Rio                   2,10              01/01/2011        31/12/2011  
        4                               4                                   2210                  Rio                   2,10              01/01/2012        31/10/2012  
        5                               5                                   2210                  Rio                   2,10              01/11/2012        15/12/2012  
        8                               8                                   2210                  Rio                   2,10              16/12/2012  
   
Comp: Dez/2007 - Cx: Dez - Per: 1  
Resultado: 5,0000
