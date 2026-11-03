---
article_id: 4410034917015
category: Financeiro - Contas a Pagar
content_hash: 661e69280ee45c2a7b59ab236fe1aaf3d58812d06ba984d9964a68dc31ff18a1
fetched_at: '2026-06-28T22:38:07.201907+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA340 - Não calcula Variação
  Cambial para PA sem taxa contratada
type: support-article
updated_at: '2023-01-25T22:21:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410034917015-Cross-Segmento-Backoffice-Linha-Protheus-FINA340-N%C3%A3o-calcula-Varia%C3%A7%C3%A3o-Cambial-para-PA-sem-taxa-contratada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min****Dúvida**Como calcular Variação Cambial para PA sem taxa contratada?  
  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – Todas as versões  
  
**Solução**Não deve de fato realizar a correção monetária pois a **PA** já gerou a movimentação no dia em que ela foi incluída, ou seja, o valor de exemplo 5 mil reais de fato já causou a movimentação bancária e esse é o comportamento padrão do sistema quando não é informado uma taxa no momento da compensação ou quando a **PA/NF** não tem taxas contratadas preenchidas nos seus respectivos registros.   
Para o cenário em que é feita uma baixa de um **PA**, o sistema calcula a correção monetária pois a operação no caso seria uma devolução do pagamento efetuado antecipadamente, e nesse cenário sim existe a possibilidade de uma **PA** de 1000 dólares ter seu respectivo valor em real atualizado pois pode existir uma diferença nas cotações do dólar entre a data de inclusão da **PA** e a devolução do pagamento. No cenário em que é feita a contabilização da variação cambial da **PA**, o feito dessa operação é apenas contábil, não influenciando financeiramente no valor da **PA**.  
  
**Saiba mais**  
[Compensação contas a pagar - FINA340 - Financeiro P12](https://tdn.totvs.com/pages/viewpage.action?pageId=504794483#Compensa%C3%A7%C3%A3ocontasapagar-FINA340-FinanceiroP12-08.DEMAISREGRASDECOMPENSA%C3%87%C3%83O)
