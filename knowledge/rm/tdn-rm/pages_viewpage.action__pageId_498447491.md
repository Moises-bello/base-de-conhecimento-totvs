---
content_hash: 9e873bab161efc47ddb897de34f01b6ef1300cb836a902698b71c34e0d24087a
fetched_at: '2026-06-29T00:10:22.644809+00:00'
page_id: '498447491'
product: rm
source: tdn-rm
title: Lançamentos Financeiros - Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498447491
version: 4
---

Informação para selecionar os períodos de gozo de férias considerados para o lançamento financeiro de Férias.   
Lembrando que somente ficará disponível se o usuário selecionar um tipo de lançamento ativo de Férias (3-Líquido férias e 17 – Pensão Férias).

**Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo**

Marque para habilitar os campos de filtro: "Data Inicial", "Data Final" e "Considerar apenas o último período de gozo".

**Data Inicial e Data Final**  
Informe o período no qual o sistema buscará os períodos de gozo de férias observando a data de pagamento destes.

**Considerar apenas o último período de gozo**  
Marque para o sistema considerar apenas o último período de gozo de férias com a data de pagamento entre a Data Inicial e Data Final.

**Observação:**

* Para o Líquido de férias será considerado o dia do pagamento conforme competência do processo, sendo que será verificado o período selecionado dentro da competência.
* Para Pensão nas férias será considerado se o período de gozo está dentro da competência selecionada no processo e a data de pagamento conforme a data selecionada

**Exemplos:**

**Funcionário Chapa 00002**

Pensão de um dependente – 5% sobre o líquido

1º Período de gozo – 03/02/2021 a 12/02/2021 - Data pagamento – 01/02/2021

2º Período de gozo – 16/02/2021 a 25/02/2021 - Data pagamento – 12/02/2021

**Funcionário Chapa 00007**

Pensão de um dependente – 10% sobre o líquido

1º Período de gozo – 01/02/2021 a 10/02/2021 - Data pagamento – 27/01/2021

2º Período de gozo – 15/02/2021 a 24/02/2021 - Data pagamento – 11/02/2021

|  |  |  |
| --- | --- | --- |
|  | **FUNCIONÁRIO 00002** |  |
|  | **LIQUIDO** | **PENSÃO** |
| **PER 1** | 4221,75 | 469,07 |
| **PER 2** | 3336,60 | 496,08 |
| **TOTAL** | 7558,35 | 965,15 |
|  |  |  |
|  | **FUNCIONÁRIO 00007** |  |
|  | **LIQUIDO** | **PENSÃO** |
| **PER 1** | 3743,70 | 197,03 |
| **PER 2** | 3739,20 | 202,79 |
| **TOTAL** | 7482,90 | 399,82 |

**COMPETÊNCIA DO PROCESSO GERAÇÃO DO LANÇAMENTO FINANCEIRO – 02/2021**

Parâmetro “Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo” **desmarcado**

Liquido considerado

Chapa 00002 – 7558,35 (Competência do processo 02/2021 e Pagamento 01/02/2021 e 12/02/2021)

Chapa 00007 – 3739,20 (Competência do processo 02/2021 e Pagamento 11/02/2021)

Pensão considerada

Chapa 00002 – 965,15 (período de gozo em 02/2021)

Chapa 00007 – 399,82 (período de gozo em 02/2021)

**COMPETÊNCIA DO PROCESSO GERAÇÃO DO LANÇAMENTO FINANCEIRO  – 02/2021**

Parâmetro “Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo” **marcado** e data 27/01/2021 a 28/02/2021

Liquido considerado

Chapa 00002 – 7558,35 (Competência do processo 02/2021 e Pagamento 01/02/2021 e 12/02/2021)

Chapa 00007 – 3739,20 (Competência do processo 02/2021 e Pagamento 11/02/2021)

Pensão considerada

Chapa 00002 – 965,15 (período de gozo em 02/2021 e data Pagamento 01/02/2021 e 12/02/2021)

Chapa 00007 – 399,82 (período de gozo em 02/2021 e data Pagamento 27/01/2021 e 11/02/2021)

**COMPETÊNCIA DO PROCESSO GERAÇÃO DO LANÇAMENTO FINANCEIRO  – 02/2021**

Parâmetro “Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo” **marcado** e data 12/02/2021 a 28/02/2021

Liquido considerado

Chapa 00002 – 3336,60 (Competência do processo 02/2021 e Pagamento 12/02/2021)

Pensão considerada

Chapa 00002 – 496,08 (período de gozo em 02/2021 e data Pagamento 12/02/2021)

**COMPETÊNCIA DO PROCESSO GERAÇÃO DO LANÇAMENTO FINANCEIRO MÊS ANTERIOR – 01/2021**

Parâmetro “Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo” **marcado** e data 27/01/2021 a 28/02/2021

Liquido considerado

Chapa 00007 – 3743,70 (Competência do processo 01/2021 e Pagamento 27/01/2021)

Pensão considerada

Não foi considerada a pensão paga em 27/01/2021 porque o período de gozo (01/02/2021 a 10/02/2021) não corresponde ao mês de competência do processamento.

**COMPETÊNCIA DO PROCESSO GERAÇÃO DO LANÇAMENTO FINANCEIRO – 02/2021**

Parâmetro “Considerar apenas os períodos de gozo de férias com data de pagamento entre as datas abaixo” **marcado** e data 01/02/2021 a 28/02/2021 e Parâmetro “Considerar apenas último período de gozo” **marcado**

Liquido considerado

Chapa 00002 – 3336,60 (Competência do processo 02/2021 e Pagamento 12/02/2021)

Chapa 00007 – 3739,20 (Competência do processo 02/2021 e Pagamento 11/02/2021)

Pensão considerada

Chapa 00002 – 496,08 (período de gozo em 02/2021 e data Pagamento 12/02/2021)

Chapa 00007 – 202,79 (período de gozo em 02/2021 e data Pagamento 11/02/2021)

---

[Voltar a pagina inicial](http://tdn.totvs.com/pages/viewpage.action?pageId=452719571)
