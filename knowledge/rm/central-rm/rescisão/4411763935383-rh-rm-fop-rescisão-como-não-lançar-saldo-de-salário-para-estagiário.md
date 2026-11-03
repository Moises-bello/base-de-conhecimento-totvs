---
article_id: 4411763935383
category: Rescisão
content_hash: df23542a38a9b0151df5f85fe5b0f31a3ed121d03000f471e5f2e41bdb8bae2f
fetched_at: '2026-06-28T22:46:54.490911+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Como não lançar saldo de salário para estagiário'
type: support-article
updated_at: '2024-09-16T20:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411763935383-RH-RM-FOP-Rescis%C3%A3o-Como-n%C3%A3o-lan%C3%A7ar-saldo-de-sal%C3%A1rio-para-estagi%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **0min 55sec****Dúvida**Como fazer para que não seja lançado evento saldo de salário na rescisão de estagiários e lançar o evento de bolsa estágio?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acessar **Configurações | Parametrizador | Rescisão | Cálculo**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8904349816087/mceclip0.png)

2. Marcar o parâmetro **Fórmula p/ evento de saldo de salário**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8904367543831/mceclip1.png)**

3. Abaixo uma fórmula de exemplo a ser criada:  
  
**SE  TABFUNC('CODTIPO','s') <> 'T' ENTAO 'x' SENAO 'y' fimse**A fórmula acima irá verificar o tipo do funcionário, se diferente de T- Estagiário o sistema irá lançar o evento X, mas se for igual a T- Estagiário, irá lançar o evento Y.

X = evento de saldo de salário normal

Y = evento de bolsa estágio  
  
**Importante**A fórmula apresentada neste artigo é apenas uma exemplo, fica a critério do usuário modifica-la e ajustar de acordo com a sua necessidade.
