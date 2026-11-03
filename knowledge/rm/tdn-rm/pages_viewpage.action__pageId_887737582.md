---
content_hash: 4acfab2fb0dbbfe981fcd0d6b8400a2a0dc6b375efc030e5a29eb028dd305dbc
fetched_at: '2026-06-29T00:12:00.731555+00:00'
page_id: '887737582'
product: rm
source: tdn-rm
title: Evento de exclusão S-3500 - Leiaute 1.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=887737582
version: 1
---

O evento S-3500 é acionado através do botão **Excluir** exibido na informação mestre dos evento S-2500 e S-2501.

**S-2500**

**S-2501**

[Regra da exclusão](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-retificada-em-02122022.pdf/), conforme definição do eSocial:

A exclusão de um evento S-2500 não pode ser efetuada se houver um evento S-2501 que faça referência a ele. Ou seja, para a exclusão do evento S-2500 deve-se excluir, primeiramente, o(s) evento(s) S-2501 a ele vinculado(s).

Após a exclusão, será executado o gatilho para geração do XML na [fila de evento existente no Folha de Pagamento](https://tdn.totvs.com/display/LRM/Fila+de+Eventos).
