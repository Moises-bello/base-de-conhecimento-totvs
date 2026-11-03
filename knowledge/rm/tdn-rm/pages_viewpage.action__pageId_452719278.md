---
content_hash: 00b23e59d31b90ed2f0fe2c6c1ef2d8d662344fdeb1f3c09c6abdfdef1867eac
fetched_at: '2026-06-29T00:10:05.188804+00:00'
page_id: '452719278'
product: rm
source: tdn-rm
title: Remuneração Base de Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719278
version: 9
---

Nesta pasta serão exibidas 6 subpastas com parâmetros para o cálculo da Remuneração nos seguintes tipos de cálculo: Férias Normais, Férias na Rescisão, 13º Salário, 13º na Rescisão, Aviso Prévio, Salário Maternidade.  
Em todas subpastas existirão parâmetros comuns que serão aplicados de acordo com cada processo de cálculo:

**No caso de valor proporcionalizado, efetuar engenharia reversa para obter valor integral**

Quando for marcado este parâmetro, será aplicada uma proporção tipo "regra de 3" no valor calculado dos eventos, para os funcionários que não trabalharam a escala integral do mês competência.  
Para calcular os valores integrais dos meses em que o funcionário esteve ausente de forma parcial, deverá realizar uma engenharia reversa para obter o valor integral, já que os valores estão proporcionalizados no mês.   
   
Exemplo: Caso o funcionário tenha gozado férias em 27 dias do mês, o evento que incide na remuneração base foi proporcionalizado para ser pago referente a 3 dias trabalhados. Efetuando a engenharia reversa, ele considerará o evento com o valor integral, ou seja, calculado sobre os 30 dias.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Mês/Ano** | **Evento** | **Descrição** | **Horas** | **Ref** | **Pago na Ficha Financeira** | **Valor Considerado** | **Situação** |
| fev/15 | 1040 | Repouso Semanal Professor | 10:00 | 10,0 | 203,73 | 203,73 | Ativo |
| mar/15 | 1040 | Repouso Semanal Professor | 15:00 | 15,0 | 305,60 | 305,60 | Ativo |
| abr/15 | 1040 | Repouso Semanal Professor | 12:30 | 12,5 | 254,67 | 254,67 | Ativo |
| mai/15 | 1040 | Repouso Semanal Professor | 10:00 | 10,0 | 203,73 | 203,73 | Ativo |
| jun/15 | 1040 | Repouso Semanal Professor | 6:00 | 6,0 | 122,24 | 183,34 | Afastado 10 dias |
| jul/15 | 1040 | Repouso Semanal Professor | 0:00 | 0,0 | 0,00 | 0,00 | Afastado 30 dias |
| ago/15 | 1040 | Repouso Semanal Professor | 12:00 | 12,0 | 244,48 | 293,38 | Afastado 5 dias |
| set/15 | 1040 | Repouso Semanal Professor | 15:00 | 15,0 | 305,60 | 305,60 | Ativo |
| out/15 | 1040 | Repouso Semanal Professor | 12:30 | 12,5 | 254,67 | 254,67 | Ativo |
| nov/15 | 1040 | Repouso Semanal Professor | 10:00 | 10,0 | 203,73 | 203,73 | Ativo |
| dez/15 | 1040 | Repouso Semanal Professor | 14:00 | 14,0 | 285,23 | 316,92 | Férias 3 dias |
| jan/16 | 1040 | Repouso Semanal Professor | 2:30 | 2,5 | 50,93 | 509,33 | Férias 27 dias |
| **TOTAL** |  |  |  |  | 2.434,61 | 3.034,70 |  |

Para a tabela acima, podemos considerar as seguintes informações:  
Afastamento pela previdência no período de 05/06/2015 a 05/08/2015.  
Gozo de férias de 29/12/2015 a 27/01/2016.  
   
Evento do salário composto: 1040 - Repouso Semanal Professor  
Salário Nominal: 305,60  
Jornada Mensal: 15,0  
Salário Hora: 20,373333  
   
Dias trabalhados:  
Jun/15 = Serão considerados 20 dias trabalhados pois contará com os 15 dias de atestado devido ao tipo de afastamento.  
Jul/15 = 0 dias trabalhados.  
Ago/15 = Serão considerados 25 dias trabalhados pois está com 5 dias de afastamento e é considerado o mês comercial com 30 dias.  
Dez/15 = 27 dias trabalhados  
Jan/16 = 3 dias trabalhados  
Observação: Os eventos do tipo Hora, Dia e Referência serão atualizados de acordo com o valor do salário atual do funcionário, já os eventos do tipo Valor serão considerados os valores pagos na época.  
Cálculo para eventos do tipo Hora/Referência:  
Hora ou Referência \* %Incidência no evento \* Valor do salário hora = Valor atualizado  
   
Cálculo para eventos do tipo Dia:  
Referência \* (Salário Nominal / 30) = Valor atualizado  
   
Cálculo para eventos do tipo Valor:  
Valor lançado na ficha financeira  
   
Efetuando a engenharia reversa:  
Valor atualizado / Dias trabalhados \* 30 = Valor Considerado  
   
Ex.: Cálculo do evento tipo Hora 1040 – Repouso Semanal Professor  
   
Mês 06/2015: 6,000000 \* 1,0 (%inc.) \* 20,373333 = 122,239998   
(122,239998 / 20 \* 30 = 183,359997)  
   
Para o exemplo acima, as 6 horas lançadas no mês 06/2015 foram atualizadas com o salário atual chegando ao valor de 122,24. Como foram trabalhados 20 dias nesse mês, o sistema divide o valor atualizado pelos dias trabalhados e multiplica por 30, assim se obtém o valor integral do evento.

**Observação:** Caso o funcionário possua outros eventos incidentes na Remuneração Base que não componham o seu salário composto, o valor do salário hora no cálculo será o somatório de todos os eventos do salário composto dividido pela soma de suas jornadas.

**Observação:**

O evento de código de cálculo **145 - Atestado Médico (Previdência)** deve ser usado para pagamento dos 15 dias de afastamento pagos pela previdência e não deve ter o parâmetro “Compõe Remuneração Base de Professor” marcado.

**Exemplo:**

* Afastamento de 15 dias dentro do mês - No envelope deve existir o evento CC 145 sem marcar o parâmetro “Compõe Remuneração Base de Professor”.
* Pagamento de salário composto de 15 dias dentro do mês – No envelope deve existir os dois salários compostos com o parâmetro “Compõe Remuneração Base de Professor” marcado.

O cálculo da proporcionalização será feiro da seguinte forma:

Calculando média do evento tipo H: **0253 - HORA AULA ADMINISTRAÇÃO**

Mês 10/20XX: 55,000000 \* 1,00 (%inc.) \* 13,636364 = 750,000000 (750,000000 / 15 \* 30 = 1.500,000000)

 Calculando média do evento tipo H: **0255 - HORA AULA SISTEMAS DE INFORMAÇÃO**

 Mês 10/20XX: 55,000000 \* 1,00 (%inc.) \* 13,636364 = 750,000000  (750,000000 / 15 \* 30 = 1.500,000000)

**Quantidade de meses**  
   
Neste campo deverá ser informado os últimos N meses a serem utilizados para apuração do tipo de cálculo, ou seja, o sistema verificará as informações até o mês anterior ao de competência atual retroagindo à quantidade informada.  
   
Somente para os cálculos de Férias Normais e Férias na Rescisão, se for informado o número zero serão considerados os meses do Período Aquisitivo do funcionário. Os demais processos não poderá informar zero nesse campo.  
Observação: Caso a admissão do funcionário tenha ocorrido após a projeção do período de apuração, a quantidade de meses será diminuída proporcionalmente aos meses trabalhados. Por exemplo, se foi solicitada a média dos últimos 12 meses, e o funcionário foi admitido somente a 7 meses atrás, o cálculo da média passará a ser dos últimos 7 meses para esse funcionário.

**Desconsiderar meses do ano competência anterior**  
   
Esse parâmetro ficará disponível apenas para as subpastas de 13º Salário e 13º Rescisão.  
   
Marcando esse parâmetro, caso a quantidade de meses ultrapasse o ano de competência atual, o sistema não considerará os meses do ano anterior para os cálculos da Remuneração Base.  
Observação: Caso esteja no mês de Janeiro e use o parâmetro marcado, o sistema não calculará a base de remuneração para eventos de 13º salário e 13º rescisão, ou seja, para esses eventos a remuneração base será zerada. Isso porque o limite de verificação é sempre o mês anterior à competência do cálculo.

**Tipo de Cálculo**  
    
**Maior Remuneração**  
   
Nesta opção será verificado mês a mês dentro da quantidade de meses informada o maior valor de remuneração base do funcionário.  
   
Serão considerados todos os eventos lançados na ficha financeira que possuam o parâmetro "Compõe Remuneração Base de Professor" marcado. Eles serão somados a cada mês, e o mês com maior valor será o considerado como Remuneração Base do Professor.  
   
Este somatório de valores será efetuado aplicando a atualização dos valores dos eventos do tipo hora, dia e referência ao salário atual, e somando o valor pago na época dos eventos tipo Valor.  
Observações:

* O salário atual é a soma do Salário Composto vigente na competência corrente.
* Para esse tipo de cálculo serão considerados apenas o número de meses informados. Caso o funcionário não tenha movimentação dentro do número de meses, a remuneração base será zerada.

**Média da Remuneração**  
   
Nesta opção irá buscar na ficha financeira, todas as ocorrências dos eventos marcados com a incidência "Compõe Remuneração Base de Professor", considerando a quantidade de meses de acordo com cada processo de cálculo.  
   
Será aplicado a atualização dos valores dos eventos do tipo hora, dia e referência ao salário atual, e para os eventos do tipo Valor será considerado o valor pago na época.  
   
Após a atualização, será feita a média aritmética das remunerações dentro da quantidade de meses informada para cada processo de cálculo.  
   
Se durante o período de apuração ocorrer algum mês em que o funcionário esteve integralmente afastado ou de férias, sem nenhuma remuneração, será aplicada a última carga horária trabalhada antes do afastamento. Caso o funcionário não tenha remuneração no começo do período de apuração, o sistema continuará a percorrer a ficha financeira até que encontre o mês com remuneração incidente.  
   
**Exemplo:**   
Competência do cálculo de rescisão: 03/2016  
Remuneração Base de Aviso Prévio dos últimos: 12 meses.  
Período a ser considerado: 03/2015 a 02/2016  
Nos meses 09, 10 e 11/2015 o funcionário esteve afastado de forma integral e sem lançamento de remuneração.  
   
Resumo da Remuneração Mensal:  
    Mês 03/2015: 7.955,283528  
    Mês 04/2015: 6.854,755027  
    Mês 05/2015: 7.371,662486  
    Mês 06/2015: 3.346,667716  
    Mês 07/2015: 6.587,396519  
    Mês 08/2015: 15.738,995874  
    Mês 12/2015: 1.261,921499  
   
    Na competência 09/2015 será considerada a Remuneração do mês 08/2015: 15.738,995874  
    Na competência 10/2015 será considerada a Remuneração do mês 09/2015: 15.738,995874  
    Na competência 11/2015 será considerada a Remuneração do mês 10/2015: 15.738,995874  
    Na competência 01/2016 será considerada a Remuneração do mês 12/2015: 1.261,921499  
    Na competência 02/2016 será considerada a Remuneração do mês 01/2016: 1.261,921499  
    Média da Remuneração: 98.857,513271 / 12 = 8.238,126106  
   
Total da Remuneração Base de Aviso Prévio: 8.238,126106  
   
Observação: Caso o evento incidente tenha como Base de Salário (Cadastro de eventos I Anexos I Eventos Relacionados Reprogramação Salarial) um evento que não consta atualmente no cadastro de Salário Composto, será considerado o valor pago na época, sem a atualização para o salário atual mesmo que seja um evento do tipo Hora, Referência ou Dia.  
   
**Última Remuneração**   
   
Nesta opção será considerada a Remuneração Integral do mês anterior, somando os valores de todos os eventos marcados com a incidência "Compõe Remuneração Base de Professor".   
   
Será aplicado a atualização dos valores dos eventos do tipo hora, dia e referência ao salário atual, e para os eventos do tipo Valor será considerado o valor pago na época.  
   
Se no mês anterior o funcionário esteve integralmente afastado ou de férias, sem nenhuma remuneração, será considerada a última carga horária trabalhada antes do afastamento, ou seja, o sistema continuará a percorrer a ficha financeira até que encontre o último mês com remuneração incidente.  
Observação: Utilizando esse tipo de cálculo, o sistema ignorará o campo "Quantidade de meses", pois sempre buscará o último mês com a remuneração.

**Comparativo Média X Última Remuneração**   
   
Nesta opção o sistema calculará a Remuneração Base utilizando os métodos de Média e Última Remuneração e aplicará o maior valor entre ele.

**Considera mês atual**

Marcando este parâmetro será considerado o mês atual para o cálculo da remuneração do professor.

Se o número de meses for 3 e o sistema estiver na competência 10, será considerado da seguinte maneira:

* Considera mês atual marcado = meses 8, 9 e 10
* Considera mês atual desmarcado = meses 7, 8 e 9

**Observação:** Para funcionário admitido no mês atual deve haver eventos lançados na ficha financeira para que sejam considerados no cálculo.

**Exemplo:** O cálculo da primeira parcela do 13º salário deve ser feito após o cálculo da folha de pagamento quando o funcionário for admitido no mês atual e o parâmetro “Considera mês atual” estiver marcado.

**Calcula a média considerando o valor do evento**

Marcando este parâmetro os eventos dos tipos Dia, Hora e Referência serão calculados de acordo com os valores dos eventos pagos e registrados na ficha financeira.

**Observação:** Estes valores poderão ser corrigidos marcando também os parâmetros “Corrige valores pelo salário da época” e “Corrige valores considerando o salário hora”.

**Exemplos:**

  Calculando média do **evento tipo R:** 0178 - ADICIONAL NOTURNO EXTRA 75%

    Mês 02/20XX: 1.200,00

    Media do Evento 0178: 1.200,000000 / 12 = 120,000000

  Calculando média do **evento tipo D:** 0223 - FALTAS ABONADAS

    Mês 02/20XX: 1.500,00

    Media do Evento 0223: 1.500,000000 / 12 = 125,000000

  Calculando média do **evento tipo H:** 0253 - HORA AULA - ADMINISTRAÇÃO

    Mês 01/20XX: 1.100,00

    Media do Evento 0253: 1.100,000000 / 12 = 91,666667

**Corrige valores pelo salário da época**

Marcando este parâmetro os eventos do Tipo Valor serão corrigidos de acordo com o histórico salarial do funcionário para o cálculo da remuneração base do professor. Neste caso será considerado o valor total do salário base, ou seja, se houver salário composto será considerado a soma de todos os salários composto que é o salário base do funcionário.

**Exemplo:** Pagando média anterior a seis meses corrigindo o valor do DSR considerando o salário base:

  Calculando média do evento tipo V: 0102 - DESCANSO SEMANAL REMUNERADO

    Mês 11/20XX: 1.258,89 / 607,09 (Sal.Histórico) \* 1.667,80 (Sal.Atual) = 3.458,427485

**Corrige valores considerando o salário hora**

Este parâmetro somente será habilitado marcando o parâmetro “Corrige valores pelo salário da época” anterior. Sendo marcado este parâmetro, os eventos do Tipo Valor serão corrigidos de acordo com o valor hora do salário do histórico salarial do funcionário para o cálculo da remuneração base do professor.

**Exemplo:** Pagando média anterior a seis meses corrigindo o valor do DSR considerando o salário hora:

  Calculando média do evento tipo V: 0102 - DESCANSO SEMANAL REMUNERADO

    Mês 11/20XX: 1.258,89 / 2,76 (Sal.Histórico) \* 7,58 (Sal.Atual) = 3.457,386304

**Processos influenciados no cálculo**  
Para os funcionários com tipo de recebimento P – Professor que utilizem o sindicado que está parametrizado para utilizar a Remuneração Base terão influencias em outros processos que envolvem cálculos de Férias, Rescisão e Salário Maternidade.

* Cálculo de Salário Maternidade: Para todos os cálculos que envolvam a licença maternidade, a quantidade de meses a ser verificada será até a anterior à competência do afastamento. Serão analisados os parâmetros de Remuneração Base I Licença Maternidade no cadastro do sindicato.  
  Para os períodos de afastamento, no momento do cálculo da diferença salarial, o sistema respeitará a parametrização atual, ou seja, caso a parametrização tenha sido alterada após o lançamento do salário maternidade, o sistema não avaliará a parametrização da época do pagamento.

* Provisões de Férias e 13º Salário: A geração do histórico de Provisões, quando executado para funcionários Ativos irá considerar o mesmo cálculo parametrizado para "Férias Normais" e "13º Salário", e quando a execução for para demitido no mês, o cálculo irá verificar a parametrização selecionada para "Férias Rescisão" e "13º Rescisão".
* Diferença de 13º Salário: Quando ocorrer aumento salarial retroativo a dezembro, após o pagamento da 2ª Parcela do 13º Salário, deverá ser efetuado o cálculo da Diferença de 13º. Neste processo será considerada a mesma parametrização utilizada no cálculo da 2ª Parcela, onde a Remuneração apurada será aplicada ao salário vigente em dezembro.  
  Para os períodos de afastamento, no momento do cálculo da diferença, o sistema respeitará a parametrização atual, ou seja, caso a parametrização tenha sido alterada após o lançamento do 13º Salário, o sistema não avaliará a parametrização da época do pagamento.  
     
  Os eventos do tipo Hora terão a carga horária aplicada ao salário hora de dezembro, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente na competência dezembro.
* Diferença de Férias: Quando ocorrer aumento salarial retroativo ao período em que o funcionário estiver de férias, deverá ser efetuado o cálculo da Diferença de Férias. Neste processo será considerada a mesma parametrização utilizada no cálculo do Recibo de Férias, onde a Remuneração apurada será aplicada ao novo salário do funcionário.  
  Para os períodos de afastamento, no momento do cálculo da diferença, o sistema respeitará a parametrização atual, ou seja, caso a parametrização tenha sido alterada após o lançamento das férias, o sistema não avaliará a parametrização da época do pagamento.  
     
  Os eventos do tipo Hora terão a carga horária aplicada ao novo salário hora, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente no mês das férias.   
    
  Observação: Em uma situação de férias partidas, iniciando em um mês, e terminando no mês posterior, caso o aumento salarial comece a vigorar no início no segundo mês das férias, o valor calculado de diferença será proporcionalizado aos dias de férias do segundo mês.
* Rescisão Complementar: Quando ocorrer aumento salarial retroativo ao mês de demissão do funcionário ou durante a projeção do Aviso Prévio Indenizado, deverá ser efetuado o cálculo da Rescisão Complementar. Neste processo serão consideradas as mesmas parametrizações utilizadas no cálculo da Rescisão, considerando os tipos "Férias Rescisão", "13º Rescisão" e "Aviso Prévio", onde a Remuneração apurada será aplicada ao novo salário do funcionário.  
  Para os períodos de afastamento, no momento do cálculo da diferença, o sistema respeitará a parametrização atual, ou seja, caso a parametrização tenha sido alterada após o cálculo da rescisão, o sistema não avaliará a parametrização da época do pagamento.  
     
  Os eventos do tipo Hora terão a carga horária aplicada ao novo salário hora, e os eventos tipo Valor com fórmula, terão as fórmulas recalculadas, considerando o novo salário e a parametrização vigente no mês do aumento.   
  Observação: Caso o aumento salarial tenha início da vigência durante a projeção do Aviso Prévio Indenizado, no mês posterior ao mês da demissão, o aumento será aplicado proporcionalmente ao Aviso Prévio considerando somente os dias após a alteração salarial. No caso de Férias e 13º a diferença será paga integralmente com o novo salário.
* Logs: Todos os processos efetuados para apurar a Remuneração Base do Professor serão exibidos em uma Memória de Cálculo e ficarão gravados no Gerenciador de Log de Cálculo.

* Existe a possibilidade de utilização das funções de fórmula [MEDREMBASE e MEDREMBASEDATA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719272).
