---
article_id: 360034196073
category: Gestão de Armazenagem (WMS)
content_hash: 9879e91766e69e24990465e112cc764607130cbade31169bc022f83d37d308f3
fetched_at: '2026-06-28T22:45:48.027623+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Diferença entre retornar o pedido de venda
  para carteira ou apto a faturar na exclusão do documento de saída
type: support-article
updated_at: '2022-01-11T20:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034196073-Log%C3%ADstica-Linha-Protheus-WMS-Diferen%C3%A7a-entre-retornar-o-pedido-de-venda-para-carteira-ou-apto-a-faturar-na-exclus%C3%A3o-do-documento-de-sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00****Dúvida**Qual a diferença entre **retornar** o pedido de venda para carteira ou **apto a faturar** na exclusão do documento de saída?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 11.80  
  
**Solução**Para o **SIGAWMS - Gestão de Armazenagem** haverá comportamentos diferenciados na **Exclusão de Documento de Saída - MATA521A**, se usado para retornar o pedido de venda para carteira ou apto a faturar, a partir da tecla de atalho **F12**.  
  
**Quando em carteira:**  
- Permitirá alterar o pedido de venda;  
- Retornará a situação do pedido para não liberado;  
- Voltará o saldo para doca sem empenho e eliminará a liberação do pedido. Como esse saldo ficará na doca, poderá ser transferido manualmente para endereços do armazém ou ainda poderá ser informado em um pedido de venda, no endereço origem, para consumir esse saldo da doca.  
  
**Quando apto a faturar:**- Não permitirá alterar o pedido de venda;  
- Logo, terá de estornar o serviço no **WMS - Warehouse Management System**, se precisar alterar o pedido;  
- Refará o empenho na doca e permitirá faturar novamente o mesmo pedido de venda.  
  
**Importante**A doca não é um endereço utilizado no processo de busca de endereços para separação, somente se informado no pedido.  
  
No **WMS** atual, ao usar a opção em carteira, para conseguir faturar o pedido de venda será necessário informar o endereço de destino no **C6\_LOCALIZ - Endereco** e sem o serviço de **WMS**.  
  
Já no novo **WMS**, precisará informar o **C6\_LOCALIZ - Endereco** e o serviço de **WMS**. Será gerada uma **O.S. - Ordem de serviço** fictícia do endereço de origem doca para o endereço de destino doca, a qual terá de ser finalizada pelo **Monitor de Serviços - WMSA332**.
