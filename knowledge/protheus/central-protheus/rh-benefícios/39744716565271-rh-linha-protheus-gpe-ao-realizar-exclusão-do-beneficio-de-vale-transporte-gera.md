---
article_id: 39744716565271
category: RH - Benefícios
content_hash: da55a14b16236907033729ce0bf845b7a84dab7e672153e663e64d7b76eb2728
fetched_at: '2026-06-28T22:44:03.482853+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao realizar exclusão do beneficio de Vale Transporte
  gera mensagem de HELP: FWFORMBEFORE'
type: support-article
updated_at: '2026-04-14T18:38:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39744716565271-RH-Linha-Protheus-GPE-Ao-realizar-exclus%C3%A3o-do-beneficio-de-Vale-Transporte-gera-mensagem-de-HELP-FWFORMBEFORE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39744716551319) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Ao realizar exclusão do beneficio de Vale Transporte gera mensagem de HELP: FWFORMBEFORE.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39744687818903)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A mensagem de help é gerada quando tentamos excluir o vinculo do beneficio de vale transporte pela rotina **Atualizações (GPEA133)**, **com calculo ainda existente.**  
  
Para realizar a exclusão corretamente, é necessário primeiro **cancelar o calculo** e depois excluir o vinculo do beneficio.   
[Cancelamento de Cálculo GPEM160](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9628171182231-RH-Linha-Protheus-GPE-Cancelamento-de-c%C3%A1lculo-GPEM160)  
  
**Obs.:** Para cancelar o calculo é necessário que o campo **Ped.Compra** na rotina **Atualização (GPEA133)** esteja como **Em Aberto**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39744687819415)

**Saiba Mais**  
[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)
