---
content_hash: 5c54b30320f27a5a366a489b490f516d50bb9b05b438dff6d45dd91a9e89bd80
fetched_at: '2026-06-29T00:09:59.947200+00:00'
page_id: '452718459'
product: rm
source: tdn-rm
title: Conversor Perfil DIRF X Operadora Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718459
version: 2
---

Conversor responsável por buscar os dados informados no Parametrizador da DIRF aba "Operadoras de Assistência à Saúde" e gravar no Cadastro de "Operadora de Assistência à Saúde" do eSocial.  
 Observações:

* Ao cadastrar uma operadora de saúde pelo Parametrizador da DIRF, será incluído automaticamente no cadastro de "Operadora de Assistência à Saúde" do eSocial.
* Caso exista algum registro com natureza da rubrica(eSocial) diferente de '9219 - Desconto de assistência médica ou odontológica' no Parametrizador da DIRF, o processo será executado normalmente.
* Sempre que excluído um registro do cadastro de "Operadora de Assistência à Saúde" que a origem seja do conversor, os mesmos serão reinseridos caso o processo seja executado novamente, sendo que o código nem sempre será o mesmo.
