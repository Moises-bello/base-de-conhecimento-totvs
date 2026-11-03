---
content_hash: f8926d3069595f5571216b6181561facd01cfee532324aae299ebddf5cef413d
fetched_at: '2026-06-29T00:10:35.442386+00:00'
page_id: '528915055'
product: rm
source: tdn-rm
title: Inclusão de usuário supervisor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528915055
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Como adicionar usuário supervisor em coligadas/módulos que ainda não existem usuários supervisor.

## **02. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse: Serviços Globais | Administração | Coligadas

2) Selecione as coligadas que deseja adicionar o usuário supervisor nos módulos que ainda não possui nenhum usuário supervisor.

3) Após selecionar as coligadas clique em processos e logo após Incluir usuário supervisor nos módulos.

Após clicar no processo serão adicionadas as permissões de supervisor para os módulos que não existirem usuário supervisor, as permissões serão atribuídas para o usuário logado.

Atenção

O processo de "**Incluir usuários supervisor nos módulos**" será exibido somente para os usuários que forem supervisor no módulo **Serviços Globais**.

Após executar o processo é **necessário atribuir os perfis ao usuário, pois o processo não atribui os perfis ao usuário.**

Se o **CRC** da Coligada estiver **inválido** não será adicionado o usuário supervisor. O erro poderá ser visto no **trace** da aplicação..
