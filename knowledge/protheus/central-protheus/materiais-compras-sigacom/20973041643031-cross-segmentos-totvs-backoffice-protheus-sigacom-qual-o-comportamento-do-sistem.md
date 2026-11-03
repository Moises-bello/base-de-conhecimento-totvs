---
article_id: 20973041643031
category: Materiais - Compras (SIGACOM)
content_hash: 45b7cbe065f4bb50bfeb50da1d26a452dd9fc7768101639c67982fea97bca615
fetched_at: '2026-06-28T22:41:24.291917+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o comportamento
  do sistema ao utilizar o pergunte Filtra Compradores ?
type: support-article
updated_at: '2024-01-30T13:32:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20973041643031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-comportamento-do-sistema-ao-utilizar-o-pergunte-Filtra-Compradores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20973003836567) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o comportamento do sistema ao utilizar o pergunte "Filtra Compradores ?" em conjunto com o parâmetro MV\_RESTCOM habilitado ("S").   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Solicitante que tem seu grupo de compras (**AI\_GRUPCOM**) informado no cadastro de solicitantes (**MATA084**).    
  
Ao acessarmos a rotina "Atualiza Cotações" (**MATA150**) com o solicitante e definirmos os perguntes conforme abaixo :  
  
  Cenário 1                                                                               Cenário 2   
![](https://tdn.totvs.com.br/download/thumbnails/822220757/image-2024-1-29_11-3-51.png?version=1&modificationDate=1706538349497&api=v2)                    ![](https://tdn.totvs.com.br/download/thumbnails/822220757/image-2024-1-29_11-20-16.png?version=1&modificationDate=1706538349027&api=v2)  
  
Resultado apresentado (Cenário 1 ) :Serão apresentados todas as cotações em aberto, que estejam preenchidas com o grupo de compras pertencentes ao solicitante (**C8\_GRUPCOM**) e as cotações que **NÃO\*** tenham um grupo de compra preenchido.   
  
Resultado apresentado (Cenário 2 ) : Serão apresentados todas as cotações em aberto.

**Saiba Mais:**

**[Qual o comportamento do sistema ao utilizar o pergunte "Filtra Compradores ?" em conjunto com o parâmetro MV\_RESTCOM habilitado ("S")](https://tdn.totvs.com.br/pages/viewpage.action?pageId=822220757)**

**[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655)**

**[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**
