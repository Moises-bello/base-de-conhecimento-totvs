---
content_hash: e7db2d3a71483f41d99b4107e68788ac9f2ff21ab4983ac4a8d9f213354c2803
fetched_at: '2026-06-29T00:12:14.593368+00:00'
page_id: '968134884'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Cadastros > Cadastro de Estoque > Classificação Produto
  / Categoria Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=968134884
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Campos da tela**
3. ### Regras de Negócio

   Visão Geral

   ## **01. VISÃO GERAL**

   A funcionalidade de **Cadastro de Categoria de Produto** permite ao usuário criar, editar, desativar e visualizar categorias que classificam os produtos do sistema.

   Esta tela é essencial para a organização e correta categorização de medicamentos, materiais, órteses, entre outros itens utilizados na instituição.

   ## **02. CAMPOS DA TELA**

   * **Descrição**  
     Campo de texto livre para informar o nome da categoria.  
     **Limite:** até 100 caracteres.
   * **Tipo de Item**  
     Seleção do tipo de item ao qual a categoria pertence. Exemplos incluem:

     + Medicamento
     + Material
     + Órtese
     + Outros tipos definidos pelo sistema.
   * **Situação (Ativo/Inativo)**  
     Indica se a categoria está disponível para uso ou foi desativada.

   ## **03. REGRAS DE NEGÓCIO**

   1. **Unicidade de Categoria**  
      Não é permitido cadastrar uma nova categoria com a **mesma descrição** e **mesmo tipo de item** de uma já existente no sistema.
   2. **Validação de Descrição**  
      A descrição deve conter no **máximo 100 caracteres**. O sistema não permitirá o salvamento caso este limite seja excedido.
   3. **Vínculo com Produtos**

      * Categorias **com vínculo a produtos** não podem ser excluídas.
      * Nestes casos, é permitido apenas **desativar** a categoria, garantindo a integridade dos dados relacionados.
   4. **Exclusão de Categoria**

      * Só é possível excluir categorias **sem vínculo com nenhum produto**.
      * O sistema deve apresentar uma mensagem informativa caso o usuário tente excluir uma categoria vinculada.
