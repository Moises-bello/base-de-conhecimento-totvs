---
article_id: 10124252575511
category: Férias
content_hash: f7a508c45b221c01f46f8426cb9841fe0ba23855c3026245c546188defb88265
fetched_at: '2026-06-28T22:46:56.223480+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Apuração de faltas período aquisitivo
type: support-article
updated_at: '2024-10-18T15:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10124252575511-RH-RM-FOP-Apura%C3%A7%C3%A3o-de-faltas-per%C3%ADodo-aquisitivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min****Dúvida**Como é realizado a apuração período aquisitivo quando há faltas do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O sistema convencionou a apuração de faltas por período aquisitivo da seguinte forma: o sistema sempre considera as faltas no mês do vencimento do período aquisitivo independente do dia, ou seja, se o vencimento for 03/12/2016 e houver 20 faltas no mês 12/2016, essas faltas serão consideradas no período aquisitivo de final 03/12/2016.  
  
De acordo com o RM Folha, foi convencionado que, quando determinado funcionário tiver um período aquisitivo que começa e termina em um mesmo mês, por exemplo:  
  
               - 10/12/2016 a 09/12/2017 -> período vencido  
               - 10/12/2017 a 09/12/2018 -> período proporcional  
  
Suponha que seja um caso de demissão, que a competência atual seja 12/2018 e que se possua faltas na competência 12/2017. O sistema irá abater estas faltas sempre no período aquisitivo que possuir mês/ano de final de período aquisitivo, exceto se o início do período aquisitivo coincidir com o mês/ano de admissão. Logo, as férias serão abatidas do período vencido.  
  
Se as faltas tiverem ocorrido na competência 12/2016, elas serão abatidas do período vencido, pois não há nenhum período aquisitivo antes do período de férias vencidas (coincidente com a data de admissão). O único caso em que os meses de final do período aquisitivo vencido e início do período proporcional serão diferentes, é quando o período aquisitivo começar no dia 1º de determinado mês. Por exemplo:  
  
               - 01/12/2016 a 30/11/2017 -> período vencido  
               - 01/12/2017 a 30/11/2018 -> período proporcional  
  
Neste caso, não haverá problemas com o mês/ano de ocorrência da falta.  
  
**Saiba Mais**

[RH - RM - FOP - Utiliza Controle de Faltas para Cálculo de Avos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6179243296663-RH-RM-FOP-Faltas-per%C3%ADodo-aquisitivo-de-f%C3%A9rias)
