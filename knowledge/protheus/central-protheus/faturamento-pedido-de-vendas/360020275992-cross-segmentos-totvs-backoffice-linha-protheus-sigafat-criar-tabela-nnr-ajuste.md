---
article_id: 360020275992
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3ab12cc33be346ca4c0cf2c10c8c71dc617dc0c35e593cb8a0bf09e6adfbbe1f
fetched_at: '2026-06-28T22:38:41.120528+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Criar tabela
  NNR - Ajuste dos Helps A430LOCAL e A410LOCAL
type: support-article
updated_at: '2021-11-17T18:10:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020275992-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Criar-tabela-NNR-Ajuste-dos-Helps-A430LOCAL-e-A410LOCAL
---

**Dúvida**

Como corrigir os Helps A430LOCAL e A410LOCAL (Criar tabela NNR)?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Foram incluídas validações para tabela **NNR** (Cadastro de Armazém), elas são executadas na rotina de "Pedidos de Vendas" (**MATA410**), exibindo o Help **A430Local** e não permitindo a inclusão do pedido de vendas sem o prévio cadastro do armazém.

Para solução do Help, basta atualizar o dicionário de Dados do Ambiente e realizar a execução do UPDDISTR: [**Atualizar Dicionário de Dados (UPDDISTR)**](https://tdn.totvs.com/x/nJLYCg)

Para maiores informações entre em contato com o Time de Suporte ao módulo Estoque/Custos.
