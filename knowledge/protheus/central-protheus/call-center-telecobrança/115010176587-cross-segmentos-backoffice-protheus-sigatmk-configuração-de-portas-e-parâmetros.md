---
article_id: 115010176587
category: Call Center - Telecobrança
content_hash: 04c8d9e23ca9b6f99c266f2aec841d0fc25a0f5854867933442a50934ef4c94f
fetched_at: '2026-06-28T22:41:28.574203+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Configuração de portas e
  parâmetros de segurança no Protheus para envio de e-mail no TeleCobrança quando
  provedor utilizado for Gmail
type: support-article
updated_at: '2024-04-25T13:10:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010176587-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Configura%C3%A7%C3%A3o-de-portas-e-par%C3%A2metros-de-seguran%C3%A7a-no-Protheus-para-envio-de-e-mail-no-TeleCobran%C3%A7a-quando-provedor-utilizado-for-Gmail
---

**Dúvida**

Como configurar  e-mail no telecobrança com uso do GMAIL?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

Para utilizar o servidor SMTP do Gmail é necessário informar a porta de acordo com o requisito de configuração, se usar SSL a porta deve ser a 465 e o TLS deve estar desativado.

No exemplo utilizamos apenas o SSL como .T. e a porta 465 para SMTP.

Segue relação de parâmetros a serem configurados:

* MV\_RELSERV = [smtp.gmail.com](http://smtp.gmail.com/)
* MV\_RELACNT = [user@gmail.com](mailto:user@gmail.com)
* MV\_RELAPSW = senha do e-mail
* MV\_RELAUSR = user
* MV\_RELAUTH = .T.
* MV\_RELFROM = [user@gmail.com](mailto:user@gmail.com)
* MV\_RELPSW = senha do e-mail
* MV\_RELSSL = .T.
* MV\_RELTLS = .F.
* MV\_PORSMTP = 465

Após a configuração destes é necessário informar no cadastro do operador que irá realizar o atendimento em ações relacionadas > e-mail e informar o user e senha do servidor utilizado no envio. Apenas o login sem o @[gmail.com](http://gmail.com/).

|  |  |
| --- | --- |
| **Observações:** | Para utilizar o servidor SMTP do Gmail é necessário ativar a permissão de acesso para aplicativos menos seguros. |
