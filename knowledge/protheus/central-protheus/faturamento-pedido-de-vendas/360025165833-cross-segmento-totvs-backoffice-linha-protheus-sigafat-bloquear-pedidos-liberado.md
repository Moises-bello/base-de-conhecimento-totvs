---
article_id: 360025165833
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9be0b50bf731f9c378b8b027c0fe0a0b81b80679f3e721f30a9cfc45f1680e8b
fetched_at: '2026-06-28T22:38:38.453815+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Bloquear pedidos
  liberados parcialmente na preparação da nota via pedido
type: support-article
updated_at: '2023-04-20T13:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025165833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Bloquear-pedidos-liberados-parcialmente-na-prepara%C3%A7%C3%A3o-da-nota-via-pedido
---

**Dúvida**Quando se está na tela de pedido de venda (**MATA410**) e vai gerar a Nota de Saída(**MATN410C**/**MATA461**) em Prep. docs. em outras ações, o pedido não possui saldo em todos os itens inseridos, porém, o sistema permite o faturamento parcial dos itens, sendo assim é possível não permitir faturamento parcial do pedido de venda?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Na tela do pedido, não há validação para o processo de bloqueio de pedido liberado, o assistente de  preparação automática da nota fará as verificações do que se pode faturar no momento do acionamento de faturamento e se houver saldo parcial,  ele fará um faturamento parcial.  
O que se pode fazer é tentar criar uma regra para esta necessidade ,utilizando o ponto de entrada,  **M410PVNF** , a documentação encontra-se no TDN:**<http://tdn.totvs.com/pages/viewpage.action?pageId=6784152>**.
