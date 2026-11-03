---
content_hash: 16e0061070b40d09bb68c43221cacbcf5c1f529a4701ce6335dbad1a18e8a4ba
fetched_at: '2026-06-29T00:11:48.773061+00:00'
page_id: '827315485'
product: rm
source: tdn-rm
title: DT - DIRF 2024 - Desconto Simplificado LOG
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+DIRF+2024+-+Desconto+Simplificado+LOG
version: 9
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF 2024 - Desconto Simplificado LOG |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9346](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9346 "View this issue") |

## **02.****LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2302.265
* 12.1.2306.228
* 12.1.2310.167
* 12.1.2402.107 e superiores.

## **03.****SITUAÇÃO/REQUISITO**

Implementar a geração de um log detalhado, o qual liste os períodos em que houve desconto de IRRF e indique se esses descontos foram realizados com a aplicação do desconto simplificado. Esse log será valioso para facilitar a conferência e análise dos cálculos de IRRF.

## **04.****SOLUÇÃO**

Criamos a aba "Debug", destinada a listar os períodos (envelopes de pagamentos) por caixa de pagamento que contenham desconto de IRRF, e indicar se foram aplicados com a utilização do desconto simplificado.

Para facilitar a compreensão, segue um exemplo do formato de geração:

Abaixo temos os detalhes para a chapa 00036:

**Chapa 00036 : Desconto Simplificado.**  
**Considerado apenas os períodos com desconto de IRRF, conforme abaixo:**  
**Caixa 5/2023**  
**Período   IRRF Simplificado   Data de Pagamento**  
**1               Sim                           31/05/2023**  
**Desconto Simplificado = R$ 528,00**

**Caixa 6/2023**  
**Período   IRRF Simplificado   Data de Pagamento**  
**1               Sim                           30/06/2023**  
**Desconto Simplificado = R$ 528,00**

**Caixa 7/2023**  
**Período   IRRF Simplificado   Data de Pagamento**

**1               Sim                           15/07/2023**  
**2               Sim                           30/07/2023**  
**Desconto Simplificado = R$ 528,00**

**Caixa 8/2023**  
**Período   IRRF Simplificado   Data de Pagamento**  
**1               Sim                           30/08/2023**  
**Desconto Simplificado = R$ 528,00**

**Caixa 9/2023**  
**Período   IRRF Simplificado   Data de Pagamento**  
**1               Sim                           30/09/2023**  
**Desconto Simplificado = R$ 528,00**

**Caixa 12/2023**  
**Período   IRRF Simplificado   Data de Pagamento**  
**1               Sim                           05/12/2023**  
**Desconto Simplificado = R$ 528,00**

**ATENÇÃO:**

1. Os períodos (envelopes de pagamento) referentes ao 13º salário não serão listados no log.
2. Apenas os períodos (envelopes de pagamento) que possuem desconto de IRRF serão considerados para análise da regra e listados no log.
3. O valor no campo "Desconto Simplificado" será retornado apenas quando todos os períodos (envelopes de pagamento) do mês caixa tiverem o campo "IRRF Simplificado" igual a "Sim".

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
