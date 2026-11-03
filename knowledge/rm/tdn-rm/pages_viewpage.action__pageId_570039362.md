---
content_hash: e0a49dbc1098f641b5f19bc5e088f46e4ee35b6b947d839a9fd08be800c46465
fetched_at: '2026-06-29T00:10:52.053784+00:00'
page_id: '570039362'
product: rm
source: tdn-rm
title: Configuração de Instalação - Portal da Obra e Cockpit TOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570039362
version: 14
---

Atenção!

##### **MUDANÇA NO PORTAL** *A partir da release **12.1.2506** a URL do Portal do TOTVS Construção Obras e Projetos mudou!* **Instalação pelo host:** http://{domínio}:{porta}/portaldaobra **Instalação pelo IIS:** http://{dominio}/FrameHTML/Web/App/Prj/PortalDaObra

##### *A partir da release **12.1.2606** a URL do Portal do TOTVS Construção Obras e Projetos mudou!* **Instalação pelo host:** http://{domínio}:{porta}/wwwroot/portaldaobra

##### Guarde o novo caminho nos seus favoritos!

##### **Acesse o Portal da Obra:** novo nome, novo layout e novo local.

**Objetivo:**

Este documento tem por objetivo detalhar a configuração necessária para a utilização do Portal da Obra e do Cockpit TOP.

Instalação e Configuração.Instalação

* Na instalação da biblioteca do RM deve-se atentar a porta informada para o host para que seja utilizado nas configurações posteriores.

* É obrigatório que esteja instalado o URL Rewrite como componente do IIS. Esse componente permite que a URL do site seja reescrita durante a navegação.

* É importante verificar também em Tipos de MIME se o tipo de mime ".json" está inserido.

Observação: O cadastro do Tipo de MIME é necessário para que o IIS consiga ler os arquivos ".json" do Portal. A verificação é necessária pois caso o MIME não estiver cadastrado o portal pode apresentar erros na leitura dos arquivos.

Configurando IIS

O Portal da Obra e o Cockpit pode ser hospedado no IIS  ou no RM.Host, sendo que ao optar por hospedar eles no RM.Host não é necessário a utilização do instalador ... e do IIS.

Ao finalizar a instalação da Biblioteca do RM Portal, será criado um site no IIS com o nome FrameHTML. O site é criado e toda a comunicação do IIS acontece na pasta **C:\TOTVS\CorporeRM\FrameHTML**

Caso queira utilizar o Cockpit através do IIS, a pasta do mesmo deve estar no mesmo nível onde se encontra o Portal da Obra (**C:\TOTVS\CorporeRM\FrameHTML\web\app\Prj**).

* O IIS realiza interações com a pasta do site e ele deve ter permissão total de acesso a pasta. É necessário inserir nas propriedades da pasta o controle total para o IIS: **NOMEDAMAQUINA\IIS\_IUSRS**.

* Uma das melhores formas de se testar a comunicação do IIS com a pasta é abrir o site logo após essas configurações é abrir o site pelo Procurar Site:

* Se o site for aberto sem nenhum erro é porque a comunicação entre a pasta e o IIS está corretamente configurada. Caso encontre algum erro nesse passo vá até a aba desse documento com nome **Erros e Soluções**.

Site aberto:

* Com o site aberto navegue entre as pastas **RM/Login/Login.aspx** ou simplesmente insira na URL do navegador dessa forma **<http://localhost:8080/RM/Login/Login.aspx.>**Ressaltando que, no caso a minha porta de comunicação do IIS é **:8080** conforme exibido no IIS na etapa Procurar site. Caso a porta cadastrada no IIS seja diferente deve ser informada a porta  correta para realizar esse segundo teste de validação. Se a página de login aparecer com sucesso sem exibir nenhum erro é porque a comunicação do IIS com a pasta está correta.

Página de Login:

Configuração Web.config e Host

O Portal da Obra e o Cockpit pode ser hospedado no IIS  ou no RM.Host, sendo que ao optar por hospedar eles no RM.Host não é necessário a utilização do instalador ... e do IIS.

É de extrema importância que o arquivo **Web.config (C:/TOTVS/CorporeRM/FrameHTML/Web.config)** e a configuração do **RM.Host ou RM.Host.Service** **(C:/TOTVS/CorporeRM/RM.Net)**estejam corretamente preenchidos pois eles carregarão a informação da base de dados para o Portal.

* **RM.Host ou RM.Host.Service**(Não use os dois ao mesmo tempo e com a mesma porta para que não há conflito de comunicação)
  + Antes de qualquer alteração, o Host deve estar desativado.
  + Os valores para "DefaultDb", "Port" e "ApiPort" deve estar informados corretamente:
    - "DefaultDB": é o nome do alias que será utilizado por default ao acessar o Portal RM. **(Extremamente importante para acesso no Portal da Obra)**;
    - "Port": é a porta do host;
    - "ApiPort": é a porta onde será realizada a comunicação da API. **(Extremamente importante para acesso no Portal da Obra, caso não exista essa tag no host o sistema utiliza o valor 8051 como default)**.

Lembrando que, as portas informadas para o host na chave **Port** e a porta informada na chave **ApiPort** deve estar **permitidas** no **Firewall**para que a comunicação funcione corretamente.

* **Web.config**
  + Os valores para "Port", "Host" e "ServiceAlias" deve estar informados corretamente.:
    - "Port": o valor da porta informada é o valor da porta do Host, seja ele RM.Host ou RM.Host.Service;
    - "Host":  é o nome da máquina;
    - "ServiceAlias": é o nome do alias que será utilizado.

Caso não há essas configurações inseridas no arquivo inseri-las para que o sistema funcione corretamente.

Configuração Monitor de Obras e PERT Web

* A última configuração que deve ser feita para o correto funcionamento do Portal da Obra é informar o valor correto desejado no arquivo **config.json.** Este arquivo é localizado nos locais abaixo e de acordo com a forma de acesso:

Acesso pelo **IIS: C:\totvs\CorporeRM\FrameHTML\Web\App\Prj\PortalDaObra\config\config.json;**

Acesso pelo **HOST: C:\totvs\CorporeRM\RM.Net\wwwroot\PortalDaObra\config\config.json.**

Acessando o Monitor de Obras

A URL de acesso do Portal da Obra é [http://localhost:8080/web/app/Prj/PortalDaObra/index.html](http://localhost:8080/web/app/Prj/PortalTOPWeb/index.html). Ressaltando que, nessa URL informada, [http://localhost:8080](http://localhost:8080/) é apenas um exemplo e caso há alteração para o nome completo do computador no arquivo **config.json** essa URL deverá ser alterada. (Exemplo: [http://bhn050102752.bh01.local:8080/web/app/Prj/PortalDaObra/index.html)](http://bhn050102752.bh01.local:8080/web/app/Prj/PortalTOPWeb/index.html))

* A base que estiver informada no alias cujo o valor está informado no "DefaultDB" será a base acessada no login.
* O usuário para login deve ser o usuário de login no RM.

Parametrização do Mapa

Acessar a plataforma de mapas do google : <https://cloud.google.com/maps-platform/?hl=pt>

Clicar em Primeiros Passos:

Selecionar o projeto google:

*Caso não há nenhum projeto criado, ao clicar sobre a seta é possível inserir um novo projeto.*

Ao avançar, será exibida a página para configurar o faturamento do Google Maps Plataform:

Informar a Etapa 1 e continuar.

Informar corretamente todos os dados na Etapa 2 e clicar em "INICIAR MINHA AVALIAÇÃO GRATUITA".

Ao avançar na Etapa 2, será exibida a ativação da Plataforma do Google Maps e clicando em "PRÓXIMA" será exibida a chave do Google Maps criada.

Agora adicione a sua Chave da API em **Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais | Google | Google Maps**

Caso seu ambiente possua proxy, preencha as configurações do proxy.

Erros e Soluções

1. Um dos primeiros erros que podem acontecer no teste da comunicação do IIS é relacionado a configuração "directoryBrowse". Em alguns casos ele está definido como "false" e o Portal necessita que a configuração esteja "true".

1.1. Para realizar o ajuste é necessário entrar no editor de configurações e alterar o "directoryBrowse" para true e aplicá-la

2. Erro **403 - Forbidden: Acess is denied**

2.1. Esse erro na maioria das vezes pode acontecer pois a configuração de Autenticação Anônima do IIS está incorreta. Para alterar deve-se acessar a Autenticação → Selecionar a Autenticação Anônima com um clique → Editar → Informar a Identidade de usuário anônimo: Identidade de pool de aplicativos

3. Erro por ausência do arquivo ou ausência de informação no arquivo A**lias.dat (C:/TOVS/CorporeRM/RM.Net/Alias.dat)**

3.1. Para corrigir esse erro o arquivo deve existir na pasta. Esse erro não é tão comum de acontecer quando se instala a Biblioteca RM e em seguida o Portal, pois na instalação da Biblioteca RM já se informa uma base de dados e automaticamente essa base será preenchida no arquivo **Alias.dat**

----
