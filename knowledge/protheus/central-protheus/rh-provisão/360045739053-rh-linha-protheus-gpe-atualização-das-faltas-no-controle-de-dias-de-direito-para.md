---
article_id: 360045739053
category: RH - Provisão
content_hash: 4af1c8e438580c712f8fd66b71e8ba18939fb2127cbc6c3cf9423479bc4291a0
fetched_at: '2026-06-28T22:43:55.625995+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Atualização das faltas no controle de dias de direito
  para que ocorra a perda de avos na troca de período aquisitivo proporcional para
  vencido no cálculo de provisão
type: support-article
updated_at: '2023-03-11T00:58:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045739053-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-das-faltas-no-controle-de-dias-de-direito-para-que-ocorra-a-perda-de-avos-na-troca-de-per%C3%ADodo-aquisitivo-proporcional-para-vencido-no-c%C3%A1lculo-de-provis%C3%A3o
---

**Dúvida**Sistema não atualiza as faltas para perda de avos na troca de período aquisitivo proporcional para vencido quando é calculada a provisão com a folha aberta.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Para que o sistema atualize as faltas para perda de avos na troca de período aquisitivo proporcional para vencido realize o fechamento da folha para que o sistema atualize o controle de dias de direito e realize o cálculo da prisão corretamente.

Controle de dias de direito:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062781294/mceclip0.png)

Acumulado de provisão 11º avo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062784994/mceclip1.png)

Acumulado provisão 12º avo: Se pegarmos os 30 dias apresentados e subtrairmos os 6 de falta, obteremos os 24 em questão após o fechamento da folha de pagamento.  
  
Referente aos cálculos:  
  
Se pegarmos o salário do funcionário 1200 /30 \* 24 = 960,00 conforme foi provisionado;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062785074/mceclip2.png)

Relatório demonstrando o resultado esperado com as faltas e a perda do avo em questão.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063673613/mceclip3.png)
