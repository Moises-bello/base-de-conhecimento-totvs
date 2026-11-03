---
content_hash: 100fa6be5e9a6cfe5c9be3673439717739d5517f025ddb48d1056f389906223e
fetched_at: '2026-06-29T00:08:47.313742+00:00'
page_id: '319787298'
product: rm
source: tdn-rm
title: Manual - Parâmetros da Geração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319787298
version: 3
---

O contexto de Parâmetros da Geração permite que sejam criados parâmetros que serão informados pelo usuário no momento da geração. Existem vários tipos de parâmetros que podem ser usados e os seus valores podem ser utilizados na passagem de parâmetros de outros contextos, para preencher valores de campos do registro, em expressões de filtro e de campos.

![](/download/attachments/319787298/parametros_da_geracao.png?version=1&modificationDate=1512921911000&api=v2)

1Adicionar

Clique para adicionar um novo parâmetro da geração. Os seguintes tipos de parâmetros estão disponíveis:

##### Texto

O parâmetro do tipo texto é usado para que o usuário informe um texto qualquer utilizando um controle de caixa de texto.

##### Número Inteiro

O parâmetro do tipo número inteiro é usado para que o usuário informe um número sem casas decimais utilizando um controle de entrada de texto.

##### Número Decimal

O parâmetro do tipo número decimal é usado para que o usuário informe um número com casas decimais utilizando um controle de entrada de texto.

##### Data

O parâmetro do tipo data é usado para que o usuário informe uma data utilizando um controle de seleção de datas.

##### Lógico

O parâmetro do tipo lógico é usado para que o usuário informe um valor lógico utilizando um controle de marcar/desmarcar.

##### Lista

O parâmetro do tipo lista é usado para que o usuário informe um valor qualquer baseado em um controle de lista de items e valores (combo). Para mais informações consulte [Parâmetro de Lista](/pages/viewpage.action?pageId=319787299).

##### Filtro

O parâmetro do tipo filtro é usado para que o usuário informe um filtro de SQL baseado em uma tabela do banco de dados. Para mais informações consulte [Parâmetro de Filtro](/pages/viewpage.action?pageId=319787300).

##### Lookup (RM)

O parâmetro do tipo lookup é usado para que o usuário informe um valor baseado na pesquisa de um cadastro do RM. Para mais informações consulte [Parâmetro de Lookup](/pages/viewpage.action?pageId=319787301).

2Remover

Clique para remover o parâmetro selecionado.

3Mover para Cima

Clique para mover o parâmetro selecionado para cima na lista de parâmetros.

4Mover para Baixo

Clique para mover o parâmetro selecionado para baixo na lista de parâmetros.

5Parâmetros

Exibe a lista de parâmetros da geração.

6Nome

Informe o nome identificador do parâmetro. Ele será utilizado para fazer as ligações e nas expressões do gerador. Este nome é único e não pode haver dois parâmetros com o mesmo nome.

7Título

Informe um texto descritivo do parâmetro. Este valor é opcional e é usado para exibir um nome amigável do parâmetro no momento de execução. Caso ele não seja informado o nome é exibido como padrão.

8Descrição

Informe um texto descritivo para o parâmetro. Este texto será utilizado para geração do arquivo de documentação do Layout.

9Obrigatório

Selecione se o parâmetro é obrigatório para execução do Layout. Neste caso o Layout só poderá ser executado se o seu valor for informado.

#### Exemplo

Ao utilizar o contexto de parâmetros, deve ser solicitado ao usuário que informe os parâmetros para execução do Layout. A tela de parâmetros será gerada utilizando controles de acordo com cada tipo de parâmetro:

![](/download/attachments/319787298/859C9C1A15BBB3F5452E560C7EBE82A2.jpg?version=1&modificationDate=1512921912000&api=v2)
