---
content_hash: d6325b1e47e8f7a9ef2f931cf729cc747cae29e5d2ce926748c0173088f43e50
fetched_at: '2026-06-29T00:10:52.277356+00:00'
page_id: '571539060'
product: rm
source: tdn-rm
title: Validações do Prestador Responsável e Solicitante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571539060
version: 3
---

Ao fazer o encerramento da conta é feita algumas consistências sobre o cadastro do medico responsável e solicitante.

Os médicos prestadores devem possuir informações do conselho como Numero, Uf e o nome do conselho, e verifica se a versão TISS que o convenio usa aceita o conselho que foi selecionado:

Quando essas regras não forem atendidas é apresentada as seguintes mensagens no encerramento da parcial:

* Não foi possível identificar o conselho profissional do prestador Solicitante XXXXXX. Realize a correção no cadastro.
* Não foi possível identificar a UF da identidade profissional do prestador Solicitante XXXXXX. Realize a correção no cadastro.
* Não foi possível identificar a identidade profissional do prestador Solicitante XXXXXX. Realize a correção no cadastro.
* Conselho profissional CRV do prestador Solicitante XXXXXX, não definido na versão 3.03.03 do padrão TISS - ANS. Realize a correção no cadastro.
