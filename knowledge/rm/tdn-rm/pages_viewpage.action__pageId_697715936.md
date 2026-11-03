---
content_hash: cdf286255d26eaebacb6dbbf2e930b71da0f91de237375d8d909dba1e922d474
fetched_at: '2026-06-29T00:11:21.994429+00:00'
page_id: '697715936'
product: rm
source: tdn-rm
title: Portal de Imóveis - Instalação e configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697715936
version: 197
---

Portal de Imóveis

* [Arquitetura e Portabilidade](https://tdn.totvs.com/display/LRM/Arquitetura+e+Portabilidade)
  + [Servidores](https://tdn.totvs.com/display/LRM/Servidores)
  + [Serviços‎](https://tdn.totvs.com/pages/viewpage.action?pageId=656059783)

PortalinstalacaoInstalação

**Objetivo**

Esta página tem como objetivo aproximar o usuário ao conhecimento do processo instalação e configuração do Portal de Imóveis.

Instalação em Bases Oracle

Caso o seu banco de dados do Portal de Imóveis seja Oracle, verifique a aba **Pré-requisitos Oracle.**

**Procedimentos para Instalação do Portal de Imóveis**

Para clientes novos,  o Portal de Imóveis deverá ser instalado através do instalador RM Portais (extensão .MSI).

A partir da release **12.1.2506**, o Portal de Imóveis passará a utilizar o **PHP 8 (v8.3.30)**. Devido à vulnerabilidade e insegurança do protocolo HTTP, esta nova versão **exige** o uso de certificado SSL (HTTPS) por padrão. Caso o ambiente não possua a certificação configurada, o portal não poderá ser acessado externamente, ficando restrito apenas ao uso local ( usando localhost).

No vídeo abaixo, demonstra a instalação dos itens:

* [PHP Manager](https://tdn.totvs.com/display/LRM/PHP+Manager+para+IIS)
* Instalação do Portal de Imóveis

true

#FF9000Notas

1. Finalizando o processo de instalação, se você manteve a pasta padrão de instalação o caminho onde os arquivos do Portal de Imóveis foram instalados será: **C:\TOTVS\CorporeRM\FrameHTML\Web\App\Imb\PVI**
oraclePré Requisitos OracleImportante

Esta seção destina-se apenas aos clientes novos ou que utilizam base migrada do RM para utilização no Portal de Imóveis na versão 1212310. Para clientes não migrados, ainda não é possível a utilização de banco de dados Oracle no portal.

**Objetivo**

Esta página tem como objetivo listar os pré-requisitos para o acesso ao Portal de Imóveis utilizando banco de dados Oracle.

Para clientes que utilizam banco de dados Oracle, será necessário realizar uma modificação no arquivo INI do PHP. Essa alteração permitirá que o servidor IIS liste os drivers OCI (Oracle Call Interface) do Oracle, permitindo a integração adequada com o banco de dados.

Para fazer essa alteração, siga os passos abaixo:

1. Localize o arquivo INI do PHP no seu servidor. Geralmente, ele está localizado na pasta de instalação do PHP ou em um subdiretório chamado "conf" ou "php.ini".
2. Abra o arquivo INI do PHP utilizando um editor de texto.
3. Procure a seção do arquivo INI relacionada à extensão OCI do Oracle. Pode ser chamada de "oci8" ou similar (são eles):  
   extension=php\_pdo\_oci.dll   
   extension=php\_oci8.dll   
   **Oracle Server Versão 12 :** extension=php\_oci8\_12c.dll  
     
   *A Totvs tem a orientação de arquitetura de provider de banco em*:   
   **Oracle Server Versão 19c:** extension=php\_oci8\_19.dll
4. Verifique se as linhas correspondentes ao driver OCI está comentada (iniciada com ponto e vírgula ";"). Se estiver, remova o ponto e vírgula para habilitar a extensão.
5. Certifique-se de que a configuração correta para o driver OCI esteja definida. Isso inclui informações como o caminho para a biblioteca do cliente Oracle (por exemplo, "oci.dll" ou "[oci.so](http://oci.so)") e outros parâmetros relevantes.
6. Salve o arquivo INI modificado.

Para conferência, as linhas abaixo no arquivo .ini precisam estar habilitadas.

php

Após realizar essas alterações, reinicie o servidor IIS para que as modificações tenham efeito. Agora, o IIS será capaz de listar e utilizar os drivers OCI do Oracle ***(conforme imagem abaixo)***, permitindo a integração adequada com o banco de dados Oracle.

Caso a extensão não esteja habilitada como mostra a imagem acima, recomendados que faça as seguintes conferências

Arquivos **php\_oci8\_19.dll** e **php\_oci8.dll** presentes no diretório ext da pasta do PHP.

Em anexo seguem as duas dll's que podem ser utilizadas:

Em variáveis de ambiente do Windows, o caminho para o Oracle client ou Oracle Server devem estar definidos.

No exemplo acima o PATH do Oracle Client está localizado em *C:\OraHome\bin*

*Após definir o PATH, reinicie a máquina.*

Configurando o PHP com os procedimentos acima a extensão OCI deverá estar habilitada no IIS.

Caso precise, o arquivo em anexo permite que confira o estado da extensão OCI8 e se está habilitada no sistema

O arquivo acima deve ser descompactado em um diretório e após isso deverá ser executado via prompt, usando o comando:

php

**Ajuste de configuração para bases Oracle**

Para melhor leitura e escrita de dados na base Oracle, principalmente no tratamento de textos que contenham acentuação e caracteres especiais, é necessário adicionar o parâmetro charset=utf8 na configuração do DSN no arquivo config\_db.php.

A linha deve ficar da seguinte forma:

**'dsn' => (getenv('DB\_DSN') ? getenv('DB\_DSN') : 'oci:dbname=%s/%s;charset=utf8'),**

Observação: em instalações TOTVS Cloud, essa alteração deve ser solicitada ao time responsável pelo ambiente.

Feito as alterações listadas acima o banco de dados estará pronto para ser utilizado no Portal de Imóveis.

iisConfigurando IIS

**Objetivo**

Esta página tem como objetivo descrever o processo de configuração do Portal de Imóveis utilizando IIS

Para configurar, siga os passos abaixo:

Etapas do Wizardiispasso1Passo 1

**Pré-requisitos e instalações do IIS**

| **itens** |
| --- |
| **URLRewrite**  O URLrewrite é uma extensão para o IIS, que provê poderosos controles sobre as URL´s e facilitando a administração e busca de sites. Acesse o endereço **<http://www.iis.net/downloads/microsoft/url-rewrite#additionalDownloads>** e baixe a versão correspondente ao seu sistema operacional. |
| **PHP Manager**  PHP Manager é o software gerenciador do PHP para o IIS. Acesse **<https://github.com/phpmanager/phpmanager/releases>** vá para a opção Downloads e escolha o arquivo que correto para a versão do seu sistema operacional (32 ou 64 bits) |
| **Microsoft® ODBC Driver 17 for SQL Server**  Driver SQL 17 para conexão com banco de dados. Faça o download no link da Microsoft Acesse **[ODBC Driver 17 for SQL Server,](https://go.microsoft.com/fwlink/?linkid=2223304)** selecione o idioma do seu SQL Server. E marque o arquivo para download. |
| **Microsoft Visual C++ Redistributable**  Microsoft Visual C++ Redistributable, baixe a versão mais recente do microsoft visual c++  Acesse **<https://support.microsoft.com/pt-br/topic/os-downloads-do-visual-c-mais-recentes-com-suporte-2647da03-1eea-4433-9aff-95f26a218cc0>** Baixe a versão de acordo com o seu sistema operacional. |
| **ORACLE - Drive client (para clientes que possuem base de dados ORACLE)**  Certifique-se de que o driver Oracle esteja instalado e configurado adequadamente no servidor para garantir o funcionamento adequado e a integração perfeita com o banco de dados Oracle. Acesse: **<https://www.oracle.com/br/database/technologies/instant-client/downloads.html>** |
| **WebDAVModule**  Durante a instalação do IIS, através do recurso [**"Ativar ou desativar recursos do Windows"**](https://docs.microsoft.com/pt-br/iis/), recomendamos que a opção "**[Publicação WebDAV](https://learn.microsoft.com/pt-br/iis/publish/using-webdav/using-the-webdav-publishing-feature-with-iis)**" seja *desmarcada para evitar possíveis restrições na realização de chamadas PUT via API.* Esse cuidado é especialmente importante para desenvolvedores que precisam alterar dados no portal por meio da API. |
| **Necessário para utilização do PHP 8 Downloads mais recentes do Pacote Redistribuível do Microsoft Visual C++ com suporte <https://learn.microsoft.com/pt-br/cpp/windows/latest-supported-vc-redist?view=msvc-170>** |

iispasso2Passo 2

**Configurando o Portal de Imóveis no IIS**

Ao finalizar a instalação da Biblioteca do RM Portal, será criado um site no IIS com o nome PVI. O site é criado e toda a comunicação do IIS acontece na pasta **C:\TOTVS\CorporeRM\FrameHTML\web\app\Imb\PVI**  caminho que foi definido durante o processo de instalação do Portal de Imóveis

iispasso3Passo 3

**Alterando o Application Pool**

Acesse o IIS (Internet Information Service - pode digitar INETMGR na pesquisa de programas do windows)

Expanda "Application Pools", selecione "Corpore.Net", clique "Advanced Settings" e altere "Load User Profile (carregar perfil do usuário)" para "True (verdadeiro)". Clique Ok para salvar.  
**Nota: Apesar de estar mostrando .Net 4.0 na configuração, é indiferente usar .Net 2.0 ou 4.0.**

Ainda em Aplication Pools, devemos colocar o usuário administrador da máquina ou administrador do domínio no campo Modelo de Processo -> Identidade. Será exigido nome do usuário e senha.

iispasso4Passo 4

**Permissão da pasta ao IIS**

O IIS realiza interações com a pasta do site e ele deve ter permissão total de acesso a pasta. É necessário inserir nas propriedades da pasta o controle total para o IIS: **NOMEDAMAQUINA\IIS\_IUSRS**.  
Acesse a pasta da instalação do portal, **C:\TOTVS\CorporeRM\FrameHTML\Web\App\Imb\PVI**

iispasso5Passo 5

**Configurando o PHP Manager**

Para garantir o adequado desempenho do Portal de Imóveis, será necessário registrar a versão do PHP instalada na máquina. O instalador da Biblioteca RM disponibiliza o PHP instalado no diretório onde a biblioteca foi instalada.

Caso precisar fazer o download e instalar manualmente o PHP Manager, você pode obtê-lo através do seguinte link: <https://www.iis.net/downloads/community/2018/05/php-manager-150-for-iis-10>

1) Para configurar, acesse o IIS selecionando o site onde a extensão será apresentada;

2) Ao selecionar a opção para Registrar, será necessário buscar o caminho onde o PHP encontra-se instalado. Neste caso o mesmo poderá ser localizado no diretório de instalação da biblioteca RM e na pasta PHP selecionar a opção: php-cgi.exe

3) Após selecionar, clique em OK;

4) Ao clicar em Verificar phpinfo, o IIS irá listar as informações referentes ao PHP instalado e registrado neste servidor;

iispasso6Passo 6

**Testando a comunicação do IIS**

Uma das formas de se testar a comunicação do IIS é abrir o site clicando em Procurar Site:

configpiConfigurando o Portal de Imóveis

**Objetivo**

Esta página tem como objetivo de configurar o Portal de Imóveis.

A partir da versão 12.1.33, o wizard de instalação do Portal de Imóveis foi modificado, simplificando a instalação do portal e a configuração dos bancos de dados e webservices RM.

Etapas do Wizardconfigpipasso1Passo 1

**Sobre o instalador**  
Esta etapa é apenas uma introdução que resume os procedimentos que deverão ser executados

configpipasso2Passo 2

**Conexão com WebService TOTVS**  
Neste momento deveremos definir o caminho público da URL dos webservices TOTVS que serão consumidos pelo Portal de Imóveis.

* **Informe a URL do WebService TOTVS**: Endereço do webservice. Exemplo: *[http://url:porta/wsDataServerPVI/MEX?wsdl](http://localhost:8051/wsDataServerPVI/MEX?wsdl)*
* **Usuário**: Usuário de acesso ao webservice;
* **Senha**: Senha do usuário

Acesso ao endereço da Url

1) A configuração da URL do servidor deve ser uma URL de acesso público, ou seja, acessível externamente, uma vez que o exemplo abaixo utiliza o '**localhost**', que não pode ser acessado publicamente.

2) Lembre-se que os **acessos para WebServices deverão estar disponíveis** no perfil do usuário administrador que está realizando a configuração desta etapa:

Importante: Caso sua base seja **unificada** e você deseje alterar posteriormente estas URL's e o usuário de acesso, realize esta alteração via Parâmetros do RM. [Consulte a documentação aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)configpipasso3Passo 3

**configpipasso3  
Caminho do banco de dados**  
  
Nesta etapa iremos configurar os dad [Lista de Marcadores](https://tdn.totvs.com/pages/editpage.action?pageId=697715936) os do banco onde o Portal de Vendas de Imóveis será instalado

* **DBMS:**MySql (*Somente Versão Legado Sem Unificação de Base de Dados*), SQLServer ou Oracle (*Não Aceita Conexão por SID somente Sevidor e Instancia os dois campos devem ser preenchidos*)
* **Servidor:**Selecionar o IP ou IP/Instância;
* **Porta:**Usar a padrão do DBMS ou a definida no DBMS;
* **Nome do Banco de Dados:**Por padrão o nome do banco de dados default é o Portal de Imóveis podendo ser alterado;
* **Usuário do Banco do Portal de Imóveis:**Usuário de acesso do banco de dados;
* **Senha do Banco do Portal de Imóveis:** Senha de acesso do usuário.

---

**Produto recém-adquirido (Primeira Instalação):**

Para clientes que estão adquirindo o Portal de Imóveis pela primeira vez (Produto recém-adquirido – Primeira Instalação), o sistema irá preparar a base de dados com informações padronizadas exclusivamente para esse cenário, garantindo que as configurações iniciais estejam adequadas. É importante reforçar que ***clientes que já possuem o Portal de Imóveis em uso na empresa*** ***não devem selecionar este parâmetro***, pois ele é destinado **apenas a novas instalações**. Esse processo assegura que o ambiente esteja configurado corretamente para novos clientes e evita conflitos em casos de bases antigas ou configurações inadequadas.

1) No parametrizador selecione a opção:

2) Será perguntado ao usuário se o mesmo deseja seguir com a configuração;

3) Ao final será apresentado para o usuário a informação referente a conclusão da parametrização da base de dados.

#### ***USUÁRIO MESTRE: Instalação Nova***

*Quando o PI é instalado a partir de uma **base nova**, o sistema **cria automaticamente um usuário mestre padrão**. Esse usuário é gerado por meio de **scripts presentes no conversor**, responsáveis por configurar os dados e campos default necessários para o funcionamento inicial da aplicação.*

**Critérios para validação de Base na Instalação:**  
**1. Validação de Base na Instalação e Configuração:**

* Durante o processo de instalação ou configuração do portal de imóveis, o sistema deve validar se a base de dados do cliente está vazia.
* Bases consideradas vazias (sem os registros mínimos esperados) serão classificadas como "base inconsistente".

**Procedimentos em Caso de Base RM Vazia:**

* Caso a base seja identificada como vazia, clientes configurando uma base RM deverão:
* Selecionar a opção "primeira instalação" para prosseguir.
* Caso essa opção não seja escolhida, o sistema exibirá uma mensagem indicando inconsistência.

**2. Proibição de Instalação em Bases Antigas:**

* Clientes novos ou aqueles que possuem bases do modelo antigo (portal de imóveis que possui a base separada da base RM) devem obrigatoriamente migrar para o novo modelo.
* Bases vazias do modelo antigo não serão aceitas para instalação do portal.

**3. Migração e Conversão de Clientes Existentes  
Requisitos para Clientes do Modelo Antigo**

* Clientes que já utilizam o portal de imóveis no modelo antigo deverão:
* Realizar a conversão para o novo modelo.
* Migrar dados relacionados a [comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=784209752) e [reajustes.](https://tdn.totvs.com/pages/viewpage.action?pageId=546679564)

**Manutenção de Bases RM Antigas**

* Clientes com bases RM antigas podem continuar utilizando o portal, desde que:
* Façam as configurações necessárias para ajustes no novo sistema.

**4. Regras de Comissões e Reajustes  
Requisitos para Utilização de Funcionalidades de Portal de Imóveis (Integrado)**

      Para acessar as funcionalidades de comissões e reajustes no novo sistema, é obrigatória:

* A migração para o modelo atualizado de [gestão de comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=784209752)e [reajustes;](https://tdn.totvs.com/pages/viewpage.action?pageId=546679564)[;](https://tdn.totvs.com/Reajuste Revitalizado / Conversor.)
* Ajustes em bases que não atendam aos requisitos mínimos, com o suporte técnico.  
    
  **Veja mais:**
configpipasso4Passo 4

**Instalação concluída**  
Nesta etapa será apenas um informativo com as configurações de login para o primeiro acesso no Portal de Imóveis.

Antes de realizar o primeiro acesso, edite o arquivo config.json que fica no diretório 'C:\totvs\CorporeRM\RM.Net\wwwroot\Config', colocando o mesmo valor do passo 2, sem a barra '/' no final.

configcomissaoConfigurando a Comissão 2.0linkuteisLinks Úteis

**Objetivo**

Esta página tem como objetivo disponibilizar os links dos pacotes adicionais necessários para instalação Portal de Imóveis.

**URLRewrite**

O URLrewrite é uma extensão para o IIS, que disponibiliza controles sobre as URL´s e facilitando a administração e busca de sites.  
Acesse o endereço <http://www.iis.net/downloads/microsoft/url-rewrite#additionalDownloads> e baixe a versão correspondente ao seu sistema operacional.

**PHP Manager**

PHP Manager é o software gerenciador do PHP para o IIS.   
Acesse <https://github.com/phpmanager/phpmanager/releases> vá para a opção Downloads e selecione o arquivo correto para a versão do seu sistema operacional (32 ou 64 bits)

**Microsoft® ODBC Driver 17 for SQL Server**

Driver SQL 17 para conexão com banco de dados. Faça o download no link da Microsoft  
Acesse <https://www.microsoft.com/en-us/download/details.aspx?id=56567> Selecione o idioma do seu SQL Server, e marque o arquivo para download.

**Microsoft Visual C++ Redistributable**

Microsoft Visual C++ Redistributable, baixe a versão mais recente do microsoft visual c++   
Acesse <https://support.microsoft.com/pt-br/topic/os-downloads-do-visual-c-mais-recentes-com-suporte-2647da03-1eea-4433-9aff-95f26a218cc0>  Baixe a versão de acordo com o seu sistema operacional.

errosesolucoesErros e Soluções

**Objetivo**

Este documento visa listar alguns erros que podem ser encontrados durante a instalação, configuração do portal, bem como suas possíveis soluções.

Importante

Antes de analisar os itens de erros e soluções, convido você executar o “**ambiente-check”** do portal de imóvel, cujo seu propósito é realizar checagem de ambiente, permitindo avaliar possíveis inconsistência.  
  
Para acessar, basta informar ao seu endereço do portal /ambiente-check.php  
Exemplo: <http://localhost:2205/ambiente-check.php>

**Lista erros e soluções:**

404 Not Found / CORS error

**Mensagem de erro:**

* **Problema:**Ao tentar logar no portal, é apresentado mensagem de erro:  
  Desculpe, não foi possível processar sua solicitação neste momento.  
  Se necessário, entre em contato com a equipe de TI ou administrador do sistema. Status: ***"404 Not Found"***.  
  URL: ./api/login
* **Solução:**Certifique a existência do arquivo ***web.config***  em seu ambiente de instalação do portal.    
  Geralmente, é adotado o caminho fisico,  (C:\TOTVS\CorporeRM\FrameHTML\Web\App\Imb\PVI\API\ mas isso não é uma regra.

  Segue o padrão do Web.config

  xmlEclipseWeb.config



























  ]]>#FF9000Notas
  + errosesolucoescorsVale lembrar que, por padrão o compartilhamento de recursos com origens diferentes ([CORS](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS))  vai liberado.  
    Caso seja necessário bloquear algumas destas configurações, o Web.config do portal de imóveis na pasta /PVI/api, deverá ser alterado. as tag's responsáveis são:

    xmlEclipseCors




    ]]>
405 URL: /api/login

**Mensagem de erro:**

* **Problema:**Ao tentar logar no portal, é apresentado mensagem de erro:  
  Desculpe, não foi possível processar sua solicitação neste momento.  
  Se necessário, entre em contato com a equipe de TI ou administrador do sistema. Status: ***"405 URL: /api/login"***.  
    

  **Solução:**Acesse o IIS e em seguida ao selecionar o diretório do Portal (clique no ícone Gerenciador do PHP)
* Neste momento selecione a promeira configuração para registrar o PHP,  
    
    
  Selecione o caminho para carregar o PHP.exe e em seguida clique em abrir;
* Em seguida selecione a opção Verificar PHPINFO
* Será apresentado a menasgem informando que o PHP encontra-se corretamente configurado.
Não há licença disponível para continuar acessando o sistema. Favor entrar em contato com o suporte

**Mensagem de erro:  
Não há licença disponível para continuar acessando o sistema. Favor entrar em contato com o suporte.**

* **Problema:**

  Ao acessar a tela de configuração do PI e informar o webservice, api e usuário e senha do RM;  
  Em seguida ao clicar em avançar, será gerada a mensagem de erro abaixo:

  **Não há licença disponível para continuar acessando o sistema. Favor entrar em contato com o suporte.**

  *OBS: O usuário possui permissão total em seu perfil no módulo do TCGI.*
* **Solução:**Para solucionar esta mensagem será necessário realizar acesso ao módulo Gestão de Imóveis (via RM.EXE).  
  Esta mensagem ocorre quando o usuário nunca acessou o módulo de Gestão de Imóveis.
Erro retornado pelo TOTVS: Unauthorized - DataServer: ReadView

**Mensagem de erro:**

* **Problema:**Ao informar o caminho público da URL dos webservices TOTVS que serão consumidos pelo Portal de Imóveis. (usuário e senha) ao clicar em "Conectar" o sistema apresenta a mensagem:  
  Ocorreu uma exceção no sistema: Erro retornado pelo TOTVS: Unauthorized  
  DataServer: ReadView  
  Parâmetros  
  Array  
  (  
      [DataServerName] => ImbStatusLicencasTodosAppsData  
      [Filtro] => 1=1  
      [Contexto] => CODCOLIGADA=0;CODUSUARIO=mestre  
  )
* **Solução:**Será necessário avaliar se o nome do Alias informado nas configurações do RM possui um espaço no campo. Veja este exemplo abaixo:
* Após salvar, reinincie novamente os serviços do RM.Host e valide novamente o acesso ao Portal de Imóveis.
* **Dica 2:** Apague os aliases existentes e inclua um novo (tomando cuidado para não deixar espaço no campo nome do Alias).
* **Dica 3:** Validar se o arquivo ***CONFIG Host*** possui as TAG´s abaixo: *(caso não tenha, após adiciona-las, será necessário parar o serviço do RM.Host e inicia-lo novamente).*  
  *<add key="Port" value="8050" />*  
  *<add key="Host" value="nome do servidor" />*  
  *<add key="HttpPort" value="8051" />*  
  *<add key="ApiPort" value="8051" />*  
  *<add key="DefaultDb" value="CorporeRM"/>*
SOAP-ERROR: Parsing Schema: can't import schema from

**Mensagem de erro:**

* **Problema:**Neste momento deveremos informar o caminho público da URL dos webservices TOTVS que serão consumidos pelo Portal de Imóveis.  
  **Informe a URL do WebService TOTVS**: Endereço do webservice. Exemplo: *[http://url:porta/wsDataServerPVI/MEX?wsdl](http://localhost:8051/wsDataServerPVI/MEX?wsdl)***Usuário**: Usuário de acesso ao webservice; **Senha**: Senha do usuário  
  Ao clicar em conectar, deparamos com a mensagem Erro retornado pelo TOTVS: SOAP-ERROR: *Parsing Schema: can't import schema from* '[http://url:porta/wsDataServerPVI/mex?xsd=xsd0](http://10.10.10.1:8051/wsDataServerPVI/mex?xsd=xsd0)'
* **Solução:**Para expor os *WebServices* para acesso externo, torna-se necessária a inclusão da tag ServicesHostName, onde seu valor deverá ser o DNS ou IP Público da instituição.   
  É provável que essa Tag no HOST do serviço RM esteja inconsistente.**<add key="ServicesHostName" value="DNS da instituição" />**
Function is not a valid method for this service

**Mensagem de erro:**

* **Problema:**Ao tentar tentar ativar /inativar o empreendimento é apresentado mensagem de erro:  
  Function   
  ("SincronizaAtivacaoEmpreendimentoPortalDeImoveis") is not a valid method for this service
* **Solução:**Certifique a a informação do parâmetro **WebService TOTVS: URL.**Esse parâmetro, você o encontra no portal de imovel>> Parâmetros - TOTVS >> **WebService TOTVS: URL**O dataserver utilizado deve ser o dataserverPVI, sendo assim o método SincronizaAtivacaoEmpreendimentoPortalDeImoveis será encontrado.  
  Exemplo do caminho WebService TOTVS
Erro ao atualizar as páginas do módulo de Aluguel

**Mensagem de erro:**

* **Problema:**Ao atualizar as páginas do módulo de Aluguel é apresentado a mensagem de erro:  
  404 - Arquivo ou diretório não encontrado  
  O recurso que você está procurando pode ter sido removido, ter tido seu nome alterado ou estar temporariamente indisponível.

* **Solução:**Acesse o diretório de instalação do Portal de Imóveis (C:\...\CorporeRM\FrameHTML\web\app\Imb\PVI) e verifique na raiz da pasta o arquivo **Web.config**. Caso o arquivo não exista, o mesmo deve ser criado. Abra o arquivo e informe a seguinte linha no atributo da principal regra:

***<action type="Rewrite" url="/aluguel/" />***

Exemplo:

O processo FastCGI excedeu o tempo limite de atividade solicitado

**Mensagem de erro:   
Erro HTTP 500.0 - Internal Server Error C:\php\php-cgi.exe - O processo FastCGI excedeu o tempo limite de atividade solicitado**

* **Problema:**

Ao executar alguns processos dentro do portal e exceder o tempo de resposta do servidor.  
Como exemplo, o processo de sincronização ou impressão de relatórios.

* **Solução:**

 Acesse o IIS e em seguida selecione no servidor principal a opção de configuração de FastCGI

Ao acessar esta tela (ainda no IIS) marque o caminho de configuração do FastCGI e clique em Editar...

Observe que na tela em aberto existem algumas informações com valores já pré determinados na instalação nativa do IIS.  
Dentre estas opções altere o valor da propriedade ***"Tempo de Espera de Atividade"*** default 300 (esse valor padrão refere-se a segundos) dividindo o valor de tempo por 60 = 5 minutos. Este valor poderá ser definido pelo usuário. Uma vez alterado (clique em salvar).

Feito estes ajustes, selecione novamente o servidor principal e clique na opção para reiniciar os serviços do IIS;

Após realizar os ajustes via IIS, ainda deverá ser realizado outra parametrização, acessando no explorer o diretório onde encontra-se instalado o PHP.  
Uma vez acessando o diretório edite o arquivo de inicialização **PHP.INI** ***(OBS: Por padrão o arquivo é encontrado no diretório: $:\totvs\PHP)***  
Com o arquivo editado localize a TAG "**max\_execution\_time"** (que possui o valor padrão 300) podendo ser aumentado de acordo com a necessidade do usuário, lembrando que este valor também refere-se a segundos.

Não há licença disponível para continuar acessando o sistema. Favor entrar em contato com o suporte

**Não há licença disponívelMensagem de erro:   
Não há licença disponível para continuar acessando o sistema. Favor entrar em contato com o suporte.**

* **Problema:**

Ao informar o WebServices e em seguida clicar em conectar, o sistema apresenta falha de licenças.

* **Possível solução:**

 Acesse o RM e em perfis, selecione o sistema: Gestão de Imóveis e em seguida edite o perfil associado ao usuário que está realizando a conexão com o Webservices, habilitando a opção: Acesso Irrestrito aos Dados dos Web Services.

Após salvar, acese novamente o configurador do Portal de imóveis e ao realizar o mesmo processo (informando o WebServices) o sistema possibilitará conectar sem apresentar falhas de Licença.  
***Observação: é importante lembrar que a COLIGADA da base de dados deve ter a devida autorização para acessar as licenças necessárias a fim de utilizar os utilitários para realizar os processos de conversão.***

Sincronizando o Portal de Imóveis com o TCGI

Conforme demonstrado na arquitetura o Portal de Imóveis usa a estrutura de WebServices da TOTVS para troca de informações e para que este processo funcione é necessário parametrizar alguns dados no TOTVS RM e no Portal de Imóveis.

**Parametrização no TOTVS RM**

Para realizar o sincronismo dos dados entre Portal de Imóveis e RM devemos habilitar os WebServices conforme documentação do link a seguir:

[Como Expor os Web Services do RM através do Host](https://tdn.totvs.com/pages/viewpage.action?pageId=89620766)

Ainda no RM devemos agora habilitar as actions usadas no processo de comunicação de dados, para isto vamos seguir os passos abaixo:

1. Iniciamos o processo com a atualização das actions do sistema. Para isto devemos acessar o menu de "Serviços Globais" e depois selecionar "Actions do Sistema";
2. Ao abrir a tela de actions, selecione o menu de "Processos" e selecione "Atualização de Actions Cadastradas";
3. Ainda no menu de "Serviços Globais", acesse a opção de "Servidores de Aplicação" e no menu "Processos" selecione "Carregar dados de descrição dos serviços". *Este procedimento pode demorar até 5 minutos, favor acompanhar a janela de mensagens no rodapé do TOTVS;*
4. Feito este processo podemos chamar a URL do portal de vendas – Portal de Imóveis acessar a opção backend > Sincronizar. Ao clicar nesta opção, caso haja alguma action para ser parametrizada o sistema informará o nome destas. Estes serão os nomes usados nas etapas seguintes do processo de parametrização das actions;
5. Se ao tentar sincronizar o Portal de Imóveis com o RM apareceu a tela acima com os nomes das actions que necessitam parametrização, então acesse novamente o RM em Serviços Globais > Servidores de Aplicação. Clique no botão para adicionar um novo registro e ao abrir a tela de inclusão, clique no botão para listar os ID´s dos servers cadastrados. Ao abrir a janela de pesquisa, digite no campo descrição o nome de uma das actions listadas na tela do Portal de Imóveis (vide nomes no quadro vermelho). Selecione o registro que aparecer com esta descrição e tecle OK;
6. Na tela de cadastro, coloque o valor "-1" no campo "Número máximo de registros" e clique em Salvar;
7. Repita este processo a partir da etapa 5 enquanto houverem nomes na janela vermelha da tela de sincronismo do Portal de Imóveis.  
     
   Saiba mais acessando:
Erro 500 ao imprimir contrato ou proposta

**Erro 500 ao imprimir contrato ou proposta**

Caso apareça uma mensagem de **Erro 500** ao tentar imprimir um contrato ou proposta, siga os passos abaixo:

1. Acesse o diretório onde o PHP está instalado.
2. Localize e edite o arquivo **php.ini**.
3. Encontre a linha `extension=zip` e **verifique se ela não está comentada** (ou seja, sem o caractere `;` no início da linha).

   * Exemplo correto: `extension=zip`
4. Após a alteração, **salve o arquivo php.ini**.
5. Acesse novamente o portal de imóveis e tente imprimir o documento.
The FastCGI process has failed frequently recently. Try the request again in a while

Esse erro geralmente é apresentado em servidores que **utilizam PHP 8.**

**Possíveis causas:**Indica um conflito entre a versão da DLL do Visual C++ Runtime instalada no sistema e a versão que o PHP 8 espera usar.  
O que isso significa?

* O PHP 8 foi compilado para ser usado com a versão **14.29 do Microsoft Visual C++ Redistributable**.
* No seu sistema, a DLL `VCRUNTIME140.dll` que está sendo carregada é da versão **14.0**, que é incompatível.

Para resolvê-lo, é necessário acessar o link abaixo e baixar o pacote mais recente compatível com a sua versão do sistema.  
**<https://learn.microsoft.com/pt-br/cpp/windows/latest-supported-vc-redist?view=msvc-170>**  
  
Após o download, realize a instalação normalmente e, em seguida, reinicie o computador para que as alterações tenham efeito.

recemprimeirainstalacaoProduto recém-adquirido - Primeira instalação

**Objetivo**

Esta opção irá preparar internamente a base de dados para utilização dos dados do RM, e irá criar as tabelas necessárias para integrar o portal com o Backoffice.  
Nesta etapa iremos configurar os dados do banco onde o Portal de Vendas de Imóveis será instalado

* **DBMS:**MySql (*Somente Versão Legado Sem Unificação de Base de Dados*), SQLServer ou Oracle (*Não Aceita Conexão por SID somente Sevidor e Instancia os dois campos devem ser preenchidos*)
* **Servidor:**Selecionar o IP ou IP/Instância;
* **Porta:**Usar a padrão do DBMS ou a definida no DBMS;
* **Nome do Banco de Dados:**Por padrão o nome do banco de dados default é o Portal de Imóveis podendo ser alterado;
* **Usuário do Banco do Portal de Imóveis:**Usuário de acesso do banco de dados;
* **Senha do Banco do Portal de Imóveis:** Senha de acesso do usuário.

---

**Produto recém-adquirido (Primeira Instalação):**   
  
Para clientes que estão adquirindo o Portal de Imóveis pela primeira vez (Produto recém-adquirido – Primeira Instalação), o sistema irá preparar a base de dados com informações padronizadas exclusivamente para esse cenário, garantindo que as configurações iniciais estejam adequadas. É importante reforçar que ***clientes que já possuem o Portal de Imóveis em uso na empresa*** ***não devem selecionar este parâmetro***, pois ele é destinado **apenas a novas instalações**. Esse processo assegura que o ambiente esteja configurado corretamente para novos clientes e evita conflitos em casos de bases antigas ou configurações inadequadas.

1) No parametrizador selecione a opção: 

2) Será perguntado ao usuário se o mesmo deseja seguir com a configuração;

3) Ao final será apresentado para o usuário a informação referente a conclusão da parametrização da base de dados.

**Instalação concluída**  
Nesta etapa será apenas um informativo com as configurações de login para o primeiro acesso no Portal de Imóveis.

Antes de realizar o primeiro acesso, edite o arquivo config.json que fica no diretório 'C:\totvs\CorporeRM\RM.Net\wwwroot\Config', colocando o mesmo valor do passo 2, sem a barra '/' no final.

**Critérios para validação de Base na Instalação:**  
**1. Validação de Base na Instalação e Configuração:**

* Durante o processo de instalação ou configuração do portal de imóveis, o sistema deve validar se a base de dados do cliente está vazia.
* Bases consideradas vazias (sem os registros mínimos esperados) serão classificadas como "base inconsistente".

**Procedimentos em Caso de Base RM Vazia:**

      Caso a base seja identificada como vazia, clientes configurando uma base RM deverão:

* Selecionar a opção "primeira instalação" para prosseguir.
* Caso essa opção não seja escolhida, o sistema exibirá uma mensagem indicando inconsistência.

**2. Proibição de Instalação em Bases Antigas:**

* Clientes novos ou aqueles que possuem bases do modelo antigo (portal externo) devem obrigatoriamente migrar para o novo modelo.
* Bases vazias do modelo antigo não serão aceitas para instalação do portal.

**3. Migração e Conversão de Clientes Existentes  
Requisitos para Clientes do Modelo Antigo**

      Clientes que já utilizam o portal de imóveis no modelo antigo deverão:

* Realizar a conversão para o novo modelo.
* Migrar dados relacionados a [comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=784209752) e [Reajustes](https://tdn.totvs.com/pages/viewpage.action?pageId=546679564)[.](https://tdn.totvs.com/Reajuste Revitalizado / Conversor.)

**Manutenção de Bases RM Antigas**

      Clientes com bases RM antigas podem continuar utilizando o portal, desde que:

* Façam as configurações necessárias para ajustes no novo sistema.

**4. Regras de Comissões e Reajustes  
Requisitos para Utilização de Funcionalidades de PI (Proposta Integrada)**

       Para acessar as funcionalidades de comissões e reajustes no novo sistema, é obrigatória:

* A migração para o modelo atualizado de [gestão de comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=784209752)e [reajustes;](https://tdn.totvs.com/pages/viewpage.action?pageId=546679564)
* Ajustes em bases que não atendam aos requisitos mínimos, com o suporte técnico.  
    
  **Veja mais:**
migrar37Migrar versão 3.7.X para superiores

**Objetivo**

Realizar a migração da versão 3.7.x para versões atualizadas acima da 12.1.x  
  
**Procedimentos:**

* Acesse o diretório de instalação do portal 3.7.x e copie as pastas: tmp e uploads;

* Estas pastas (tmp e Uploads) deverão ser copiadas para o diretório onde o Portal de Imóveis encontra-se instalado no servidor, neste nosso exemplo, o portal encontra-se instalado em um diretório padrão de instalação: C:\totvs\CorporeRM\FrameHTML\web\app\Imb\PVI

* Ao acessar o IIS será necessário parar o serviço do site da versão 3.7.x, mantendo iniciado somente o site da Versão 12.1.x que será o novo site que será parametrizado.  
  Ao selecionar o novo site PVI (realize a configuração do PHP Manager para comunicaçao com esse novo portal).
* PHP conectado com sucesso:
* Quando selecionado o Site do PVI é necessário incluir a Permissão para o usuário IIS\_IURS com as permissões totais para este usuário.
* Validar a autenticação do usuário no Application pool, neste parametrização (Basic Settings) informar o usuário Administrador do IIS;
* Realizar a instação do Conversor Word e Conversor PDF;
* Acesse o diretório de instalação do Portal: C:\TOTVS\CorporeRM\FrameHTML\web\app\Imb\PVI\api (apague o arquivo: licença.lic). Em seguida acesse o Portal de Imóveis onde será necessário realizar as configurações conforme solicitadas na tela.  
    
    

  Neste momento deveremos definir o caminho público da URL dos webservices TOTVS que serão consumidos pelo Portal de Imóveis.

  + **Informe a URL do WebService TOTVS**: Endereço do webservice. Exemplo: *[http://url:porta/wsDataServerPVI/MEX?wsdl](http://localhost:8051/wsDataServerPVI/MEX?wsdl)*
  + **Usuário**: Usuário de acesso ao webservice;
  + **Senha**: Senha do usuário
* **Instalação concluída**  
  Nesta etapa será apenas um informativo com as configurações de login para o primeiro acesso no Portal de Imóveis.  
    
    
    
  Antes de realizar o primeiro acesso, edite o arquivo config.json que fica no diretório 'C:\totvs\CorporeRM\RM.Net\wwwroot\Config', colocando o mesmo valor do passo 2, sem a barra '/' no final.
conversaobasepiPreparação para Conversão de Base

**conversaobasepi**

A conversão de base exige alguns requisitos que dependem de quem irá executar o procedimento, abaixo é possível obter orientação específica em cada caso.
