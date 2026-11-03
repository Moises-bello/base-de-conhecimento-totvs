---
article_id: 360057345093
category: RH - Benefícios
content_hash: 3baf64690753912f6b5ba6bb4ddb7e23c52def38531e34e91f6c4854ad2d34d2
fetched_at: '2026-06-28T22:44:03.908940+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Desconto de Vale Transporte com parâmetro MV_CVTPROP
  = P
type: support-article
updated_at: '2025-09-26T14:03:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057345093-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-com-par%C3%A2metro-MV-CVTPROP-P
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32069502770327) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como calcular o desconto do vale transporte considerando os dias pagos de vale transporte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para que o desconto do vale transporte seja proporcional aos dias pagos do benefício é necessário configurar o parâmetro **MV\_CVTPROP com P** e **MV\_CVTUSO** com **1**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32069526812695)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32069502772503)**

**Exemplo de Cálculo**Funcionário receberá 17 dias de vale transporte em decorrência de férias.   
O desconto será feito sobre os dias informados ou calculados no Campo R0\_DIASPRO (Dias proporcionais de vale transporte).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32069526816023)

**Base para Desconto** = Salário / 30 dias (ou dias do período) x Dias proporcionais de vale transporte.

Salário: 4.000,00  
Total de dias referente ao período (MV\_DIASPER): 30  
Dias proporcionais de vale transporte: 17  
4.000,00 / 30 \* 17 = 2.266,67  
2.266,67 \* 6% = **136,00**

**Obs.:** No momento do calculo deve ser informado que o cálculo será proporcional de acordo com a  situação de cada funcionários (Admissão, Férias e Afastamento):![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093859594)

**Saiba Mais**[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP)  
[RH - Linha Protheus - GPE - MV\_CVTPROP igual a P para Horistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052131333-RH-Linha-Protheus-GPE-MV-CVTPROP-igual-a-P-para-Horistas)  
[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo)
