---
content_hash: efe629b05235193c81586d8645f8c3ac08ce69db33a7fbff1df72f77995fd45c
fetched_at: '2026-06-29T00:10:08.561588+00:00'
page_id: '452719537'
product: rm
source: tdn-rm
title: Compensação de Dia Ponte - Anexos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719537
version: 87
---

Este anexo é utilizado para cadastrar o dia ponte, o período para alteração do horário e o número de horas utilizadas para alterar o número de horas diárias que o funcionário deve trabalhar. Para se cadastrar compensação do dia ponte é necessária preencher os campos abaixo de acordo com as informações: **Data** Informe a data a ser considerada como Dia Ponte.  
**Data Início** Informe a data início da compensação do dia ponte.  
**Data Fim** Informe a data fim da compensação do dia ponte  
**Tempo Máximo** Informe o tempo máximo da compensação do dia ponte. Ou seja informe o tempo que o funcionário deverá trabalhar a mais por dia para compensar as horas de falta do dia ponte.

**Observação** Apenas os funcionários com horário do tipo rígido e banco de horas diário por ocorrência podem utilizar o tempo máximo. Para usar o tempo máximo no cálculo devem ser informados apenas os seguintes campos: Data, Data Início, Data Fim e Tempo máximo. Os demais campos desta tela não podem ser preenchidos.

**Exemplo** É feriado dia 25/12 terça-feira, e os funcionários deverão trabalhar durante 16 dias trinta minutos a mais da jornada de trabalho (de 08:00 horas) para compensar a segunda-feira que não será trabalhada. Cadastrando o dia ponte, os dias da compensação e o tempo que o funcionário deverá trabalhar a mais para a compensação, o sistema não irá calcular horas extras para os funcionários durante os dias de compensação. Para a segunda-feira, dia 24/12 deverá ser lançado um evento de abono. As horas que excederem o tempo máximo serão pagas ou enviadas para o banco de horas (dependendo do tratamento para elas no aplicativo). Os atrasos gerados pelo não cumprimento do número de horas estabelecido no dia ponte terão uma atitude diferente dos demais atrasos e não serão utilizados no cálculo.  
Dia Ponte: 24/12 Período utilizado para compensar: 03/12 a 26/12. Nº de horas a compensar: 00:30 Horário do funcionário: 08:00 12:00 14:00 18:00 Batidas: Dia 03/12 08:00E 12:00S 14:00E 18:30S Dia 04/12 08:00E 12:00S 14:00E 18:20S Dia 05/12 08:00E 12:00S 14:00E 18:40S  
Movimentação: Dia 03/12 00:00 de hora extra, 00:00 de atraso. Dia 04/12 00:00 de hora extra, 00:10 de atraso, atitude 2(desconsiderar). Dia 05/12 00:10 de hora extra, 00:00 de atraso, atitude 0 ou 1(Depende do tratamento).

**Alterar horário do funcionário considerando incrementar somente os dias de compensado:** Marcando este parâmetro o sistema fará a alteração do horário do funcionário considerando incrementar somente os dias de compensado.Será considerado somente a jornada cadastrada do compensado para estender o intervalo no início ou fim do dia com base na jornada executada.

**Altera horário do funcionário conforme horas a incrementar ou decrementar:** Marcando este parâmetro o sistema vai habilitar os campos "Horas a incrementar" e "Horas a decrementar". Este parâmetro juntamente com um dos parâmetros abaixo fará a alteração do horário do funcionário incrementando ou decrementando de acordo com a necessidade.

**Observação** Para marcar esta opção o campo tempo máximo não pode estar preenchido.  
**Consideração sobre alteração da jornada** **Altera o início da jornada** Marcando este parâmetro o sistema altera o horário do funcionário no início de sua jornada.  
**Altera o término da jornada** Marcando este parâmetro o sistema altera o horário do funcionário no final de sua jornada.  
**Horas a incrementar** Informe neste campo o número de horas ou minutos que o sistema deve incrementar ao horário do funcionário. Quando devemos utilizar este parâmetro? Quando tiver um feriado em uma quinta-feira e a empresa permitir que seus funcionários trabalhem uns minutos a mais no dia durante um certo período para que seus funcionários compensem a sexta-feira. Marcando o parâmetro "Altera horário do funcionário conforme horas a incrementar" e informando o número de horas a incrementar o sistema passa a incrementar as horas informadas no horário do no período determinado. O cálculo das horas extras, atrasos e faltas são considerados de acordo com as horas que serão incrementadas no horário do funcionário. Consideração sobre alteração da jornada O sistema dará as opções "Altera o início da jornada" e "Altera o término da jornada" para considerar o número de horas a incrementar ou decrementar no início ou fim da jornada do funcionário.

**Observação:** No horário flexível as horas são acrescentadas após a compensação diária.

**Exemplo 2:** Horário do funcionário: 22:00 às 05:00 Dia Ponte: 08/07/2006 Data Início: 12/07/2006 Data Fim: 16/07/2006 X Altera horário do funcionário conforme horas a incrementar ou decrementar. X Altera término da jornada 00:30 incrementar Horário do funcionário: 07/07/05 QUI - 05:00S 22:00E 08/07/05 SEX - 05:00S 22:00E 09/07/05 SAB - 05:00S Batidas do funcionário: 07/07/05 QUI - 05:00S 22:00E 08/07/05 SEX - 05:00S Movimento do funcionário: 05:00 horas extras normais para o dia 08/07.

**Observação** No dia ponte não pode ter batida. O sistema calculará hora extra para qualquer intervalo de horas trabalhadas no dia ponte.  
**Horas a decrementar** Informe neste campo o número de horas ou minutos que o sistema deve decrementar ao horário do funcionário. Quando devemos utilizar este parâmetro? Para os funcionários que trabalham a mais durante a semana para compensarem no sábado. Em um determinado sábado temos um feriado, os funcionários não terão necessidade de trabalhar mais durante a semana para compensar este sábado.

**Observação** Para os funcionários com horário do tipo rígido e semi-flexível, o sistema irá decrementar as horas apenas na última batida do horário do funcionário. Já no horário flexível as horas são diminuídas após a compensação diária.

**Observação** A fórmula só será considerada se o parâmetro "Altera horário do funcionário conforme horas a incrementar ou decrementar" estiver marcado.

**Exemplo** Caso queira que o funcionário compense o dia ponte apenas na segunda-feira do período informado basta criar uma fórmula para verificar se o dia da semana é segunda-feira retornar verdadeiro. Dia Ponte: 27/05/2005 Período: 30/05/2005 à 30/06/2005 Horas a incrementar: 00:30 Fórmula a ser criada: SE DIASEM(PAR) = 'SEG' ENTAO VERDADE SENAO FALSO  FIMSE  
Com esta parametrização o sistema vai considerar apenas as segundas para a compensação. Horário: 08:00 12:00 14:00 18:00 Batidas: 30/05/2005 - 08:00 12:00 14:00 18:30 Horas Base: 08:30 Horas trabalhadas: 08:30  
Batidas: 31/05/2005 - 08:00 12:00 14:00 18:30 Horas Base: 08:00 Horas trabalhadas: 08:30 Horas Extras: 00:30

**Alterar horário do funcionário considerando incrementar somente os dias de compensado:** Este parâmetro marcado permite que o Dia Ponte seja compensado apenas em dias de compensado que esteja  
dentro do período informado em "Data início" e "Data fim", criando jornadas com a quantidade de horas informadas no campo "Horas a incrementar".
