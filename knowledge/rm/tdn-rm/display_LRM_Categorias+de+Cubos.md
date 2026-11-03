---
content_hash: a7e6816a788dd4b37fdc0af9ad548333363b20fbf3f124a79f75e61aef9d1a6b
fetched_at: '2026-06-29T00:10:38.832807+00:00'
page_id: '545245402'
product: rm
source: tdn-rm
title: Categorias de Cubos
type: documentation
url: https://tdn.totvs.com/display/LRM/Categorias+de+Cubos
version: 3
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   Todo  necessita de ser atrelado à uma categoria para ser registrado com sucesso. Nesta documentação, você encontrará todo o entendimento necessário para utilizar e regrar seus  por meio das categorias destes.

# Introdução:

---

   Os Cubos.Net, assim como a maior parte dos recursos do RM, estão sujeitos as permissões determinadas por . Porém, diferente de outros recursos, os cubos também possuem uma camada adicional de segurança. As Categorias de Cubo, que trabalham em conjunto com os perfis para regrar o acesso de diferentes perfis aos cubos.

Lembre-se de que para gerenciar as Categorias de Cubos, é necessário possuir as devidas permissões no perfil que se está usando o sistema:

Para mais informações, acesse .

# Como funciona:

---

   As Categorias de Cubo funcionam modulando o acesso por perfis. Dessa forma, é possível determinar que diferentes perfis tenham acesso à diferentes tipos de funções dentro de uma mesma categoria.

Um exemplo

Possuo a categoria "RH" e dentro desta, determino um perfil chamado "Supervisor", que pode criar e editar Cubos enquanto também, na mesma categoria "RH", determino um perfil chamado "Usuário", que pode apenas, além de visualizar, exportar e atualizar Cubos.

# Inserindo/Editando uma Categoria:

---

Primeiramente, iremos acessar a área de Categorias de Cubos. Para fazer isso, acessamos: **Inteligência de Negócios → Gestão Estratégica → Cubos → Categoria**

Neste documento, iremos demonstrar o processo de inserção de uma nova categoria, porém a edição de categorias segue a mesma regra.

No cadastro de categorias, temos duas abas, uma com os dados cadastrais (Título, Descrição e conexão com banco de dados externo).

   E outra com as informações dos perfis autorizados. É nessa aba que a configuração complementar das permissões dos cubos é realizada.

   Ao incluir um novo registro em **Perfis Autorizados**, devemos selecionar um perfil para receber a configuração e quais as ações permitidas a ele naquela categoria.

   Após selecionar as permissões desejadas, na visão de cubos será possível selecionar a categoria cadastrada para um cubo.

Quando um cubo é associado a uma categoria, ele herda todas as permissões definidas na categoria.

falsefalse

**Produto:**

false

**Versão:** 12.1.XX

false

**Processo:** Categoria de Cubos

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
