---
content_hash: 56c9adba795d07acb4ecf09be2b32d542dd304a4528444b3823dc23d80fc22b9
fetched_at: '2026-06-29T00:10:25.875665+00:00'
page_id: '506373365'
product: rm
source: tdn-rm
title: Portal da Obra - Instalação e Configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506373365
version: 27
---

PortalInstalação

* Na instalação da biblioteca do RM deve-se atentar a porta informada para o host para que seja utilizado nas configurações posteriores.

* É obrigatório que esteja instalado o URL Rewrite como componente do IIS. Esse componente permite que a URL do site seja reescrita durante a navegação.

* É importante verificar também em Tipos de MIME se o tipo de mime ".json" está inserido.

Observação: O cadastro do Tipo de MIME é necessário para que o IIS consiga ler os arquivos ".json" do Portal. A verificação é necessária pois caso o MIME não estiver cadastrado o portal pode apresentar erros na leitura dos arquivos.

Configurando IIS

Ao finalizar a instalação da Biblioteca do RM Portal, será criado um site no IIS com o nome FrameHTML. O site é criado e toda a comunicação do IIS acontece na pasta **C:\TOTVS\CorporeRM\FrameHTML**

* O IIS realiza interações com a pasta do site e ele deve ter permissão total de acesso a pasta. É necessário inserir nas propriedades da pasta o controle total para o IIS: **NOMEDAMAQUINA\IIS\_IUSRS**.

* Uma das melhores formas de se testar a comunicação do IIS com a pasta é abrir o site logo após essas configurações é abrir o site pelo Procurar Site:

* Se o site for aberto sem nenhum erro é porque a comunicação entre a pasta e o IIS está corretamente configurada. Caso encontre algum erro nesse passo vá até a aba desse documento com nome **Erros e Soluções**.

Site aberto:

* Com o site aberto navegue entre as pastas **RM/Login/Login.aspx** ou simplismente insira na URL do navegador dessa forma **<http://localhost:8080/RM/Login/Login.aspx.>**Ressaltando que, no caso a minha porta de comunicação do IIS é **:8080** conforme exibido no IIS na etapa Procurar site. Caso a porta cadastrada no IIS seja diferente deve ser informada a porta  correta para realizar esse segundo teste de validação. Se a página de login aparecer com sucesso sem exibir nenhum erro é porque a comunicação do IIS com a pasta está correta.

Página de Login:

Configuração Web.config e Host

É de extrema importância que o arquivo **Web.config (C:/TOTVS/CorporeRM/FrameHTML/Web.config)** e a configuração do **RM.Host ou RM.Host.Service** **(C:/TOTVS/CorporeRM/RM.Net)**estejam corretamente preenchidos pois eles carregarão a informação da base de dados para o Portal.

* **RM.Host ou RM.Host.Service**(Não use os dois ao mesmo tempo e com a mesma porta para que não ocorra conflito de comunicação)
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

Caso não tenha essas configurações inseridas no arquivo, aconselhamos inseri-las para que o sistema funcione corretamente.

Parametrização do MapaConfiguração Portal da Obra

* A última configuração que deve ser feita para o funcionamento do Portal da Obra é informar o valor correto nos arquivos **config.json (C:\totvs\CorporeRM\FrameHTML\Web\App\Prj\PortalTopWeb\config\config.json) e (C:\totvs\CorporeRM\Bin\wwwroot\config\config.json).**
* Os arquivos não possuem muitas informações mas é necessário se manter atento ao preenchimento para o correto funcionamento do portal.
  + Após a instalação o arquivo estará preenchido conforme abaixo, onde destacamos um exemplo do IP e a porta da API:

* "apiServer": endereço da API para ser acessado no Portal da Obra.
  + Devem ser informados os valores corretamente;
  + A porta da API deve estar preenchida com a **mesma porta** informada na **configuração do Host:  "ApiPort".**Se a tag estiver com valor 8052 a porta deve ser alterada (conforme destacado na aba Configuração Web.config e Host;
  + O endereço localhost limita o acesso no portal somente para ambiente de desenvolvimento. Para acessos externos o endereço deve ser alterado para o nome completo do computador (Exemplo: <http://bhn050102752.bh01.local:8051)> onde BHN050102752 é o nome da máquina, ou o IP, como exemplo da imagem anterior.

* "apiKeyGoogleMaps": chave gerada pelo google maps para que as localizações dos apontamentos provenientes do TOP Mobile sejam visualizadas no Porta da Obra.

Acessando o Portal da Obra

A URL de acesso do Portal da Obra é <http://localhost:8080/web/app/Prj/PortalTOPWeb/index.html> se estiver configurado pelo IIS. Ressaltando que, nessa URL informada, <http://localhost:8080> é apenas um exemplo e é necessário a alteração para o nome completo do computador ou IP no arquivo **config.json** (Conforme destacado na aba "Configuração Portal da Obra") e essa URL deverá ser alterada também de acordo com a definição desse arquivo. (Exemplo: <http://bhn050102752.bh01.local:8080/web/app/Prj/PortalTOPWeb/index.html)>

Pelo host a URL segue o exemplo [http://bhn019401325:8051/portalTopWEb/login](http://bhn019401323:8051/portalTopWEb/login):

* A base que estiver informada no alias cujo o valor está informado no "DefaultDB" será a base acessada no login.
* O usuário para login deve ser o usuário de login no RM.

Erros e Soluções

1. Um dos primeiros erros que podem acontecer no teste da comunicação do IIS é relacionado a configuração "directoryBrowse". Em alguns casos ele está definido como "false" e o Portal necessita que a configuração esteja "true".

1.1. Para realizar o ajuste é necessário entrar no editor de configurações e alterar o "directoryBrowse" para true e aplicá-la

2. Erro **403 - Forbidden: Acess is denied**

2.1. Esse erro na maioria das vezes pode acontecer pois a configuração de Autenticação Anônima do IIS está incorreta. Para alterar deve-se acessar a Autenticação → Selecionar a Autenticação Anônima com um clique → Editar → Informar a Identidade de usuário anônimo: Identidade de pool de aplicativos

3. Erro por ausência do arquivo ou ausência de informação no arquivo A**lias.dat (C:/TOVS/CorporeRM/RM.Net/Alias.dat)**

3.1. Para corrigir esse erro o arquivo deve existir na pasta. Esse erro não é tão comum de acontecer quando se instala a Biblioteca RM e em seguida o Portal, pois na instalação da Biblioteca RM já se informa uma base de dados e automaticamente essa base será preenchida no arquivo **Alias.dat**
