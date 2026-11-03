---
article_id: 14844490521239
category: Folha Mensal
content_hash: 226e15e161bde05df3218b9c2bf75bb3db4c83418dc3239fad4ba3b4bb4e5526
fetched_at: '2026-06-28T22:46:58.226013+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP -  Como irá funcionar o novo cálculo IRRF Simplificado quando
  houver Adiantamento?
type: support-article
updated_at: '2025-02-20T20:51:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14844490521239-RH-RM-FOP-Como-ir%C3%A1-funcionar-o-novo-c%C3%A1lculo-IRRF-Simplificado-quando-houver-Adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Quando a empresa trabalha com regime caixa e possui adiantamento, o sistema está considerando as deduções legais para o cálculo, e não a dedução simplificada. Nesse caso, como proceder?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - **Versões e patches a partir**

* 12.1.2205.267
* 12.1.2209.222
* 12.1.2302.144
* e Superiores

**Solução**

Para que o sistema considere o IRRF simplificado no adiantamento, é necessário que o evento de Código de Cálculo 19 - Adiantamento, esteja com a flag **"Estorna IRRF"** marcada.

Pois, quando os eventos de Adiantamento de Salário e Pensão Alimentícia estão com incidência em **"Dedutível IRRF"**, os mesmos são considerados deduções legais. Ou seja, para as deduções legais, é considerado:

* Valor do INSS;
* Valor a deduzir por dependentes - de acordo com a parametrização do cadastro de dependentes;
* Valor Dedutível - Eventos marcados como Dedutível IRRF em seus respectivos cálculos Folha, 13º salário ou Férias.

**Atenção:** A marcação do campo Valor Dedutível ou Estorna IRRF é de responsabilidade do usuário, sendo que o valor dedutível refere-se ao que é dedução legal e o valor que estorna é o valor que abate na base do imposto de renda, por exemplo falta.

Para melhor entendimento, verifique abaixo as duas formas de cálculo: 

**EVENTO CC19 MARCADO COMO DEDUTÍVEL DE IRRF:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14843854798999)**

No log de cálculo será apresentado conforme abaixo:

Valor Dedutível = 822,00 + Valor do INSS: 166,77 = 988,77, o resultado é maior do que o valor de 528,00 cadastrado como valor fixo.

Proventos = 2.055,01 - 988,77 = Base de IRRF: 1.066,24  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14843848605079)

**EVENTO CC19 MARCADO COMO ESTORNA IRRF:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14843918680215)**

No log de cálculo será apresentado conforme abaixo:

O valor do adiantamento entra como Descontos = 822,00

Proventos = 2.055,01 - Descontos = 822,00 = Base de IRRF: 1.233,01

Valor do INSS: 166,77  
Total das deduções do funcionário: 166,77  
**Valor a deduzir no IRRF Simplificado: 528,00**  
Base de IRRF: 1.233,01 - 528,00 = 705,01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14844230865431)

Após configurar o evento de Adiantamento para "Estorna IRRF", o sistema considerou o valor de 528,00 sendo o mais benéfico para o colaborador.

**Saiba Mais:**

[Código de Cálculo 19 - Adiantamento](https://tdn.totvs.com/pages/releaseview.action?pageId=452719767)

[RH - RM - FOP - Novo Cálculo IRRF - LEI MP 1.171](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14708217734039-RH-RM-FOP-Nova-Tabela-IRRF-2023-LEI-MP-1-171?source=search)
