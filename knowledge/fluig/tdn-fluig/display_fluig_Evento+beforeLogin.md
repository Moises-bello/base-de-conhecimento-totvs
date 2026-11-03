---
content_hash: ad19f6a28fe85f4e50f8128828776b739a8dc21361e2a2fbb344de48161acbce
fetched_at: '2026-06-28T21:35:17.066027+00:00'
page_id: '1022378002'
product: fluig
source: tdn-fluig
title: Evento beforeLogin
type: documentation
url: https://tdn.totvs.com/display/fluig/Evento+beforeLogin
version: 3
---

---

O evento **beforeLogin** é um evento global do Fluig executado **após** as validações de senha e de bloqueio do usuário e **antes** da conclusão do login. Ele pode ser utilizado tanto para monitoramento quanto para bloquear o login de um usuário em determinadas situações.

Atenção!

O uso indevido do evento **beforeLogin** pode causar inconsistências no processo de login da plataforma, impedindo que usuários consigam acessar o sistema.

Em casos mais críticos, até mesmo o **usuário administrador** pode ser bloqueado, o que impossibilita a atualização ou correção do próprio evento beforeLogin. Nessas situações, torna-se necessária uma **intervenção direta no banco de dados** para resolver o problema.

# Sintaxe

---

A seguir é apresentada a sintaxe básica do evento **beforeLogin**. Esse evento deve ser implementado por meio de uma função chamada **beforeLogin**, que é executada automaticamente durante o processo de autenticação do usuário. Dentro dessa função, é possível realizar validações adicionais ou aplicar regras personalizadas e, se necessário, bloquear o login lançando uma **Exception** com a mensagem que será exibida ao usuário.

js

# Parâmetros

---

**login**

* Uma string com o login do usuário que está tentando fazer o login

**origin**

* Uma string contendo o valor do atributo "com.totvs.technology.security.protocol" da requisição. O valor padrão para tentativas de login via web é **null**.

**requestInfoVO**

* Um objeto do tipo  contendo os dados  da requisição de login.

## Confira abaixo alguns exemplos

---

#### **Consultando um serviço cadastrado no Fluig para verificar se há um bloqueio**

jstrue

#### **Obrigando que o IP de requisição seja de uma faixa específica**

jstrue

## Compatibilidade

---

O parâmetro **requestInfoVO** foi implementado na versão **2.0.0-260224**.
