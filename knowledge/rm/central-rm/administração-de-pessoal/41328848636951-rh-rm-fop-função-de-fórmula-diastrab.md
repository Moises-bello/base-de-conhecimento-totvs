---
article_id: 41328848636951
category: Administração de Pessoal
content_hash: 2bac7f49d649756495c0c2d5ad3e66ed209258500e96d2cdb02df1480b2b3404
fetched_at: '2026-06-28T22:47:01.053137+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Função de fórmula DIASTRAB
type: support-article
updated_at: '2026-06-18T18:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41328848636951-RH-RM-FOP-Fun%C3%A7%C3%A3o-de-f%C3%B3rmula-DIASTRAB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41328816489367)/ Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
Como as funções de fórmula DIASTRAB se comportam no sistema Totvs Folha de pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

**Função DIASTRAB**  
Retorna a quantidade de dias dentro de uma carga hora diária que o funcionário deve trabalhar em uma determinada situação**.**  
DIASTRAB(DATAINICIO, DATAFIM, MINUTOS1(INT), MINUTOS2(INT), SITUACAO(STRING), PARAMGERAIS(STRING))  
   
**Importante:**

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
   
**SITUAÇÃO**:

Informar qual situação o sistema deve considerar, conforme valores abaixo:  
T          = Trabalhadas  
F          = Férias  
AT        = Atestado Médico  
AF        = Afastado (todos os tipos)   
AF\_X    = Afastado do tipo específico. Exemplo 'P'

**PARAMGERAIS:**

Atualmente contém dois parâmetros, sendo eles:  
**Considera feriado**  
Informe 'S' para que o sistema considere os feriados do calendário da seção do funcionário.  
Caso contrário informe 'N' para que os feriados não sejam considerados.  
   
**Observação**  
Quando no Automação de Ponto o funcionário utiliza cartão de ponto, este parâmetro somente tem efeito caso esteja parametrizado no funcionário para considerar feriados.  
   
**Considera intervalo de refeição**  
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

**Para acessar todas as funções e fórmulas padrões existentes no sistema**, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=452718597)
