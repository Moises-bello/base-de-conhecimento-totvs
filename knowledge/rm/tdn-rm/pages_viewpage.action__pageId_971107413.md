---
content_hash: f81486b855136c25cccaf8638d82a2a8e6337a39cc8943db1badefdb470843d8
fetched_at: '2026-06-29T00:12:15.130527+00:00'
page_id: '971107413'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Cadastros > Cadastro de Estoque > Classificação Produto
  / Família Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971107413
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Campos da tela**
3. ### Regras de Negócio

   Visão Geral

   ## **01. VISÃO GERAL**

   A funcionalidade de **Cadastro de Família de Produto** permite ao usuário criar, editar, desativar e visualizar classes que classificam os produtos do sistema.

   Esta tela é essencial para a organização e correta classificação dos produtos

   ## **02. CAMPOS DA TELA**

   * **Descrição**  
     Campo de texto livre para informar o nome da família.  
     **Limite:** até 100 caracteres.
   * **Classe**  
     Selecione a classe previamente cadastrada no menu Classe Produto
   * **Situação (Ativo/Inativo)**  
     Indica se a família está disponível para uso ou foi desativada.

   ## **03. REGRAS DE NEGÓCIO**

   1. **Unicidade de Família**  
      Não é permitido cadastrar uma nova família com a **mesma descrição** e **mesma classe** de uma já existente no sistema.
   2. **Validação de Descrição**  
      A descrição deve conter no **máximo 100 caracteres**. O sistema não permitirá o salvamento caso este limite seja excedido.
   3. **Vínculo com Produtos**

      * Famílias **com vínculo a produtos** não podem ser excluídas.
      * Nestes casos, é permitido apenas **desativar** a família, garantindo a integridade dos dados relacionados.
   4. **Exclusão de Família**

      * Só é possível excluir família **sem vínculo com nenhum produto**.
      * O sistema deve apresentar uma mensagem informativa caso o usuário tente excluir uma família vinculada.
