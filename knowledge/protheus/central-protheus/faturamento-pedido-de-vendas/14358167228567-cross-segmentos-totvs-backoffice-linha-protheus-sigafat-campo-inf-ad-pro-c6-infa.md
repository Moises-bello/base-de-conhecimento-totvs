---
article_id: 14358167228567
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 64452cbecc206d140ef96c5754d400a0cf7253bf8b7ac2f476e3318c34b3cc33
fetched_at: '2026-06-28T22:38:42.650584+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campo "Inf.
  Ad. Pro [C6_INFAD]" duplicando conteúdo
type: support-article
updated_at: '2023-05-04T16:58:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14358167228567-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-Inf-Ad-Pro-C6-INFAD-duplicando-conte%C3%BAdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Por qual motivo no campo MEMO "Inf. Ad. Pro [C6\_INFAD]" está com a mesma informação que coloquei em outro pedido de venda (anterior)?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

A mensagem nesse campo pode ficar duplicada, devido a antiga função: "**E\_MSMM(SC6->C6\_CODINF,80)**"

que deve ser substituída manualmente por: "**M410MSMM()**"

**Para solucionar:**

1 - Entre no Configurador > Base de Dados > Dicionário > Bases de Dados

2 - Localize o campo C6\_INFAD na tabela SC6 e altere.

3 - Na aba "Opções", no campo "Inic. Padrão" coloque "**M410MSMM()**"

4 - Salve completamente (para salvar o sistema precisa estar em ambiente exclusivo)

5 - [Atualize os fontes para o mais atual do Faturamento, clique aqui.](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/FAT_expedicao_continua)

Antes (ANTIGO):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14358106200599)

Depois (CORRETO):

![](https://tdn.totvs.com/download/attachments/733944132/image2023-1-19_10-56-40.png?version=1&modificationDate=1674136686210&api=v2)

**Saiba Mais**

**[DSERFAT-26116 DT Campo C6\_INFAD duplicando informação na alteração do Pedido de Venda](https://tdn.totvs.com/x/RBm-Kw)**
