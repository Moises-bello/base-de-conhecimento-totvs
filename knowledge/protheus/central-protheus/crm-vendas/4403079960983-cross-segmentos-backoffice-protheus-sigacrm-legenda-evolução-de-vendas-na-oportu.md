---
article_id: 4403079960983
category: CRM - Vendas
content_hash: 2e89124516c950a049ff2cdc465afd3eef131f6fcdc91df7b976967cbdf29e19
fetched_at: '2026-06-28T22:40:25.832887+00:00'
product: protheus
section_id: 1500001549102
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Legenda evolução de vendas
  na oportunidade
type: support-article
updated_at: '2024-03-28T19:16:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403079960983-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Legenda-evolu%C3%A7%C3%A3o-de-vendas-na-oportunidade
---

**Dúvida**Legenda evolução de venda na oportunidade  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da versões 12.  
  
**Solução**Para a análise da **Evolução da venda da oportunidade** é necessário incluir o tempo de duração de cada estágio nos **Processos de venda**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403071755031)

**Situação real do estágio ativo:**  
![](https://tdn.totvs.com/download/thumbnails/362450568/br_verde.png?version=2&modificationDate=1526590383000&api=v2)Significa que o estágio está **em dia**.

![](https://tdn.totvs.com/download/thumbnails/362450568/br_amarelo.png?version=2&modificationDate=1526590373000&api=v2)Significa que o estágio está próximo da data de encerramento estipulado. Quando entra nessa situação recebe o alerta referente à proximidade da data de encerramento.  
![](https://tdn.totvs.com/download/thumbnails/362450568/br_vermelho.png?version=2&modificationDate=1526590360000&api=v2)Significa que o estágio está **atrasado**e continua ativo.

**Situação do estágio encerrado:**![](https://tdn.totvs.com/download/thumbnails/362450568/br_branco.png?version=1&modificationDate=1526590332000&api=v2)Significa que o estágio avançou sem atraso.  
![](https://tdn.totvs.com/download/thumbnails/362450568/br_preto.png?version=1&modificationDate=1526590339000&api=v2)Significa que o estágio avançou com atraso, após a data de encerramento estipulado.  
  
O sistema baseia-se nas informações dos estágios, calcula no processo de venda o período total da evolução da venda. A partir desse total exibe-se na consulta de oportunidade, o *status,* de acordo com a evolução da venda. Por exemplo, uma oportunidade avançou atrasada nos estágios iniciais, porém não utilizou todo o tempo para os estágios finais. Nesse caso ela pode finalizar **em dia** mesmo com os estágios iniciais em atraso.
