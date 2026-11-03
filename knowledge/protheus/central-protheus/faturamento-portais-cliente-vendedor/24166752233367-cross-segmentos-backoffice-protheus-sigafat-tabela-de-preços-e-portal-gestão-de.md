---
article_id: 24166752233367
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: a9a28a8f909b72c81c9d42c21df898a617b9c882a41a8b1c6460cf7888e57c0e
fetched_at: '2026-06-28T22:38:24.047225+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tabela de Preços e Portal
  Gestão de Vendas
type: support-article
updated_at: '2024-06-13T20:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24166752233367-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tabela-de-Pre%C3%A7os-e-Portal-Gest%C3%A3o-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24166752197271) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Estamos aplicando a diferença de preço por faixa de produto. Quando utilizada esta funcionalidade no portal, a diferença não é apresentada. Como resolver?  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.  
  
**Causa**As regras de funcionamento da tabela de preços no Portal Gestão de Vendas sempre pegam o primeiro preço encontrado na tabela.

O PGV não trabalha com as faixas de valores na tabela de preço. Hoje, o mesmo não executa gatilhos que estão na tabela, então sempre pega o primeiro preço encontrado no produto.

**Solução**Uma forma paliativa de resolver esta questão é aplicar um desconto para o produto diretamente na rotina de REGRAS DE DESCONTO (FATA080), na qual é possível determinar um desconto por faixa. O percentual de desconto será aplicado para determinada quantidade de produto e, acima desta quantidade, outro desconto.  
  
**Obs: O desconto será aplicado ao salvar o pedido venda no portal.**  
  
Em saiba mais o artigo completo da regra de desconto:  
[FAT0093 Regras de Desconto (FATA080)](https://tdn.totvs.com/pages/viewpage.action?pageId=240979573)  
  
Veja o vídeo deste processo: [How To | MP - SIGAFAT - Regras de desconto (FATA080)](https://youtu.be/yuI3sP4EgzQ)
