---
content_hash: e788c31e6adbad5cfe013592cbc69c2a083dacd0316c922bce936c2106cae88e
fetched_at: '2026-06-29T00:11:04.493562+00:00'
page_id: '627734306'
product: rm
source: tdn-rm
title: Histórico de Senhas do Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627734306
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

**Disponível a partir da versão 12.1.33**

       Foi criado no RM a funcionalidade do **Histórico de Senha,** onde o sistema irá armazenar as últimas senhas utilizadas pelos usuários, validando para que o mesmo não utilize senhas que ja tenho cadastrado anteriormente.

       Para ativar essa funcionalidade, existe o parâmetro "**Quantidade das últimas senhas armazenadas para um usuário"**, onde é definido a quantidade de senhas que serão armazenadas no histórico (a quantidade máxima permitida no parâmetro é 10)

       Esse parâmetro tem por padrão o valor **0 (zero)**, representando que esta funcionalidade está **desativada**.

Delphi

**Esse funcionalidade não deve ser utilizada caso haja alguma aplicação Delphi sendo utilizada em paralelo à MDI!**

Caso o campo "**Quantidade das últimas senhas armazenadas para um usuário"** seja informado e houver alteração de senha do usuário, ao realizar login em alguma aplicação Delphi, poderá ser gerado mensagens do tipo:

## **02. EXEMPLO DE UTILIZAÇÃO**

       Para utilização da funcionalidade, é necessário alterar o parâmetro "**Quantidade das últimas senhas armazenadas para um usuário"** para um valor diferente de **0 (zero).**

       Ao alterar o valor do parâmetro para 3 (três), por exemplo, o sistema não permitirá que o usuário utilize as últimas três senhas cadastradas anteriormente (armazenada no histórico de senhas) ao cadastrar uma nova senha.

      Essa validação acontecerá em todos os pontos passiveis de realizar a troca de senha, como por exemplo:

* Cadastro de Usuário
* Tela de login (Alterar senha no próximo login, Esqueceu sua senha, etc)
* Troca de senha
* Portal RM

       Foi criado na tabela "**GUSUARIO**" o campo "**ULTIMASSENHAS**", onde está sendo armazenado esse histórico de senhas (informação criptografada).
