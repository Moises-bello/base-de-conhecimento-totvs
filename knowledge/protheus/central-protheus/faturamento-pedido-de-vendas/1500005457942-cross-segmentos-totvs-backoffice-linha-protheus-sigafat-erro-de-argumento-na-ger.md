---
article_id: 1500005457942
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 32ee3fcb58d92b9729e0145f038dc218b1044ab9020ef8d70270046ded16c822
fetched_at: '2026-06-28T22:38:41.124430+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro de argumento
  na geração do pedido de venda
type: support-article
updated_at: '2024-07-09T22:00:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005457942-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-de-argumento-na-gera%C3%A7%C3%A3o-do-pedido-de-venda
---

**Ocorrência**

Ao gerar um pedido de venda está gerando erro de argumento :

**argument [#0](https://totvssuporte.zendesk.com/agent/tickets/0) error, expected C->D, function ctod on A410TUDOK(MATV410A.PRW) 18/03/2021 19:47:54 line : 512**  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- a partir da release 12.1.23.  
  
**Causa**

O erro ocorre por que o parâmetro **MV\_NT2006I**  deve ter sido criado como  tipo  **data**, sendo o correto tipo **carácter**.

**Solução**Efetue o ajuste no parâmetro **MV\_NT2006I**, via Configurador, Ambiente, Cadastros, Parâmetros, o deixando com o tipo carácter ao invés de data, desta forma, o erro deixará de ocorrer.

![](https://totvssuporte.zendesk.com/hc/article_attachments/1500006934161/MV_NT2006I.gif)

***\*imagem da configuração do parâmetro retirada do artigo do SPED - 438 Rejeição.***

**Saiba mais sobre NT2020.006:**

**[MP - FAT - Pedido de Venda - Código do Intermediador (Validações e Emissão da NF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005084801-MP-FAT-Pedido-de-Venda-C%C3%B3digo-do-Intermediador-Valida%C3%A7%C3%B5es-e-Emiss%C3%A3o-da-NF-)**

**[MP - NFE - Nota técnica 2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634-MP-NFE-Nota-t%C3%A9cnica-2020-006)**

[**MP - NFE - 438 Rejeição: Obrigatória as informações do intermediador da transação para operação por site de terceiros**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002431261-MP-NFE-438-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3ria-as-informa%C3%A7%C3%B5es-do-intermediador-da-transa%C3%A7%C3%A3o-para-opera%C3%A7%C3%A3o-por-site-de-terceiros-)
