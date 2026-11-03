---
content_hash: 3752a1d8ffd4f8974399f8f46d05c92a7354716c646e16bc9359d631d827ecfe
fetched_at: '2026-06-29T00:11:22.169495+00:00'
page_id: '700486136'
product: rm
source: tdn-rm
title: 04. Portal do Fornecedor | Erros e Soluções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=700486136
version: 20
---

5%90%

Esta seção é reponsável por registrar o erros mapeados até o momento, as possíveis causas e soluções:

HTTP 403.14 Forbidden

Erro apresentado ao tentar testar conexão do IIS com o diretório de instalação.

**Solução**

Acessar o recurso **Pesquisa no Diretório** do website **FrameHTML** e **habilitar**.

Usuário e Senha inválidos!

Ao tentar logar no Portal com o usuário e senha recebido por email pelo fornecedor apresenta o erro abaixo:

**Causa 1:** **Ausência** do usuário **PORTALDOFORNECEDOR** no cadastro de usuário.

**Solução 1:** Realizar uma nova comunicação ao fornecedor, exportando para web, para que o usuário seja criado.

Mais informações:

**Causa 2:** Usuário **PORTALDOFORNECEDOR** foi criado manualmente

**Solução 2:** Excluir o usuário que foi criado manualmente, e realizar uma nova comunicação ao fornecedor, exportando para web, para que o usuário seja criado.

Mais informações:

**Causa 3:** Uso parametrização de **Logon Unificado**

**Solução 3:** Acessar o cadastro do usuário **PORTALDOFORNECEDOR** e na pasta rede informar um usuário de rede válido.

Mais informações:

Servidor não está respondendo

Ao tentar logar no Portal com o usuário e senha recebido por email pelo fornecedor apresenta o erro abaixo:

**Causa 1:** **Host** não foi iniciado como **Administrador**

**Solução 1:** Iniciar o Host como administrador

Mais informações:

**Causa 2:**  O arquivo config.json não está configurado apontando para o diretório de API correto.

**Solução 2:** Ajustar o arquivo config.json 

Mais informações:  

Erro ao consultar as cotações no servidor - Usuário logado não tem privilégios suficientes.

Ao tentar logar no Portal com o usuário e senha recebido por email pelo fornecedor apresenta o erro abaixo:

**Causa 1:** **Perfil** informadoão foi iniciado como **Administrador**

**Solução 1:** Ajustar os perfil informado nos parâmetros que foi usado na criação do usuário **PORTALDOFORNECEDOR**

Mais informações: [Usuário e autenticação](https://tdn.totvs.com/pages/viewpage.action?pageId=639955763#Configuracoes-Usuario_e_autenticacao)

Portal carrega a tela de login em branco

Esse incidente pode ocorrer devido à recursos não instalados nas configurações do IIS.

Para solucionar essa ocorrência, realize os seguintes passos:

       1. Siga a documentação descrita no link: .

       2. Marque também as opções destacadas abaixo.

 HTTP Error 500.19 - Internal Server Error

Erro apresentado ao carregar o Portal

**Solução**

Esse incidente pode ocorrer devido à recursos não instalados nas configurações do IIS.

Para solucionar essa ocorrência, realize os seguintes passos:

       1. Siga a documentação descrita no link: .

       2. Marque também as opções destacadas abaixo.

0solid

---

---

560px

 [Voltar para o Menu Principal](https://tdn.totvs.com/display/LRM/Portal+do+Fornecedor)

---

---

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
