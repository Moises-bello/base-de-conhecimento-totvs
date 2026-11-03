---
article_id: 360043793254
category: Call Center - Dúvidas Gerais
content_hash: 5996e36dee41a3921cc43c4ea73927ac27341d702e95d9d94d6fc71337a1ebf5
fetched_at: '2026-06-28T22:41:26.862442+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - TK062NLIST
type: support-article
updated_at: '2022-06-17T13:42:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043793254-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-TK062NLIST
---

**Dúvida**

Ao acessar a rotina de Lista de telecobrança o sistema informa que não foi definido o uso de listas no cadastro de Regras de seleção :

![TK062NLIST.JPG](https://totvssuporte.zendesk.com/attachments/token/dSRsfYJJjNdTiXEglhI6tSqKb/?name=TK062NLIST.JPG)

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK  – A partir da release 11.80.  
  
**Solução**

A mensagem somente ocorre  se a regra de seleção de cobrança for definida como grupo cobrança e está tentando utilizar lista de cobrança.

Ao acessar essa rotina, se o cadastro de Regras de Seleção estiver vazio (em branco), é apresentada uma mensagem de alerta, questionando se o usuário deseja trabalhar com a lista de cobrança para realizar os atendimentos de Telecobrança.

Se sim, a cobrança será realizada pela rotina Agenda do Operador (menu Atendimento), por meio de listas geradas pela rotina Listas de Cobrança (menu Marketing). Se não, é possível criar as regras de seleção por grupos de atendimentos; a cobrança será realizada pela rotina Pré-Atendimento (menu Cobrança).

O somatório do campo "Prazo" (Dias) não pode ser superior a 100.000 dias. Esse valor representa 273 anos (100000 / 365 dias), tempo suficiente para efetuar a cobrança dos títulos atrasados.

Ocorre uma exceção se a cobrança for executada pelas rotinas Listas de Cobranças e Agenda do Operador. Nessa situação, o sistema gera automaticamente o prazo com o intervalo 000001 a 999999.

Exemplo: Se o campo "Prazo/Dias" estiver definido como "30" dias, serão cobrados os títulos em aberto vencidos até 30 dias da data base.

Detalhes desse assunto em : **<https://tdn.totvs.com/pages/releaseview.action?pageId=239037537>**
