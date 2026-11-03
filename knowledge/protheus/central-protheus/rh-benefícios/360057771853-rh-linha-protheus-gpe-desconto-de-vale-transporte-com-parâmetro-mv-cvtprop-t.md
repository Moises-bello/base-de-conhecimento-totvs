---
article_id: 360057771853
category: RH - Benefícios
content_hash: 5fe326754fa67f6b7b592044a7d16a62d99dcfc13146c48627d79db4cad5681e
fetched_at: '2026-06-28T22:44:03.912705+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto de Vale Transporte com parâmetro MV_CVTPROP
  = T
type: support-article
updated_at: '2025-09-17T17:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057771853-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-par%C3%A2metro-MV-CVTPROP-T
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16803753583895) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como sistema considera o calculo para o desconto de 6% do vale transporte sobre os dias trabalhados proporcionais (Parâmetro MV\_CVTPROP=T)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**Para que o desconto do vale transporte seja proporcional aos dias trabalhados, é necessário configurar o parâmetro **MV\_CVTPROP** com **T** e **MV\_CVTUSO** com **1:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32292396668823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32292396669847)

**Exemplo de Cálculo:**- Funcionário admitido em 15/05/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32292419174167)

- Base para Desconto = Salário / 30 dias (ou dias do período) X Dias trabalhados e DSR

Salário: 3.000,00  
Total de dias referente ao período (MV\_DIASPER): 30  
Dias trabalhados e DSR: 14 dias (12 dias trabalhados + 2 dias de DSR)  
3.000,00 / 30 \* 14 = 1.400,00  
1.400,00 \* 6% = **84,00**

**Obs.:** No momento do cálculo dever ser informado que o cálculo será proporcional de acordo com a situação de cada funcionário (Admissão, Férias e Afastamento):![](https://centraldeatendimento.totvs.com/hc/article_attachments/32292419176087)

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP)  
[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo)
