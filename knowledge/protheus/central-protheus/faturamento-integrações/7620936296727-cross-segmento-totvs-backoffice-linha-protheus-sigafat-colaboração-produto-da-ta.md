---
article_id: 7620936296727
category: Faturamento - Integrações
content_hash: ba8ad206eff8feb2aece40f87dcacae1993e75dce69e9a915af1ec5c747d23d5
fetched_at: '2026-06-28T22:38:26.610853+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Colaboração
  produto da tabela SA7
type: support-article
updated_at: '2022-07-21T13:20:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7620936296727-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Colabora%C3%A7%C3%A3o-produto-da-tabela-SA7
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual origem do código do Produto na integração do Colaboração com o Pedido de Vendas Protheus  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -SIGAFAT - Todas as Versões  
  
**Solução**A integração Colaboração (Neogrid) pode buscar o código do Produto de dois campos diferentes : A7\_PRODUTO ou B1\_CODBAR  
  
O que define de onde é feita a busca da tag \_TYPECODPROD é o Tipo do Produto

'EN' ou 'UP' - Busca o produto por meio do código de barras (B1\_CODBAR)  
'BP' - Busca pela amarração de clientes x produtos (A7\_PRODUTO)  
  
Exemplo abaixo

Cadastro do Produto  
  
![](https://totvssuporte.zendesk.com/attachments/token/CetSos4SoNre95MAIlA2rgyq0/?name=image.png)  
  
Cadastro Produto X Cliente

![](https://totvssuporte.zendesk.com/attachments/token/gQVYAd0T57wXrOUF75hIr9PRc/?name=image.png)

XML  
  
![](https://totvssuporte.zendesk.com/attachments/token/NmRneoFroKxGO6HVbyeBveOaf/?name=image.png)

No exemplo acima o sistema busca o código do produto pelo campo A7\_PRODUTO ao invés do campo  B1\_CODBAR
