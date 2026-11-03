---
article_id: 360060461433
category: Encargos
content_hash: f56d109b643faad15367a1ec943db5e609d8787bbf727659149cf04d4bbc985c
fetched_at: '2026-06-28T22:46:53.284859+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Bloqueia reversão do 13º na contabilização em
  janeiro'
type: support-article
updated_at: '2025-03-05T18:27:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060461433-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Bloqueia-revers%C3%A3o-do-13%C2%BA-na-contabiliza%C3%A7%C3%A3o-em-janeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:40 min  
  
Dúvida**Qual a funcionalidade do parâmetro: **Bloqueia reversão automática de 13º salário no mês de janeiro**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Acesso ao parâmetro: **Configurações | Parametrizador | 13º Salário | Cálculo | Bloqueia reversão automática de 13º salário no mês de janeiro.**

Com este parâmetro marcado, no momento da realização da contabilização da provisão mensal de 13º salário no mês de janeiro, o sistema considerará o valor da provisão acumulada do mês anterior igual a zero. Portanto, a provisão mensal do mês de janeiro é a própria provisão acumulada do mês de Janeiro.     
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11099419643543)  
  
Esclarecemos que, em Dezembro, a provisão acumulada é relativa a 12/12 avos e em Janeiro a provisão acumulada é de apenas 1/12 avos. Ao final de um ano contábil, é necessário uma reversão nas contas de resultado de provisão da contabilidade.

O TOTVS Folha de Pagamento faz isto automaticamente, quando o usuário opta pela provisão mensal **valor acumulado mês atual - valor acumulado do mês anterior**, pois esta é negativa e o sistema inverte as contas débito/crédito. Esta reversão só ocorre no mês de Janeiro.

Quando as empresas fazem a reversão por conta própria em Dezembro **o próprio contador faz um artifício contábil sem o conhecimento do TOTVS Folha de Pagamento para que seja zerada o conteúdo das contas de resultado de provisão**, não é mais necessário a reversão automática das contas débito/crédito que o TOTVS Folha de Pagamento faz. Logo, este parâmetro possibilita o bloqueio desta reversão de contras automaticamente.  
  
**Exemplos:**

Mês de competência Janeiro  
Provisão acumulada do mês atual (Janeiro): R$ 41,67 (1/12)  
Provisão acumulada do mês anterior (Dezembro): R$ 522,47 (12/12)  
Contabilização dos encargos tipos 7 (Provisão de 13º), 8 (Provisão FGTS de 13º) e 9 (Provisão Encargos de 13º)  
Conta Débito: 1.0001.1  
Conta Crédito: 2.0001.0  
Cálculo da provisão Mensal = Provisão acumulada mês atual (Janeiro) - Provisão acumulada do mês anterior (Dezembro)

* **Com parâmetro marcado:**

Resultado: R$ 41-67 - 0 = R$ 41,67

Lançamento Contábil:

Conta Débito: 1.0001.0 = R$ 41,67

Conta Crédito: 2.0001.0 = R$ 41,67

* **Com parâmetro desmarcado:**

Resultado: R$ 41,67 - R$ 522,47 = R$ -480,80 (valor negativo - reversão das contas débito/crédito)  
   
Lançamento Contábil:

Conta Débito: 2.0001.0 = R$ 480,80

Conta Crédito: 1.0001.0 = R4 480,80

**Saiba mais**[Cálculo - 13º Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=452719329)
