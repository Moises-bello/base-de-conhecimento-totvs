---
content_hash: 803614e4bda8b340021916e049e9bc0392a571243bfa4e2b5dca9e001d9eb668
fetched_at: '2026-06-29T00:11:02.542541+00:00'
page_id: '61932106'
product: rm
source: tdn-rm
title: LDAP - Integração do RM com LDAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61932106
version: 107
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é demonstrar como integrar o sistema RM com o LDAP. Disponibilizamos a seguir o passo a passo da integração e uma vídeo aula com a explicação.

# Introdução

---

**LDAP**, Lightweight Directory Access Protocol, é um protocolo de manipulação de diretórios que roda por cima do protocolo de comunicação TCP/IP ou de uma outra conexão existente. Esse protocolo torna a forma de comunicação mais leve e segura, além de suportar um grande fluxo de informação. Buscando acompanhar essa tendência de mercado os produtos RM dispõem de integração com o LDAP.

          Atualmente a funcionalidade LDAP do RM é homologada para ser utilizado com o AD (Active Directory) e possui duas formas de ser integrada: **Integração LDAP** e **Logon LDAP.**

##### Diferenças entre **Integração LDAP** e **Logon LDAP**

Na ***Integração LDAP***, as inserções, edições e remoções feitas no RM serão replicadas no **Active Directory**, porém o usuário **NÃO** autenticará utilizando o LDAP (Autenticação utilizando credenciais de acesso do *Active Directory* só será possível caso a funcionalidade **Logon LDAP** esteja ativa) logo, caso a senha ou usuário deste seja alterado diretamente no *Active Directory*, essa alteração não será refletida no RM, que continuará a exigir as informações de autenticação anteriores.

Já no ***Logon LDAP,***o usuário deverá utilizar as informações de autenticação provenientes do **AD** (Active Directory) para autenticar no RM, porém as alterações realizadas no usuário dentro do RM **NÃO** serão replicadas no LDAP (Alterações realizadas no RM só serão replicadas no AD caso a ***Integração LDAP*** esteja ativa).

Assim sendo, caso queira apenas que os usuários autentiquem usando o AD, ative o **Logon LDAP**. Caso queira que as alterações do RM reflitam diretamente no AD, ative a **Integração LDAP**, e caso queira ambos, basta ativar as duas funcionalidades juntas!

# Integração LDAP

---

         Com o RM integrado ao LDAP, usuários cadastrados no RM serão automaticamente criados no sistema de diretórios com o mesmo login e senha do RM. Além da criação de usuários é possível alterar a senha ou deletar um usuário pelo RM e esta ação será replicada no sistema de diretórios.

**Configurando o RM para a Integração LDAP**

         É necessário configurar seu ambiente LDAP nos parâmetros do RM. Para isso, acesse o menu ***Ambiente > Parâmetros >***  ***Parâmetros Globais***. Em seguida, clique na aba ***Integração LDAP***.

 

**Nessa tela, preencha os campos de acordo com o seu ambiente LDAP:**

* **Ativa Integração Ldap:** Marque o para ativar a integração LDAP;
* **Caminho LDAP:** Insira o domínio que irá trabalhar com o protocolo LDAP. Não esqueça que para ter um domínio válido ele deve ser precedido do protocolo **LDAP://**;

  A porta poderá ser informado, adicionando :389 ou :636(SSL) (Para o protocolo padrão ou seguro)
* **Grupo LDAP:** Informe qual grupo de usuários o usuário que será inserido irá pertencer. Ex: User, DNS;
* **Habilitar LDAPS(SSL):**  Ativa ou desativa o comunicação usando protocolo seguro SSL.  
  A porta deverá ser informada, exemplo: LDAP://localhost**:636**
* **Permitir remoção de usuários:** marcando esse campo, ao excluir um usuário do RM, ele será excluído também do serviço de diretório;
* **Utiliza nome como chave:**marcando este campo, ao criar um novo usuário no RM ao envia-lo para o AD o CN(Common Name do Active Directory) do mesmo será o **nome do usuário.** Com a opção desmarcada será enviado para o AD o **CODUSUARIO**.
* **Usuário:** Informe o usuário que tem acesso ao sistema de diretórios;
* **Senha:** Informe a senha do usuário que tem acesso ao sistema de diretórios.

   

Depois de preencher os dados para a integração, clique no botão OK para salvar as alterações. Neste instante serão feitas validações do caminho LDAP, Grupo LDAP, Usuário e Senha. Em seguida será necessário fazer **Login/logout** no sistema para que as alterações tenham efeito.

Importante         Ao criar um novo usuário no RM e envia-lo para o AD, o campo CN(Common Name do Active Directory) só será preenchido caso o campo "Usuário de Rede" na aba Rede do cadastro de usuários esteja preenchido.Importante

         Para que as operações de cadastro, alteração e remoção do usuário no diretório do domínio funcionem corretamente, é necessário que o usuário cadastrado nos **Parâmetros globais**, tenha privilégios para as operações.

Atenção

A Opção **Utiliza nome como chave** está disponível a partir das versões 12.1.24.191, 12.1.25.124, 12.26.

Ao utilizar **nome como chave** o AD não aceita dois usuários com o mesmo CN(Common Name do Active Directory) então ao criar usuários que possuem nomes Homônimos  será apresentado erro ao envia-lo para o Active Directory

Lembre-se!

A funcionalidade **Integração LDAP,** apesar de incluir, editar e excluir usuários no AD conforme o mesmo comportamento seja feito no RM, ela não engloba juntamente o sistema de Login utilizando o **LDAP**, logo, para ativá-lo, é necessário ativar o **Logon LDAP** também.

Atenção

Disponível a partir da versão 12.1.2209 Patch(**116**) e 12.1.2302

A instalação do certificado e configurações necessárias no servidor LDAPS (SSL) não são de responsabilidade da TOTVS.

Para facilitar a configuração do ambiente, existem algumas ferramenta de terceiros:

* NetTool (<https://nettools.net/ldap-search/>)
* Ldp.exe (Habilitado pelo Server Manager do Windows)
* AdInsight (<https://download.sysinternals.com/files/AdInsight.zip>)

Para aplicações Delphi, ao utilizar os recursos do LDAP ou LDAPS, tem a possibilidade de gerar ocorrências não previstas, sendo assim não há garantia de funcionamento por falta de incompatibilidade com as novas atualizações do RM.

Informação

Caso as funcionalidades **Integração LDAP**, **Logon LDAP**, e **Utilizar usuário da rede** estejam simultaneamente ativas, ao alterar o **Usuário de rede**de um usuário, este tentará associar a um usuário já existente no LDAP. Caso tal usuário não seja encontrado no AD, é necessário também preencher o campo **Senha** no RM para que haja o cadastro do usuário no AD.

# Logon LDAP

---

Uma forma mais contida de integrar o RM ao LDAP é utilizando o Logon LDAP. Neste caso, apenas as funcionalidades de Login serão integradas, não havendo alteração ou criação de usuários no AD.

O Logon LDAP permite que os usuários cadastrados no RM que estejam cadastrados no sistema de diretórios tenham acesso aos produtos RM. Para isso, é necessário configurar nos ***Parâmetros Globais*** a opção de ***Logon Ldap***.

Acesse o menu ***Ambiente > Parâmetros > Parâmetros Globais****.* Em seguida, clique na aba ***Geral*** e marque a opção ***Ativa Logon LDAP***.

         Depois de marcar a opção Logon LDAP será possível preencher o campo Caminho LDAP. Insira o caminho LDAP do domínio que se deseja trabalhar com o LDAP. Em seguida, salve as configurações. Nesse momento o sistema fará  a validação do Caminho LDAP. .Não esqueça que o protocolo do LDAP é LDAP://.Após inserir as informações é necessário que se faça Login/logout no sistema para que as alterações tenham efeito.

Observação:

         Quando se marca o Logon LDAP, a opção de Logon Unificado fica automaticamente desabilitada e o mesmo ocorre quando se marca a opção de Logon Unificado. *Não há como trabalhar com as duas opções dentro do RM*.

Observação:

Se a integração for configurada para utilizar a comunicação segura LDAPS (SSL), o caminho deverá ser informado com a porta, exemplo: LDAP://localhost:636  
  
As regras de troca de senha do RM não serão válidas neste caso.   
Usuários com Logon LDAP e sem integração LDAP, não poderão troca a senha.

Caso seja marcada a flag *Ignorar Integração/Logon LDAP,* para este usuário passa a valer as regras do RM.

# Ignorar Integração/Logon LDAP

---

A partir da versão **12.1.20** a opção "*Ignorar **Autenticação** LDAP*" foi alterada para "*Ignorar **Integração/Logon** LDAP*" que, como o nome já diz, ignora a integração de um determinado usuário ao LDAP, ou seja, mesmo que a opção "**Logon LDAP** ou **Integração LDAP**" estejam configuradas, todas as operações que envolvem o **LDAP** serão ignoradas como: *Login , Criação, Edição e Exclusão de usuário.*

Após integrar o **Logon LDAP** ou a **Integração LDAP**, ao acessar a tela de edição/inserção de usuários, na aba Rede é possível ter acesso a esta tela:

Este campo, como o próprio nome já diz, é utilizado quando um usuário deve ser uma exceção à regra do LDAP, ou seja, não possui nenhuma integração com o LDAP. Caso seja marcado, os seguintes comportamentos não serão contemplados:

### Logon LDAP

O usuário marcado com esta opção utilizará o ***usuário e senha do RM para autenticar***, estando sujeito as regras do RM, tais quais complexidade e histórico de senhas por exemplo.

### Integração LDAP

O usuário determinado com esta opção não será atribuído à nenhum usuário do AD, ou seja, não será criado nenhum usuário referente ao seu acesso no AD e deverá utilizar o usuário e senha do RM para autenticar, tal qual o **Logon LDAP**

Informações

A partir dos últimos patches das versões 12.1.27, 12.1.28, 12.1.29 e release 12.1.31, as mensagens de erro durante o Login com LDAP foram unificadas com as mensagens do Login RM. Dessa forma, o texto de erro será padrão para os dois contextos.

**Ignorar Integração LDAP X Autenticação por usuário de Rede:**

A integração LDAP pode ser feita de duas formas: Com usuário do RM e com usuário de Rede.

Ao configurar um usuário para Ignorar a integração LDAP, nenhum processo deste usuário passará pelo Active Directory (AD), o login, por exemplo, será feito pelo RM; não haverá inclusão, edição ou exclusão de usuário no AD.

Entretanto, caso a configuração do Login, nos parâmetros globais, esteja configurada para utilizar o usuário de rede, será necessário que os dados da aba Rede, no cadastro do usuário, sejam preenchidos. Pois mesmo não havendo integração com LDAP para esse usuário específico, o login será feito pelo RM com os dados informados na aba Rede. Nesse caso, a senha de login será a senha cadastrada no RM.

Como Configurar o usuário de Rede para Login

**Como Configurar o Usuário de Rede para login:**

É possível escolher qual campo o sistema usará para verificar o login no RM: ***Usuário do RM*** ou ***Usuário de Rede***. Mas para isso, é preciso que pelo menos um usuário supervisor tenha cadastrado o usuário de rede na aba Rede do cadastro de Usuário. (Clique na imagem para ampliar)

**Utilizar usuário do RM:** Selecione esta opção para realizar o login no RM utilizando o código do usuário informado no cadastro do Usuário, como mostrado na imagem abaixo:

**Utilizar usuário da rede:** Selecione esta opção para realizar o login no RM utilizando o usuário de rede informado no cadastro do Usuário, na aba Rede. Como mostrado na imagem abaixo, onde alteramos o cadastro de rede do usuário mestre:

Observação

A configuração para integração LDAP não possibilita o login automático do usuário.

Leia mais sobre .

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Integração LDAP

false

**Subprocesso:** Parametrização do RM para integração com LDAP

falsefalse

**Status:** Finalizado

false

**Data:** 19/12/2016

false

**Autores:**

Scripts
