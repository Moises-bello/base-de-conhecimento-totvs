---
content_hash: fafda67fbf441ca56766f9de2db88f2c8c8b0993effba5dc0708be9f3fac418e
fetched_at: '2026-06-28T21:35:19.356217+00:00'
page_id: '201745850'
product: fluig
source: tdn-fluig
title: Identity | Por que não consigo acessar o Identity após configurar o Desktop
  SSO?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201745850
version: 14
---

**Dúvida**

Por que não consigo acessar o Identity após configurar o Desktop SSO?

**Solução**

Provavelmente os endereços IP externos das máquinas utilizadas para acessar o Identity não estão cadastrados na lista de IPs permitidos na configuração do Desktop SSO.

Fique atento

Os endereços IP permitidos devem ser apenas **IPs externos**, não internos.

Para identificar o IP externo da estação de trabalho e adicioná-lo à lista de IPs permitidos, siga os procedimentos abaixo:

desktopssoIdentificar o IP externo  

* Acessar o site [Meu Endereço IP](http://www.meuenderecoip.com/) (ou similar) a partir da estação de trabalho para verificar o endereço do IP externo.

* O endereço IP será apresentado em **Meu IP neste momento é**.

Permitir o IP no Desktop SSO

* Acessar o contexto da empresa no Identity com o administrador.

* Acessar a configuração do Desktop SSO conforme instruído no help .

* Incluir o endereço IP externo da estação de trabalho obtido pelo site [Meu Endereço IP](http://www.meuenderecoip.com/), ou uma faixa de IPs que inclua esse endereço.

* Salvar as alterações.

Importante

Não é necessário atualizar o arquivo remote\_auth.asp no servidor do IIS ao acrescentar um novo endereçou ou nova faixa de IP ao Desktop SSO.
