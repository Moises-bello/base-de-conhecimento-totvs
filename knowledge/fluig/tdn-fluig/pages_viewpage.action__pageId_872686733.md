---
content_hash: 3fced9ed52fdd9304879affdcebc952e6a885e9114294bb4979bed7015b47c29
fetched_at: '2026-06-28T21:35:31.097771+00:00'
page_id: '872686733'
product: fluig
source: tdn-fluig
title: Formulários - Campo Pesquisa (zoom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=872686733
version: 13
---

1

O campo de pesquisa (ou campo zoom) é uma ferramenta poderosa para otimizar a seleção e visualização de dados em formulários. Com um simples campo, o usuário passa a ter acesso à dados de uma forma ágil, podendo filtrar e selecionar valores de outros componentes e formulários do Fluig ou mesmo de aplicativos externos através de Datasets.

---

# Nesta documentação

Nesta doc.\*nonefalse

# Pré-requisitos

Essa documentação é indicada para desenvolvedores familiarizados com html e javascript, e com o uso de  no Fluig.

# Sintaxe

html/xml]]>html/xml]]>

# Atributos

**zoomvalue**

Uma string com o nome de um campo do dataset que pode ser armazenado além do texto visível em tela.

O campo de pesquisa pode ser usado para armazenar uma informação para o usuário (como nome de uma pessoa ou empresa) mas a solicitação precisa de um código de identificação (como id do usuário, cpf, cnpj) para alguma integração ou mesmo mecanismo de atribuição. Quando não utilizado o atributo zoomvalue, apenas o valor que é exibido após a seleção é gravado.

Ao utilizar o zoomvalue, o formulário deve conter um campo com nome e id iguais ao do campo de pesquisa com o prefixo "**hidden\_**" (por exemplo, campo "**pessoa**" precisa do campo "**hidden\_pessoa**"). Assim, ao selecionar um registro, o Fluig irá automaticamente preencher o **hidden\_campo** com o campo do dataset definido no atributo.

Importante: O campo definido no zoomvalue deve estar entre os campos listados em **fields** no atributo **data-zoom**

O atributo data-zoom recebe um objeto onde a maior parte das configurações possíveis para o campo pesquisa são feitas. Ele é um objeto complexo onde é definido qual o dataset, qual campo deste dataset será usado para preencher o campo, se permite mais de uma item selecionado e quais os campos podem ser usados de filtro. Consulte mais sobre ele .

# Métodos

---

O campo zoom invoca algumas funções que podem ser sobrescritos para uma maior personalização do formulário.

**setSelectedZoomItem (Object item)**

Esta função é chamada sempre que um item é selecionado em um campo pesquisa. Pode ser utilizado para armazenar outra informação do item de dataset selecionado em outro campo, validações ou mesmo para atualizar os filtros de outros componentes e campos pesquisa do formulário.

**removedZoomItem (Object item)**

Esta função é chamada sempre que um item é removido do campo pesquisa. Normalmente é usado em conjunto com setSelectedZoomItem para "desfazer" as ações.

**reloadZoomFilterValues (String inputName, String filterValues)**

Esta função é usada para atualizar o **filterValues**da configuração realizada no atributo **data-zoom**, e pode ser utilizado para adicionar filtros extras conforme outros dados do formulário ou outras opções selecionadas em outros campos pesquisa. Por exemplo, o usuário selecionou um cliente em um campo pesquisa e eu posso adicionar esta seleção como um novo filtro no campo de pedido.

# Dependências

---

Para o funcionamento correto do componente, o seu formulário deve carregar as seguintes bibliotecas

xml
]]>

# Exemplos de uso

---

### Consulta simples ao cadastro de usuários buscando e ordenando pelo nome

html/xml
Usuário
