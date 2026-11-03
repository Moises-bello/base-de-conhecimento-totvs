---
article_id: 4416141730711
category: Folha Mensal
content_hash: 086d09e67a4b2f778cb56c5c7f9e32f40dba43bf5e27a20a7071768b4d757129
fetched_at: '2026-06-28T22:46:59.279334+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: restituição de inss 13º na rescisão'
type: support-article
updated_at: '2025-01-22T18:28:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416141730711-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-restitui%C3%A7%C3%A3o-de-inss-13%C2%BA-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:32 min****Ocorrência**Ao realizar rescisão após o pagamento da 2ª parcela e o valor do 13º salário lançado em rescisão ser menor do que o pago em 2ª parcela está gerando a seguinte mensagem de erro referente a restituição de INSS de 13º salário: **O sistema identificou restituição de INSS para o funcionário de chapa XXXXX. Porém, para o eSocial não é permitido ter restituição de INSS em período onde não consta o desconto com valor igual ou superior ao valor da restituição.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois quando já houve o cálculo da 2ª parcela de 13º salário e transmissão para para o eSocial ou pagamento do funcionário e o mesmo é demitido no dia 10/12, gerando um valor de 13º salário menor na rescisão, já que não completou o avo de dezembro.   
  
**Solução**Para que a restituição não seja paga na rescisão e consequentemente não exibir a mensagem acima, criamos o passo a passo abaixo para solucionar. Para verificar a proposta de solução, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=654942683)  
  
**Glossário**  
**INSS-** Instituto Nacional do Seguro Social
