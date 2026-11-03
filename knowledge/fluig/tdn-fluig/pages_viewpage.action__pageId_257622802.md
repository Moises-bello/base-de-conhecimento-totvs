---
content_hash: ff83836d3d9b3d298c1b41efe3daa19802da834bb1346b2b725f845d4a1253e1
fetched_at: '2026-06-28T21:35:23.510927+00:00'
page_id: '257622802'
product: fluig
source: tdn-fluig
title: Instalação da plataforma no Linux - Instalador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257622802
version: 51
---

3.\*ndice

# Pré-requisitos requisitos

---

Antes de iniciar uma instalação, certifique-se de que os procedimentos e requisitos abaixo foram preenchidos:

* Leia atentamente o .

* Verifique se as configurações e especificações do servidor estão de acordo com os requisitos estipulados no [Dimensionamento](http://tdn.totvs.com/display/fluig/Dimensionamento) e na [Matriz de Portabilidade](http://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade).

* Confirme se a base de dados foi criada em um banco de dados homologado, conforme as orientações descritas em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464), [SQL Server](http://tdn.totvs.com/pages/viewpage.action?pageId=257623499) ou [Oracle](http://tdn.totvs.com/pages/viewpage.action?pageId=257623480).

* Conheça as orientações listadas no documento [Configurações sugeridas em ambientes Linux.](http://tdn.totvs.com/pages/viewpage.action?pageId=242389225)

* É obrigatório que a instalação da plataforma seja realizada utilizando o usuário **root** ou um usuário que tenha os privilégios de instalação de pacotes e alteração de serviços.

Importante!

É necessário que o usuário utilizado para iniciar o serviço do Fluig seja o mesmo usuário proprietário (owner) da pasta de instalação.

* Para realizar a instalação, será necessário possuir um gerenciador de interface gráfica ativo no Linux. Para instalações em modo caractere, acesse .

* Ter instalado o pacote *unzip* para descompactação de arquivos.

# Distribuições homologadas

---

As distribuições Linux homologadas para a plataforma TOTVS Fluig podem ser consultadas na .

Orientação de segurança

Por motivos de segurança recomendamos que, após a instalação da plataforma em ambientes Linux, seja retirado o usuário como root seguindo o processo na documentação [Configurar ambiente Linux para não utilizar o usuário root](http://tdn.totvs.com/x/v2cWGw).

# Passo a passo para a instalação da plataforma

---

Atenção!

Por questões de segurança orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

Abra o terminal do sistema operacional e execute o seguinte comando:

bash

Em seguida, acompanhe o passo a passo para instalação gráfica do Fluig em Linux:

0.5falseinstall-linuxfadetrue101Selecione a linguagem

* Na primeira tela, o idioma da mídia de instalação deve ser selecionado.

202Termo de uso

* Em **Termo de uso** é exibido o contrato de licença do produto que contém os termos de uso, *copyright* e recomendações para a execução da instalação que deverão ser lidos atentamente.

* Para prosseguir, assinale a opção **Eu concordo com este contrato de licença** e em seguida, clique em **Próximo**.

303Instalação da plataforma

* Em **Instalação do TOTVS Fluig** informe se deverá ser realizada a instalação ou atualização da plataforma.

* Mantenha assinalada a opção **Instalar o TOTVS Fluig**.

404Diretório de Instalação

* Em **Diretório de instalação** informe o diretório destino da aplicação. Por padrão a pasta de instalação será chamada "fluig" e ficará armazenada na unidade em que o sistema operacional está instalado. Por exemplo: "/opt/fluig".

Importante!

Não é permitida a instalação da plataforma em pastas cujo nome contenha acentuações e/ou espaços.

505Dados do Servidor

* Em **Dados do servidor** devem ser preenchidas as informações de acesso ao servidor Fluig.

* O campo **Endereço IP** é preenchido automaticamente pelo instalador, porém confirme se este é o IP correto de acesso ao servidor, pois em um servidor com múltiplas interfaces de rede, a sugestão de endereço IP pode não ser a interface de rede principal.

* **Porta:** porta do servidor que será utilizada para a execução da plataforma.

* **URL pública**: endereço público pelo qual a plataforma pode ser acessada.

A plataforma não permite o uso do "*localhost*" no campo Endereço IP. Para ambientes focados exclusivamente em desenvolvimento sobre a plataforma ou treinamento, recomendamos o uso do endereço "127.0.0.1" ou o *hostname* do servidor.

606Banco de Dados

* Em **Banco de dados** selecione o banco mais adequado às suas necessidades.

Importante!

O sistema gerenciador do banco de dados deve estar instalado e o banco ou instância deve ter sido previamente criado, conforme os pré-requisitos listados no .

707Conexão com Banco de Dados

* Nesta etapa informe os dados para conexão com o banco de dados.

* Cada banco de dados possui uma configuração de conexão distinta, portanto confira abaixo as informações necessárias para cada um dos banco de dados e utilize o guia referente ao banco de dados selecionado anteriormente:

0.5falsedb-configfademysqlMySQLImportante!

Para o **banco de dados MySQL**, é necessário que a base seja criada conforme descrito em [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464);

 Para configurar a conexão com um banco de dados MySQL, é necessário informar os seguintes dados:

* **Arquivo do Driver:** informe o caminho do driver MySQL. Para obter o driver do MySQL, consulte a página [Configuração de banco de dados MySQL](http://tdn.totvs.com/pages/viewpage.action?pageId=257623464#ConfiguraçãodebancodedadosMySQL-DownloaddoDriver);

* **Usuário:** usuário utilizado para conexão com o banco de dados;

* **Senha:** senha do usuário utilizado para conexão com o banco de dados;

* **Servidor:** endereço do servidor;

* **Porta:** porta lógica do servidor;

* **Banco:** nome do banco de dados.

sqlserverMicrosoft SQL ServerImportante!

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

* Em **Configuração de *e-mail*** os campos não são obrigatórios. Poderão ser informados o endereço do **Servidor SMTP**, a **Porta SMTP** e o ***E-mail* do remetente** padrão para envio de notificações a respeito das ações tomadas no Fluig.

* Caso o servidor SMTP exija autenticação é necessário assinalar a opção **Servidor exige autenticação** e informar um usuário e senha válidos.

909Servidor de Licenças

* Em **Tipo de licenciamento** escolha a opção mais adequada para seu ambiente.

99ºTipo de Licencimaneto

* Nesta etapa são oferecidas duas opções de licenciamento. Cada uma é configurada de forma diferente na plataforma.

* Clique nas opções abaixo e verifique.

0.5falsedb-configfadelsLicense Server

Em **Servidor de licenças** informe o endereço do **Servidor de licenças** e **Porta do servidor de licenças**, para que a plataforma seja habilitada para uso. Esta configuração é válida para todas as empresas cadastradas. Os valores preenchidos podem ser editamos após a instalação através do painel administrativo da plataforma.

Importante!

Os valores preenchidos automaticamente pelo instalador são apenas uma sugestão e não apontam necessariamente para um servidor de licenças válido.

Clientes Cloud devem abrir um ticket para a Equipe de Atendimento Cloud TOTVS solicitando alteração do License Server.

partnerFluig Identity Partner

O**Fluig Identity Partner** é um modelo de licenciamento que utiliza o TOTVS Identity na nuvem para controlar o acesso à plataforma. Para que clientes atuais e novos utilizem o modo License Server.

Sua configuração é realizada após acessar a plataforma, utilizando um usuário com perfil de administrador.

1010Servidor Realtime

* Em **Servidor *Realtime***, assinale a opção **Habilitar *Realtime***, se desejado.

* Se a opção acima for assinalada, informe o **IP/Nome do servidor**, a **Porta pública** e a **Porta interna**.

* O mesmo servidor utilizado para a instalação da plataforma pode ser utilizado para a configuração do *chat*, basta informar o endereço IP preenchido no passo 5.

Nota:

O Servidor de Chat é responsável por atualizar a [Central de notificações](http://tdn.totvs.com/pages/viewpage.action?pageId=233763951) do usuário, sem que seja necessário atualizar toda a página da plataforma.

1111Servidor de Indexação  

* Na tela configuração **Servidor de indexação** é possível configurar o servidor que será utilizado no processo de indexação dos documentos do repositório. Informar a **URL** do servidor.

1312Pacotes de Instalação  

* Neste passo o instalador informa os pacotes do sistema que serão instalados.

* Em seguida, o instalador irá verificar a compatibilidade dos componentes de software existente no servidor e preparar a instalação com os dados informados anteriormente.

1413Instalação  

* Os arquivos serão copiados para a pasta destino da instalação.

1514Executar processos externos  

* Nesse passo o instalador exibe a execução dos processos externos e um relatório sobre a instalação do produto. O sistema será registrado como um serviço do Microsoft Windows.

Importante!

Algumas distribuições Linux não possuem o comando **chkconfig**, o que gera um alerta informando que o comando não foi encontrado durante a execução dos processos externos da instalação. Caso isto ocorra, clique em **Sim** na caixa de diálogo aberta para continuar com o processo de instalação.

1615Instalação terminada  

* A instalação da plataforma é concluída com sucesso. Clique em **Ok** e, depois, em **Sair** para encerrar.

Importante!

Por questões de segurança é altamente recomendável efetuar a encriptação da senha conforme o procedimento informado .

Importante!

Não se esqueça de revisar as orientações apresentadas na página de [Configurações sugeridas em ambientes Linux.](http://tdn.totvs.com/pages/viewpage.action?pageId=242389225)

# Exceção Firewall

---

Caso o servidor onde a plataforma foi instalada possua *firewall* ativo é necessário adicionar exceções para as seguintes portas utilizadas pela plataforma:

* Porta do Servidor de Aplicação do Fluig;
* Porta do Servidor para RealTime;
* Porta do Servidor de Chat.

# Inicialização inicializacao

---

Os procedimentos de inicialização estão disponíveis na página .

# Primeiro acesso

---

Para informações sobre os próximos passos, que envolvem o primeiro acesso à plataforma, acesse a documentação .

Dica

Para informações sobre utilização da plataforma, acesse o , acompanhe os primeiros passos e se familiarize com o produto!
