---
article_id: 360021352391
category: Materiais - Compras (SIGACOM)
content_hash: 6bf4ba8a7f9e2f7d755bb53f694b5587aa8687d12a1eadf810c3d447de786e26
fetched_at: '2026-06-28T22:41:10.428778+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rateio de Entidades
  Contábeis da Pré-Nota é apagado ao ser estornada a classificação
type: support-article
updated_at: '2025-01-15T19:33:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021352391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rateio-de-Entidades-Cont%C3%A1beis-da-Pr%C3%A9-Nota-%C3%A9-apagado-ao-ser-estornada-a-classifica%C3%A7%C3%A3o
---

**Dúvida**

Rateio de Entidades Contábeis da Pré-Nota é apagado ao ser estornada a classificação

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
  
**Solução**

Na situação em que no Pedido de Compra (**MATA121**) existe Rateio de Entidades Contábeis e o mesmo é vinculado na Pré-Nota / Documento de Entrada ou é informado manualmente o rateio no Documento de Entrada (**MATA103**) ao ser classificado e estornada a classificação via Pré-nota (**MATA140**) o rateio por padrão é apagado.

Para que o rateio não seja excluído através da rotina, estorno da pré nota, é necessário habilitar o parâmetro [**MV\_DELRATC**](https://tdn.totvs.com/pages/viewpage.action?pageId=838222184), que indica se deve apagar ou manter o rateio por centro de custo no estorno da classificação do Documento de Entrada, podendo escolher uma das três opções:

***1=Excluir***   
***2=Mantem o rateio***  
***3=Pergunta se deseja excluir ou manter***

***Saiba Mais :***

***[MV\_DELRATC](https://tdn.totvs.com/pages/viewpage.action?pageId=838222184)***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
