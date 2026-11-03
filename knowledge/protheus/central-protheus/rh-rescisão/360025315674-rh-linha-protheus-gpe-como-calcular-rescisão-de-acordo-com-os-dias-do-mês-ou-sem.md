---
article_id: 360025315674
category: RH - Rescisão
content_hash: 1cddc5b3e8b195dcabc5f0e1a8f812012d265ae210d6548123566a25282ddd05
fetched_at: '2026-06-28T22:43:48.602162+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular rescisão de acordo com os dias do
  mês ou sempre por 30 (divisão salário) (P_DIASRES)
type: support-article
updated_at: '2026-04-08T16:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025315674-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-acordo-com-os-dias-do-m%C3%AAs-ou-sempre-por-30-divis%C3%A3o-sal%C3%A1rio-P-DIASRES
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26823225246615)***Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como calcular rescisão onde a divisão dos dias seja de acordo com os dias do mês (28, 29, 30 ou 31) ou sempre por 30?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
**Solução**Para determinar se a divisão do salário na rescisão para pagamento de saldo de salário, médias e outras verbas será sobre os dias do mês (28, 29, 30 e 31) ou sempre por 30 é usado o mnemônico P\_DIASRES, que quando parametrizado com 1, o sistema faz a divisão do salário de acordo com os dias do mês (28, 29, 30 ou 31) e quando parametrizado com 2 o sistema faz a divisão do salário sempre por 30, independente da quantidade de dias que tem o mês, abaixo exemplo:

P\_DIASRES = 1  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039227594)  
Rescisão em mês de 31 dias, sistema irá fazer os cálculos com base em divisão de 31 dias, conforme abaixo:  
SALÁRIO BASE R$ 2.500,00  
SALÁRIO DIA = salário base / 31 = 80,65  
SALÁRIO HORA = salário base / (hrs. mensais / 30 \* 31) = 11,00  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040068153)  
No exemplo acima, o saldo de salário foi calculado com divisão sobre 31 dias (SALÁRIO BASE / 31 \* 10 = 806,45)  
Para cálculo de rescisão em meses de 28, 29 ou 30 dias, o cálculo será o mesmo, apenas o divisor será alterado conforme o dia do mês

P\_DIASRES = 2  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039229474)  
Quando o mnemônico P\_DIASRES estiver parametrizado com 2, a divisão para chegar ao salário dia e salário hora será sempre sobre 30 dias, independente da quantidade de dias do mês, conforme abaixo:  
SALÁRIO BASE R$ 2.500,00  
SALÁRIO DIA = salário base / 30 = 83,33  
SALÁRIO HORA = salário base / hrs. mensais = 11,36  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039229714)  
No exemplo acima, o saldo de salário foi calculado com divisão sobre 30 dias (SALÁRIO BASE / 30 \* 10 = 833,33)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
