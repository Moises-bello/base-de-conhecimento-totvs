---
article_id: 360052816954
category: RH - Dissídio
content_hash: 1fb40ffbfb961ff5e2727e4f3eef38972ee8ca0778e84c844f190083cd5160f7
fetched_at: '2026-06-28T22:43:43.480521+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Base de INSS 13º salário negativa quando existe
  diferença de 13º (Id 0028) no cálc. Dissídio
type: support-article
updated_at: '2021-04-30T00:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052816954-RH-Linha-Protheus-GPE-Base-de-INSS-13%C2%BA-sal%C3%A1rio-negativa-quando-existe-diferen%C3%A7a-de-13%C2%BA-Id-0028-no-c%C3%A1lc-Diss%C3%ADdio
---

**Ocorrência**Ao calcular o dissídio retroativo da competência 12, o sistema gera a base de INSS 13º negativa por não somar o valor de diferença/ complemento de 13º salário - identificador 0028.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O sistema gera diferença de 13º salário quando existe na folha da competência 12 algum pagamento referente a 13º que foi pago após o fechamento do roteiro 132.   
Como o pagamento da segunda parcela de 13º pode ser realizada até o dia 20/12 é comum que os funcionário recebam horas extras, comissões ou prêmios após essa data. Esses pagamentos geralmente estão configurados com Sim para médias de 13º e sim para INSS, isso gera um valor de diferença na verba com id 0028 e consequentemente uma base de INSS 13º salário nos ids 0019 e/ou 0020 dentro da folha de pagamento.  
No cálculo do dissídio é necessário que a verba de id 0019 que está na folha - Roteiro FOL seja somada a verba de id 0019 que foi gerada no cálculo de 13º - Roteiro 132.  
  
Veja o exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087891533/mceclip1.png)  
  
O valor da verba 720 - id 0019 corresponde a soma das verbas de 13º salário + a diferença de médias que foi gerada na verba 145 - id 0028.  
  
Para que o sistema faça a soma é necessário que os parâmetros de médias, gerados antes da finalização do cálculo estejam assim:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086735854/mceclip2.png)
