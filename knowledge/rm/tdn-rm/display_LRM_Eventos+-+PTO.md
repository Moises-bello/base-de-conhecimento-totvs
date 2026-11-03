---
content_hash: 9f2e650752fd0c66d8d76efe6528918ed110b78f705e103080da28ef3c3565a8
fetched_at: '2026-06-29T00:10:07.781566+00:00'
page_id: '452719436'
product: rm
source: tdn-rm
title: Eventos - PTO
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+-+PTO
version: 5
---

**Eventos**

---

Na aba Eventos no parametrizador do Sindicato são incluídos os eventos que serão utilizados para o cálculo da folha de pagamento. Para cada parâmetro Sindicato, devem ser cadastrados quais os eventos que, se presentes no movimento do funcionário que possui este parâmetro Sindicato, serão lançados para o RM Labore.   
   
**Código do evento calculado no Totvs Automação de Ponto**  
   
Informe o evento utilizado para o cálculo do movimento no Totvs Automação de Ponto (Chronus)  
   
**Código do evento relacionado RM Labore**  
   
Este evento será associado ao evento no Totvs automação de ponto e utilizado para lançamentos na folha de pagamento (Labore).  
   
**Código do evento do banco de horas lançado no movimento**  
   
Informe o evento para cálculo de horas no banco de horas e que posteriormente, poderá ser lançado no movimento (Chronus).  
   
**Cadastrar este evento nos eventos a serem lançados o Labore**  
   
No momento da inclusão de um evento o sistema habilita esta opção para incluí-lo também na pasta de "Eventos a serem lançados no Labore"  
   
**Considera percentual na compensação de horas**  
   
Ao habilitar este parâmetro o sistema passará a considerar o percentual cadastrado para o evento e irá multiplicar as horas extras por seus respectivos percentuais para realizar a compensação. Caso contrário, irá compensar extras com atrasos na proporção 1/1.  
   
*Exemplo:*  
   
O funcionário fez 02:00 horas extras 50% e 01:00 de falta. Cálculo efetuado pelo sistema:  
   
-Transformar as horas extras em minutos para facilitar o cálculo.Hora Extra = 02:00 = 120 minutos   
   
-Multiplicar o total das horas extras pelo percentual informado no evento no sistema RM Labore. No caso do exemplo o percentual é 50%. Vamos multiplicar as horas extras por 1.50  
120 X 1.5 = 180   
   
-Transformar as horas de falta em minutos.  
Hora de falta = 01:00 = 60 minutos  
   
-Diminuir as horas extras das horas de falta.  
180 - 60 = 120 (minutos de extra)  
   
-Temos que dividir as horas extras pelo percentual novamente para enviá-las para o movimento ou permanecer no banco de horas. As horas extras têm que voltar a sua forma original.  
120 / 1.5 = 80 minutos de extra = 01:20  
   
**Observação:**  
   
O cálculo do saldo do banco de horas nos relatórios do Espelho do Cartão de Ponto, Banco de Horas, Justificativas de Exceções também serão feitos de acordo com o percentual dos eventos se o parâmetro estiver marcado.  
   
**Utiliza na compensação manual de horas**  
   
Será utilizada apenas para os funcionários que possuem banco de horas por **período**, pois ao selecioná-la, o sistema irá lançar as extras dos funcionários para o banco de horas. Caso não selecionar esta opção o sistema irá lançar as horas extras para o movimento do funcionário.

O campo será habilitado quando o “Código do evento calculado no TOTVS Automação de Ponto” ser preenchido com um evento do tipo extra, sendo eles:

* 0018: 1a Faixa de Extra,
* 0019: 2a Faixa de Extra,
* 0020: 3a Faixa de Extra,
* 0021: 4a Faixa de Extra,
* 0022: 1a Faixa de Extra Descanso,
* 0023: 2a Faixa de Extra Descanso,
* 0024: 1a Faixa de Extra Feriado,
* 0025: 2a Faixa de Extra Feriado,
* 0026: 1a Faixa de Extra Compensado,
* 0027: 2a Faixa de Extra Compensado,
* 0036: 5a Faixa de Extra,
* 0047: Extra Reduzida,
* 0048: Extra Compensado Reduzida,
* 0049: Extra Descanso Reduzida,
* 0050: Extra Feriado Reduzida.

Eventos de Falta e Atraso

Para que eventos de atrasos e faltas sejam enviados para banco nesse caso, deve ser utilizado limite de horas diárias na parametrização de banco por periodo:

Documentação de apoio:

**Fórmula para lançamentos para o banco de horas**  
   
Informe neste campo uma fórmula de cálculo para o sistema lançar as horas calculadas pela fórmula para o banco de horas.Existindo a fórmula neste campo, o sistema irá desconsiderar o código de cálculo interno e será considerado o resultado da fórmula  
   
**Informações Adicionais - Atitude a ser Considerada no Dia/Evento** Informe neste campo qual atitude é desejada para o evento cadastrado. A informação deste campo está relacionada com o parâmetro 'Considera Atitude do Evento' localizado na parte de Banco de Horas.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

|  |
| --- |
|  |
