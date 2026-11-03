---
content_hash: e756b7b20f1032e8e8b0ba524cb87107f54eaf82785872898d5ac9e7f93674c0
fetched_at: '2026-06-28T21:35:19.088858+00:00'
page_id: '189316902'
product: fluig
source: tdn-fluig
title: Identity | Mensagem "The AD Token value does not validate" na configuração
  do SmartSync
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189316902
version: 16
---

**Ocorrência**

Ao tentar configurar o SmartSync é apresentada a seguinte mensagem de erro:

**Causa**

O campo **ADSync Service Server**, localizado na aba FluigIdentity Server das configurações do SmartSync, foi preenchido com a URL do AD Sync do ambiente de homologação, enquanto o Active Directory está vinculado ao ambiente de produção (ou vice versa).

O ambiente de homologação é identificado pelo domínio **customerfi.com** e o ambiente de produção pelo domínio **fluigidentity.com**.

**Solução**

Na aba FluigIdentity Server, informar no campo ADSync Service Server a URL do mesmo ambiente em o AD será utilizado no Identity.

Por exemplo, se o contexto for <https://minhaempresa.fluigidentity.com>, informar <https://app.fluigidentity.com/adsync>.

Se for [https://minhaempresa.customerfi.com](https://minhaempresa.fluigidentity.com%2C/), informar [https://app.customerfi.com/adsync](https://app.fluigidentity.com/adsync).

Alterar também o campo **HTTPS Type** para **SSL3**.
