---
article_id: 360018565072
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d29b22b60d150b9e6ccacd557952d80724daa42406876e75bf36f838224bcf0c
fetched_at: '2026-06-28T22:38:29.870003+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Prioridade de Comissão de
  Vendedores
type: support-article
updated_at: '2026-04-02T14:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018565072-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Prioridade-de-Comiss%C3%A3o-de-Vendedores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39468767617687)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Qual a hierarquia / priorização de busca do sistema, das definições de comissão cadastradas, para gerar comissão ao vendedor, sobre um Pedido de Vendas?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

O sistema irá buscar (e considerar este percentual), para gerar a comissão do Vendedor, se houver comissão registrada no campo:

           1º lugar:**C6\_COMIS1** - Item do Pedido de Venda (MATA410);

           2º lugar: **B1\_COMIS** - Cadastro do Produto (MATA010);

           3º lugar: **C5\_COMIS1** - Cabeçalho do Pedido de Venda (MATA410);

           4º lugar: **A1\_COMIS** - Cadastro do Cliente (MATA030);

           5º lugar: **A3\_COMIS** - Cadastro do Vendedor (MATA040).

|  |
| --- |
| Assista ao vídeo explicativo para entender o fluxo de cadastro e comissão:  [How To | MP - SIGAFAT - Configuração de vendedor para comissões](https://www.youtube.com/watch?v=hxKM-ESpAKI) |

**Saiba mais:**

[**FAT0036 Hierarquia priorização de busca de comissão para gerar comissão ao vendedor sobre Pedido de Vendas**](http://tdn.totvs.com/pages/releaseview.action?pageId=232818579)
