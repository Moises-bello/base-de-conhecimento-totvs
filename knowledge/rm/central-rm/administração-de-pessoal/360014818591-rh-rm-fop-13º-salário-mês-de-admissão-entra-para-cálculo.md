---
article_id: 360014818591
category: Administração de Pessoal
content_hash: 9541d8cf0f65add9bbeeef3fab736044d03bc4ca48af522db37aaecdbdbeb011
fetched_at: '2026-06-28T22:47:02.344213+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Mês de admissão entra para cálculo'
type: support-article
updated_at: '2025-03-13T11:19:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014818591-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-M%C3%AAs-de-admiss%C3%A3o-entra-para-c%C3%A1lculo
---

**Dúvida**Como funciona e como devo parametrizar corretamente o parâmetro **Mês de admissão entra para cálculo se admitido até dia?**  
   
 **Ambiente**RM - Folha de Pagamento - Todas as versões  
   
**Solução**Para verificar a funcionalidade do parâmetro. veja os comentários abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360010003591/mceclip0.png)  
  
O sistema **Totvs Folha de Pagamento** permite que seja definida um dia para que o mês de admissão seja ou não considerado no cálculo do 13º Salário. Para verificar a parametrização, acesse **Administração de Pessoal | Sindicato | 13º Salário**. Nesta visão procure pelo parâmetro **Mês de admissão entra para cálculo se admitido até dia**.

O sistema irá verificar a data de admissão do funcionário para determinar se o mês de admissão será ou não considerado para o calculo das médias de 13º Salário.

O parâmetro é executado da seguinte forma:

* Valor 0 - o mês de admissão NÃO entrará neste cálculo.
* Valor 31 - quando o usuário quiser sempre considerar o mês.

**Observação**  
Este parâmetro se refere ao cálculo das médias, pois referente ao cálculo de avos do décimo terceiro deve ser considerado de acordo com a legislação, então independente do parâmetro se o funcionário trabalhou 15 dias ou mais no mês terá direito aquele avo.
