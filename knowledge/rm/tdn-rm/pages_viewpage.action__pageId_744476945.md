---
content_hash: c0ae2b81b17315332b2bcb90efd598c627407a36c81f623fd8768adce1c0b40a
fetched_at: '2026-06-29T00:11:32.090532+00:00'
page_id: '744476945'
product: rm
source: tdn-rm
title: 02 - Configurando os Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=744476945
version: 19
---

## **01.** **Configurando Parâmetros do Sistema**

Para realizar a parametrização para acessar o Login do Portal E-commerce, siga os passos: Em Processo Seletivo **>** Parâmetros **>**clique em Parâmetros do sistema.

Aba "Portal E-commerce".

**Tipo de informação para realizar o login:**

Tipo de informação que o usuário poderá utilizar para realizar o login no portal.

**Operador do critério de busca para validar existência de usuário:**

Indica qual é operador que será utilizado para consultar a existência usuário ao realizar o login.

**Informações para o envio de e-mail:**

Para que o e-mail de 'Solicitação de Troca de Senha' seja enviado com sucesso, é imprescindível o preenchimento dos campos 'Nome do Remetente' e 'E-mail do Remetente'

Exemplo

CPF informado: **059.840.988-19** e e-mail: **[totvs@totvs.com.br](mailto:totvs@totvs.com.br)**

**Cenário 1**

Considerando que o tipo de informação marcado foi "**CPF**" e "**E-mail**" e o operador selecionado for "**E**", ao realizar a procura do usuário o sistema vai considerar a seguinte regra:

CPF = '**059.840.988-19**' AND EMAIL = '**totvs@totvs.com.br**', ou seja, para identificar o usuário no banco de dados o sistema vai considerar que dois campos têm de ser iguais ao dado informado.

**Cenário 2**

Considerando que o tipo de informação marcado foi "**CPF**" e "**E-mail**" e o operador selecionado for "**OU**", ao realizar a procura do usuário o sistema vai considerar a seguinte regra:

CPF = '**059.840.988-19**' OR EMAIL = '**[totvs@totvs.com.br](mailto:totvs@totvs.com.br)**', ou seja, para identificar o usuário no banco de dados o sistema vai considerar que um pelo menos um dos campos seja igual ao dado informado.

**Habilitar login integrado para usuários do portal do aluno/RM  com aproveitamento de pessoa**

Indica que o login do portal do e-commerce será integrado com o cadastro de usuário do RM, isso possibilita que um aluno, professor ou outro tipo de usuário do RM possa autenticar no portal do e-commerce informando o mesmo usuário do RM.

Regras de autenticação

**Regra 1:** Quando a autenticação for com usuário do **RM** e o usuário possuir vínculo com **o cadastro de Pessoa,** e a pessoa possuir vínculo com o cadastro de **usuário do TOTVS Processo Seletivo,** então segue com a autenticação normal baseado no usuário do **RM**.

**Regra 2:** Quando a autenticação for com usuário do **RM**e o usuário possuir vínculo com **o cadastro de Pessoa,** e a pessoa **NÃO** possuir vínculo com o cadastro de **usuário do TOTVS Processo Seletivo****,** então será aplicado o aproveitamento de pessoa utilizando o critério de unicidade por CPF (para estrangeiro será considerado a nacionalidade e registro geral).

O aproveitamento de pessoa consiste em criar um novo cadastro de **usuário para o TOTVS Processo Seletivo** a partir do cadastro da pessoa vinculada ao usuário do **RM**

**Regra 2:** Quando a autenticação for com usuário do **RM**e o usuário **NÃO** possuir vínculo com **o cadastro de Pessoa,** e a pessoa **NÃO** possuir vínculo com o cadastro de **usuário do TOTVS Processo Seletivo****,** então será criado automaticamente um novo **usuário do TOTVS Processo Seletivo** levando em consideração apenas as informações básicas do cadastro de usuário do RM, tais como: nome, nome social, e-mail.

**Habilitar login integrado com o Facebook e Habilitar login integrado com o Google**

Habilita no portal a possibilidade de autenticar utilizando o Google ou Facebook.

Este parâmetro será habilitado somente se o RM estiver com os devidos provider configurado. Para maiores informações [clique aqui.](https://tdn.totvs.com/display/LRM/Login+OAuth)

**Informações para envio de e-mail:**

Informações padrão que serão consideradas no envio de e-mail realizado pelo portal do e-commerce

Envio de e-mail

Para que ocorra automaticamente o envio de e-mail confirmando o cadastro do usuário é necessário existir uma mensagem criada no caminho: **Educacional > Processo seletivo > Cadastro > Notificações > Mensagem de notificação** com objetivo de "**Enviar e-mail de confirmação do cadastro de novo usuário no Portal do e-commerce**"
