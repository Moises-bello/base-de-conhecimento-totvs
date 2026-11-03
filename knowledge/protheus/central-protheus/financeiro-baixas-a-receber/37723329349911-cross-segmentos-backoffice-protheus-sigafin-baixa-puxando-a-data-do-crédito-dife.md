---
article_id: 37723329349911
category: Financeiro - Baixas a Receber
content_hash: 8729d75a4bada7ba1f9a625fbc492b45bcce3f6076144c05f31fe7990f4d9a01
fetched_at: '2026-06-28T22:37:43.811832+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - Baixa puxando a data do crédito
  diferente a data base
type: support-article
updated_at: '2026-01-16T13:37:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37723329349911-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-Baixa-puxando-a-data-do-cr%C3%A9dito-diferente-a-data-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37723329347351) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Data do crédito na baixa manual diferente da data-base. Por qual motivo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

No cadastro de bancos, o campo **Dias de Retenção (A6\_RETENCA)** tem como finalidade ajustar a **data de crédito** utilizada tanto para o cálculo da data de disponibilidade do recebimento no fluxo de caixa quanto para os processos de baixa que envolvem operações bancárias.

Nesse contexto, o processo de baixa é realizado considerando uma **data de crédito distinta da data-base** do título. O sistema permite essa diferenciação para atender às regras operacionais, financeiras e bancárias, assegurando que o registro da baixa reflita a data efetiva do crédito, ainda que não coincida com a data-base originalmente definida.

Essa funcionalidade é especialmente relevante em situações nas quais o crédito ocorre em data posterior ou anterior à data-base, como nos casos de transferências e TEDs que se efetivam apenas em dias subsequentes à data do recebimento. Dessa forma, garante-se a correta apuração financeira e contábil.
