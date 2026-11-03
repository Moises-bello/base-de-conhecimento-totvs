---
article_id: 9982071011479
category: Encargos
content_hash: 96fac456c0130390d54e739594a5d16c04c0d4e0c05810c5cb2605b8f1be02d6
fetched_at: '2026-06-28T22:46:52.399518+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Geração de lançamento Financeiro de IRRF da folha através
  de Fórmula '
type: support-article
updated_at: '2025-03-11T10:36:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9982071011479-RH-RM-FOP-Gera%C3%A7%C3%A3o-de-lan%C3%A7amento-Financeiro-de-IRRF-da-folha-atrav%C3%A9s-de-F%C3%B3rmula
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao gerar o lançamento financeiro de IRRF da folha através de fórmula, não é preenchido o código da receita, e classificação é levada incorretamente para o módulo Gestão Financeira. Com esta ocorrência, não é possível gerar a DARF para o módulo Fiscal pois o mesmo valida o campo código da receita e classificação.   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Ao realizar o lançamento financeiro de IRRF da folha através de fórmula não é disponibilizado no sistema a aba Período de apuração Imposto de renda, conforme o print 1.   
Consequentemente não é gerado o código de receita sendo apresentado como NULL, e a classificação é apresentada como 40, informação incorreta para ser considerado no módulo Fiscal, visto que no módulo fiscal são considerados as classificações 13,41,42,45,52 para geração da DARF, conforme o print 2.

Portanto, quando é realizado no módulo Folha de Pagamento, um lançamento financeiro de IRRF calculado por fórmula, não será preenchido o código de receita e classificação conforme exigências do módulo Fiscal para geração da DARF. 

**Print 1**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9981404515351)

**Print 2**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9982169033623)  
  
**Solução**  
Para que seja a os valores de IRRF seja apresentado na DARF no módulo Fiscal, será necessário gerar o lançamento financeiro de IRRF com o Tipo de lançamento 20 - Total de IRRF , para que o código de receita e a classificação seja preenchido automaticamente e ao acessar a DARF os valores sejam apresentados conforme esperado.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9981992078103)

Após realizar o lançamento utilizando o Tipo de lançamento 20 - IRRF Total , será preenchido o código da receita e a classificação do mesmo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9982462328727)

**Saiba Mais:  
[RH - RM - FOP - Parametrização dos Lançamentos Financeiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414130953111-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-dos-Lan%C3%A7amentos-Financeiros)**
