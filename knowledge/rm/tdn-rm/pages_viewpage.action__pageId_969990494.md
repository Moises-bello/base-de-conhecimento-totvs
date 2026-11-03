---
content_hash: 3995e4bdc64187019ad93dabf8f4bde9efc2e81f03778e0de7826acff5fa5415
fetched_at: '2026-06-29T00:12:14.669074+00:00'
page_id: '969990494'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Cadastros > Cadastro de Estoque > Classificação Produto
  / Classe Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969990494
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Campos da tela**
3. ### Regras de Negócio

   Visão Geral

   ## **01. VISÃO GERAL**

   A funcionalidade de **Cadastro de Classe de Produto** permite ao usuário criar, editar, desativar e visualizar classes que classificam os produtos do sistema.

   Esta tela é essencial para a organização e correta classificação dos produtos

   ## **02. CAMPOS DA TELA**

   * **Descrição**  
     Campo de texto livre para informar o nome da classe.  
     **Limite:** até 100 caracteres.
   * **Categoria**  
     Selecione a categoria previamente cadastrada no menu Categoria Produto
   * **Situação (Ativo/Inativo)**  
     Indica se a categoria está disponível para uso ou foi desativada.

   ## **03. REGRAS DE NEGÓCIO**

   1. **Unicidade de Classe**  
      Não é permitido cadastrar uma nova classe com a **mesma descrição** e **mesma categoria** de uma já existente no sistema.
   2. **Validação de Descrição**  
      A descrição deve conter no **máximo 100 caracteres**. O sistema não permitirá o salvamento caso este limite seja excedido.
   3. **Vínculo com Produtos**

      * Classes **com vínculo a produtos** não podem ser excluídas.
      * Nestes casos, é permitido apenas **desativar** a classe, garantindo a integridade dos dados relacionados.
   4. **Exclusão de Classe**

      * Só é possível excluir classe **sem vínculo com nenhum produto**.
      * O sistema deve apresentar uma mensagem informativa caso o usuário tente excluir uma classe vinculada.
