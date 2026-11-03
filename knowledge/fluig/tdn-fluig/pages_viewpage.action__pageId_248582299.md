---
content_hash: 673ee013a9f818a4e0b13ae23a21d6535ae8a7407d3f7f0f20597ab6450bec86
fetched_at: '2026-06-28T21:35:23.429861+00:00'
page_id: '248582299'
product: fluig
source: tdn-fluig
title: BPM 082 - Como impedir a criação de solicitações com dados repetidos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=248582299
version: 15
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:** 1.5.0 e 1.6.0

# Ocorrência

Após preencher os campos do formulário e enviar a atividade, quando é clicado no botão "Iniciar Novas solicitações" os formulários continuam preenchidos.

# Solução de contorno.

Uma solução provisória para este caso é criar uma validação no formulário, utilizando o evento de formulário *validateForms*. Neste evento é possível consultar o dataset do próprio formulário usando como constraint os campos do formulário que sejam campos chave para o negócio. Caso já exista um registro de formulário criado é possível retornar uma mensagem de erro para o usuário, informando-o de que já existe uma solicitação aberta com esses mesmos dados informados.

Em anexo a seguir, estão disponibilizados um projeto para o plugin Fluig para o Eclipse com uma implementação modelo da solução de contorno citada acima e também um vídeo guia que irá auxiliar na aplicação e desenvolvimento dessa solução no seu processo.

250250
