---
article_id: 14607771435031
category: RH - Folha de Pagamento
content_hash: d016f3fae9ef1792c330907b65ec1de45d86b4f45f2550677f1d6862a6491a52
fetched_at: '2026-06-28T22:44:12.159953+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como as verbas de férias transitam na folha de
  pagamento
type: support-article
updated_at: '2025-10-06T13:22:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14607771435031-RH-Linha-Protheus-GPE-Como-as-verbas-de-f%C3%A9rias-transitam-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26235922756631) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como as verbas de férias transitam na folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**As verbas de férias transitam na folha apenas como demonstração após integração do roteiro FER e cálculo da folha, então no padrão, quando existe cálculo de férias no período, não tem como não demonstrar as verbas de férias na folha, e no caso de férias partidas, no período de início das férias serão demonstradas as verbas de férias do mês e verbas de férias do mês seguinte, e no período seguinte serão demonstradas as verbas de férias mês seguinte que viravam férias do mês.

Exemplos  
  
**1 - Férias que abrange apenas um período:**

Recibo de férias  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14606827873815)

Cálculo da folha após integração do roteiro FER  
Somando os proventos de férias menos os descontos de férias, temos a verba de líquido de férias para zerar os valores de férias e ser apenas demonstrativo na folha  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14606879837591)

**2 - Férias partidas que abrange dois períodos:**

Recibo de férias, constam as verbas de férias do mês e verbas de férias mês seguinte:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14606947231639)

Cálculo da folha após integração do roteiro FER, período de início das férias  
É demonstrada na folha as verbas de férias do mês e férias mês seguinte, e somando todos os proventos de férias menos todos os descontos de férias, temos a verba de líquido de férias que zera os valores de férias na folha:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14607406821655)

Cálculo da folha após integração do roteiro FER, período fim das férias  
Também é demonstrada na folha as verbas de férias, mas por ser o período final das férias, as verbas que eram férias mês seguinte viraram verbas de férias mês, e somando os proventos de férias menos os descontos de férias, temos a verba de líquido férias que zera os valores de férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14607513189015)

**Observação:** O INSS de férias pode ser calculado de 3 formas diferentes de acordo com o MV\_DINSSFM, então a demonstração dele na folha também.

**Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Como configurar verbas de férias mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027941171)  
[RH - Linha Protheus - GPE - Configuração do parâmetro MV\_DINSSFM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016451652)
