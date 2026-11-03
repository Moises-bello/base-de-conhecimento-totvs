---
content_hash: f98777a22e4be5324939019276839980b7b28f77a2fbf9e62c494d21f49bd900
fetched_at: '2026-06-29T00:11:48.729253+00:00'
page_id: '827314858'
product: rm
source: tdn-rm
title: DT - DIRF 2024 - Desconto Simplificado - Adequação na regra para considerar
  somente períodos com IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=827314858
version: 7
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF 2024 - Desconto Simplificado - Adequação na regra para considerar somente períodos com IRRF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9215](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9215 "View this issue") |

## **02.****LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2302.264
* 12.1.2306.227
* 12.1.2310.166
* 12.1.2402.106 e superiores.

## **03.****SITUAÇÃO/REQUISITO**

É necessário que a geração do campo 'Desconto Simplificado' na DIRF leve em consideração exclusivamente os períodos em que houve desconto de IRRF, assim atenderia [Perguntas e Respostas Dirf 2024](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dirf/dirf2024-perguntas-respostas-v20231208.pdf/@@download/file).

## **04.****SOLUÇÃO**

Conforme orientação da Receita Federal,  o campo "Desconto Simplificado" na DIRF 2024 deve ser preenchido somente se o desconto foi usado para calcular o IRRF daquele pagamento.  
  
Devido a diferença na forma de registro entre nosso sistema (por envelope de pagamento) e a DIRF (por caixa), realizamos uma adaptação. Agora, o sistema verifica somente os envelopes com desconto de IRRF.   
  
O valor do "Desconto Simplificado" será gerado somente se todos os envelopes com desconto de IRRF tiverem o campo "Desconto Simplificado" igual a "1"; caso contrário, não será gerado valor.  
Passamos a analisar somente os envelopes com desconto de IRRF, pois entendemos que quando o valor não atinge o limite para desconto de IR, não deve ser informado.  
  
Lembramos que este campo é apenas informativo, e o valor de IRRF de cada funcionário referente ao ano-base é recalculado pela Receita mediante a declaração anual de IRPF.

1) Criado o registro "**RTDS - Rendimentos Tributáveis - Dedução - Desconto Simplificado Mensal**" referente ao item "Registro de Valores Mensais". A tratativa adotada foi:

* + **FOLHA/FÉRIAS:** Verifica se o campo **PFPERFF.IRRF** ou o campo **IRRFFERIAS** são maiores que zero e analisa a regra do campo **PFPERFF.IRRFSIMPLIFICADO**
  + **13º SALÁRIO**: Verifica o campo **PFPERFF.IRRF13** é maior que zero e  analisa a regra do campo **PFPERFF.IRRF13SIMPLIFICADO**

 **OBSERVAÇÕES:**

1. Quando ocorre folha mensal e férias no mesmo caixa, e todos os períodos são simplificados, o valor do "Desconto Simplificado" é consolidado em uma única vez. Isso se deve ao fato de que a base de cálculo do IRRF para férias e folha de pagamento é única.
2. Quando ocorre uma rescisão e há base de IRRF mensal e IRRF sobre o 13º salário, o valor do "Desconto Simplificado" será gerado duas vezes. Isso se deve à distinção das bases de cálculo do IRRF, que são tratadas separadamente nesse contexto específico.

**Exemplo 1:**

Abaixo temos um envelope demonstrado no mês de 12/2023, onde o valor do IRRF é zero. Note que não apresenta a informação do simplificado.

Veja que no mês de dezembro não foi apresentado o valor no calculo simplificado.

**Exemplo 2:**

Abaixo temos dois envelopes demonstrado no mês de 08/2023, um com o calculo simplificado e outro sem o calculo simplificado.

Veja que no mês de agosto não foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 3:**

Abaixo temos dois envelopes demonstrado no mês de 08/2023, ambos com o calculo simplificado.

Veja que no mês de agosto foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 4:**

Abaixo temos um envelope demonstrado no mês de 08/2023, sem o calculo simplificado.

**ATENÇÃO:** Esse campo passou a ser gerado somente a partir de Abril/2023, conforme publicada [Instrução Normativa nº 2.141](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=130822).

**Adequação da DIRF para Conferência para trazer as informações do desconto simplificado.**

**ATENÇÃO:** Para visualizar o campo do desconto simplificado na DIRF para conferência, é essencial excluir o relatório anterior e importar o novo leiaute disponível no TOTVS Compartilhamento.

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
