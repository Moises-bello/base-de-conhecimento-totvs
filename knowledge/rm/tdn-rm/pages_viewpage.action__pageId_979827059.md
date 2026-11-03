---
content_hash: faa8af6a1556fc302f5c83b93cf1b55d60943abc1f68d308d5e9da74cbb90b4c
fetched_at: '2026-06-29T00:12:15.521446+00:00'
page_id: '979827059'
product: rm
source: tdn-rm
title: 1- Pré-requisitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979827059
version: 5
---

Os portais **Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor**, fazem o uso de API para buscar e armazenar informações, o controle destas APIs é feito pelo host. Para que os portais funcionem corretamente, é necessário expor as APIs para web, desta maneira, é necessário o uso do módulo URL Rewrite do IIS para que este módulo filtre as solicitações e encaminhe para o host as solicitações que sejam para a API.

1- Configuração do ARR e URL Rewrite

Como requisito para o funcionamento dos portais é necessário instalar o **URL Rewrite** e **ARR (Application Request Routing)** no IIS.

ARR (Application Request Routing)

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Apenas uma vez para cada IIS

**A instalação deve ser realizada apenas uma vez para cada IIS.**

Habilitar o proxy

Após finalizar a instalação **ARR (Application Request Routing),** deverá ser **habilitado** a propriedade **"Enable proxy"**

URL Rewrite

A instalação deve ser realizada no servidor do portal desejado.

Atenção

**A partir da versão 12.1.2402**

É possível utilizar as api's do host diretamente, sem o uso do módulo do **URL** **Rewrite**. Para isso deve expor o host para a web e informar o endereço do host nos arquivos de config dos portais.

**Importante** ficar atento a questões de **segurança** ao expor o host para a web. A forma como será utilizado fica a critério da instituição.

0.1tempfadeInstalaçãofade

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “URL Rewrite” no IIS

Configuração Rewritefade

Deve ser necessário configurar **duas** regras para o **URL** **Rewrite***:*

* A 1º regra **(regra comum para todas as versões)** é utilizada para direcionamento de **API** onde não é necessário passar o alias selecionado;
* A 2º regra **(apenas para versões anteriores à 12.1.2402)** é utilizada para as **API** onde é necessário passar o alias selecionado.

Exclusivamente para os novos portais

A configuração deve ser realizada **exclusivamente** nos portais: **Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor** em: **Sites | Default Web Site | FrameHTML | Web | App |Edu | 'Pasta referente ao portal'.** Caso a configuração **não** seja realizada no caminho especificado anteriormente, o portal do Aluno poderá ser impactado.

A ordem das regras deve ser respeitada.

A ordem das regras deve ser respeitada.

Regra comum para todas as versões

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado (Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor) -> URL *Rewrite*

**2.**Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.**No campo "**Name**" informar um nome para a regra que está sendo criada

**4.**Na opção: Match URL, no campo: "**Pattern"** inserir as informação: api/(.\*)

**5.**Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://nome\_da\_maquina\_do\_host:porta/api/{R:1](http://localhost:8052/%7BR:1)}*

Regra adicional necessário para versões anteriores a 12.1.2402

**Para as versões anteriores à 12.1.2402** é necessário configurar uma nova regra.

Atenção

A porta utilizada deve ser a mesma que está configurada na chave "ApiPort" no arquivo de host **RM.Host.Service.exe.config**.

**1.**Acessar o IIS -> Ir no aplicativo que está sendo configurado (**Portal Gestão Educacional / Portal da Biblioteca / Novo Portal do Professor**) -> URL *Rewrite*

**2.** Dar um duplo click no ícone URL Rewrite e em seguida clicar em: **Adicionar uma *Rule* do tipo*****Inboud Rule**.*

**3.** No campo "**Name**" informar um nome para a regra que está sendo criada

**4.** Na opção: Match URL, no campo: "**Pattern**" inserir as informação: aliasname\.(.\*)/api/(.\*)

**5.**Na opção*: "**Actions"**, no campo: Rewrite URL informar o link: [http://{R:1}.nome\_da\_maquina\_do\_host:porta/api/{R:](http://localhost:8052/%7BR:1)2}*

**6.**Marcar a opção*: "**Stop processing of subsequent rules"***

2- Configurar aquivo de config do Host do RM

Após configurar o servidor conforme o item: 1- Pré-requisitos, é necessário configurar o arquivo de configuração do Host do RM. Para isso, acesse o arquivo **RM.Host.Service.exe.config** que está disponível no caminho padrão do instalador do RM.exe.

Inserir as chaves as chaves abaixo:

      <add key="ApiPort" value=**"porta\_definida\_no\_rewrite (IIS)"** />  
      <add key="DefaultDB" value=**"informe\_aqui\_o\_nome\_do\_alias"** />

A chave: "**EnableRealtime**" é responsável pela comunicação entre o App Meu eduCONNECT e o Portal Gestão Educacional.

Inserir a chave abaixo no config. do Host do RM.

<add key="EnableRealtime" value="**true**" />

Versão anteriores à 12.1.2402

Inserir a chave abaixo:

<add key="SubDomainMask" value="**[ALIAS].nome\_da\_máquina\_do\_host**" />

Para a opção "SubDomainMask", o nome da máquina deve ser inserido todo utilizando letras **minúsculas**. O texto [ALIAS] **não deve ser alterado**, deve ser inserido o texto desta forma, o que deve ser alterado é o "nomeDaMaquinaDoHost".

**Exemplo:** a máquina do host possui o nome de ServerXYZ, desta forma, deve ser inserido o texto [ALIAS].serverxyz.

falseUsuário associado ao serviço

O usuário associado ao **serviço** tem que ter **permissão** para acessar a porta da **API** definida no **URL Rewrite**.

3- Configurar arquivo de config do Portal

Após configurar o servidor conforme o item: 1- Pré-requisitos, é necessário configurar o arquivo de configuração no portal. Para isso, acesse o arquivo **config.json** que está disponível no caminho padrão do instalador do Portal.

“C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\"**Pasta referente ao portal**" \config\”.

* **Exemplo do portal do professor:** FrameHTML| Web | Edu | Portal | PortalDoProfessor
* **Exemplo do portal do gestão educacional:** FrameHTML| Web | Edu | Portal | PortalGestaoEducacional
* **Exemplo do portal da biblioteca:** FrameHTML| Web | Edu | Portal | portalbiblioteca

No arquivo, as seguintes configurações são possíveis:

|  |
| --- |
| `{` `"apiServer": "http://localhost/FrameHTML/Web/App/Edu/PortalXXXXXX",` `"basePath": "/FrameHTML/Web/App/Edu/PortalXXXXX",` `"defaultAlias": "informe_o_nome_do_Alias",` `"urlCorpore": "http://localhost/Corpore.Net",` `"imgBannersLogin": [` `{` `"name": "banner01.jpg"` `},` `{` `"name": "banner02.jpg"` `},` `{` `"name": "banner03.jpg"` `}` `]` `}` |

Parâmetro "apiServer"

Essa configuração é utilizada para realizar o **redirecionamento para a API** que será feito pelo **URL Rewrite** do IIS.

Deve ser configurado com o **endereço público do portal conforme o exemplo a seguir:**.

* **Exemplo do portal do professor:** http://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/PortalDoProfessor
* **Exemplo do portal do gestão educacional:** http://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/PortalGestaoEducacional
* **Exemplo do portal da biblioteca:** http://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/portalbiblioteca

**\*EndereçoDaInstituição\* refere-se ao DNS da Instituição de ensino.**

**A partir da versão 12.1.2402**

Este parâmetro poderá **ficar vazio**, pois a instalação do portal irá preenche-lo com o mesmo endereço configurado para acessar o portal automaticamente. Além disso, será possível configurar este parâmetro com um endereço diferente do utilizado para acessar o portal. Para isto, o host deve estar configurado para acesso externo, ou seja, **o host deve estar exposto para internet**. Desta maneira o valor a ser preenchido neste parâmetro, deve ser o endereço no qual o host está sendo exposto.

* **Exemplo do portal do professor:** O portal está sendo acessado pelo seguinte endereçohttp://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/PortalDoProfessor e o host está exposto no seguinte endereço [**https://\*EndereçoDaInstituição\*:9051**,](https://portaltotvs.com.br:9051,) desta maneira, o valor que deve ser preenchido no parâmetro deve ser o **[https://\*EndereçoDaInstituição\*:9051](https://portaltotvs.com.br:9051,).**

* **Exemplo do portal gestão educacional:** O portal está sendo acessado pelo seguinte endereçohttp://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/PortalGestaoEducacional e o host está exposto no seguinte endereço [**https://\*EndereçoDaInstituição\*:9051**,](https://portaltotvs.com.br:9051,) desta maneira, o valor que deve ser preenchido no parâmetro deve ser o **[https://\*EndereçoDaInstituição\*:9051](https://portaltotvs.com.br:9051,).**

* **Exemplo do portal da biblioteca:** O portal está sendo acessado pelo seguinte endereçohttp://**\*EndereçoDaInstituição\***/FrameHTML/web/app/edu/portalbiblioteca e o host está exposto no seguinte endereço [**https://\*EndereçoDaInstituição\*:9051**,](https://portaltotvs.com.br:9051,) desta maneira, o valor que deve ser preenchido no parâmetro deve ser o **[https://\*EndereçoDaInstituição\*:9051](https://portaltotvs.com.br:9051,).**

**\*EndereçoDaInstituição\* refere-se ao DNS da Instituição de ensino.**

Parâmetro "basePath"

Deve ser configurado com o **caminho relativo** do portal.

* **Exemplo do portal do professor:** FrameHTML| Web | Edu | Portal | PortalDoProfessor
* **Exemplo do portal do gestão educacional:** FrameHTML| Web | Edu | Portal | PortalGestaoEducacional
* **Exemplo do portal da biblioteca:** FrameHTML| Web | Edu | Portal | portalbiblioteca

Parâmetro "defaultAlias"

Esta configuração **não define** qual o alias que será utilizado para acessar o portal, apenas **seleciona automaticamente** o alias na caixa de seleção na tela de login quando possui mais de um alias cadastrado. 

Deve ser configurado com o alias padrão utilizado para fazer o acesso à base de dados. Este alias, deve estar **cadastrado** no **arquivo alias.dat**.

Parâmetro "urlCorpore" (apenas no portal do professor)

Deve ser configurado o **endereço público do portal Corpore.NET**, para que as funcionalidades ainda **não migradas** do **portal do professor**, sejam redirecionadas para o Corpore.NET.

Quando o ambiente possuir mais de um servidor WEB contendo uma instalação do **Portal do Professor** e **Corpore.NET**, seja possível cada servidor redirecionar para o Corpore.NET do seu próprio servidor. Ou, em casos que o endereço do Corpore.NET parametrizado no RM esteja sendo utilizado para outras finalidades, apontando para um ambiente específico.

Apenas para o portal do professor

Configuração apenas para o **portal do professor,** **não sendo utilizada nos demais portais.**

Configuração mandatória é no arquivo config.json

A configuração **mandatória** é no arquivo config.json, portando, quando preenchida o portal não irá utilizar o caminho parametrizado no RM.

Usando o Parâmetros Globais do RM.exe

Esta parametrização também pode ser feita no RM em: **Educacional |** **Ambiente | Parâmetros | Parâmetros Globais | Gerais | URL de acesso ao Portal RM**

No campo: *URL de acesso ao Portal RM* informar o endereço: [http://SERVIDOR/NOMEAPLICATIVO\_CORPORE.NET/](http://servidor/NOMEAPLICATIVO_CORPORE.NET/) (Exemplo: [http://instituicao.br/corpore.net/](http://servidor/corpore.net/))

Parâmetro "imgBannersLogin"

Deve ser configurado os banners que são exibidos na tela de login do portal. Para alterar as imagens, basta adicionar ou remover imagens desejadas no **diretório do portal** e no **arquivo config.json**.

* **Exemplo do portal do professor:** C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\portaldoprofessor\assets\img\banners-login
* **Exemplo do portal do gestão educacional:** C:\RM\Atual\Release\FrameHTML\web\app\Edu\portalgestaoeducacional\assets\img\banners-login
* **O portal da Biblioteca não possui esse formato de banner. A imagem da tela principal deve ser inserida conforme instruções <https://tdn.totvs.com/x/n9PGLg>**

O nome da imagem da lista no **arquivo config.json** deve ser o mesmo nome da imagem no diretório do portal.

Tamanho das imagens

Para que o banner tenha uma boa apresentação sugerimos que a imagem tenha a **dimensão de 720 (largura) x 1024 (altura)**.

Parâmetro "multitenant"

Deve ser configurado o portal para o Multi-Tenancy. **Para mais informação**

**A partir da versão 12.1.2402**

As chaves **multitenant** e **subdomainMask**devem ser **removidas**do **arquivo config.json,** com exceção de ambiente que esteja configurado como multitenant.

4- Configurar arquivo de Host do Windows (Versão anterior a 12.1.2402)

Essa configuração é utilizada para a requisição da **API** que chega no **IIS**, ela é filtrada pelo **URL Rewrite** e é redirecionada para o **host**, mas como a requisição vem do **IIS**, o mesmo **não consegue encontrar** o endereço do host, desta forma, a configuração que é feita no arquivo de **host do Windows,** irá informar para o **IIS** qual a máquina do host.

Atenção

**A partir da versão 12.1.2402** está configuração **não é necessária**.

Esta configuração é necessária ser realizada em **todas as máquinas que o IIS** estiver configurado.

* Acessar o arquivo de host do windows (geralmente se encontra em C:\Windows\System32\drivers\etc\hosts)

* Para cada alias cadastrado no rm, deve existir um registro no arquivo de host. Deve ser inserido um registro no mesmo padrão que foi informado no arquivo de configuração do host (ver a configuração do [Rewrite](https://tdn.totvs.com/pages/viewpage.action?pageId=837434579#temp--771829624), na aba configuração do config), onde deve ser inserido no seguinte padrão: Nome\_Do\_Alias.Nome\_Da\_Maquina\_Do\_Host **todo em minúsculo.**
* Caso a máquina em que o host se encontra configurado seja a mesma máquina em que o IIS está instalado, **deve ser informado o nome ou IP das configurações do [Rewrite](https://tdn.totvs.com/pages/viewpage.action?pageId=837434579#temp--771829624) (na opção: "Actions" e no campo Rewrite URL), lembrando que o valor pode localhost ou 127.0.0.1**, caso o host esteja configurado em uma máquina diferente da do IIS, o IP informado deve ser o IP da máquina do host.

**Exemplo 1**:

Como exemplo, existem dois alias cadastrados no RM.exe, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o**IIS** e nestas maquinas rodam o host, uma com o nome de ServerXYZ e outra com o nome de SERVERZYX, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

- 127.0.0.1 corporerm.serverxyz  
- 127.0.0.1 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 127.0.0.1 corporerm.serverzyx  
- 127.0.0.1 corporermoracle.serverzyx

**Exemplo 2:**

Como exemplo, existe dois alias cadastrados no rm, um com o nome de CorporeRM e outro com o nome de CorporeRMOracle, e existe duas máquinas rodando o*IIS* e uma máquina rodando o host, as máquinas rodando o IIS tem os nomes de ServerXYZ e outra com o nome de SERVERZYX, e a máquina de host tem o nome de hostxyz e o IP 10.0.0.52, desta forma, no arquivo de host da máquina ServerXYZ, ficaria da seguinte maneira:

- 10.0.0.52 corporerm.serverxyz  
- 10.0.0.52 corporermoracle.serverxyz

Para a máquina SERVERZYX:  
- 10.0.0.52 corporerm.serverzyx  
- 10.0.0.52 corporermoracle.serverzyx

5- Configurar tempo de timeout do portal

O portal permite que a instituição realize a configuração do *Time out* da forma que desejar.

Algumas funcionalidades tenha um comportamento adequado sugerimos que o tempo seja de 240 segundo (4 minutos).

Reiniciar o IIS

Após realizar as configurações é necessário reiniciar o IIS

**1.**Acessar o IIS -> Ir na pasta "Default Web Site"

**2.** Selecione a opção **"Configurações Avançadas"**

**3.** Preencha com tempo desejado em "**Tempo Limite de Conexão (segundos)**"

**4.** Acessar o IIS -> Ir no pasta do servidor -> **Application Request Routing Cache**

**5.** Clicar em: **Server Proxy Settings**

**6.** Preencha com tempo desejado em "**Time-out (seconds)**"

**7.**Em seguida, clicar no botão: **Aplicar**
