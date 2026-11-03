---
content_hash: 0fb629b302efc6c7ad0ed84a7845a4a9688cb897d6564c22db2d6a60455e242d
fetched_at: '2026-06-29T00:08:50.788832+00:00'
page_id: '334338569'
product: rm
source: tdn-rm
title: 01 - Instalação e configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334338569
version: 49
---

Índice

## **01. INSTALAÇÃO**

Os servidor web que hospedará a aplicação precisará atender aos seguintes pré-requisitos:

##### IIS – Internet Information Services versão 7.0 ou superior.

##### Framework .Net versão 4.0 ou superior;

##### Biblioteca RM - Caso exista um servidor de aplicação, este deve ter instalada a Biblioteca RM. Caso contrário, se o servidor web for também o servidor de aplicação, a instalação da Biblioteca RM deve ser feita nesse servidor.

Atenção

A partir da release 12.1.20 do TOTVS Educa Mobile a versão mínima do Framework .NET é a 4.7.

Após a instalação dos pré-requisitos, o instalador do TOTVS Educa Mobile compatível com a Biblioteca RM instalada deve ser executado. O instalador criará o diretório virtual no IIS e também a pasta da aplicação no diretório que foi escolhido.

Importante

Fique atento às versões de Biblioteca RM e TOTVS Educa Mobile que estão instaladas no seu ambiente, principalmente após a instalação de versões específicas.

Exemplo: se você atualizou a versão da Biblioteca RM para a 12.1.191.254, não se esqueça de atualizar a versão do TOTVS Educa Mobile para a versão 12.1.19.254, pois caso contrário seu ambiente poderá apresentar instabilidades devido à essa diferença.

Sempre que uma nova versão da Biblioteca RM é disponibilizada para download, uma versão do TOTVS Educa Mobile com o mesmo número também é disponibilizada.

Ao término da execução do instalador do TOTVS Educa Mobile, as configurações de Host RM, Alias e Visualização Mobile estarão com as opções padrão. Caso o cliente queira alterar essas configurações, dentro da pasta da aplicação existe um arquivo chamado “web.config.xml” onde essas configurações podem ser alteradas.

## **02. CONFIGURAÇÃO**

##### Configurações de Host RM

Essas configurações são as mesmas existentes atualmente para o Portal Corpore.Net, ou seja, as chaves "Host" e "Port" ficam por padrão com os mesmos valores configurados para o Portal Corpore.Net.

Atenção

Os valores das chaves "Host" e "Port" devem ser o nome ou endereço IP do servidor onde o RM.Host está instalado e o número da Porta onde o RM.Host está configurado, respectivamente.

##### Alias para conexão com banco de dados

Nessa chave deve ser configurado o nome do Alias para conexão com o banco de dados que será utilizado pela aplicação TOTVS Educa Mobile.

##### Ativação da visualização mobile pelo navegador

Essa é a chave que contém a configuração onde é definido se as funcionalidades do TOTVS Educa Mobile poderão ser acessadas no formato mobile pelo navegador de um computador e não somente pelo celular.

Atenção

Atualmente o TOTVS Educa Mobile não disponibiliza outros formatos de visualização, portanto esse valor não deve ser alterado.

##### Personalização de cores

Essa chave define o diretório onde se encontra a configuração de cores (tema) padrão do TOTVS Educa Mobile criada no [ThemeRoller](http://themeroller.jquerymobile.com). No item "" abordaremos detalhadamente os procedimentos para personalizar as cores do aplicativo.

##### Personalização de imagens

Dentro da pasta citada no item "Personalização de cores" sempre é criada a pasta "images". Nessa pasta exitem dois arquivos chamados "minha\_empresa.png" e "aplicativo.png", respectivamente, listados a seguir:

Para personalizar essas imagens deve-se trocá-las, mantendo o mesmo nome e características de extensão e dimensões.

##### Personalização do nome

       Essa chave permite alterar o nome do TOTVS Educa Mobile .O nome fica disponível na barra superior após efetuar o login.

Após alterar:

Importante

Como o TOTVS Educa Mobile e o Portal Corpore.Net utilizam a mesma parametrização para suas funcionalidades, caso o cliente já tenha o Portal Corpore.Net instalado e disponibilizado, as permissões para as funcionalidades já foram concedidas e a parametrização realizada.

Após o item concluir esse guia de instalação e configuração não é mais necessário nenhuma configuração adicional. Caso queira verificar algum detalhe sobre parâmetros ou permissões, consulte i item "".

Certifique-se que o "RM.Host.exe" ou "RM.Host.Service.exe" do servidor de aplicação esteja iniciado e acesse a URL [http://SeuDominio/EducaMobile](http://SeuDominio)*.*

## **03. APLICAÇÃO EXTERNA**

Existe a possibilidade de adicionar links para sites externos da instituição no menu principal do Educa Mobile. Basta alterar o arquivo Menu.XML (Localizado em <*Diretório de instalação do ERP*>\CorporeRM\EducaMobile\Areas\Educacional), inserindo um novo item de Menu conforme o quadro abaixo:

xml1Exemplo - Item de menu externotrue
0
NOME DO MENU

Areas/Educacional/Content/images/mn\_AplicacaoExterna.png
LINK DA APLICAÇÃO EXTERNA
A
S
S
(...)]]>

## Referência

* TAG - ID de segurança de perfil de acesso do RM. O valor zero não irá validar perfil de acesso por usuário neste item de menu. (Uso interno, valor padrão 0)
* CAPTION - Nome da funcionalidade a ser acessada
* IMAGE - caminho da imagem a ser vinculada a funcionalidade no menu
* EXTERNALURL - URL a ser redirecionada
* TIPOUSR - Menu disponível para A - aluno ou P - professor
* SETCONTEXT - S ou N se deverá abrir a seleção de contexto antes de redirecionar para URL Externa
* MODULE - Indicativo do módulo associado a funcionalidade (Uso interno, valor padrão S)

## URL Segura (HTTPs)

A funcionalidade de Aplicação Externa incluí a página indicada dentro de uma TAG de IFrame do Educa Mobile.

Caso seja incluído uma URL segura (HTTPs), alguns *browsers* podem bloquear o acesso, apresentando o erro: "Refused to display '[https://www.URLEXTERNA.com/](https://www.globo.com/)' in a frame because it set 'X-Frame-Options' to 'sameorigin'.".

A URL a ser adicionada deve atender os seguintes critérios:

* A URL segura, de destino, deve estar no mesmo domínio do Educa Mobile; ou
* O site referenciado deve permitir acesso do Educa Mobile via IFRAME. No servidor WEB deverá permitir que a URL receba requisições do Educa Mobile.

xml1Web.configtrue



(...)]]>

Exemplo de configuração do Web.Config no IIS do servidor WEB da **aplicação destino**

Caso não tenha acesso ao Servidor Web da URL, não será possível realizar a configuração acima, sendo assim não poderá utilizar este endereço como Aplicação Externa.

**1º exemplo:** adicionando a URL do Google (<https://www.google.com.br)> não será exibida no Educa Mobile, pois este link tem a origem de um servidor diferente e o *browser* irá bloquear.

**2º exemplo:** quero adicionar a URL do site de LMS da instituição no Educa Mobile. Devo disponibilizar o Educa Mobile no mesmo domínio ou permitir acesso a URL do Educa Mobile no servidor WEB da aplicação de LMS.

Referências

Um exemplo de configuração do parâmetro "X-Frame-Options"  no Corpore.Net

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023802492-RM-Frame-utilizar-o-RM-Portal-Corpore-Net-em-iFrame>

Especificação técnica sobre "X-Frame-Options"

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options>

Aplicação Externa (Sessão do Usuário)

Para mais informações sobre **Aplicação Externa (Sessão do Usuário)**, [clique aqui.](https://tdn.totvs.com/x/oMXaJw)

## **04. CONFIGURAR TEMPO DE SESSÃO DO TOTVS Educa Mobile**

false

Essa funcionalidade estará disponível a partir da versão: 12.1.31.195

O Professor/Aluno/Responsável será informado referente ao tempo de sessão do Educa Mobile, com o objetivo de orientar e tomar alguma ação antes do usuário ser redirecionado para a tela de login.

Ao acessar a algum menu, será apresentado um contador no campo superior direito.

Esse contador tem como objetivo, informar ao usuário o tempo restante de sessão; a sessão será renovada em cada ação na tela (troca de acesso ao menu, clicar para visualizar algum dado, etc).

Quando o tempo de sessão estiver próximo de expirar, será apresentado uma mensagem de alerta/confirmação, e perguntará ao usuário se o mesmo deseja renovar a sessão, ao clicar em OK, a sessão será renovada automaticamente para o tempo **total** parametrizado no web.config

## Parametrizar o tempo **Total** da sessão

Para realizar o tempo total de sessão ao acessar os menus, será necessário acessar o web.config do TOTVS Educa Mobile e informar o tempo total de sessão, que está configurado em minutos.  
Por default (seguindo o mesmo tempo definido no Portal Corpore.Net) está configurado em 20 minutos.

 **Acessar a Tag:**<sessionState mode="InProc" customProvider="DefaultSessionProvider" timeout="**20**">

## Parametrizar o tempo **Restante** da sessão

Para realizar o a configuração do tempo restante de sessão, será necessário acessar o web.config do TOTVS Educa Mobile e informar o tempo de sessão, que está configurado em minutos.

Por default, o tempo informado para notificar o cliente é de 5 minutos.

**Acessar a Tag:**  <add key="TimeMessageSessionExpired" value="**5**" />

false

## **Meu eduCONNECT**

Ao acessar o menu: **Acadêmico**, quando o tempo expirar e o usuário não renovar a sessão, o usuário será redirecionado para a tela de login. Para realizar o login, basta o usuário mudar de menu e acessar novamente o menu: Acadêmico, que o login será realizado automaticamente, sem a necessidade de informar o usuário e senha.

Para ambientes que utilizam: LoadBalance

Para ambientes que utilizam *LoadBalance,* é necessário conferir a documentação disponível em: <https://tdn.totvs.com/x/fICqCQ>

## **05. PARAMETRIZAÇÃO PARA EXIBIR A FOTO DO ALUNO**

O professor tem a opção de visualizar a foto do aluno ao acessar os menus: Notas/faltas, Digitação de frequência diária, Cadastro de ocorrências, Notas de avaliação (menus que contemplam o Diário de Classe).

Para habilitar essa funcionalidade, é necessário habilitar o parâmetro em: Gestão Educacional | Educacional | Parâmetros | Secretaria | Geral 5/7 - Exibir foto do aluno nas listagens no diário de Classe.

Após habilitar, esse parâmetro e logar no TOTVS Educa Mobile, e acessar os menus que envolvem o Diário de Classe, caso o aluno tenha uma foto vinculada em seu cadastro, o mesmo será exibido.

false

Se no cadastro do aluno, o mesmo não tiver um foto, será exibido a imagem em seu cadastro ao logar nas funcionalidades citadas acima.
