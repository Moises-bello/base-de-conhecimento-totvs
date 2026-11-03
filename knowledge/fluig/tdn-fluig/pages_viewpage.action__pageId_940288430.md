---
content_hash: a0d93e0fc007c44ee6006cd553187793741f575d3f5ed4529358af890fb72983
fetched_at: '2026-06-28T21:35:31.484199+00:00'
page_id: '940288430'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar autenticação utilizando LDAP da atualização 1.6 até 1.8.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=940288430
version: 7
---

Fique atento!

Esta página é válida para as atualizações **1.6 até 1.8.2**do TOTVS Fluig.

Se você utiliza a atualização **Voyager (2.0) ou superior**, acesse a página original .

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é orientar o administrador sobre como configurar a plataforma para permitir acesso dos usuários através das credenciais existentes em um diretório, como o Active Directory, via protocolo LDAP (*Lightweight Directory Access Protocol*).

Uma vez realizada a configuração, os usuários deverão informar os dados de acesso do LDAP (usuário/senha) na tela de login para obter acesso à plataforma.

# Configuração

---

**1.** Edite o arquivo **domain.xml** localizado na pasta [diretório\_instalação]\appserver\domain\configuration.

**2.** Localize e substitua o trecho abaixo:

xmldomain.xml






]]>

**3.** Informe os dados de acesso à fonte de dados LDAP, conforme o tipo de validação utilizado em seu Active Diretory:

falseldaptrueCom credencial encriptada

* Caso seja utilizado o LDAP com necessidade de credencial, deve-se possuir as credenciais de um usuário válido e com permissão de consulta no diretório LDAP (Active Directory).
* Os dados de acesso devem ser informados nas propriedades java.naming,security.principal (login) e bindCredential (senha encriptada - veja abaixo como gerar a senha encriptada), após substituir pelo trecho abaixo.

xmlEclipsedomain.xml







 
  








 ]]>Importante!

O TOTVS Fluig precisa estar atualizado com os pacotes [1.8.1-230718](https://tdn.totvs.com/x/VohjLQ), [1.8.0-230718](https://tdn.totvs.com/x/3QR2KQ) ou superior para o funcionamento da senha criptografada.

**Utilização do LDAPS**

---

Se for utilizado o LDAPS – que é uma extensão do protocolo LDAP – é necessário ajustar os parâmetros **java.naming.provider.url** para **ldaps** com a porta **SSL** e o **java.naming.security.protocol** para o valor **ssl**, conforme o exemplo abaixo:

xmlEclipsedomain.xml




  

   
 
  








 ]]>Importante!

Pode ser que seja necessário importar para o Cacerts o certificado utilizado no LDAPS.

**Encriptação da senha LDAP**

---

Nessa etapa, a senha LDAP é encriptada usando o método principal da classe **SecureIdentityLoginModule**, passando como parâmetro a senha em texto plano do LDAP utilizado. Para fazer a configuração, siga os passos abaixo:

falseEncriptaçãotrue01Passo 01

Navegue até a pasta raiz de instalação, e acesse a pasta **appserver.**

**Linux**              ==> /opt/fluig/appserver

**Windows**        ==> c:\fluig\appserver

02Passo 02

Gere a senha encriptada.

LinuxWindowsImportante!

Neste caso **senha#do#LDAP@123!**, será a senha de acesso ao LDAP, e o resultado será:

**Encoded password: -73d03118655333edd11db66184fee4f35a6d08d87b9a0393**

Com credencial

* Caso seja utilizado o LDAP com necessidade de credencial, deve-se possuir as credenciais de um usuário válido e com permissão de consulta no diretório LDAP (Active Directory).
* Os dados de acesso devem ser informados nas propriedades java.naming,security.principal (login) e java.naming,security.credentials (senha), após substituir pelo trecho abaixo.

xmlEclipsedomain.xml







 









 ]]>Sem credencial

* Caso seja utilizado a forma de validação direta, sem necessidade credencial, substitua pelo trecho abaixo:

xmlEclipsedomain.xml














]]>Dica!

Caso opte por utilizar o login combinado, ou seja, deseja permitir tanto o acesso através do login/senha do Active Directory quanto da plataforma, **altere o valor da propriedade** ***loginCombinedWithDatabase para "true"**.* Assim o usuário poderá utilizar ambos os tipos de credenciais para autenticar-se na plataforma.

## Autenticação do usuário wcmadmin após a configuração de autenticação LDAP

---

No arquivo **domain.xml**, quando configurada a autenticação via LDAP é informado o parâmetro:

]]>

Quando definido como *false*, este parâmetro indica que o login funciona apenas com a senha do *Active Directory* e não funcionará com a senha que há na base. Como o **wcmadmin** é um usuário apenas da plataforma, ele não existe no AD.

Há duas formas para corrigir a situação:

1. Criar um usuário com o campo login do AD igual a 'wcmadmin' e senha de sua preferência, assim a plataforma irá logar o usuário wcmadmin igual aos demais usuários, através do AD.

2. Alterar o parâmetro *"loginCombinedWithDatabase"* no arquivo **domain.xml** (que fica no diretório **<Diretório de instalação>\appserver\domain\configuration**) para '*true*'. Com isso, a plataforma irá permitir o login tanto com a senha da base de dados quanto com a senha do AD. Nesse caso o usuário wcmadmin irá se logar com a senha da base de dados normalmente. Demais usuários que tentarem se logar com a senha da base de dados também conseguirão.

## Cadastro dos usuários

---

Para que o usuário consiga acessar a plataforma utilizando LDAP, seu login deverá ser criado na plataforma utilizando o padrão do Active Directory (AD) configurado. Por exemplo, considere o login e e-mail abaixo:

* Login: nome.sobrenome

* E-mail: [nome.sobrenome@suaempresa.com](mailto:nome.sobrenome@fluig.com)

O login e e-mail do usuário no AD deverão ser **iguais** ao login e e-mail deste usuário cadastrados na plataforma. Não há necessidade da senha do usuário na plataforma ser igual à cadastrada no AD.

# Propriedades de Busca LDAP

---

O módulo de login LDAP passa as propriedades para definir a busca por um determinado usuário e seus papéis para o servidor LDAP.

#### Definindo pesquisa por papel *(Defining Role Search)*

Propriedade rolesCtxDN: utiliza a configuração de pesquisa de função semelhante às configurações do *LdapExtLoginModule*, entretanto a recursão usada encontra os papéis listados dentro de um DN. Para tanto ele usa o DN fixo do contexto de pesquisa para papéis de usuário. Considere que este não é o nome distinto de onde os papéis são reais, em vez disso, este é o DN de onde os objetos que contêm os papéis de usuário (por exemplo, para o diretório *active*, este é o DN onde a conta de usuário está).

#### Definindo pesquisa DN *(Defining DN Search)*

Propriedade baseCtxDN: define o DN fixo do contexto de pesquisa para papéis de usuário. Considere que este não é o nome distinto de onde os papéis reais estão localizados, mas o DN dos objetos que contêm a localização dos papéis de usuário (isto é, para o diretório ativo, este é o DN com a conta de usuário).

Dica!

Para mais informações sobre as propriedades rolesCtxDN e baseCtxDN clique [aqui](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/5/html/Negotiation_User_Guide/appendix-advancedldap.html) ou confira um exemplo de uso [aqui](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/5/html/Negotiation_User_Guide/apas02.html).
