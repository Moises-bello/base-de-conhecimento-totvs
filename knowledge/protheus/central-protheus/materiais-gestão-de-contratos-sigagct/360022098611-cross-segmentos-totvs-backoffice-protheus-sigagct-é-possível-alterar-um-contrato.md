---
article_id: 360022098611
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 262c4ea4365413ef612d0af369e6f4c624eb673480a9d319484666dfd1aea4d9
fetched_at: '2026-06-28T22:37:22.640955+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível alterar
  um contrato da situação de Solicitação de Finalização para Vigente ?
type: support-article
updated_at: '2022-08-15T13:13:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022098611-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-alterar-um-contrato-da-situa%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Finaliza%C3%A7%C3%A3o-para-Vigente
---

**Dúvida**

É possível alterar um contrato da situação de Solicitação de Finalização para Vigente ?  
  
**Ambiente**

Microsiga Protheus - Gestão de contratos - A partir da versão 11.8  
  
**Solução**

Quando um contrato está com a situação como "**Sol. Finalização**" (07) sua situação não pode ser alterada de para "**Vigente**" (05), podendo esta situação ser alterada somente para Finalizado ou Cancelado.

Caso seja somente o status do contrato **CN9\_SITUAC** que se desejar alterar (Cor da Legenda e não movimentações), pode ser utilizado o ponto de entrada: **CN100COR**, da qual poderá alterar a cor da legenda do contrato em questão.

Para estorno do status e suas movimentações, no padrão não há esta possibilidade, e caso realmente seja necessário desfazer a finalização, alteração via base deverá ser efetuada por um analista/consultor para recuperar os dados antes ao encerramento.

***Saiba mais:***

[CN100COR - Inclusão Alteração de Cores de Legenda do Contrato](http://tdn.totvs.com/pages/releaseview.action?pageId=6089696)

[GCT0073\_Como\_alterar\_a\_situação\_do\_Contrato\_Vigente](http://tdn.totvs.com/pages/viewpage.action?pageId=272417572)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
