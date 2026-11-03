---
article_id: 36063470796951
category: Materiais - Compras (SIGACOM)
content_hash: a1c76c286e1f3c3e58d821b44ba029042e915fa9d27de18ce1f830d5221e13d3
fetched_at: '2026-06-28T22:41:21.840445+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Na tela Necessidade
  de Compra, qual campo é verificado no Filtro por Data?
type: support-article
updated_at: '2025-11-17T15:20:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36063470796951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Na-tela-Necessidade-de-Compra-qual-campo-%C3%A9-verificado-no-Filtro-por-Data
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36063470766103) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Na tela Necessidade de Compra do Novo Fluxo de Compras, qual campo é verificado no Filtro por Data?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - a partir da Release 12.1.2210  
  
**Solução**  
Na tela Necessidade de Compra do Novo Fluxo de Compras, ao acessar uma das listas de solicitações de compras, independente da aba (Em aberto, Parcialmente atendidas e Atendidas), haverá uma série de Filtros que podem ser utilizados pelo usuário de forma individual ou combinada.

O**Filtro por Data** funciona com intervalo de duas datas (início e fim), após a seleção o filtro buscará solicitações de compras que possuem a **Data de necessidade** de acordo com o período selecionado.

![](https://tdn.totvs.com.br/download/attachments/680260500/filtro%20por%20data.gif?version=1&modificationDate=1712926134807&api=v2)

Essa **Data de necessidade** corresponde ao conteúdo do campo **C1\_DATPRF** da Solicitação de Compras.

Não temos como filtrar as solicitações pela Data de Emissão da Solicitação de Compras (**C1\_EMISSAO)**.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
