---
content_hash: 625de899f26a79b452db4b707c79f512675deca228cc3da60f222b92b4727ad2
fetched_at: '2026-06-28T21:35:23.529422+00:00'
page_id: '257622840'
product: fluig
source: tdn-fluig
title: Instalação da plataforma em Windows - Instalador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257622840
version: 41
---

3.\*ndice

# Pré-requisitos requisitos

---

Antes de iniciar uma instalação, certifique-se de que os procedimentos e requisitos abaixo foram preenchidos:

* Leia atentamente o .

* Verifique se as configurações e especificações do servidor estão de acordo com os requisitos estipulados no [Dimensionamento](http://tdn.totvs.com/display/fluig/Dimensionamento) e na [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade).

* Confirme se a base de dados da plataforma foi criada em um banco de dados homologado, conforme as orientações descritas em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464), [SQL Server](http://tdn.totvs.com/pages/viewpage.action?pageId=257623499) ou [Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).

# Passo a passo para a instalação da plataforma

---

A seguir, acompanhe o passo a passo para instalação da plataforma em Windows:

Atenção!

Por questões de segurança, orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

0.5falseinstall-windowsfadetrue101Selecione a linguagem

* Na primeira tela, o idioma da mídia de instalação deve ser selecionado.

202Termo de uso

* Em **Termo de uso**, é exibido o contrato de licença do produto que contém os termos de uso, *copyright* e recomendações para a execução da instalação que deverão ser lidos atentamente.

* Para prosseguir, assinale a opção **Eu concordo com este contrato de licença** e em seguida, clique em **Próximo**.

303Instalação do fluig

* Em **Instalação do TOTVS Fluig**, informe se deverá ser realizada a instalação ou a atualização da plataforma.

* Mantenha assinalada a opção **Instalar o TOTVS Fluig**.

Dica!

Se ao invés de instalar um novo ambiente você deseja atualizar uma instalação existente, acesse o .

404Diretório de Instalação

* Em **Diretório de instalação** informe o diretório destino da aplicação. Por padrão a pasta de instalação será chamada "fluig" e ficará armazenada na unidade em que o sistema operacional está instalado. Por exemplo: "C:\fluig".

Importante!

Não é permitida a instalação da plataforma em pastas cujo nome contenha acentuações e/ou espaços.

505Dados do Servidor

* Em **Dados do servidor** devem ser preenchidas as informações de acesso ao servidor Fluig.

* O campo **Endereço IP** é preenchido automaticamente pelo instalador, porém confirme se este é o IP correto de acesso ao servidor, pois em um servidor com múltiplas interfaces de rede, a sugestão de endereço IP pode não ser a interface de rede principal.

* **Porta:** porta do servidor que será utilizada para a execução da plataforma.

* **URL pública**: endereço público pelo qual a plataforma pode ser acessada.

Nota:

A plataforma não permite o uso do "*localhost*" no campo Endereço IP. Para ambientes focados exclusivamente em desenvolvimento sobre a plataforma ou treinamento, recomendamos o uso do endereço "127.0.0.1" ou o *hostname* do servidor.

606Banco de Dados

* Em **Banco de dados** selecione o banco mais adequado às suas necessidades.

Importante!

O sistema gerenciador do banco de dados deve estar instalado e o banco ou instância deve ter sido previamente criado, conforme os pré-requisitos listados no .

707Conexão com banco de dados

* Nesta etapa informe os dados para conexão com o banco de dados.

* Cada banco de dados possui uma configuração de conexão distinta, portanto confira abaixo as informações necessárias para cada um dos banco de dados e utilize o guia referente ao banco de dados selecionado anteriormente:

0.5falsedb-configfademysqlMySQLImportante!

Para o **banco de dados MySQL**, é necessário que a base seja criada conforme descrito em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464).

Para configurar a conexão com um banco de dados MySQL, é necessário informar os seguintes dados:

* **Arquivo do Driver:** informe o caminho do driver MySQL. Para obter o driver do MySQL, consulte a página [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464#Configura%C3%A7%C3%A3odebancodedadosMySQL-1.6-DownloaddoDriver);

* **Usuário:** usuário utilizado para conexão com o banco de dados;

* **Senha:** senha do usuário utilizado para conexão com o banco de dados;

* **Servidor:** endereço do servidor;

* **Porta:** porta lógica do servidor;

* **Banco:** nome do banco de dados.

sqlserverSQL ServerImportante!

Para o **banco de dados SQL Server**, é necessário que a base seja criada conforme descrito em [Configuração do banco de dados SQL Server](http://tdn.totvs.com/pages/viewpage.action?pageId=257623499).

Para configurar a conexão com um banco de dados Microsoft SQL Server, é necessário informar os seguintes dados:

* **Usuário:** usuário utilizado para conexão com o banco de dados;

* **Senha:** senha do usuário utilizado para conexão com o banco de dados;

* **Servidor:** endereço do servidor;

* **Porta:** porta lógica do servidor;

* **Banco:** nome do banco de dados;

* **Instância:** nome da instância do SQL Server.

oracleOracleImportante!

Para o **banco de dados Oracle**, é necessário realizar algumas configurações para inicialização da plataforma, conforme detalhes em [Configuração do banco de dados Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).

Para um banco de dados Oracle é necessário informar os seguintes dados:

* **Usuário:** usuário utilizado para conexão com o banco de dados;

* **Senha:** senha do usuário utilizado para conexão com o banco de dados;

* **Servidor:** endereço do servidor;

* **Porta:** porta lógica do servidor;

* **Banco:** SID (Oracle *System Identifier*) da instância do banco de dados.

808Configuração de Email

* Em **Configuração de e-mail** os campos não são obrigatórios. Poderão ser informados o endereço do **Servidor SMTP**, a **Porta SMTP** e o **E-mail do remetente** padrão para envio de notificações a respeito das ações tomadas na plataforma.

* Caso o servidor SMTP exija autenticação é necessário assinalar a opção **Servidor exige autenticação** e informar um usuário e senha válido.

909Servidor de Licenças

* Em **Tipo de licenciamento** escolha a opção mais adequada para seu ambiente.

99ºTipo de Licencimaneto

* Nesta etapa são oferecidas duas opções de licenciamento. Cada uma é configurada de forma diferente na plataforma.

* Clique nas opções abaixo e verifique.

0.5falsedb-configfadelsLicense Server

Em **Servidor de licenças**, informe o endereço do **Servidor de licenças** e **Porta do servidor de licenças** para que a plataforma seja habilitada para uso. Esta configuração é válida para todas as empresas cadastradas. Os valores preenchidos podem ser editados após a instalação pelo painel administrativo da plataforma.

Importante!

Os valores preenchidos automaticamente pelo instalador são apenas uma sugestão e não apontam necessariamente para um servidor de licenças válido.

Clientes *cloud* devem abrir um *ticket* para a Equipe de atendimento Cloud TOTVS solicitando alteração do *License Server*.

partnerFluig Identity Partner

O**Fluig Identity Partner** é um novo modelo de licenciamento que utiliza o TOTVS Identity na nuvem para controlar o acesso à plataforma. Para que clientes atuais e novos utilizem o modo License Server.

Sua configuração é realizada após acessar a plataforma, utilizando um usuário com perfil de administrador.

1010Servidor de Chat

* Em **Servidor *Realtime***, assinale a opção **Habilitar *Realtime***, se desejado.

* Se a opção acima for assinalada, informe o **IP/Nome do servidor**, a **Porta pública** e a **Porta interna**.

* O mesmo servidor utilizado para a instalação da plataforma pode ser utilizado para a configuração do *Realtime*, basta informar o endereço IP preenchido no passo 5.

Nota:

O Servidor *Realtime* é responsável por atualizar a [Central de notificações](http://tdn.totvs.com/pages/viewpage.action?pageId=233763951) do usuário, sem que seja necessário atualizar toda a página da plataforma.

1111Servidor de Indexação

* Em **Servidor de indexação** é possível configurar o servidor que será utilizado no processo de indexação dos documentos do repositório. Informar a **URL** do servidor.

1212Pacotes de instalação

* Neste passo o instalador informa os pacotes do sistema que serão instalados.

* Em seguida, o instalador irá verificar a compatibilidade dos componentes de software existente no servidor e prepara a instalação com os dados informados anteriormente.

1313Instalação

* Os arquivos serão copiados para a pasta destino da instalação.

1514Executar processos externos

* Nesse passo o instalador exibe a execução dos processos externos e um relatório sobre a instalação do produto. O sistema será registrado como um serviço do Microsoft Windows.

1615Instalação terminada

* A instalação da plataforma é concluída com sucesso. Clique em **Ok** e, depois, em **Sair** para encerrar.

Importante!

Por questões de segurança, é altamente recomendável efetuar a encriptação da senha conforme o procedimento informado .

# Inicialização da plataforma

---

O Fluig será instalado como um serviço no Microsoft Windows. Para iniciar ou interromper a aplicação, acesse a partir do Menu Iniciar: **Painel de Controle** → **Ferramentas Administrativas** → **Serviços**.

Antes de iniciar os serviços do Fluig, é necessário alterar o usuário de inicialização. Os serviços fluig\_Indexer, fluig\_RealTime e fluig devem ser inicializados, nesta ordem, por um usuário que tenha privilégios de administrador no servidor onde fluig foi instalado. Para isso, siga os seguintes passos:

**01.** Clique com o botão direito do mouse sobre um dos serviços do Fluig;

**02.** Selecione a opção **Propriedades**;

**03.** Selecione a aba **Logon** no topo da janela;

**04.** Selecione a opção **Esta conta** e informe um usuário com privilégios administrativos no servidor.

Esse procedimento deve ser realizado nos três serviços do Fluig. Uma vez concluída a configuração, inicie o fluig\_Indexer, o fluig\_RealTime e o fluig, nesta ordem.

Para acompanhar o processo de inicialização, acesse a pasta de instalação da plataforma, navegue até o diretório [diretório\_instalação]\appserver\standalone\log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log (até a **1.8.2**) e consulte o arquivo **server.log**. Quando a inicialização estiver concluída, a seguinte mensagem será exibida neste arquivo:

# Primeiro acesso

---

Para informações sobre os próximos passos, que envolvem o primeiro acesso à plataforma, acesse a documentação .
