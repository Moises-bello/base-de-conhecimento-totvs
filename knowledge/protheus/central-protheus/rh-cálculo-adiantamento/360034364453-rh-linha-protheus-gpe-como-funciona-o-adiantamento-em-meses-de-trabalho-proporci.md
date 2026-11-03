---
article_id: 360034364453
category: RH - Cálculo Adiantamento
content_hash: 93667d68dd649a4e2aec18c054402cdb62208c42a0bd3ceb3647f7f60159ffbe
fetched_at: '2026-06-28T22:43:14.265714+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o adiantamento em meses de trabalho
  proporcional
type: support-article
updated_at: '2025-12-09T14:25:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034364453-RH-Linha-Protheus-GPE-Como-funciona-o-adiantamento-em-meses-de-trabalho-proporcional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26440570650775) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como funciona o adiantamento em meses de trabalho proporcional (admissão, afastamento e férias)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O sistema possui o parâmetro **MV\_ADTOPRO** que calcula Adiantamento Quinzenal Proporcional no mês de admissão, férias ou afastamento.

**Lógica do MV\_ADTOPRO localizado no Configurador > Ambiente > Cadastros > Parâmetros (CFGX017).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941492375)**

**S=**Proporcionaliza o valor do adiantamento independentemente do número de dias trabalhados no mês, seja 5, 10, 12, 15, 18, com exceção a quem trabalhou 30 dias, que neste caso o sistema entenderá que o pagamento deve ser feito de forma integral.

**N=** Calcula o adiantamento Integral pra quem tiver => que 15 dias trabalhados no mês.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26440570656535)

Logo o sistema desenvolverá o seguinte processamento:

**MV\_ADTOPRO= S- Calcula o Adiantamento Quinzenal Proporcional no Mês?**

Empregado em período Normal:

T**rabalhou o mês cheio, irá calcular o valor integral.**

Adto corresponde a 40% do salário.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941493271)

Empregado Admitido no Mês:

**Admitido em 06/01/2025.**

Adto corresponde a 40% do salário.

Resumo do cálculo: 1.000,00 (salário) x 40% (percentual adiantamento) / 30 (dias do mês) x 26 dias trabalhados) = 346,67 (adiantamento).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941493655)

**Empregado em período de retorno de Férias:**

Período 01/01/2015 a 20/01/2025.

Adto corresponde a 40% do salário.

Resumo do cálculo: 1.000,00 (salário) x 40% (percentual adiantamento) / 30 (dias do mês) x 10 (dias trabalhados) = 133,33 (adiantamento).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392932681239)

**Empregado em período de retorno de Afastamento:**

Período 01/12/2024 a 15/01/2025- 15 dias trabalhados:

Adto corresponde a 40% do salário.

Resumo do cálculo: 1.000,00 (salário) x 40% (percentual adiantamento) / 30 (dias do mês) x 15 (dias trabalhados) = 200,00 (adiantamento).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941494679)

**Período 01/12/2024 a 18/01/2025- 12 dias trabalhados:**

Adto corresponde a 40% do salário.

Resumo do cálculo: 1.000,00 (salário) x 40% (percentual adiantamento) / 30 (dias do mês) x 12 (dias trabalhados) = 160,00 (adiantamento).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941495191)

Quando informada a opção **S** o sistema entenderá que o cálculo do adiantamento salarial deverá ser realizado de **forma proporcional aos dias trabalhados**, ou seja, independente se o empregado trabalhou 15 dias, ou mais, ou menos, o sistema fará o seguinte cálculo:

**Salário X Percentual de adiantamento/ 30 x o número de dias trabalhados no mês**, que poderá ser 10, 12, 15 ou 20 dias.

**MV\_ADTOPRO= N- Calcula o Adiantamento Quinzenal Proporcional no Mês?**

Empregado em período Normal:

**Trabalhou o mês cheio.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392932681623)

Empregado Admitido no Mês:

**Admitido em 05/01/2025.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392932681751)

Empregado em período de retorno de Férias:

**Período 01/01/2025 a 20/01/2025- Não calculou.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941496087)

Empregado em período de retorno de Afastamento:

**Período 01/12/2024 a 15/01/2025- 15 dias trabalhados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941496471)

**Período 01/12/2024 a 18/01/2025- 12 dias trabalhados: Não calculou.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31392941496855)

Quando informada a opção **N** o sistema entenderá que o cálculo do adiantamento salarial deverá ser realizado **apenas** para empregados que tenham **trabalhado 15 dias ou mais** no mês, sem efetuar a proporcionalização do cálculo, ou seja:

**Salário X Percentual de adiantamento**, válido para Admissão/Férias/Afastamento.  
  
Os dias de atestado pagos pela empresa são considerados como dias trabalhados no mês para fins de pagamento do adiantamento.  
  
**Saiba Mais**  
[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)  
[RH - Linha Protheus - GPE - Como calcular adiantamento em período de afastamento por doença](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058225013-RH-Linha-Protheus-GPE-Como-calcular-adiantamento-em-per%C3%ADodo-de-afastamento-por-doen%C3%A7a)
