---
content_hash: eaec78aa096fd48e629c107ff601ba5135c34463fb7a6c6b9556cba858997ae0
fetched_at: '2026-06-29T00:09:53.627249+00:00'
page_id: '440846229'
product: rm
source: tdn-rm
title: 4467005 PORTALMOBILE01-6296 Solicitação de alteração de senha - Novo Portal
  do aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440846229
version: 1
---

# Solicitação de alteração de senha - Novo Portal do aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Gestão Educacional |
| **Módulo:** | Educacional |
| **Função:** | Solicitação de alteração de senha |
| **Situação/Requisito:** | Ao realizar a solicitação de alteração de senha, através do recurso "Esqueceu sua senha?", o usuário recebia um email no qual não era redirecionado para a tela que o usuário informa a nova senha.  Ao invés disso era redirecionado para a tela de login, solicitando usuário e senha, sem apresentar a possibilidade de alteração da senha.  Outra situação ocorria quando o usuário realizava o login com um usuário que estava parametrizado para alterar a senha após o login. Neste cenário o portal apresentava a tela solicitando nome de usuário, senha e a nova senha juntamente com a confirmação. Porém ao salvar, a senha não era alterada e o usuário não conseguia realizar o login. Este problema era causado quando a instituição possuía mais de um Alias cadastrado, e o login era realizado em um Alias no qual não era o que estava selecionado no momento da abertura do portal. |
| **Solução/Implementação:** | Foi ajustado o recurso de "Esqueceu sua senha?", possibilitando o usuário alterar a senha através do link enviado por email.  Juntamente, foi ajustado a conexão com o Alias correto quando o usuário possui a necessidade de alteração de senha no próximo login. Desta maneira, o portal consegue identificar o Alias selecionado pelo usuário no momento do Login. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
