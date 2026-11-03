---
article_id: 29996299950103
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 46a211f917cef96870441b28e6047c2a0b518ca024f3e1dc6353d7aa619fd13b
fetched_at: '2026-06-28T22:38:39.633756+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Analisar crédito por cliente
  ou por loja específica
type: support-article
updated_at: '2025-02-17T11:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29996299950103-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Analisar-cr%C3%A9dito-por-cliente-ou-por-loja-espec%C3%ADfica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29996268516887) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como configurar o sistema para analisar crédito por cliente ou por loja específica?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Configure o parâmetro MV\_CREDCLI:

* Se = C (Cliente) - O limite do crédito do cliente é a soma de todas suas "lojas (A1\_LOJA)" para o mesmo "código (A1\_COD)"
* Se = L (Loja) - O limite do crédito do cliente é separado por loja específica (A1\_COD + A1\_LOJA)

Se "MV\_CREDCLI = C" então todas as lojas deverão conter conteúdo no campo "Risco (A1\_RISCO)".

Caso contrário, não será possível a avaliação de situação financeira das demais lojas para a liberação do Pedido, de modo que é exibida a mensagem:

"Atenção. É necessário que o cliente e loja estejam com configurações de risco conforme outras lojas"
