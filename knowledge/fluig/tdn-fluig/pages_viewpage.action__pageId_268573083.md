---
content_hash: 44b1911eeefa9de540393788bc5ebf7188e6663e4272d984072989888d616089
fetched_at: '2026-06-28T21:35:24.002798+00:00'
page_id: '268573083'
product: fluig
source: tdn-fluig
title: BPM 079 - É possível notificar mais de um usuário ao mesmo tempo dentro do
  diagrama de processo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268573083
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

É possível, dentro do diagrama de processo, notificar mais de um usuário ao mesmo tempo?

Por exemplo: o solicitante inicia a solicitação, que vai para o aprovador e se for aprovado notifica um usuário. Esse usuário não pode finalizar o processo, apenas ser notificado. E uma outra notificação vai para o setor Fiscal que continua o processo

# Solução

Por padrão, no acompanhamento do processo existem três opções de notificação:

- Notifica responsável;

- Notifica requisitante;

- Notifica Gestor;

Para notificar qualquer outro usuário que esteja ou não no processo é necessário desenvolver sobre a plataforma utilizando o evento [onNotify](http://tdn.totvs.com/display/fluig/Desenvolvimento+de+Eventos#DesenvolvimentodeEventos-onNotify).
