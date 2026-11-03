---
content_hash: a0a998dfcdbd895988e5670108f7571d26377a3147082f21f26d34bd89289588
fetched_at: '2026-06-28T21:35:23.837518+00:00'
page_id: '266962926'
product: fluig
source: tdn-fluig
title: BPM 069 - Por que solicitações iniciadas via startProcess definem o usuário
  que realizou a chamada do método como responsável?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266962926
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

Estou tentando utilizar o método startProcess para iniciar uma solicitação para diversos usuários de forma automática.

Ao utilizar o método informado na documentação, foi possível criar solicitações mas ocorreu que todas as solicitações que foram criadas dessa forma, tiveram como responsável o usuário que realizou a chamada do método e não o usuário desejado.

Na assinatura do método, startProcess(processId, ativDest, listaColab, "obs", completarTarefa, valoresForm, modoGestor), o terceiro parâmetro, listaColab, recebe uma lista de usuários. E eu imaginava que essa lista seriam os responsáveis pelas atividades criadas. Estou certo?

# Solução

A definição do usuário que realiza a chamada do método como responsável pode ocorrer pelos seguintes motivos:

* O completarTarefa está definido como *false.*

* Está sendo enviado mais de um usuário no parâmetro listaColab, mas a próxima atividade exige apenas um responsável.
