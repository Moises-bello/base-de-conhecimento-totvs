---
article_id: 13590741683095
category: Funcionários
content_hash: 283bb602294ee6c6da7846beff47182c874ddeb18af3c1e3a952bc169de69b39
fetched_at: '2026-06-28T22:47:03.180556+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Cálculo do percentual de aposentadoria especial
type: support-article
updated_at: '2025-01-16T20:35:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13590741683095-RH-RM-FOP-C%C3%A1lculo-do-percentual-de-aposentadoria-especial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:33 min****Dúvida**No módulo Folha de Pagamento, como é realizado o cálculo do percentual de aposentadoria especial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para o cálculo do percentual da aposentadoria especial, o sistema irá validar o cadastro de seção e o cadastro do funcionário. Para isso, siga as orientações da documentação abaixo, na qual orienta como configurar o sistema para o cálculo da aposentadoria especial.  
  
[RH - RM - FOP - Parametrização para cálculo de aposentadoria especial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419586503063-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-para-c%C3%A1lculo-de-aposentadoria-especial)

* Encargos da Folha de Pagamento

Em relação aos Encargos da Folha de Pagamento, será necessário acessar o cadastro do encargo e marcar a flag Acréscimo de aposentadoria Especial em base de INSS. Para isso, acesse: **Encargos | Cadastros | Encargos  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13588613948439)**

Com a marcação do parâmetro acima, o sistema irá buscar a parametrização da seção, e o RAT já será considerado.

Para o cálculo do encargo, o sistema irá validar o cadastro do funcionário. Sendo assim, será aplicado a informação da aposentadoria somente para quem estiver com a parametrização no cadastro do funcionário conforme orientado na documentação mencionada em primeiro momento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13589244581783)

Caso contrário, se ele não incidir em salário, será necessário informar ele dentro do parametrizar de férias e 13º salário em eventos adicionais incluindo uma fórmula de seleção, para que seja lançado apenas para os funcionários que a empresa deseja ou poderá criar uma fórmula adicional, e inserir no parametrizador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13589342091159)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13590402437783)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13590408754327)

**Importante**

Caso deseje que o evento seja proporcionalizado para todos os lançamentos, será necessário o evento conter uma fórmula, pois para habilitação da opção de Proporcionalidade  apenas será habilitado com a utilização de fórmula para o cálculo do evento. Para maiores informações quanto à proporcionalidade do evento, verifique a documentação abaixo.  
  
[RH - RM - FOP - Eventos: Proporcionalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018386171-RH-RM-FOP-Eventos-Proporcionaliza%C3%A7%C3%A3o)

**Saiba mais**

[RH - RM - FOP - Definições e cadastro de SAT, FAP e RAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007983561-RH-RM-FOP-Defini%C3%A7%C3%B5es-e-cadastro-de-SAT-FAP-e-RAT#:~:text=O%20que%20s%C3%A3o%20a)
