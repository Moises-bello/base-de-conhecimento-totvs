---
article_id: 20790361578903
category: RH – DIRF
content_hash: 19a10eed3bbe7f7928346a51baff1334be4cbf16c17e12b7d2748ac3cdaa617a
fetched_at: '2026-06-28T22:44:07.140992+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Quais ações tomar conforme retorno do log do Diagnóstico
  de base da DIRF
type: support-article
updated_at: '2025-08-13T13:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20790361578903-RH-Linha-Protheus-GPE-Quais-a%C3%A7%C3%B5es-tomar-conforme-retorno-do-log-do-Diagn%C3%B3stico-de-base-da-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20790330694551) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais ações tomar conforme retorno do log do Diagnóstico de base da DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao executar o Diagnóstico de base da DIRF, caso tenham inconsistências na base, será gerado log com as inconsistências, abaixo segue verificações que devem ser realizadas conforme retorno do log:

**• Inconsistências no cadastro de verbas - Verba com incidência de IR mas sem configuração para a DIRF**  
- Verifique no cadastro da verba que consta no log, se ela tem incidência para a DIRF, para isso, entre na rotina de Verbas pelo caminho >Atualizações >Definições cálculos >Verbas, pesquise pela verba em questão, e na aba Anuais no campo DIRF, informe uma incidência válida para a DIRF  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20790330695063)

**• Inconsistências no Cálculo do Plano de Saúde - Valor do Histórico de movimento não confere com o valor do histórico de plano de saúde**  
- Essa inconsistência informa que o valor que consta no acumulado do funcionário e que foi descontado em folha referente ao plano de saúde (tabela SRD), é diferente do valor que consta no histórico de plano de saúde, então valide se realmente há essa divergência entre os valores, conferindo o valor do acumulado do funcionário com o histórico do plano de saúde, para isso, emita o relatório de cálculo de plano de saúde ([Saiba mais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420942003351)). Se realmente os valores forem diferentes, terá que ser feito ajuste manual na DIRF referente ao plano de saúde ([Saiba mais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000515348))  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20790330696087)

**• Inconsistências em datas de pagamento de verbas entre data de cálculo de férias (SRH/SRR) e data de pagamento na folha (SRD)**  
- Essa inconsistência ocorre quando as datas de pagamento de férias entre o cálculo de férias (cabeçalho e verbas de férias) e data de pagamento das férias na folha estão diferentes. Na geração da DIRF o sistema valida a data de pagamento das férias para não levar os valores inconsistentes, então quando há diferença entre essas datas, na DIRF os valores de férias podem ser carregados errados, então se isso ocorrer, deverá ser feito ajuste manual na Manutenção arquivo referente aos rendimentos que foram carregados com valores errados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20790361572503)  
  
  
**Saiba mais**  
[Todos Artigos DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF?page=1#articles)
