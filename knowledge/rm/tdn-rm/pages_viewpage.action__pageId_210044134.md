---
content_hash: 551fb8d1044a2a6d763c38327dd14d1d8e21a76af4eb5751c8c4251394f33790
fetched_at: '2026-06-29T00:06:14.338256+00:00'
page_id: '210044134'
product: rm
source: tdn-rm
title: EDU0001 - Configuração do AppServer e Dbaccess
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210044134
version: 97
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | BackOffice Protheus Versão 12 |
| **Versões:** | 12 |
| **Ocorrência:** |  |
| **Ambiente:** | ORACLE |
| **Passo a passo:** | Configuração DBaccess e Appserver.ini  Antes de configurar o DBACCESS e Appserver.ini lembrar de criar um fonte de dados ODBC para bases de dados Sql Server ou Oracle.  ****Configuração do** DBACCESS**  Após abrir o local onde foi instalado o DBAcces.exe e no caminho do diretório, insira no final –install        O DBAccess será instalado como serviço como mostra a figura abaixo.        **Observação:**  Outra maneira de configurar o DBAcces sem instalar como serviço é:  Abra a pasta onde o DBAccess foi instalado e crie um atalho do DBAccess.exe e do DBMonitor.exe na área de trabalho.  Selecione o atalho do DBAccess e abra as propriedades do mesmo. No campo Destino no final do caminho insira: -console. ( Como mostra a figura abaixo )        Após : Basta inciar o DBAccess.exe  **Importante!!** Quando o DBAcces é iniciado dessa forma, sempre que for fechar é necessário digitar CTRL + C, e YES para confirmar.  Após confirmar é necessário aguardar o aplicativo fechar sozinho. Este procedimento deve ser realizado para não dar inconsistências na base.        Com o DBAccess iniciado , clicar em DBMonitor para configurar os bancos ( RM e Protheus )        Para configurarmos a conexão Oracle, é necessário entrar em : Configurações | Oracle.  Clique em :  “Novo” e informe a base Protheus e RM, o nome do usuário e a senha do usuário que tenha acesso as tabelas dos Bancos.  **Importante :** Marque o checkbox “Usar BLOB para campo MEMO”.        **Importante!**  O DBAccess precisa que o caminho para a biblioteca do Oracle seja informada para o seu correto funcionamento.  Fazemos isto através do arquivo DBAccess.ini no diretório onde foi instalado o DBAccess. Edite o arquivo e acrescente a propriedade clientlibrary abaixo da chave [Oracle] e informe o caminho da instalação da Dll oci.dll        Após finalizarmos a configuração das conexões podemos realizar o teste das mesmas através da aba “Assistentes”. Clique no botão “Validação de Conexão”.  Clique em “Avançar”. Selecione o SGBD e clique em “Avançar”. Informe o nome da conexão criada e clique em “Finalizar”.        Conexão encontra-se OK.          **Configuração do APPSERVER.INI**  Nesta parte da configuração do Protheus, iremos configurar o arquivo appserver.ini. Ele se encontra na pasta appserver, no diretório onde foi instalado o Protheus: C:\P12a\Protheus\bin\appserver ( Exemplo da instalação )    Seção Environment  Deve possuir as propriedades:  [Environment]  SOURCEPATH=pasta onde se encontra o RPO  ROOTPATH=pasta protheus data  STARTPATH=nome da pasta system  RPODB=tipo de conexão (TOP)  RPOLANGUAGE=linguagem do RPO (Portuguese)  RPOVERSION=versão do RPO (120)  LOCALFILES=tipo dos arquivos locais (ADS)  LOCALDBEXTENSION=extensão das tabelas locais (.dbf)  PICTFORMAT=DEFAULT  REGIONALLANGUAGE=localização (BRA)  TOPSERVER=endereço do DBAccess  TOPPORT=porta do DBAccess (7890)  DBDATABASE=banco de dados (MSSQL/ORACLE)  TOPALIAS=alias do banco Protheus        Notas:  **o** Algumas propriedades podem se encontrar na sessão DBAccess. Neste caso, retire as mesmas dessa sessão e transfira-as para a sessão Environment, inserindo TOP na frente. A sessão DBAccess deixa de existir.  **o** Altere o nome Environment por um nome que represente a conexão que está sendo criada.  **o** Caso esteja montando dois ambientes – Oracle e MSSQL – basta criar outra seção Environment.        Seção Geral  Deve possuir as propriedades:  [GENERAL]  InstallPath=pasta do Protheus  console=loga no console (0/1)  BuildKillUsers=desconecta todos os usuários quando compilar o RPO (0/1)  LogEnable=habilitar arquivo de log (0/1)  ConsoleLog=loga no console (0/1)  consolemaxsize=tamanho máximo do log (10000000)  ConsoleFile=arquivo de log  Segmento=cYdTm3WWERZF=1hu  Serie===AV        Seções [TCP], [Drivers] e [GENTCPIP]  Devem possuir as propriedades:  [TCP]  TYPE=TCPIP  Port=porta do appserver 33  [Drivers]  Active=TCP  [GENTCPIP]  Enable=0   * · Seção LICENSECLIENT   Deve possuir as propriedades:  [LICENSECLIENT]  server= servidor  port= porta      **[Retornar](http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.totvsEducacional.aspx)** |
| **Observações:** |  |

divs
