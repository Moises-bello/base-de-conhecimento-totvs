---
content_hash: d43758c50f09027da36cb1abf301c90a5533311042b347a98e852a266c6c98e9
fetched_at: '2026-06-29T00:08:34.647290+00:00'
page_id: '274828870'
product: rm
source: tdn-rm
title: Algorítimo de Identificação de incidente (hash)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274828870
version: 1
---

O algorítimo de identificação de incidente é um algorítimo que gera um valor hash para identificação unica daquele problema, este deve levar em consideração os seguintes dados:

* Ambiente (dev/production)
* Linha de produto
* Nome da aplicação
* Mensagem de erro
* Stack do erro

Durante a geração do hash, consideramos:

* Palavras chaves do stack estão normalizadas para uma idioma padrão (ingles)
* Todo o texto dos dados informados estão normalizados para caracteres minúsculos
