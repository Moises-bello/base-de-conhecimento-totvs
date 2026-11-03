---
content_hash: e429e86a009b396d09d13ff88685799683ff66bef78696262612cf78d94fb9db
fetched_at: '2026-06-29T00:08:24.584021+00:00'
page_id: '270898183'
product: rm
source: tdn-rm
title: Configuração de Perfil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270898183
version: 10
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é instruir o usuário sobre a correta configuração do perfil, utilizando a nova metodologia que permite alteração apenas pelo contexto de cada aplicativo.

# Introdução

---

       Para que o usuário consiga gerenciar os Perfis, é necessário logar no aplicativo e coligada em questão com um usuário supervisor.

       Os usuários que são Supervisor nos aplicativos tem como diferencial o acesso autorizado em algumas opções de menu/configuração que demais usuários não possuem. Dessa forma, somente usuários na condição de supervisor tem acesso completo ao cadastro de usuários.

       Consulte a tabela **GPERMIS**, para identificar quais usuários são supervisores no aplicativo em questão, conforme exemplo abaixo:

       O usuário pode ser Supervisor para apenas alguns módulos do RM. Para identificar em qual módulo o usuário é Supervisor, localize o CODSISTEMA(aplicativo), consultando a tabela**GSISTEMA:**

DICAPara facilitar a edição de perfis, recomendamos que sempre tenha um usuário Supervisor e com Permissão total em todos os Sistema/Coligadas.

# Configurando Perfis

---

       Para configurar Perfis, siga os passos abaixo.

falsePasso a Passo1º Passo

Logue na MDI (RM.exe, localizado em C:\totvs\CorporeRM\RM.Net) e Selecione o Menu iniciar – Serviços Globais:

2º Passo

Em seguida, acesse a aba Segurança > Perfis:

3º Passo

Selecione o Sistema relacionado aos perfis que devem ser alterados:

4º Passo

Selecione o Perfil que deseja editar e clique em  (editar) ou crie um novo clicando em  (Novo):

5º Passo

Gerencie as permissões de Acesso a Campos, conforme desejado:

O acesso a tabelas/campos possui configuração de permissão para consultar e alterar. Por default todos os campos possuem as duas permissões. Para alterá-las basta marcar/desmarcar os campos do agrupamento 'Permissões'.

Para visualizar apenas os campos que possuem restrições de consulta ou de alteração, clique na aba 'Restrições':

6º Passo

Gerencie as permissões de Acesso a Menus, conforme desejado:

DICA

Para informações sobre a configuração de permissão de usuários, [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=270897965).

Para informações sobre 'Acesso a Relatórios e Planilhas', .

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Configurações de Perfil

falsefalse

**Status:** Finalizado

false

**Data:** 30/01/2017

false

**Autores:**

**Douglas Maxwell de Oliveira**
