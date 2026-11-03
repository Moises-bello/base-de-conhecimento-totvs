---
article_id: 27572490948631
category: Financeiro - Baixas a Pagar
content_hash: 5c6488f8fb9d801c0db1f30f74fbf74622685bd1a332349d3c0f35f2c9615df0
fetched_at: '2026-06-28T22:37:24.898278+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 Ao estornar
  a baixa a pagar de um título tipo NF que gerou impostos no momento que baixou, e
  esses impostos não estão sendo estornados (excluídos)
type: support-article
updated_at: '2026-03-25T20:31:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27572490948631-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Ao-estornar-a-baixa-a-pagar-de-um-t%C3%ADtulo-tipo-NF-que-gerou-impostos-no-momento-que-baixou-e-esses-impostos-n%C3%A3o-est%C3%A3o-sendo-estornados-exclu%C3%ADdos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490904087) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
FINA080 Ao estornar a baixa a pagar de um título tipo NF que gerou impostos no momento que baixou, e esses impostos não estão sendo estornados (excluídos)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões.  
  
**Solução**

Situação 1)

MV\_BX10925=1  Define momento do tratamento da retenção dos impostos Pis Cofins e Csll 1 = Na Baixa ou 2 = Na Emissão

Tenho um título que vai gerar PCC no momento em que for baixar o título, tipo:NF no contas a pagar.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490905111)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490905111)

E foi criado mais 3 títulos do tipo TX

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465047703)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465047703)

Ao estornar a baixa do título o tipo:NF

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465048727)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465048727)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465052439)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572465052439)

O título tipo:NF é estornado com sucesso, porém os impostos de PCC não são estornados (excluídos).

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490915223)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490915223)

Isso pode ocorrer caso o seu parâmetro MV\_UNIAO esteja com algum conteúdo incorreto.

Exemplo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490919575)](https://centraldeatendimento.totvs.com/hc/article_attachments/27572490919575)

[Veja que o conteúdo do meu parâmetro está considerando a loja 01, é isso é incorreto, pois a loja do fornecedor UNIAO deve ser 00 sempre.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052816113-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-UNIAO)

Para corrigir, terá que deletar o conteúdo da loja '01' do parâmetro,

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Utilização do parâmetro MV\_UNIAO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052816113-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-UNIAO)
