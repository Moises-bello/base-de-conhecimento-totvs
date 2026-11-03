---
article_id: 360020179192
category: Administração de Pessoal
content_hash: 6aa8ec6745700f73d168af358ee93eeb6b1e42786850d2d570c57c2bfa53d71b
fetched_at: '2026-06-28T22:47:02.282977+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Médias: Parâmetros gerais de médias'
type: support-article
updated_at: '2025-03-05T18:57:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020179192-RH-RM-FOP-M%C3%A9dias-Par%C3%A2metros-gerais-de-m%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:12 min****Dúvida**Qual a funcionalidade dos parâmetros dos **Parâmetros gerais de médias** na aba **Média** em **Administração de Pessoal | Sindicatos**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Segue funcionalidade de cada parâmetro dos **Parâmetros gerais de médias** na aba **Média** em **Administração de Pessoal | Sindicatos:**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959614701719)

* **Considera o mês de rescisão para média:** Com este parâmetro marcado serão considerados todos os eventos que incidem em médias no mês da rescisão, para o cálculo da rescisão do funcionário. Todos os tipos de médias serão considerados, sejam férias, 13º salário ou aviso prévio. Caso o parâmetro esteja desmarcado o cálculo das médias na rescisão irá calcular as médias considerando até mês anterior da rescisão do funcionário. Para que o sistema considere o mês de rescisão para as médias em rescisões anteriores ao dia 15 do mês, também é necessário que o parâmetro abaixo esteja habilitado.
* **Considera mês atual se data (início férias/rescisão) menor do que 15:** Marcando este parâmetro o sistema irá considerar o mês de início das férias ou rescisão para o cálculo das médias independente do dia de início das férias/Rescisão. Caso o parâmetro não seja marcado, serão considerados somente quando o início de gozo das férias ou a data de rescisão for maior ou igual a 15. Quando o cálculo da média é parametrizado por período aquisitivo e a data de início do gozo é maior que o término do período aquisitivo, este parâmetro não é considerado.
* **Calcula média de salário comissão verificando número de meses de comissão:** O cálculo das médias das comissões recebidas- salário comissão, para cálculo da base de Férias, 13° Salário, Aviso Prévio ou Licença Maternidade é feito sobre o valor total das comissões recebidas no período indicado no sindicato, dividido pelo número de meses em que o funcionário recebeu a comissão.
* **Calcula média para aviso prévio descontado:** Com esta o flag habilitada, o sistema irá realizar o cálculo das médias para aviso prévio descontado. O valor das médias sobre aviso prévio neste caso será somado ao evento de desconto do aviso prévio, mesmo nos casos em que a média está parametrizada para pagamento discriminado.
* **Utiliza cálculo de média de Remuneração Base para professor:** Caso esta opção seja marcada, será habilitada a aba **Remuneração Base** no sindicato, que possuirá abas específicas para configuração da composição do salário base de todos os funcionários do tipo **P – Professor** nos cálculos de Férias, 13º Salário, Rescisão e Salário Maternidade. Para essa nova remuneração base, o sistema desconsiderará o salário composto do funcionário nos cálculos citados e serão considerados todos os eventos que possuam o parâmetro **Compõe Remuneração Base de Professor** marcado.
