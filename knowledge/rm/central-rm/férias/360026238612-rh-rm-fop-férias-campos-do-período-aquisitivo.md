---
article_id: 360026238612
category: Férias
content_hash: 3fc3d3381055ad69a2c583c5c88215071382ae3ac4e5dca62eb61c6989353e15
fetched_at: '2026-06-28T22:46:56.455384+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Campos do período aquisitivo'
type: support-article
updated_at: '2026-03-02T19:25:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026238612-RH-RM-FOP-F%C3%A9rias-Campos-do-per%C3%ADodo-aquisitivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como encontro os valores indicados no período aquisitivo, no cadastro do período de gozo do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para verificar como calcular os campos da visão do período de gozo dos funcionários, veja os comentários abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025777152/mceclip1.png)

* **Limite início de gozo:** Para encontrar esta data, verifique a data fim do período aquisitivo (28/02/2019) e o saldo do período (20 dias). Some um ano a data fim do período aquisitivo (28/02/2020) e subtraia os dias de saldo no período (20 dias). O resultado será a data do limite do inicio de gozo do funcionário (03/02/2020). Neste caso o último dia do período entra para o cálculo. Para encontrar a data exata, verifique o campo **FIMPERAQUIS.PFUFERIASPER** e realize os cálculos conforme indicado.
* **Férias a marcar:** As férias a marcar são as férias que ainda não foram gozadas, do período aquisitivo vencido. Normalmente trata-se dos dias em aberto do atual período aquisitivo do funcionário, se este já puder gozar as férias. Para verificar as férias a marcar, verifique o campo **NRODIASFERIAS.PFUFERIASPER**. Este campo indica os dias de férias que foram gozados pelo funcionário ou que serão gozados. Nesta tabela, cada linha simboliza um período de gozo. Verifique o último período aquisitivo e veja se o funcionário já pode gozar os dias em aberto do período aquisitivo. Para verificar se o funcionário já pode gozar as férias, veja o campo Limite início de gozo.
* **Saldo período:** O saldo do período são os dias de férias que ainda não foram gozadas do período aquisitivo em aberto do funcionário. Para verificar o saldo do período, verifique o campo **NRODIASFERIAS.PFUFERIASPER**. Este campo indica os dias de férias que foram gozados pelo funcionário ou que serão gozados. Para verificar o saldo do período, verifique todos os cadastros do período aquisitivo em questão. Os dias em aberto para o período aquisitivo será o saldo do período.
* **Saldo total:** O saldo total será sempre o total dos dias de férias dos períodos aquisitivos futuros em aberto do funcionário. Quando o funcionário possui férias em dobro, por exemplo, este campo irá somar os dois períodos em aberto do funcionário. Para verificar o saldo total, verifique o saldo do período e some a ele os dias em aberto dos períodos aquisitivos futuros até a presente data.
