---
content_hash: 9d33167452d838988e5633f8b1766f12a8392a0b0c0fc73126df8b79bce59b93
fetched_at: '2026-06-29T00:08:47.319121+00:00'
page_id: '319787301'
product: rm
source: tdn-rm
title: Manual - Parâmetro de Lookup da Geração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787301
version: 3
---

O parâmetro de lookup necessita que sejam informados os dados do cadastro do RM que será utilizado para pesquisa. Este parâmetro só está disponível para o Gerador RM e irá apresentar um controle de Lookup para que o usuário faça a seleção.

![](/download/attachments/319787301/parametro_de_lookup_da_geracao.png?version=1&modificationDate=1512921918000&api=v2)

1Action

Selecione a Action do cadastro do RM, qualquer cadastro padrão do sistema poderá ser utilizado.

2Campos

Selecione os campos que serão disponibilizados pelo contexto. Estes campos serão exibidos de acordo com a Action selecionada.

3Chave

Informe a chave do cadastro do RM, por padrão o sistema sugere o mesmo nome do campo da chave do cadastro, a chave é utilizada para criar Lookups em cascata, onde o valor de um Lookup depende do valor de outro (mestre/detalhe).

4Descrição

Selecione o campo que será exibido como descrição no controle de lookup.

5Código

Selecione o campo que será exibido como código no controle de lookup.

6Filtro

Informe um filtro SQL para filtrar os dados que podem ser selecionados no Lookup.
