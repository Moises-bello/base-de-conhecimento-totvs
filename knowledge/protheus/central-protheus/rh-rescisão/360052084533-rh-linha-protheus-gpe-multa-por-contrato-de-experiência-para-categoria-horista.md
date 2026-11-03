---
article_id: 360052084533
category: RH - Rescisão
content_hash: e40a40067a0497229f9a70b74608cc0f2c70ead5d5d1c3e4058395b09496781a
fetched_at: '2026-06-28T22:43:49.785359+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Multa por Contrato de Experiência para categoria
  Horista
type: support-article
updated_at: '2025-06-12T12:30:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052084533-RH-Linha-Protheus-GPE-Multa-por-Contrato-de-Experi%C3%AAncia-para-categoria-Horista
---

**Dúvida**Multa por Contrato de Experiência para categoria Horista.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Sistema está calculando o desconto de Multa Contrato Experiência (identificador de cálculo 0177) sobre 31 dias sendo o correto o cálculo ser por 30 dias onde o funcionário de categoria Horista tem sua Rescisão calculada em um mês de 31 dias e o mnemônico P\_DIASRES está como 1 para calcular o saldo de salario sobre 31 dias.

Consulta Tributária:

[Pedido de demissão - Contrato de experiência](http://tdn.totvs.com/pages/releaseview.action?pageId=396374178)

[Rescisão - Saldo de Salário - Deve ser por 30 dias ou de acordo com os dias do mês (28/29,30 ou 31)](https://tdn.totvs.com/pages/releaseview.action?pageId=185730478)

**Solução**Criado mnemônico **P\_RESMULTH** (Dias para Multa na Rescisão de Horista) cuja configuração será aplicada sobre o cálculo da Multa sobre Contrato de Experiência na geração das verbas com identificador:

0176 - Multa por Contrato de Experiência (provento)

0177 - Multa por Contrato de Experiência (desconto)

**Configuração do mnemônico (numérico):**

**1**=Dias Mês

**2**=30

O valor de salário base no cálculo da Rescisão no caso do funcionário horista irá respeitar o conteúdo do mnemônico P\_RESMULTH, consideremos a situação abaixo:

Funcionário de Categoria (RA\_CATFUNC) igual a H,

Salário (RA\_SALARIO) igual à R$ 6,00

Horas Mensais (RA\_HRSMES) igual a 220 horas,

Horas por Dia (RA\_HRSDIA) igual a 7.33.

Vencimento Experiência 1 (RA\_VCTOEXP) igual a 15/01/2019

Vencimento Experiência 2 (RA\_VCTEXP2) igual a 31/03/2019

Rescisão realizada em Janeiro (31 dias), Data de Demissão 01/01/2019

Sem verbas que incorporam ao salário.

Com configuração**P\_RESMULTH igual a 1**:

31 dias x 7.3333 horas por dia = 227.33

Salário Base = 6 x 227.33 = R$ 1.363,98

Com configuração **P\_RESMULTH igual a 2**:

30 dias x 7.3333 horas por dia = 220 horas (horas contratuais do cadastro de Funcionário)

Salário Base = 6 x 220 = R$ 1.320,00

Agora seguimos para a geração do valor de Pagto. Multa Contrato Exp. (**ID** **0176**):

Com configuração **P\_RESMULTH igual a 1**:

Salário/Dias de Cálculo x Dias à Pagar x 50%

1363.98/31 x (15/01/2018 – 01/01/2018) x 50%

44 x 14 x 50%

R$ 308,00

Com configuração **P\_RESMULTH igual a 2**:

Salário/Dias de Cálculo x Dias à Pagar x 50%

1320/30 x (15/01/2018 – 01/01/2018) x 50%

44 x 14 x 50%

R$ 308,00

**Observação Importante**

A configuração desse mnemônico irá prevalecer no cálculo da multa, sendo o mnemônico P\_DIASRES utilizado para configuração do cálculo das demais verbas do cálculo da Rescisão.
