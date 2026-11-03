---
article_id: 35201108260887
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: a7570428352c53af2a7ecc8705877fc303576d7e9f72235d50fbe0a3851ccecc
fetched_at: '2026-06-28T22:37:49.909308+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA717 - Pagamentos via PIX -
  Modelo PIX utilização de descontos na transmissão de pagamentos via API
type: support-article
updated_at: '2025-09-25T20:00:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35201108260887-Cross-Segmento-Backoffice-Linha-Protheus-FINA717-Pagamentos-via-PIX-Modelo-PIX-utiliza%C3%A7%C3%A3o-de-descontos-na-transmiss%C3%A3o-de-pagamentos-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35201108235799) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
É possível usar descontos em pagamentos via API BB em borderôs gerados via PIX - EA\_MODELO 45?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões homologadas.  
  
**Solução**  
Para pagamentos via **PIX – 45 – Transferência**, o **Banco do Brasil** não disponibiliza **TAGs de Desconto** no JSON.

**Referência:** **Documentação BB – Transferências PIX (2025):** <https://apoio.developers.bb.com.br/referency/post/63f7bfa03c7e05001251a2f9>

Dessa forma, mesmo que o desconto seja informado no título, o banco considera apenas o campo **Valor Pagamento**, desconsiderando os campos de **Desconto** ou **Decréscimo**.

Portanto, quando houver necessidade de aplicar desconto em pagamentos via PIX, este deverá ser tratado por meio de uma **regra de pagamento**, ajustando diretamente o **valor de pagamento**. Assim, o desconto será efetivamente subtraído do valor liquidado no momento da transação.  
  
**Saiba mais**  
[**Contas a pagar (Comunicação bancária online)**](https://tdn.totvs.com/pages/viewpage.action?pageId=734394071)
