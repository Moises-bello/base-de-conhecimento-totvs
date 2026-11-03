---
article_id: 360036277654
category: RH - Provisão
content_hash: c883ed492f9a9e24ac316ea3c882d5542247788543d9b3a2b8976a0d5a06f171
fetched_at: '2026-06-28T22:43:55.594547+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE -  Provisão de Férias Proporcionais com Férias Antecipadas
type: support-article
updated_at: '2025-10-24T12:51:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036277654-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-F%C3%A9rias-Proporcionais-com-F%C3%A9rias-Antecipadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998138393623)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como conferir os cálculos de Provisão de Férias com Férias Antecipadas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

Provisão de férias é uma reserva financeira para possível pagamento de férias, ou seja, se o funcionário possui 15 avos de direito, será efetuado uma reserva do valor correspondente a estes 15 avos, para que, no caso do funcionário efetivamente gozar férias, a empresa ter fundos para pagá-lo. Por outro lado, se o funcionário não tem avos de férias para tirar no mês de cálculo da provisão, nada deve ser provisionado.

Por Exemplo Funcionário admitido em 01/01/2018;  
  
- Provisão de férias calculada em 31/01/2018 será de 2,5 dias;  
- Provisão de férias calculada em 28/02/2018 será de 5,0 dias;  
- Provisão de férias calculada em 31/03/2018 será de 7,5 dias;  
- Provisão de férias calculada em 30/04/2018 será de 10,0 dias;  
- Provisão de férias calculada em 31/05/2018 será de 12,5 dias;

Em 06/2018, foi calculada férias de 20 dias para o funcionário.  
  
- Provisão de férias calculada em 30/06/2018 gera baixa referente aos 20 dias de férias, zera o campo 'Dias Férias Prop.' e preenche o campo 'Dias Férias Antec.' com 20.  
- Provisão de férias calculada em 31/07/2018 será de 0,0 dias e 'Dias Férias Antec.' com 20;  
- Provisão de férias calculada em 31/08/2018 será de 0,0 dias e 'Dias Férias Antec.' com 20;  
- Provisão de férias calculada em 30/09/2018 será de 2,5 dias e 'Dias Férias Antec.' com 20;  
- No mês em que o funcionário obteve direito a 22,5 dias de férias o sistema apresentou os 2,5 dias no cálculo da provisão, ou seja, 22,5 dias de direito subtraído os 20 dias de férias antecipados.

No exemplo o funcionário possuía 15 dias de direito e tirou 20 dias de férias, até que ele passe a ter 22,5 dias de férias, nada será provisionado, porque nada deverá ser pago até esta data. No mês que ele finalmente possuir mais dias de direito do que dias de férias antecipadas, será feita a provisão do saldo, no caso, 2,5 dias.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://tdn.totvs.com/pages/viewpage.action?pageId=317002829>
