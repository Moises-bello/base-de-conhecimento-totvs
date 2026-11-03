---
article_id: 360023266071
category: ADVPL - Rotina Automática
content_hash: c8a884c4d141db5f7ead31fb48780512462a11319d1def5b5489264be9b1e0ae
fetched_at: '2026-06-28T22:40:23.959500+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - CTBA102 - Abertura de
  tela na Rotina CTBA102 para alteração de Lançamento bloqueado
type: support-article
updated_at: '2021-12-29T13:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023266071-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-CTBA102-Abertura-de-tela-na-Rotina-CTBA102-para-altera%C3%A7%C3%A3o-de-Lan%C3%A7amento-bloqueado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**

Estamos utilizando execauto da rotina CTBA102.

Quando por exemplo uma conta ou centro de custo está bloqueado ao processar a ExecAuto o sistema apresenta a tela em anexo (AJUDA: CTA\_BLOQ) informando que a entidade está bloqueada.

Em nosso cenário este processo será executado por ação manual do usuário, gostaríamos de saber como alterar para que na execauto não seja interrompida por essa validação e que ao invés disso seja aberto a rotina CTBA102 com a tela de lançamentos para então correção dos lançamentos incorretos.

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para essa necessidade seria apenas através de customização pois dentro do preceitos da rotina automática não é possível fazer com que abra uma tela , a não ser através de customização tratando a questão do bloqueio ou realizando a criação de uma tela que possibilite realizar um ajuste da rotina.
