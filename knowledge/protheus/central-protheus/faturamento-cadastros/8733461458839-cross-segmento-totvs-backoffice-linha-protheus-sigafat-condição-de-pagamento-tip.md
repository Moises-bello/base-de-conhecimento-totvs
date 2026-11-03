---
article_id: 8733461458839
category: Faturamento - Cadastros
content_hash: c9b24bb4a4bff258b68c15fa34ae083366a5e2ee329fd1c08f69f0e327537528
fetched_at: '2026-06-28T22:38:35.271525+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Condição de
  Pagamento TIPO 09 no TOTVS Gestão de Vendas (TGV)
type: support-article
updated_at: '2022-11-23T19:29:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8733461458839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Condi%C3%A7%C3%A3o-de-Pagamento-TIPO-09-no-TOTVS-Gest%C3%A3o-de-Vendas-TGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao incluir um Pedido de Venda pelo TGV apresenta a mensagem **"Falha ao Incluir Pedido de Venda"**;

**AJUDA:A410TIPO9P**

Este pedido possui condição de pagamento tipo 9, será gerado duplicatas relacionadas ao % digitados na parcela, mas a soma das parcelas não totalizam 100%.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.33;  
  
**Solução**  
Para utilização da condição de pagamento **Tipo 9**, é necessário preencher no Pedido de Venda os campos de Parcelas e Vencimentos, mais no **TOTVS Gestão de Vendas** ainda não foi disponibilizado estes campos, sendo assim ao utilizar esta condição de pagamento, ele apresenta o Help **"A410TIPO9P"**, que conforme a documentação informa que a mensagem é apresentada por não ter sido preenchido os campos para dar 100% do valor a ser Faturado.

**[MP - FAT - Help A410TIPO9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019523812-MP-FAT-Help-A410TIPO9-)**

Sendo assim o TOTVS Gestão de Vendas, não esta configurado para fazer um Pedido de Venda com condição de Pagamento **TIPO 9.**

Para solução do incidente, utilizar uma condição de pagamento diferente da **TIPO 9,** para realizar a inclusão do Pedido de Venda pelo TGV.
