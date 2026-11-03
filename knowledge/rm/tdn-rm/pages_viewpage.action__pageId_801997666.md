---
content_hash: dbba1e02f459dc9681734c1828240b0889ce690e94b366c08c51622dbda964bd
fetched_at: '2026-06-29T00:11:43.091244+00:00'
page_id: '801997666'
product: rm
source: tdn-rm
title: 03 - Modelos de Ficha Médica - Tela de Agrupador, Seção e Campo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=801997666
version: 49
---

# Sumário

---

Sumário

# Objetivo

---

Definição dos componentes do modelo da ficha médica:

* Agrupador
* Seção
* Campo

# Agrupador

---

O agrupador é um item da ficha médica que permite agrupar seções e também campos.

Para adicionar um **Agrupador,** clique em **Adicionar Novo Agrupador +**

O cadastro de agrupador é composto das seguintes informações: **Nome** (obrigatório),  **Texto Descritivo** (opcional)  e **Inativo**.

Texto descritivo

O campo texto descritivo está preparado para utilização de tags HTML em seu corpo, para facilitar a formatação do seu conteúdo.

**Exemplo:**

Cadastro do agrupador:

Resultado:

# Seção

---

A seção é um item que poderá fazer parte do agrupador e poderá ter campos adicionados.

Após isso é possível adicionar uma Seção dentro do agrupador, onde poderão ser agrupados vários campos para preenchimento.

Para adicionar uma seção clique no ícone conforme a imagem abaixo

O cadastro de seção é composto do seguintes campos: **Nome** (obrigatório), **Texto Descritivo** (opcional) e **Inativo**.

Ordenação dos itens da ficha médica

Com objetivo de flexibilizar e facilitar a organização e ordenação dos itens da ficha médica será possível mover o item com o mouse reordenando o mesmo Agrupador.

**Ordem dos itens na Ficha:** Para ordenar os itens de acordo com sua preferência, clique sobre o item desejado, seja Agrupador, Seção ou Campo, mantenha o mouse pressionado e arraste para a ordem que desejar.

É importante ressaltar que não será possível mover um campo de uma seção para um agrupador e vice e versa, ou seja, será permitido executar a ordenação no mesmo nível.

Agrupadores e Seção

* O cadastro de agrupadores e de seções são únicos por modelo, ou seja, cada modelo tem o seu.
* Somente podem ser excluídos os agrupadores que não possuem seções ou campos associados, além disso, só poderá ser excluída uma seção se não houver um campo associado

# Campo

---

A ficha médica será composta por um conjunto de campos que poderão ser adicionados em agrupadores ou seções.

Para adicionar um campo clique no ícone conforme destacado na imagem abaixo

Ao selecionar Campo, serão exibidas todos os campos já cadastradas, onde é possível realizar uma busca pelo titulo do campo preenchendo o "**Pesquisar Campo"**.

Ao pesquisar o campo, para adicionar o mesmo na ficha médica deverá ser selecionado e na sequência clicar em "**Adicionar campo(s) selecionado(s)**"

**Novo campo**

Quando o campo não for encontrado na pesquisa será possível criar um novo campo e na sequência clicar em "**Adicionar campo(s) selecionado(s)**"

Campo global

O cadastro do campo é global, ou seja, um mesmo campo cadastrado poderá ser utilizado em outros contexto ou em vários modelos do mesmo contexto.

Por exemplo: Campo cadastrado "**Qual é o seu tipo sanguíneo?**", esse mesmo campo poderá ser adicionado em outros modelos de outros contexto ou do mesmo contexto.

É importante ressaltar que o campo nasce global de forma nativa, e permite que  a informação preenchida pelo aluno também seja global, por exemplo, se o aluno preencher o campo "**Qual é o seu tipo sanguíneo?**" na ficha médica da filial 01, e depois se esse aluno for transferido para a filial 02, e a ficha médica da filial 02 usar o mesmo campo no seu modelo de ficha médica, essa informação já vai estar preenchida na ficha médica da filial 02.

O mesmo aproveitamento acontecerá, no seguinte cenário: o usuário realiza a cópia da ficha médica "**X**" para o mesmo contexto, passando a ter a ficha médica "**X Cópia**". Na sequência inativa a ficha médica "**X**",  ativa a ficha médica "**X Cópia**" e acrescenta alguns novos campos, com isso quando o aluno acessar a ficha médica o sistema vai mostrar a ficha médica ativa "**X Cópia**" e carregara os campos já preenchidos pelo aluno.

Opções Formato do Campo

**Caixa de listagem:**  
Uma caixa de seleção que o usuário poderá selecionar somente uma opção.

**Caixa de opções:**  
Conjunto das opções em formato de bolinhas, poderá selecionar somente uma opção.

**Caixa de opções multiseleção:**  
Conjunto de opções em formato de caixinhas, poderá selecionar mais de uma opção.

**Caixa de listagem multiseleção:**  
Opção parecida com a Caixa de listagem, porém poderá selecionar mais de uma opção.

**Caixa de seleção:**  
A caixa de seleção tem uma opção para ser usada.

Para os campos que são do tipo listagem ou multiseleção será necessário definir as opções que serão disponibilizada para estes campos.

Se uma opção já foi preenchida em alguma ficha médica, a mesma não poderá ser alterada ou excluída 

Se um campo já consta como preenchido em uma ficha médica não será permitido alterar nenhuma informação em seu cadastro.

Conforme o modelo da ficha médica for sendo construído é possível gerar uma pré-visualização que possibilita visualizar como a ficha médica será apresentada, para maiores informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=808015319).
