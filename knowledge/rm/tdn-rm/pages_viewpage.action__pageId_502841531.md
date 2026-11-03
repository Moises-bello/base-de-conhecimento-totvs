---
content_hash: d4a79bb27fcd234468497bf1ccd6dfc8bceb54ccd744e7e5c0fa40af065e509c
fetched_at: '2026-06-29T00:10:25.363982+00:00'
page_id: '502841531'
product: rm
source: tdn-rm
title: EDU0001 - Configuração do AppServer e Dbaccess SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502841531
version: 67
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | BackOffice Protheus Versão 12 |
| **Versões:** | 12 |
| **Ocorrência:** |  |
| **Ambiente:** | ORACLE |
| **Passo a passo:** | Configuração Appserver.ini e DBaccess  **INSTALANDO DBACCESS COMO SERVIÇO**  Após abrir o local onde foi instalado o DBAcces.exe e no caminho do diretório, crie um atalho para para o aplicativo DBAcces.exe      No atalho insira no final em Propriedade / Destino: –install e execute.  importante: Em alguns casos o execute o atalho como administrador.    O DBAccess será instalado como serviço como mostra a figura abaixo.      **EXECUTANDO****DBACCESS NO MODULO CONSOLE**  Outra maneira de configurar o DBAcces sem instalar como serviço é:  Abra a pasta onde o DBAccess foi instalado e crie um atalho do DBAccess.exe e do DBMonitor.exe na área de trabalho.  Selecione o atalho do DBAccess e abra as propriedades do mesmo. No campo Destino no final do caminho insira: -console. ( Como mostra a figura abaixo )      Após: Basta inciar o DBAccess.exe  **Importante!!** Quando o DBAcces é iniciado dessa forma, sempre que for fechar é necessário digitar CTRL + C, e YES para confirmar.  Após confirmar é necessário aguardar o aplicativo fechar sozinho. Este procedimento deve ser realizado para não dar inconsistências na base.    **CONFIGURAÇÕES DO DBMONITOR** Adiciona uma conecção ODBC no DNS de sistema apontando para a base de dados do PROTHEUS.  Com o DBAccess iniciado, clicar em DBMonitor para configurar os bancos ( RM e Protheus )    Para configurarmos a conexão é necessário entrar em : Configurações | Oracle ou SQL.  Clique em :  “Novo” e informe a base Protheus e RM, o nome do usuário e a senha do usuário que tenha acesso as tabelas dos Bancos.  **Importante :** Marque o checkbox “Usar BLOB para campo MEMO”  para Oracle.      **Importante!**  O DBAccess precisa que o caminho para a biblioteca do Oracle seja informada para o seu correto funcionamento.  Fazemos isto através do arquivo DBAccess.ini no diretório onde foi instalado o DBAccess. Edite o arquivo e acrescente a propriedade clientlibrary abaixo da chave [Oracle] e informe o caminho da instalação da Dll oci.dll        Após finalizarmos a configuração das conexões podemos realizar o teste das mesmas através da aba “Assistentes”. Clique no botão “Validação de Conexão”.  Clique em “Avançar”. Selecione o SGBD e clique em “Avançar”. Informe o nome da conexão criada e clique em “Finalizar”.      Conexão encontra-se OK.          **Configuração do APPSERVER.INI**  Nesta parte da configuração do Protheus, iremos configurar o arquivo appserver.ini. Ele se encontra na pasta appserver, no diretório onde foi instalado o Protheus: C:\P12a\Protheus\bin\appserver ( Exemplo da instalação )    Seção Environment  Deve possuir as propriedades:  [Environment]  SOURCEPATH=pasta onde se encontra o RPO  ROOTPATH=pasta protheus data  STARTPATH=nome da pasta system  RPODB=tipo de conexão (TOP)  RPOLANGUAGE=linguagem do RPO (Portuguese)  RPOVERSION=versão do RPO (120)  LOCALFILES=tipo dos arquivos locais (ADS)  LOCALDBEXTENSION=extensão das tabelas locais (.dbf)  PICTFORMAT=DEFAULT  REGIONALLANGUAGE=localização (BRA)  TOPSERVER=endereço do DBAccess  TOPPORT=porta do DBAccess (7890)  DBDATABASE=banco de dados (MSSQL/ORACLE)  TOPALIAS=alias do banco Protheus        Notas:  **o** Algumas propriedades podem se encontrar na sessão DBAccess. Neste caso, retire as mesmas dessa sessão e transfira-as para a sessão Environment, inserindo TOP na frente. A sessão DBAccess deixa de existir.  **o** Altere o nome Environment por um nome que represente a conexão que está sendo criada.  **o** Caso esteja montando dois ambientes – Oracle e MSSQL – basta criar outra seção Environment.        Seção Geral  Deve possuir as propriedades:  [GENERAL]  InstallPath=pasta do Protheus  console=loga no console (0/1)  BuildKillUsers=desconecta todos os usuários quando compilar o RPO (0/1)  LogEnable=habilitar arquivo de log (0/1)  ConsoleLog=loga no console (0/1)  consolemaxsize=tamanho máximo do log (10000000)  ConsoleFile=arquivo de log  Segmento=cYdTm3WWERZF=1hu  Serie===AV        Seções [TCP], [Drivers] e [GENTCPIP]  Devem possuir as propriedades:  [TCP]  TYPE=TCPIP  Port=porta do appserver 33  [Drivers]  Active=TCP  [GENTCPIP]  Enable=0   * · Seção LICENSECLIENT   Deve possuir as propriedades:  [LICENSECLIENT]  server= servidor  port= porta |
| **Observações:** |  |

divs
