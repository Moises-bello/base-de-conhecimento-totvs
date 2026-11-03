---
content_hash: bf4534e1fd5910ba69330578200609da7f93e21990ea236f77d5fafc6042607d
fetched_at: '2026-06-29T00:09:08.577555+00:00'
page_id: '389555098'
product: rm
source: tdn-rm
title: Guia do Login OAuth
type: documentation
url: https://tdn.totvs.com/display/LRM/Guia+do+Login+OAuth
version: 34
---

# Índice:

---

.\*ndice:

# Objetivo

---

O objetivo deste documento é mostrar a funcionalidade do Oauth nas telas de login do Windows, Web e Portal Educacional, disponibilizada a partir da versão 12.1.22 do RM.

       Para que o usuário consiga acesso no RM através do login OAuth é necessário a criação do aplicativo que será utilizado pelo usuário, tais como Google, Facebook ou APIs terceiras e também a criação de um usuário, definindo em sua inclusão o e-mail o qual será utilizado para redirecionamento. Para mais detalhes da criação de um aplicativo acesse as documentações abaixo:

* [Criação do aplicativo do WsO2](http://tdn.totvs.com/x/VRVlFw)  
  Veja mais sobre a

       A criação do aplicativo é necessária, pois, é através dela que são geradas as chaves "Publica" e "Privada", que serão utilizadas no cadastro de um Aplicativo Externo pela nova MDI. Para mais detalhes da criação de um aplicativo externo, acesse a documentação "[Aplicativos Externos](http://tdn.totvs.com/x/WwE4Fw)".

TLS

Seguindo os padrões de segurança determinados na [RFC8705](https://datatracker.ietf.org/doc/html/rfc8705), o RM trabalha suas integrações **OAuth** utilizando TLS 1.2. Dessa forma, é recomendado que os endpoints referentes à integração estejam neste formato, para priorizar a segurança das integrações.

# Exemplos das Telas de Logins

---

Aviso

A partir da versão **12.1.32**, caso não exista nenhum Alias válido registrado (Ou o arquivo *Alias.dat* não exista), os botões de login OAuth não aparecerão no portal.

Para utilizar os aplicativos do "Facebook" e "WsO2", é necessário que o RMPortal esteja configurado em "https".

Configuração disponível na documentação: [Gerando Certificado SSL](http://tdn.totvs.com/display/public/LRM/Gerando+Certificado+SSL)

Tela de Login do Educacional

# Vínculo com o Usuário da Linha RM

---

       A vinculação ou descoberta do usuário local pelo Login Externo é feita de maneira padrão pelo e-mail do Cadastro de Usuários. Entretanto pode ser feita uma configuração no cadastro de Aplicativos Externos a fim de optar pela vinculação através do Código do Usuário (codusuario) e UserId (Id do usuário no provedor externo).

**Na MDI, Portal RM e FrameHTML:**

Ao fazer o login por algum provedor externo de login é validado se o e-mail do usuário no RM é o mesmo do e-mail utilizado como login no provedor.  
Ex.: Se o seu e-mail de login no facebook é [teste@gmail.com](mailto:teste@gmail.com), o e-mail cadastrado no seu usuário do RM deve ser [teste@gmail.com](mailto:teste@gmail.com). Caso contrário não será possível fazer login nos sistemas.

Caso exista mais de um usuário com o mesmo e-mail no RM, o sistema não fará o match entre os usuários na tela de login, impossibilitando o uso do provider externo para esse e-mail até que ele não esteja mais duplicado na base.  
Ex.:  
Usuário1 - E-mail: [teste@gmail.com](mailto:teste@gmail.com)  
Usuário2 - E-mail: [teste@gmail.com](mailto:teste@gmail.com)

Foi implementado o controle de alteração (CRC) no campo e-mail do cadastro de usuário. Caso o e-mail do usuário seja alterado diretamente na base de dados, o login será bloqueado para o CodUsuário que sofreu Update. Por isso, é importante que o cadastro de e-mail seja atualizado apenas pelos sistemas TOTVS que possuem tal funcionalidade ou DataServer.

O vínculo dos usuários é armazenado na tabela GUSUARIOOAUTHLOGINS.

Quando o vínculo é removido: Sempre que o e-mail de um usuário for alterado, se existir vínculo na tabela GUSUARIOOAUTHLOGINS para esse CodUsuario; Ou se existir algum outro usuário na tabela de vínculo que já utilize o novo e-mail salvo.

**Associação pelo Portal do Aluno**

O vínculo feito pelo Portal do Aluno segue a mesma regra explicada anteriormente, contudo possui uma possibilidade a mais.

Caso exista o mesmo e-mail cadastrado para mais de um usuário ou não exista nenhum usuário com o e-mail usado para login no provedor, após clicar no aplicativo para login na tela inicial será aberta uma janela para informar o usuário e senha do RM, onde deve ser feito o vínculo.

Se isso ocorrer, o usuário conseguirá logar pela MDI, Portal RM, FrameHTML e Portal do Aluno com o aplicativo do provider, mesmo com e-mails repetidos ou inexistentes no cadastro de usuário, pois o vínculo já foi feito pelo Portal do Aluno.

Porém, a regra para exclusão do vínculo na tabela GUSUARIOOAUTHLOGINS se mantém a mesma informada anteriormente. Lembrando que se a exclusão ocorrer, pela MDI, Portal RM e FrameHTML é possível criar o match pelo e-mail ou código do usuário.

Sempre que a exclusão ocorrer por motivo de edição de e-mail de usuário, ao logar novamente nas ferramentas será criado automaticamente um novo registro de a associação pelo e-mail ou código do usuário.

       Veja no documento  como visualizar a correspondência entre usuários.

# Carregamento Automático (AutoLoad)

---

      Foi implementada uma configuração de carregamento automático em Parâmetros Globais (Aba Gerais), onde o usuário define com qual dos seus aplicativos de Login Externo será apresentada a tela de login na inicialização do RM.

Quando ativada esta opção, a tela de login externo do provedor selecionada será apresentada, no lugar da tela principal de login do RM.  
Não é possível configurar mais de um Login ao mesmo tempo, como por exemplo:

* Login Unificado
* Login SAML
* Login Externo

Só é possível utilizar uma integração por vez.

Observações:

* Quando utilizado o portal com dois alias cadastrados, não é aconselhável utilizar esta opção, pois não será possível que o usuário faça a troca do alias, uma vez que o sistema será sempre reiniciado automaticamente.
* Não é possível apagar e nem desativar um provedor externo, que esteja selecionado e com esta opção habilitada.

---

O argumento /admin é um recurso para que o usuário volte a acessar o sistema através da tela de login (Usuário e Senha), uma vez que o parâmetro Carregamento Automático estiver ativo.

A configuração do /admin deve ser feita nas propriedades do aplicativo "RM.exe - Atalho", após a configuração a aplicação deve ser inicializada através do atalho.

Observações:

Para utilização de tal parâmetro, é necessário que o usuário seja supervisor do sistema.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.22 e superiores

false

**Processo:** Guia do Login OAuth

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**
