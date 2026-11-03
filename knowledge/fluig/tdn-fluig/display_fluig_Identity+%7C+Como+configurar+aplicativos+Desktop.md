---
content_hash: 62bb491bca45f21e303a5d7afc7535e7cabc1b8a4415b56d0c4bba4a0fe34c3e
fetched_at: '2026-06-28T21:35:22.332251+00:00'
page_id: '235585056'
product: fluig
source: tdn-fluig
title: Identity | Como configurar aplicativos Desktop
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Como+configurar+aplicativos+Desktop
version: 67
---

# Falando de aplicativos Desktop...

---

A ferramenta Desktop Launcher é utilizada para abrir aplicativos que estão instalados em seu computador e que necessitem de credenciais para serem acessados. Mas para que isto ocorra é necessário realizar a configuração desses aplicativos utilizando a ferramenta **ThickSSOProfileGenerator**

# Download do ThickSSOProfileGenerator

O passo a passo para realizar o download dessa ferramenta pode ser consultado na documentação [Gerador de perfil para aplicações desktop](https://tdn.totvs.com/x/K5hvI).

 

# Configuração do aplicativo com o ThickSSOProfileGenerator

Logo ao abrir o programa aparecem duas opções para escolha de aplicativo para configuração:

**Win32 Application**

Essa configuração é voltada a aplicações 32 bits e que permitam a identificação dos campos por meio da utilização do arquivo User32.dll.

Esse arquivo contém os elementos gráficos, como caixas de dialogo e janelas do Windows, e é utilizado para identificar os campos do aplicativo que iremos preencher com as nossas credenciais. Para utilizar essa opção é imprescindível que o aplicativo seja 32 bits.

**NO-Win32 Application**

Essa configuração é utilizada em aplicativos que não são 32 bits.

Para que essa configuração funcione e consiga realizar o preenchimento das credenciais, ela foi programada para atuar da mesma forma que o teclado ou o mouse funcionariam, só que ao invés do preenchimento dos campos ser feito pelo usuário ele é realizado por meio da programação pré-definida que realizamos.

Observação

Como a programação dos aplicativos No-Win32 Application é feita para simular o teclado e o mouse, muitas vezes esse desenvolvimento pode se tornar complexo.

# Configuração de um aplicativo Win32

No nosso exemplo utilizaremos o Yahoo Messenger, que é uma aplicação de 32 bits.

0.5falsesamplesslidetrue1Passo 1  

* Abra o aplicativo Yahoo Messenger

2Passo 2  

* Insira o nome do aplicativo no campo "*Application Name*"

3Passo 3  

* Abra o Gerenciador de tarefas e verifique o nome da aplicação para preencher o campo "*Window Title Regex*

4Passo 4  

* Copie o nome do processo na aba Processos do Gerenciador de Tarefas do Windows. Note que uma aplicação pode ter diferentes nomes de processos em sistemas diferentes, por isso suportamos uma coleção de nomes de processos.

* No gerador de perfis, abaixo de *Window Process Name*, clique no botão *Add* para inserir o conteúdo.

5Passo 5  

* Clique na lista de seleção *Operation Type* e selecione a opção **SEL\_TEXT**

* Clique na lista de seleção *Content* e selecione a opção **username**

* Clique e arraste o botão de destino  no campo de ID do Yahoo Messenger. O campo Control ID será preenchido no gerador de perfil.

* No gerador de perfil, clique no botão *Add* para inserir o conteúdo

6Passo 6  

* Clique na lista de seleção *Operation Type* e selecione a opção **SEL\_TEXT**.

* Clique na lista de seleção *Content* e selecione a opção **password**.

* Clique e arraste o botão de destino no campo de senha do Yahoo Messenger. Será preenchido o campo Control ID no gerador de perfil.

* No gerador de perfil, clique no botão *Add* para inserir o conteúdo.

7Passo 7  

* Clique na lista de seleção Operation Type e selecione a opção **CLICK\_BUTTON**.

* Clique e arraste o botão de destino  no botão de acesso do Yahoo Messenger. Isto irá popular o campo Control ID no gerador de perfil.

* No gerador de perfil, clique no botão *Add*para inserir o conteúdo.

8Passo 8  

* No gerador de perfil, clique no botão *Generate*para criar o perfil do aplicativo Yahoo Messenger.

* Copie o código do perfil e cole-o nas configurações deste aplicativo *desktop* no Identity.

9Passo 9  

* Dentro do Identity, basta criar esse aplicativo como "ThickApplication" e inserir o valor gerado pela nossa configuração no campo SSO Profile.

* Após finalizar as configurações, basta salvar.

# Configuração de um aplicativo *Non* Win32

No nosso exemplo utilizaremos o Skype na versão 7.2.2.0.1.109.

O Skype possui dois tipos de acesso: por e-mail ou por usuário. No nosso exemplo nós iremos demonstrar como configurar o preenchimento das credenciais por e-mail.

Nós iremos efetuar uma programação que funcionará com essa configuração, mas em novas atualizações do Skype, pode ser que a forma de preenchimento das credenciais mude, sendo necessária uma nova configuração.

0.5falseSkypeslidetrue1Passo 1

* Abra o aplicativo Skype.

2Passo 2

* Preencha os campos "*Application Name*" , "*Window Title Regex*" e "*Window Process Name*"

3Passo 3

* Como o aplicativo já é aberto com o foco no campo "nome Skype", iremos somente adicionar o seu valor utilizando o campo "*InputContent*", preencher o campo "*Content*" com a opção "*username*" e clicar em Add.

* Esse comando preencherá o campo do Skype com o "*User Name*" configurado no Identity no lançamento das credenciais.

4Passo 4

* Após isso, deve ser preenchida a configuração com o comando "PRESS\_TAB" que equivale ao *Tab* do teclado.

5Passo 5

* Com isso o Skype irá carregar uma nova tela para login por e-mail. Porém, como isso leva um certo tempo, será necessário preencher o campo "*Timer*" com o tempo de 6 segundos.

Observação

A configuração do *Timer* pode variar, depende da velocidade de processamento do computador que irá acessar o Skype.

6Passo 6

* Na nova tela que será aberta, será necessário configurar três vezes o comando "PRESS\_TAB" para ir para o campo senha.

7Passo 7

* Em seguida, iremos apenas adicionar o seu valor utilizando o campo "InputContent", preencher no campo "*Content*" o com a opção "*password*" e clicar em *Add*.

8Passo 8

* Agora vamos implementar a configuração "PRESS\_ENTER" que equivale ao botão "*Enter*" para efetuar o *login* no Skype.

9Passo 9

* No gerador de perfil, clique no botão *Generate*para criar o perfil do aplicativo Yahoo Messenger.

* Copie o código do perfil e cole-o nas configurações deste aplicativo *desktop* no Identity.

10Passo 10

* Dentro do Identity, basta criar esse aplicativo como "ThickApplication" e inserir o valor gerado pela nossa configuração no campo SSO Profile.

* Após finalizar as configurações, clique em salvar.

# Teste de Configuração *Thick Application*

---

O Desktop Launcher possui uma opção para que possa ser testada a configuração gerada no ThickSSOProfileGenerator. Será demonstrado como realizar esse teste com o aplicativo Skype.

0.5falseTestDesktopLauncherslidetrue1Passo 1  

* Abra o aplicativo Desktop Launcher

2Passo 2  

* Se estiver autenticado, faça o *Logout*

3Passo 3

* Clique sobre a opção "*Test*"

4Passo 4  

* Preencha o campo "*UserName*" com o usuário que irá se logar na aplicação.

* Preencha o campo "*Password*" com a senha do usuário para logar na aplicação.

* Preencha o campo "*Profile*" com a configuração realizada do Skype.

* Marque a opção "*Auto Detect*".

5Passo 5  

* Para finalizar o teste, basta abrir o aplicativo Skype e será realizado o lançamento das credenciais no Skype

* Se der tudo certo, as configurações do Skype foram realizadas com sucesso. Basta preencher a configuração do aplicativo dentro do Identity.

]]>
