---
article_id: 360018781512
category: ADVPL - Classe e Função
content_hash: e6cfcc4306acfed3e18c4443adbba58409c8a4177e1f18b725445211aa5b4a35
fetched_at: '2026-06-28T22:40:16.921932+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - HELP NO_IX
type: support-article
updated_at: '2021-07-02T14:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018781512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-HELP-NO-IX
---

**Dúvida**Ao tentar utilizar uma rotina, o sistema apresenta a mensagem ***Help*: NO\_IX, Problema: Função de usuário não está compilada no repositório**![TOTVS_-_Agente_-_Google_Chrome_3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360014793271/TOTVS_-_Agente_-_Google_Chrome_3.jpg)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Esse *Help*é apresentado pois a função não está compilada no **RPO.**Para solucionar essa ocorrência, realize os seguintes passos:

* Verifique se a função está realmente compilado no **RPO;**
* Verifique se esta apontando para o **RPO** correto;
* Verifique as configurações do menu pelo configurador em questão.
* Verifique se a chave ***IXBLOG=NORUN*** está ativada, caso esteja comente ou remova do appserver.ini
* Verifique se a customização não está bloqueada no catalogo de personalizações no configurador.

**Saiba Mais**[MP - FRAME - Desabilitar Customizações e Pontos de Entrada pelo Catálogo de Personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024863633-MP-FRAME-Desabilitar-Customiza%C3%A7%C3%B5es-e-Pontos-de-Entrada-pelo-Cat%C3%A1logo-de-Personaliza%C3%A7%C3%A3o?source=search)
