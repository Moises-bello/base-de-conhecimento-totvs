---
content_hash: 3af461c5d3ae173ad364cbc422883fa5491392ad76273aa5ee383940fb10f4da
fetched_at: '2026-06-29T00:09:11.317475+00:00'
page_id: '403746913'
product: rm
source: tdn-rm
title: Login após alteração de credencias do Banco de dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746913
version: 5
---

# Índice

---

# Objetivo

---

        Disponibilizar ao usuário mensagens claras para a correção de inconsistências quanto às credenciais de acesso à base dados, caso as conheça, ou no caso de um usuário comum, que deve avisar ao administrador do sistema para realizar as devidas alterações.

# Login após alteração de credenciais do Banco de Dados

---

        O sistema RM.exe disponibiliza via interface do login de usuário a possibilidade de trocar as credenciais de acesso do banco de dados (acesso às tabelas principais) quando a solução detectar que elas foram modificadas.

        Todas as vezes em que as credencias do banco de dados forem alteradas pelo administrador do cliente ou equipe de implantação é necessário que sejam feitas as devidas alterações na tabela GACESSO, a fim de repercutir na validação do login dos  usuários.

        Antes era necessário utilizar um programa chamado "RM Masterkey - nn.nn.exe" disponibilizado pela equipe de DBAs da Totvs para correção dessas alterações. Caso isso não fosse feito poderia impossibilitar que os usuários pudessem logar no sistema, gerando desconforto no uso do mesmo.

# Como funciona (caso conheça as credenciais)

---

        Tendo sido alteradas as credenciais de acesso à base de dados, por exemplo: a senha 'rm' para uma senha qualquer, ao tentar fazer login da próxima vez, será gerada uma mensagem ao usuário: " O usuário e senha do  usuário de acesso ao banco de dados não estão corretos. Você conhece as credenciais corretas para corrigir esta configuração ? ". Clique em SIM se conhecer as credenciais corretas.

         Será apresentada a tela "Configuração de Acesso" onde poderão ser informados usuário e senha, sendo que o Alias da base de dados estará não editável, neste momento.

        Informe as credenciais corretas (aquelas que foram alteradas no banco de dados). Clique em OK. Será informado ao usuário que as credenciais foram alteradas com sucesso.

# Como funciona (caso não conheça as credenciais)

---

       Tendo sido alteradas as credenciais de acesso à base de dados, por exemplo: a senha do usuário 'rm' para uma senha qualquer, ao tentar fazer login da próxima vez, será gerada uma mensagem: "O usuário e senha de acesso ao banco de dados não estão corretos".

       Caso seja um usuário comum e desconheça essas credenciais, clique em NÃO. Será informado: "Entre em contato com o administrador do banco de dados ou com seu suporte para correção destas credenciais."

       Ao clicar no botão OK, o sistema deve apresentar novamente a tela de login. Após os profissionais responsáveis terem feito a correção destas credenciais será possível realizar o login com sucesso.

false

**Observação:**

A funcionalidade é válida tanto para bancos de dados SQL Server quanto Oracle.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Login após alteração de credencias do Banco de dados

falsefalse

**Status:** Finalizado

false

**Data:** 30/11/2018

false

**Autores:**
