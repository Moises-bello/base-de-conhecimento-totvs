---
article_id: 1500000165062
category: RH - Rescisão
content_hash: 3a86a1dfa7934568c8bfc63a9e01844eb9f3edd43298f52041b79dc761773aee
fetched_at: '2026-06-28T22:43:52.025775+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir saldo de salário horista em rescisão
  quando o mnemônico P_LDSRHRSP está preenchido com .T.
type: support-article
updated_at: '2022-08-16T16:59:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000165062-RH-Linha-Protheus-GPE-Como-conferir-saldo-de-sal%C3%A1rio-horista-em-rescis%C3%A3o-quando-o-mnem%C3%B4nico-P-LDSRHRSP-est%C3%A1-preenchido-com-T
---

**Dúvida**Como conferir saldo de salário horista em rescisão quando o mnemônico P\_LDSRHRSP está preenchido com .T. ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O saldo de salário horista em rescisão com o mnemônico P\_LDSRHRSP preenchido com .T., terá como cálculo a quantidade de horas dias cadastradas em Tabelas de Horário Padrão.  
  
**Exemplo:**Funcionário horista trabalha de segunda a sexta-feira (compensando o sábado), com carga horária dia 8,8. Neste exemplo o saldo de salário será calculado para os dias de segunda a sexta-feira por 8,80 horas e o DSR por 7,33 horas.  
  
**Cadastro Tabela Horário Padrão**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099044734/mceclip0.png)

**Cálculo Rescisão**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099044914/mceclip1.png)

Com a data de demissão 11.11.2020, temos a seguinte composição:

8 dias normais de segunda a sexta-feira com jornada 8,80 ( dias 02, 03, 04, 05, 06, 09, 10 e 11.11)

2 dias DSR jornada 7,33 (dias 01 e 08.11).

**Cálculo sistema:**

Salário hora: 6,18

8,80 \* 6,18 (salário hora) x 8 (dias normais) = 435,07

7,33 \* 6,18 (salário hora) x 2 (DSR) = 90,60

Total saldo de salário 11 dias = 435,07 + 90,60 = **525,67**
