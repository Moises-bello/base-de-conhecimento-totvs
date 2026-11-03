---
content_hash: ed6e7a2369e2d3221b2be2263262bc914e12eecc81f2342e13fc2c7e3ab2bdc0
fetched_at: '2026-06-29T00:08:24.541559+00:00'
page_id: '270897965'
product: rm
source: tdn-rm
title: Gerenciar permissões no cadastro de usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270897965
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Ao cadastrar ou editar um usuário qualquer, nota-se que existe a opção de tornar este usuário supervisor, isto é, dar acesso a algumas opções que os demais usuários não tem. Para que isso ocorra, é necessário estar logado no sistema com um usuário que já esteja na condição de supervisor na coligada que deseja alterar, para assim, fazer as mudanças desejadas.

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Para saber quais usuários tem a condição de supervisor, basta fazer uma consulta SQL na tabela **GPERMIS,**onde mostre a coligada e o módulo desejados.

sendo 0 para quem não é supervisor e 1 para quem tem a condição.

* Essa consulta também pode ser feita dentro do sistema.

**Acesse:** Gestão | Visões de Dados

Inclui uma nova consulta possuindo o Código a escolha.

salve e depois clique em executar para ver a pesquisa.

* Para identificar qual é a aplicação (codsistema), consulte a tabela GSISTEMA (select \* from gsistema).

2. Para gerenciar as permissões de usuários, siga as orientações abaixo:

**Acesse:** Serviços Globais | Segurança | Usuários

selecione um sistema no qual deseja editar/criar o usuário.

Na aba de segurança, pode-se selecionar a coligada que o usuário terá acesso, se será supervisor ou não e a qual perfil estará atrelado.

As configurações mudam de acordo com o  sistema, esteja atento se está realmente alterando no sistema desejado.

DICAPara documentação sobre configuração de Perfil, **[clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=270898183).**
