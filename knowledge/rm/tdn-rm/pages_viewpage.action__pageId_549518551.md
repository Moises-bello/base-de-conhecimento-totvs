---
content_hash: 1d7d9b7a8004f660ba188656057367281f18cdf232083d50f692893e48201edb
fetched_at: '2026-06-29T00:10:43.119846+00:00'
page_id: '549518551'
product: rm
source: tdn-rm
title: Configuração do URL Rewrite
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549518551
version: 9
---

Deve ser instalado o URL Rewrite e o ARR (Application Request Routing).

Link para o URL: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após instalado o URL Rewrite deve configurado, conforme abaixo:

Acessar o IIS -> Ir no aplicativo do EducaMobile -> URL Rewrite

Adcionar uma *Rule* do tipo *Inboud Rule,*com os dados a seguir:

:

* Preencher as informações de Match *URL:*

* Preencher as informações de *Conditions*

* Preencher as informações de *Action*

Importante

Verificar a porta configurada na tag ApiPort do arquivo de configuração do Host, por padrão é usada a porta 8051.
