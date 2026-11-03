---
article_id: 18409038491415
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 641ae53323c3f6fb2c269ec8fc8b58d015bc02311ad5c38b37b5b388018b0cb0
fetched_at: '2026-06-28T22:38:38.435740+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao salvar o
  pedido de venda pelo PGV apresenta o Help "AJUDA: A410NATPED"(PGV) '
type: support-article
updated_at: '2023-10-19T20:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18409038491415-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-salvar-o-pedido-de-venda-pelo-PGV-apresenta-o-Help-AJUDA-A410NATPED-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18409078223895) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao realizar a inclusão de um pedido de venda pelo PGV, apresenta a mensagem:  
  
**AJUDA:A410NATPED**  
O parâmetro MV\_1DUPNAT está configurado para gerar duplicatas com a natureza indicada no pedido de venda (MV\_1DUPNAT = SC5>C5\_NATUREZ). Contudo este campo não foi informado no pedido de venda.   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33;  
  
**Solução**  
No Portal Gestão de Venda ainda esta em desenvolvimento a inclusão de alguns campos que são apresentados no cabeçalho do Pedido de Venda pelo Protheus, devido a isso alguns campos não são preenchidos apresentando help ao salvar o Pedido pelo PGV, devido a isso hoje o Portal Gestão de Vendas, não realiza a gravação do Pedido de Venda quando o parâmetro **MV\_1DUPNAT** esta configurado, para pegar as informações do campo "**SC5>C5\_NATUREZ**", pois este campo não esta disponível no Layout dos campos do Portal Gestão de Vendas.
