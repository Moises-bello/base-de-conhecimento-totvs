---
article_id: 22926586972951
category: TAF - REINF
content_hash: 4a9bf7a59ef40d98c73798b063c2b7f04ae9aa9644878ad8e5a4e4130c8022b6
fetched_at: '2026-06-28T22:41:34.653836+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'CROSS Segmentos - Backoffice Protheus - TAF - REINF - Erro de Schema:  tag
  RelFontPg'
type: support-article
updated_at: '2024-04-19T16:55:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22926586972951-CROSS-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-Schema-tag-RelFontPg
---

**Ocorrência**  Ao realizar apuração de um participante residente no exterior é apresentado erro de Schema da tag RelFontPg:

![RELFONT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22926570138519)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATAF - Todas as versões  
  
**Causa**

  Erro ocorre pela falta de preenchimento do campo **C1H\_RELFON**.  
  
**Solução**

Para correção siga os passos abaixo:

* Acesse cadastro de Participantes do TAF, menu atualizações > cadastros > fiscais > participantes; localize o cadastro do participante que foi rejeitado, e preencha a informação do campo Rel Fonte PG(**C1H\_RELFON)**, campo localizado na aba exterior do cadastro de participante:

![RELFONTPG.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22926570139543)

* Após o Preenchimento do campo, exclua a apuração rejeitada:

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como excluir apuração inconsistente.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549885209879-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-excluir-apura%C3%A7%C3%A3o-inconsistente)

* Acesse o painel reinf, apure e transmita o evento novamente.
