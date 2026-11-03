---
content_hash: 5c2bb0a3df08a4788ef6d1d256cd8c403601efc3986dbf38a7ca708ead6c0e5c
fetched_at: '2026-06-29T00:08:52.513655+00:00'
page_id: '341217083'
product: rm
source: tdn-rm
title: 1718230 EDUCACIONAL01-3428 DT Validaçao de permissões na atualização de endereço
  no cadastro de aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341217083
version: 93
---

# CADASTRO DE ALUNO - VALIDAÇÃO DE PERMISSÕES NA ATUALIZAÇÃO DE ENDEREÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Cadastro de aluno* |
| **Situação/Requisito:** | O cadastro de aluno permite a atualização de dados de endereço de pessoas e cliente/fornecedor, mesmo o usuário não tendo permissão para tal operação. |
| **Solução/Implementação:** | Foi realizada uma alteração no botão de atualização de endereço para que o mesmo valide a permissão referente ao módulo de cadastro do responsável que será atualizado.  Para a habilitação do botão de atualização, no cadastro de aluno, o usuário precisa ter permissão para realizar alterações no cadastro de aluno, caso contrário o botão aparecerá desabilitado.  ***Educacional - [01] Currículo e Oferta - [01.01] Aluno e Professor - [01.01.01] Alunos - [01.01.01.05] Editar aluno***  A atualização de endereços permite que sejam atualizadas as informações dos responsáveis financeiro, acadêmico, pai, mãe e demais do cadastro de filiação.  Para que os devidos responsáveis sejam exibidos na tela de atualização, o perfil do usuário precisar ter permissão de alteração no módulo de cadastro do responsável.  Responsável financeiro:  ***Educacional - [11] Outras permissões - [11.01] Outros módulos - [11.01.02] Clientes e fornecedores - [11.01.02.03] Editar clientes e fornecedores***  Responsáveis acadêmico, pai, mãe e demais do cadastro de filiação:  ***Educacional - [11] Outras permissões - [11.01] Outros módulos - [11.01.01] Pessoas - [11.01.01.21] Alterar endereço principal*** |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
