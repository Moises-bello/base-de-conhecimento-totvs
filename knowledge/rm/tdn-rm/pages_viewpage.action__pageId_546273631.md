---
content_hash: e886ad465e28818e9d4207ae10aa78eb101082d425089a896b53b1de1318d463
fetched_at: '2026-06-29T00:10:41.755903+00:00'
page_id: '546273631'
product: rm
source: tdn-rm
title: Instalação e configuração do ambiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546273631
version: 57
---

SumárioIMPORTANTE

A partir da versão 12.1.28 a instalação dos novos portais foram modificadas para que os mesmos sejam utilizados na mesma porta dos portais Corpore.Net, sendo assim, as URL's que são disponibilizadas para seus clientes devem ser modificadas.

Novo padrão de URL:

* Portal do aluno:  [http://](http://xn--local_de_instalaoporta-s4b9g/)[SERVIDOR](http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/)[/FrameHTML/web/app/Edu/PortalEducacional/login](http://xn--local_de_instalaoporta-s4b9g/)
* Portal do Processo Seletivo: [http://](http://xn--local_de_instalaoporta-s4b9g/)[SERVIDOR](http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/)[/FrameHTML/web/app/Edu/PortalProcessoSeletivo/#/es/informacoes](http://xn--local_de_instalaoporta-s4b9g/)

Os passos abaixo devem ser seguidos para uma utilização correta dos portais.

Atenção

Caso o sistema operacional do servidor web onde o novo portal do aluno ficará hospedado seja o Windows Server 2008 R2, é necessário que o Hotfix (relacionado ao roteamento das APIs) citado no link a seguir esteja instalado, além das atualizações do Windows.

<https://support.microsoft.com/pt-br/help/980368/a-update-is-available-that-enables-certain-iis-7-0-or-iis-7-5-handlers>

Depois de instalar a Biblioteca RM siga os passos abaixo para instalar o novo portal do aluno.

A instalação poderá ser completa ou personalizada.

* **Completa**: O sistema irá instalar todos os portais: Novo portal do aluno e Novo portal do processo seletivo, onde ambos serão instalados automaticamente.

* **Personalizada**: Será instalado o portal específico, isto é, o usuário irá selecionar qual Portal que deseja instalar, que atualmente foram liberados o Novo portal do aluno, Novo portal do processo seletivo , Novo portal RH e o Novo portal do Cliente - Incorporação Imobiliária.

Para ambas instalações, seguir o mesmo procedimento:

**1º-** A instalação inclui a estrutura do Corpore.NET (Referente ao antigo portal ) e a estrutura da FrameHTML (Referente a instalação dos Novos portais).

Dica

Validar de forma correta a porta e o nome do servidor caso não for utilizar localhost.

**2º-** Para acessar o Novo Portal do Aluno, seguir as configurações abaixo.

Devido a algumas funcionalidades ainda não migradas do antigo portal Corpore.NET para o novo portal do aluno, o portal utiliza a mesma autenticação disponível no portal Corpore.NET. Desta forma, é possível acessar as funcionalidades ainda não migradas do antigo portal Corpore.NET através do novo portal do aluno de forma transparente e sem necessidade de uma nova autenticação.

Se o perfil do usuário logado no novo portal possuir permissões de acesso às funcionalidades do Corpore.NET, senão listado através do menu *Portal (antigo)* todas as funcionalidades que o usuário possui permissão, e que ainda não foram migradas para o novo portal do aluno.

Ao acessar qualquer funcionalidade listada neste menu, o usuário será redirecionado para o Corpore.NET sem a necessidade de realizar novamente o Login.

Para permitir esta integração entre os portais, é necessário realizar a configuração abaixo onde é informado o caminho de instalação de ambos os portais.

falseImportante

**A partir da versão 12.1.2602, não é mais necessário realizar as configurações de URL do Portal do Corpore.NET e URL da FrameHTML, tanto no RM quanto nos arquivos web.config do Corpore.NET e pasta FrameHTML mencionados abaixo devido a evolução do processo de Login do Portal Educacional, no qual remove a exigência do ambiente do Corpore.NET funcionando para que o processo de Login seja realizado. A partir desta versão, o Portal Educacional não utiliza mais o Corpore.Net para autenticação, consequentemente deixando de ser necessário estas configurações e em casos de não haver integração do Educacional com o TOTVS Avaliação e Pesquisa também não fica sendo necessário o ambiente Corpore.NET.**

## **01. CONFIGURAR A URL DO PORTAL CORPORE.NET**

Deve ser especificado o endereço do Corpore.NET em: **Totvs Gestão Educacional |****Ambiente | Parâmetros | Parâmetros Globais | Gerais | URL de acesso ao Portal RM**

No campo: *URL de acesso ao Portal RM* informar o endereço: <http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/> (Exemplo: <http://servidor/corpore.net/>)

## **02. CONFIGURAR A URL DO PORTAL FrameHTML**

Deve ser especificado o endereço da FrameHTML em: **Totvs Gestão Educacional |****Ambiente | Parâmetros | Parâmetros Globais | FrameHTML**

No campo: *Defina o endereço da FrameHTML* informar o endereço: [http://](http://xn--local_de_instalaoporta-s4b9g/)[SERVIDOR](http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/)[/NOMEAPLICATIVO\_FRAMEHTML](http://xn--local_de_instalaoporta-s4b9g/) (Exemplo: [http://servidor/FrameHTML/](http://servidor:9999/))

A configuração acima é utilizada principalmente quando há apenas um único servidor de instalação para o Corpore.NET ou um outro para o novo portal do aluno.

falseImportante

Quando existem mais de um servidor WEB e se utilizam de um Load Balancing, existe a necessidade de que cada servidor web com a instalação do Corpore.NET responda diretamente para um servidor específico que esteja instalado o novo Portal do Aluno para a comunicação adequada no processo de login. Normalmente, a instalação de ambos os portais é feita no mesmo servidor, mas em várias máquinas diferentes.

Desta forma, cada uma das instalações em cada servidor deve apontar para o Corpore.NET e FrameHTML referente ao seu servidor específico.

Para atender esta demanda, foi criado uma nova chave em cada um dos Web.Config dos portais. Um no Web.Config da FrameHTML referente ao novo portal do aluno, e outra chave no web.config contido no ambiente do Corpore.NET.

### Web.Config do portal FrameHTML

Este arquivo estará na raiz da pasta de instalação da FrameHTML. A chave abaixo estará comentada no arquivo, para isso deve retirar o comentário HTML da chave e especificar o endereço do portal Corpore.NET.

<add key="UrlCorpore" value="[http://servidor/Corpore.Net](http://localhost/Corpore.Net_atual)" />

### Web.Config do portal Corpore.NET

O arquivo está localizado na raiz pasta ..\Corpore.Net\Source\Edu-Educacional\Public\Web.config, e deverá conter o endereço do portal FrameHTML.

<add key="UrlFrameHTML" value="[http://servidor/FrameHTML](http://localhost:8050)" />

**ATENÇÃO:** Ao utilizar esta configuração através dos arquivos de Web.Config dos portais, não serão mais utilizados as configurações definidas nos parâmetros do sistema, e sim de forma exclusiva o caminho parametrizado nos arquivos Web.Config.

### Config Global para o Portal Corpore.Net

Para o cenário que utiliza a configuração **config global**, é necessário realizar as alterações no arquivo do **config global,** pois quando está usando este recurso, ele sobrescreve todas as informaçõesdo web.config do portal Corpore.NET. **Saiba mais sobre** [Config Global](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042337054-Framework-Linha-RM-Frame-Gerenciador-de-Config-Global)

Adicionar a seguinte tag

<add key="NomePastaInstalacaoPortalEducacional" value="web" />

O endereço da FrameHTML em **Totvs Gestão Educacional |****Ambiente | Parâmetros | Parâmetros Globais | FrameHTML** no campo "Defina o endereço da FrameHTML" **não acrescentar a informação "/web"** no final do endereço

**O ambiente da TCLOUD** normalmente utiliza o config global, e desta forma é necessário realizar o procedimento acima para o correto funcionamento.

## **03. INSTALAÇÃO DO REWRITE E DO ARR (APPLICATION REQUEST ROUTING)**

Como requisito para o funcionamento do portal é necessário instalar o **URL Rewrite** e **ARR (Application Request Routing)** no IIS.

### **ARR (Application Request Routing)**

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do ARR**:  <https://www.microsoft.com/en-us/download/details.aspx?id=47333> 

Apenas uma vez para cada IIS

**A instalação deve ser realizada apenas uma vez para cada IIS.**

Após finalizar a instalação **ARR (Application Request Routing),** deverá ser **habilitado** a propriedade **"Enable proxy"**

### **URL Rewrite**

A instalação deve ser realizada no servidor do portal desejado.

**Link para download do URL Rewrite**: <https://www.iis.net/downloads/microsoft/url-rewrite>

Após a Instalação, será criado um ícone: “**URL Rewrite**” no IIS

Após configurar o servidor, é necessário configurar o arquivo de configuração do Host do RM. Para isso, acesse o arquivo **RM.Host.Service.exe.config** que está disponível no caminho padrão do instalador do RM.exe.

Inserir as chaves as chaves abaixo:

      <add key="**ApiPort**" value=**"porta\_definida\_no\_rewrite (IIS)"** />  
      <add key="**DefaultDB**" value=**"informe\_aqui\_o\_nome\_do\_alias"** />

O usuário associado ao **serviço** tem que ter **permissão** para acessar a porta da **API** definida no **URL Rewrite**.

## **04. CONFIGURAÇÃO** **DO REWRITE**

Acessar o IIS -> Ir no aplicativo FrameHTML -> Abrir até a pasta do Portal Educacional  -> URL Rewrite

Editar as informações da regra criada:

Editar a URL de ação do Rewrite e incluir o nome do servidor e a porta de comunicação configurada na tag "**ApiPort**" do arquivo de configuração do Host.

Verificar a porta configurada na tag ApiPort do arquivo de configuração do Host, por padrão é usada a porta 8051.

### **Configuração do tempo de timeout do portal**

O portal permite que a instituição realize a configuração do *Time out* da forma que desejar.

Algumas funcionalidades tenha um comportamento adequado sugerimos que o tempo seja de 240 segundo (4 minutos).

**1.**Acessar o IIS -> Ir na pasta "Default Web Site"

**2.** Selecione a opção **"Configurações Avançadas"**

**3.** Preencha com tempo desejado em "**Tempo Limite de Conexão (segundos)**"

**4.** Acessar o IIS -> Ir no pasta do servidor -> **Application Request Routing Cache**

**5.** Clicar em: **Server Proxy Settings**

**6.** Preencha com tempo desejado em "**Time-out (seconds)**"

**7.**Em seguida, clicar no botão: **Aplicar**

Importante

Após realizar as configurações, é necessário reiniciar o IIS

## **05. ACESSO AO PORTAL EDUCACIONAL (PORTAL DO ALUNO)**

Após estas configurações, acessar o novo portal através do link:[http://LOCAL\_DE\_INSTALAÇÃO/FrameHTML](ttp://LOCAL_DE_INSTALA%C3%87%C3%83OPORTA)/web/app/edu/portaleducacional/login

Caso a instituição deseje utilizar os novos portais como nas versões antigas, utilizando a porta 8080, acesse o link para realizar os ajustes: <https://tdn.totvs.com/x/eLmnI>

Aviso Importante

O novo Portal do Aluno depende do recurso de manipulação URL’s sem extensão definida esteja disponível no IIS (utilizado para funcionamento dos serviços REST). Contudo, identificamos que algumas versões do IIS não vem com suporte a tal recurso instalado por padrão, impossibilitando o funcionamento da aplicação.

Caso tenha algum problema de funcionamento após sua instalação, a Microsoft lançou um hotfix para atualização do IIS para habilitar tal recurso.

Link para download: <https://support.microsoft.com/en-us/help/980368/a-update-is-available-that-enables-certain-iis-7.0-or-iis-7.5-handlers>

## **06. CONFIGURAR O ACESSO DO USUÁRIO BANCO DE DADOS PARA ACESSAR O NOVO PORTAL DO ALUNO**

Após a instalação do novo portal, certificar se o usuário/senha TOTVSPortal de acesso ao banco de dados está de acordo com o mesmo usuário/senha do banco de dados configurado no servidor. A verificação é realizada em:

 **Servidos Globais | Segurança | Acesso | Código de Acesso**

Selecionar o usuário: TOTVSEdu e verificar se o usuário/senha está de acordo com o usuário/senha de acesso ao banco de dados.

## **07. LISTAR O ALIAS NO NOVO PORTAL**

Ao acessar a tela de login do novo portal, serão listados todos os alias cadastrados no Gerenciamento de Alias (salvos no arquivo "Alias.dat") e listados para o usuário em ordem alfabética.

Exemplo: No ambiente possui dois alias cadastrados, sendo:

* CorporeRM\_Alias01

* CorporeRM\_BaseTeste

Ao acessar o Login do novo portal do aluno, **o primeiro alias da lista será automaticamente selecionado:**

* CorporeRM\_Alias01

Arquivo de configuração

A tela de Login do novo Portal do Aluno não utiliza o parâmetro **ServiceAlias** definida no arquivo Web.Config da pasta FrameHTML.

## **08.** **OCULTAR DROPDOWN DE SELEÇÃO DE ALIAS**

**1)** Acessar a pasta: ...\FrameHTML\web\app\Edu\PortalEducacional\js\

**2)** Localizar o arquivo edu-constantes.global.config.js

**3)** Editar o arquivo e localizar a variável EDU\_CONST\_GLOBAL\_EXIBIR\_ALIAS=**true** e alterar para: EDU\_CONST\_GLOBAL\_EXIBIR\_ALIAS=**false**

Desta forma o portal apresentará a tela de login sem a opção de seleção de alias.

Seleção do alias

Quando o novo portal do aluno está parametrizado para não exibir a seleção de alias, o portal do aluno irá utilizar o primeiro alias da lista cadastrada no Gerenciamento de Alias, sendo o primeiro item após realizado uma ordenação por ordem alfabética.

Para os clientes que utilizam a Biblioteca em 3 camadas, atente-se para a configuração da tag <add key="**Host**" value="**localhost**" />, certificando que a mesma aponta para os servidores corretos.
