---
content_hash: 1194ec19d9e8f38116aec6e10e0a0e41a0ea35ebffa4a6568744eb00d7edb78b
fetched_at: '2026-06-29T00:10:07.372680+00:00'
page_id: '452719414'
product: rm
source: tdn-rm
title: Abonos - Automação de Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719414
version: 6
---

**Abonos**   
Durante o período de apuração de ponto, a movimentação pode registrar atrasos e/ou faltas que poderão ser abonadas ou anuladas conforme justificativa do empregado, como por exemplo, o atestado médico.  
Este menu permite cadastrar os tipos de abonos que a empresa adota, que posteriormente serão lançados na movimentação do funcionário conforme justificativa, abonando atraso e/ou falta.  
Para ser considerado, o abono deverá ser lançado ou inserido para o funcionário na data onde foi registrado o atraso ou a falta.

**Observação:** Coloque uma descrição referente ao verdadeiro abono, para lembrar com facilidade do mesmo em outros processos.  
   
Para as empresas que fazem o controle do DSR (Descanso Semanal Remunerado), o cadastro disponibiliza formas com o qual o abono atuará perante o DSR, abonando-o ou não. Veja a seguir as opções de parametrização do abono:

* Abona também o DSR: Para o sistema abonar as faltas e/ou atrasos e também o DSR.
* Abona somente o DSR: Para o sistema abonar apenas o DSR da semana, os atrasos e faltas serão descontadas dos funcionários.
* Não abona o DSR: Para o sistema abonar as faltas e/ou atrasos e não abonar o DSR, fazendo com que o funcionário perca o DSR.

Poderá ser informado o evento que deverá ser relacionado ao abono cadastrado. O evento só será pago em evento discriminado no movimento do funcionário, se no parâmetro coletivo do funcionário estiver cadastrado, na pasta de eventos, o código de cálculo 0005 – horas abonadas.

   
O recurso 'Limite' serve para limitar o número de dias ou horas em que o abono será utilizado. Juntamente, deverão ser preenchidos os parâmetros "Número de dias a considerar" e "Data de início" para o sistema considerar o limite de dias.

Caso o limite seja ultrapassado, o sistema emitirá uma mensagem no momento do lançamento de abono informando que o funcionário ultrapassou o limite de horas estabelecido.

**Observação**

* **Antiga gestão:** Na tela de lançamento de abono sintético o sistema irá perguntar se deseja continuar o lançamento, caso confirme, irá fazer o lançamento do abono mesmo tendo ultrapassado o limite.
* Funcionamento do recurso de limite na .

**Exemplo**

Se cadastrarmos um limite de 4 Dias de abono, com o Número de dias igual a 30 e Data de início igual a 01/08/2004, o sistema vai fazer a validação do lançamento de abonos apenas para o período de 01/08/2004 à 30/08/2004. Após 30/08/2004 este limite não será considerado para o lançamento.

Para que as horas abonadas sejam incluídas nas horas trabalhadas deverá ser utilizado o parâmetro 'Inclui nas horas trabalhadas'.

**Observação:** Esse parâmetro é válido para abono parcial ou seja quando o funcionário tem uma jornada de trabalho executada na data.  
   
**Exemplos:**  
Parâmetro "Inclui nas horas trabalhadas" marcado:  
Colaborador teve 4 Horas Trabalhadas e 4 horas de atraso, ao abonar as horas de atraso será demonstrada na visualização do espelho aba Totais do dia a informação 8 Horas trabalhadas.   
   
Parâmetro "Inclui nas horas trabalhadas " desmarcado:  
Colaborador teve 4 Horas Trabalhadas e 4 horas de atraso, ao abonar as horas de atraso será demonstrada na visualização do espelho aba Totais do dia a informação 4 Horas trabalhadas.  
  
Parâmetro "Disponível no RM Portal" marcado:  
Torna visível o abono no portal.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cópia de abono entre coligadas  
   
   
   
HelpWiki - RH - Automação de Ponto
