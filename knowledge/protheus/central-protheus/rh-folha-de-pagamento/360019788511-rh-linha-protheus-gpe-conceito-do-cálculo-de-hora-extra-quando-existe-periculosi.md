---
article_id: 360019788511
category: RH - Folha de Pagamento
content_hash: 04eed1915a709eab51cde9fd1cb57e229a081cf104cdfe70f9a20532341f8491
fetched_at: '2026-06-28T22:44:14.841009+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito do cálculo de hora extra quando existe
  periculosidade sobre salário e verbas
type: support-article
updated_at: '2025-08-11T20:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019788511-RH-Linha-Protheus-GPE-Conceito-do-c%C3%A1lculo-de-hora-extra-quando-existe-periculosidade-sobre-sal%C3%A1rio-e-verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26345619926167) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Conceito do cálculo de hora extra quando existe periculosidade sobre salário e verbas

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Na versão 12, é possível efetuar o cálculo de periculosidade utilizando o salário como base ou sobre o salário e verbas. Caso a periculosidade seja configurada para incorporar ao salário, haverá uma diferença no cálculo de hora extra devido a forma de apuração da periculosidade, pois poderá ser apurada antes ou após o cálculo da hora extra.

Por exemplo, um funcionário com salário mensal de R$ 5.000,00, que recebe periculosidade, que trabalha 220 horas por mês, que recebeu R$ 1.000,00 como gratificação e 10 horas extras a 100%, sendo que a verba de gratificação está configurada para incidir para periculosidade, a hora extra está configurada para ser calculada sobre o salário incorporado e a periculosidade está configurada para incorporar ao salário.

Se, no cadastro do sindicato, estiver definido que a periculosidade é calculada sobre o salário, o sistema efetuará o cálculo na seguinte ordem:

1. Cálculo da periculosidade sobre o salário;
   1. 30% X R$ 5.000,00 = R$ 1.500,00.
2. Cálculo da hora extra.
   1. Salário incorporado = R$ 6.500,00 (R$ 5.000,00 + R$ 1.500,00);
   2. Salário/hora = R$ 29,545 (R$ 6.500,00 ÷ 220);
   3. Salário/hora 100% = R$ 59,09 (R$ 29,545 X 2);
   4. Hora Extra = R$ 590,90 (10 X R$ 59,09).

Se, no cadastro do sindicato, estiver definido que a periculosidade é calculada sobre o salário + verbas, o sistema efetuará o cálculo na seguinte ordem:

1. Cálculo da hora extra;
   1. Salário incorporado = R$ 5.000,00;
   2. Salário/hora = R$ 22,727 (R$ 5.000,00 ÷ 220);
   3. Salário/hora 100% = R$ 45,45 (R$ 22,727 X 2);
   4. Hora Extra = R$ 454,50 (10 X R$ 45,45).
2. Cálculo da periculosidade sobre o salário + verbas.
   1. 30% X (R$ 5.000,00 + R$ 1.000,00) = R$ 1.800,00.

Dessa forma, haverá uma diferença no valor calculado da hora extra e da periculosidade, devido a ordem de cálculo da periculosidade, que poderá ser antes do cálculo da hora extra, quando configurada para ser calculado sobre o salário, ou poderá ser depois do cálculo da hora extra, quando configurada para ser calculado sobre salário e verbas.

No primeiro caso, entende-se que o cálculo da hora extra deverá ter valor maior pois irá considerar o salário e a periculosidade; já no segundo caso, entende-se que a periculosidade deverá ter valor maior pois irá considerar o salário + verbas que incidem para periculosidade.  
  
**Observação**A insalubridade e os adicionais por tempo de serviço também podem ser calculados sobre o salário ou sobre salário + verbas. Essa definição é efetuada através do Cadastro de Sindicatos.

A incidência da verba para periculosidade é definida no Cadastro de Verbas, através do campo RV\_PERICUL.

A base de cálculo da verba (salário base ou salário incorporado) é definida no Cadastro de Verbas, através do campo RV\_BASCAL.

A incorporação da verba o salário é definida no Cadastro de Verbas, através do campo RV\_INCORP.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
