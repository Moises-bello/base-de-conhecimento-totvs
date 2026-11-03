---
article_id: 360024976291
category: RH - Provisão
content_hash: 35214c7d26ec896eb77703aba984ef5dea75556a0c3756f9019a62aebb3b53f6
fetched_at: '2026-06-28T22:43:56.844698+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não esta calculando a provisão de fevereiro
  para alguns funcionários
type: support-article
updated_at: '2025-10-24T13:16:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024976291-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-esta-calculando-a-provis%C3%A3o-de-fevereiro-para-alguns-funcion%C3%A1rios
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32904170883479)*** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Sistema não esta calculando a provisão de fevereiro para alguns funcionários  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Sistema não calcula a provisão de fevereiro, quando o calculo entrar no seguinte cenário:

Empregado tenha sido admitido no dia 15 de qualquer mês, no mês de fevereiro não haverá calculo de provisão, pois, até a data do dia 28/02 não irá completar mais de 15 dias.

Entre o dia 15 até o dia 28/02 corresponde a 14 dias.

Vale lembrar que para o empregado receber 2,5 dias ou 1/12 avos tem que trabalhar 15 dias ou mais.

O mnemônico **P\_PGSALFEV** não interfere no calculo da provisão.

Abaixo a demonstração do calculo.

Provisão de janeiro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023363511)  
  
Provisão fevereiro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023325512)  
  
Em março o sistema irá calcular 1/12 avos a mais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023325552)

Se o empregado receber férias, por exemplo, em fevereiro. Será pago os 12,5 dias conforme o calculo da provisão de fevereiro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023325592)

Caso ocorra uma demissão no mês de fevereiro, com data de 15/02. Irá ser pago 12,5 dias de férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023325672)

Ou com data do dia 28/02 o pagamento será 12,5 dias equivalente a 5/12 avos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023325732)

**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) [Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
