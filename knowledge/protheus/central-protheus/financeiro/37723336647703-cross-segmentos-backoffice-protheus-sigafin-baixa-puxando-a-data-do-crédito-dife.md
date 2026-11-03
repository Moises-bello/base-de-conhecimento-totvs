---
article_id: 37723336647703
category: Financeiro
content_hash: 170e36989468cad2df8400a8374a927e6abd6d76e9e63868afe0333cd49281a1
fetched_at: '2026-06-28T22:38:01.012624+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - Baixa puxando a data do crédito
  diferente a data base
type: support-article
updated_at: '2026-01-16T13:37:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37723336647703-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-Baixa-puxando-a-data-do-cr%C3%A9dito-diferente-a-data-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37723336642967) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Data do crédito na baixa manual diferente da data-base. Por qual motivo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

No cadastro de bancos, o campo **Dias de Retenção (A6\_RETENCA)** tem como finalidade ajustar a **data de crédito** utilizada tanto para o cálculo da data de disponibilidade do recebimento no fluxo de caixa quanto para os processos de baixa que envolvem operações bancárias.

Nesse contexto, o processo de baixa é realizado considerando uma **data de crédito distinta da data-base** do título. O sistema permite essa diferenciação para atender às regras operacionais, financeiras e bancárias, assegurando que o registro da baixa reflita a data efetiva do crédito, ainda que não coincida com a data-base originalmente definida.

Essa funcionalidade é especialmente relevante em situações nas quais o crédito ocorre em data posterior ou anterior à data-base, como nos casos de transferências e TEDs que se efetivam apenas em dias subsequentes à data do recebimento. Dessa forma, garante-se a correta apuração financeira e contábil.
