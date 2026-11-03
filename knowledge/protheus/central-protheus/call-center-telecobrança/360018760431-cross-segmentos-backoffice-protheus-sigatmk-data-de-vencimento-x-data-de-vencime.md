---
article_id: 360018760431
category: Call Center - Telecobrança
content_hash: 2c31f1603ea3b248a9b29d33ea41803cebb4e792b46cc6e67e92e1d6991b52dd
fetched_at: '2026-06-28T22:41:28.582834+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Data de Vencimento x Data
  de Vencimento Real para o Cálculo de Juros do Telecobrança
type: support-article
updated_at: '2025-10-08T17:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018760431-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Data-de-Vencimento-x-Data-de-Vencimento-Real-para-o-C%C3%A1lculo-de-Juros-do-Telecobran%C3%A7a
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35496243418263) Tempo aproximado para leitura: **00:02:00 min******

**Dúvida**

Qual a data correta de vencimento a ser considerada para validação dos dias de juros no telecobrança?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**

Quando temos um titulo com um vencimento em um dia não bancário (Sábado, Domingo ou Feriado), por lei, o fornecedor deve dar o próximo dia útil para o cliente pagar esse titulo sem a cobrança de juros.

O sistema irá considerar a data de vencimento (que caiu no final de semana ou feriado) acordado no momento da venda para calcular os dias de juros, e não a data do vencimento real, que é uma data do próximo dia bancário que o fornecedor cede para pagamento, sem ter juros aplicado.

Alguns parâmetros podem influenciar no processo de cálculo de juros como exemplo:

**MV\_TMKAJUR** = define se o método de juros na cobrança realizado por meio do Telecobrança (TMKA271), caso estiver igual a "1", os valores serão compostos pelo Financeiro(SIGAFIN). Caso estiver igual "2", os valores serão compostos pelo Loja(SIGALOJA).

**MV\_TXPER**  = exclusivamente utilizados para definir percentual de taxa de juros nos módulos de Faturamento e Call Center.

**Saiba Mais**: 

* [TMK0031 Data de Vencimento x Data de Vencimento Real para o Cálculo de Juros do Telecobrança](https://tdn.totvs.com/x/icFZE)
* [Cross Segmentos - Backoffice Protheus - SIGATMK - Liquidação / Renegociação no processo de Telecobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020277611-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Liquida%C3%A7%C3%A3o-Renegocia%C3%A7%C3%A3o-no-processo-de-Telecobran%C3%A7a)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Tratamento de juros no módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024357552-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tratamento-de-juros-no-m%C3%B3dulo-Faturamento)
* [Telecobrança (TMKA271 - SIGATMK)](https://tdn.totvs.com/x/uLZWF)
