---
article_id: 4406743112727
category: SIGAEST - CUSTOS
content_hash: 24c201f9ace9542436ec76f172fc5d79b30f15c3be112b504083483422060bb5
fetched_at: '2026-06-28T22:39:02.350136+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Reavaliação do Custo
  Médio (MATA338)-  Help A338CADA
type: support-article
updated_at: '2023-05-24T12:11:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406743112727-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Reavalia%C3%A7%C3%A3o-do-Custo-M%C3%A9dio-MATA338-Help-A338CADA
---

**Ocorrência**Ao fazer a Reavaliação de Custo Médio de um produto aparece o help A338CADA.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Ao fazer a Reavaliação do Custo Médio é apresentado o seguinte help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406742764951/mceclip0.png)

**Solução**

Nesse caso o help informa que já houve um reajuste para esse produto no período em questão.  
  
Verifique na sua base se já houve reavaliação de custo médio para esse produto.

Conforme próprio fonte do help:

// Verifica se ja existe o registro cadastrado  
SDQ->(dbSetOrder(1))  
If SDQ->(dbSeek(xFilial("SDQ")+M->DQ\_COD+M->DQ\_LOCAL+DTOS(M->DQ\_DATA)))     
 Help(' ',1,'A338CADA')  
    lRet := .F.  
EndIf

**Saiba mais:**

*[MP - SIGAEST - Reavaliação de Custo Médio - MATA338](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608652-MP-SIGAEST-Reavalia%C3%A7%C3%A3o-de-Custo-M%C3%A9dio-MATA338)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
