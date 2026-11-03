---
article_id: 41181774758167
category: Férias
content_hash: 41fe205435843048b9703e16a3993ea4dd3ec3a62316577493d09ac5a75d0f01
fetched_at: '2026-06-28T22:46:56.087063+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Férias - Provisionamento nas Férias verificando a data Últ.
  Competência Importada
type: support-article
updated_at: '2026-06-15T12:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41181774758167-RH-RM-FOP-F%C3%A9rias-Provisionamento-nas-F%C3%A9rias-verificando-a-data-%C3%9Alt-Compet%C3%AAncia-Importada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41181774732951) Tempo aproximado para leitura: **00:02:45 min**  
  
**Dúvida**  
No módulo de Folha de Pagamento, ao calcular o recibo de férias de um colaborador com provisionamento do Crédito do Trabalhador, o sistema não está realizando o lançamento dos eventos de provisão.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277  
12.1.2410.229  
12.1.2502.145  
12.1.2506 e superiores  
  
**Solução**  
Em **Configurações | Parametrizador | Folha Normal | Crédito do Trabalhador**, existe a data **Últ. Competência Importada**que será consultada para o cálculo da provisão de empréstimos nas férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41181774733591)

**Exemplo de utilização**  
  
Veja abaixo os exemplos de combinações de datas.

Dados Fictícios:  
  
**PROVISIONA - ANTES DA IMPORTAÇÃO DO MÊS ATUAL E AS FÉRIAS INICIAM NO MÊS ATUAL**

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS - **19/03/2025 A 07/04/2025**

![](https://tdn.totvs.com/download/attachments/1049386448/image-2026-3-10_9-28-17.png?version=1&modificationDate=1773147183927&api=v2&effects=border-simple,shadow-kn)

**NÃO PROVISIONA - ANTES DA IMPORTAÇÃO DO MÊS ATUAL QUANDO AS FÉRIAS SERÁ NO PRÓXIMO MÊS**

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS **- 01/04/2025 A 30/04/2025**

![](https://tdn.totvs.com/download/attachments/1049386448/image-2026-3-10_9-29-42.png?version=1&modificationDate=1773147183843&api=v2&effects=border-simple,shadow-kn)

Outros cenários:

**FÉRIAS NO MÊS ATUAL**

**CENÁRIO 01 -**PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **03/2025**
* GOZO DE FÉRIAS - **19/03/2025 A 07/04/2025**

**CENÁRIO 02 -**NÃO PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO NÃO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE  - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS - **19/03/2025 A 07/04/2025**

**CENÁRIO 03 -** PROVISIONA - ANTES DA IMPORTAÇÃO DO MÊS ATUAL (caso do primeiro print acima)

* COMPETÊNCIA ATUAL DA BASE -**03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS - **19/03/2025 A 07/04/2025**

**FÉRIAS PRÓXIMO MÊS**

**CENÁRIO 01** - PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **03/2025**
* GOZO DE FÉRIAS - **01/04/2025 A 30/04/2025**

**CENÁRIO 02** - NÃO PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO NÃO ESTÁ NA IMPORTAÇÃO (caso do segundo print acima)

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO -**02/2025**
* GOZO DE FÉRIAS - **01/04/2025 A 30/04/2025**

**CENÁRIO 03 -**NÃO PROVISIONA - ANTES DA IMPORTAÇÃO DO MÊS ATUAL

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS -**01/04/2025 A 30/04/2025**

**MAIS DE UM PERÍODO DE GOZO**

**CENÁRIO 01 -** PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE**- 03/2025**
* COMPETÊNCIA PARAMETRIZADOR **- 03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **03/2025**
* GOZO DE FÉRIAS - **03/03/2025 A 07/03/2025**
* GOZO DE FÉRIAS - **01/04/2025 A 25/04/2025**

**CENÁRIO 02 -** NÃO PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO NÃO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR -**03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO -**02/2025**
* GOZO DE FÉRIAS - **03/03/2025 A 07/03/2025**
* GOZO DE FÉRIAS - **01/04/2025 A 25/04/2025**

**CENÁRIO 03** - ANTES DA IMPORTAÇÃO DO MÊS ATUAL

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR -**02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS - **03/03/2025 A 07/03/2025 - PROVISIONA**
* GOZO DE FÉRIAS - **01/04/2025 A 25/04/2025 - NÃO PROVISIONA**

**PERÍODO DE GOZO NO SEGUNDO MÊS APÓS O ATUAL**

**CENÁRIO 01 -**NÃO PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE -**03/2025**
* COMPETÊNCIA PARAMETRIZADOR -**03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO -**03/2025**
* GOZO DE FÉRIAS - **02/05/2025 A 30/05/2025**

**CENÁRIO 02 -** NÃO PROVISIONA - DEPOIS DA IMPORTAÇÃO DO MÊS ATUAL E O FUNCIONÁRIO NÃO ESTÁ NA IMPORTAÇÃO

* COMPETÊNCIA ATUAL DA BASE - **03/2025**
* COMPETÊNCIA PARAMETRIZADOR - **03/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO - **02/2025**
* GOZO DE FÉRIAS - **02/05/2025 A 30/05/2025**

**CENÁRIO 03** - NÃO PROVISIONA - ANTES DA IMPORTAÇÃO DO MÊS ATUAL

* COMPETÊNCIA ATUAL DA BASE -**03/2025**
* COMPETÊNCIA PARAMETRIZADOR -**02/2025**
* COMPETÊNCIA CADASTRO DE EMPRÉSTIMO -**02/2025**
* GOZO DE FÉRIAS - **02/05/2025 A 30/05/2025**

Caso solução acima não resolva valida os demais pontos abaixo:

* [FOP - Férias: Crédito do Trabalhador - Não está ocorrendo o provisionamento de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40389817692567-RH-RM-FOP-F%C3%A9rias-Cr%C3%A9dito-do-Trabalhador-N%C3%A3o-est%C3%A1-ocorrendo-o-provisionamento-de-f%C3%A9rias)
