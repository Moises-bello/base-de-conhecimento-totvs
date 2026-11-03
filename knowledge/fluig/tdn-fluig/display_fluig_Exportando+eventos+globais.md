---
content_hash: 7174e6df7b9a8c147e3a15237f604cebab5f81502ba69bde87256328257e1d3c
fetched_at: '2026-06-28T21:35:22.697781+00:00'
page_id: '239019348'
product: fluig
source: tdn-fluig
title: Exportando eventos globais
type: documentation
url: https://tdn.totvs.com/display/fluig/Exportando+eventos+globais
version: 8
---

Os eventos globais são eventos disparados durante a utilização do fluig e podem ser desenvolvidos sobre a plataforma.

O desenvolvimento de um evento é realizado por meio da criação de *scripts* na linguagem JavaScript. O código de implementação de cada *script* é armazenado no banco de dados do fluig, dispensando o uso de qualquer outro arquivo.

Atenção

Para que um usuário que não é administrador da empresa possa exportar eventos globais é necessário que ele possua a permissão "Configurar Eventos Globais". Esta permissão pode ser concedida pelo administrador através do item "Permissões" disponível no agrupador "Pessoas" do Painel de Controle do fluig.

Saiba como realizar esse procedimento [clicando aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=269431799).

samples1Passo 1

Na perspectiva Fluig, localize o arquivo desejado dentro do projeto, no caminho events/[nome\_servidor]/[evento].js.

Clique com o botão direito sobre o arquivo do evento e selecione a opção **Export...**

Escolha a opção **Exportar para Servidor Fluig** e clique em **Next**.

2Passo 2

Selecione o servidor para onde o evento será exportado. Na tabela são mostrados ao usuários todos os eventos do servidor. Também é possível alternar as opções de manter, atualizar, eliminar ou criar novos eventos.

Após configurar, clique em **Finish** e aguarde o término do processamento.
