---
content_hash: 9cf92b7e8123aed24ade742d368f33147b5c70ad1f97dc882579787d1c312a8e
fetched_at: '2026-06-28T21:35:29.980955+00:00'
page_id: '782310484'
product: fluig
source: tdn-fluig
title: UserVO
type: documentation
url: https://tdn.totvs.com/display/fluig/UserVO
version: 6
---

Este objeto é o objeto retornado ao acessar as variáveis  e  e compõe outros objetos como [MovementResultVO](https://tdn.totvs.com/display/fluig/MovementResultVO).

# Descrição

Este objeto possui alguns dados do usuário como matrícula, nome, email e login. Pode ser usado para preencher formulários ou mesmo integrações usando a matrícula do usuário.

# Atributos da instância

**long id**

O código único do usuário no Fluig

**String userCode**

Retorna uma string com a matrícula do usuário.

**String firstName**

Retorna uma string com o primeiro nome do usuário.

**String lastName**

Retorna uma string com o sobrenome do usuário.

**String fullName**

Retorna uma string com o nome completo ("Nome de Exibição") do usuário.

**String email**

Retorna uma string com o e-mail do usuário.

**String login**

Retorna uma string com o login do usuário.

Exemplos de uso

## Imprimindo os dados do usuário atual no log

jstrue

## Imprimindo os dados do usuário no log

jstrue 0) {
    console.log("Não foi possível identificar apenas um usuário apto a receber a atividade. Estes são os usuários possíveis:");
    for (var i = 0; i < users.length; i++) {
        console.log(users[i].fullName + "(" + users[i].userCode + ")"); // para cada usuário da lista, imprime: Nome Completo Do Usuário (matricula)
    }
}]]>
