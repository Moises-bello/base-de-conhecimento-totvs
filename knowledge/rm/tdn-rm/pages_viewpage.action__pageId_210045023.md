---
content_hash: 1bff40c54aaf2bc093307001ac27ea7116cdf79dae49fd85fa992ae644db2bdd
fetched_at: '2026-06-29T00:06:14.386486+00:00'
page_id: '210045023'
product: rm
source: tdn-rm
title: EDU0002 - Configuração EAI Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210045023
version: 106
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Educacional & BackOffice Protheus |
| **Versões:** | 12 |
| **Ocorrência:** |  |
| **Ambiente:** | ORACLE |
| **Passo a passo:** | Configuração do EAI ( BackOffice Protheus )  Entrar no Protheus em qualquer módulo para que possa ser carregada as tabelas ( Em caso de primeiro acesso em base vazia )  Acesso ( Ex: SIGAADV )        No processo de dar carga nas Tabelas do Protheus, clicar em : data        Processo prossegue criando as Tabelas do Protheus      **EXISTE ESSE DOCUMENTO PARA FALAR SOBRE A CONFIGURAÇÃO DO EAI**  Após o processo de criação das Tabelas, abra o SmartClient com ( **APWEBWIZARD** ) como mostra a figura abaixo        Usuário : admin  Senha : ( Em branco )  OK em seguida          Clicar em Inserir um Novo módulo como mostra a figura abaixo e em seguida / Módulos Web        Em módulo web selecione WS Microsiga Protheus 11 Web Services  Nome da instância = EAI  O diretório raiz é preenchido automaticamente  Selecione o enviroment (Ambiente) ( Informado no Appserver.ini )  O parâmetro habilitar processos faz o WS subir automaticamente com o appserver e criará a tag ONSTART=\_\_WSSTART    no .ini        Neste assistente, é necessário informar **NO HOST**: Localost, o IP da máquina e o nome da máquina , todos com a porta em seguida. Como é informado no Print abaixo.  Ao adicionar cada host, é necessário em seguida selecionar a filial (não é necessário fazer o procedimento para todas as filiais)  E clicar em relacionar. O registro aparecerá na parte de baixo da janela.  Relacionar com filial o Nome da máquina e IP também.  A imagem abaixo mostra como ficou após o processo de configuração        Insira o número mínimo de usuários e o número máximo. Clique em avançar  ( No exemplo abaixo é informado 1 para mínimo e 5 para máximo )        Confirmar ( SIM ) Instalar o Módulo Web - EAI        As configurações serão validadas somente após o servidor Protheus for reiniciado.        Criada configuração automaticamente no Appserver.ini do EAI ( Protheus )        Estes Campos tem que ser incluídos Manualmente caso não esteja marcado o Parâmetro : Habilitar processos na inicialização do servidor  Criada configuração automaticamente no Appserver.ini do EAI ( Protheus )        Testando WS Protheus  Iniciando Servidor Protheus ( Appserver.ini )        <http://localhost:89/EAISERVICE.apw?WSDL>  ( Testando WS Protheus )  Inserir o IP da máquina , Localhost ou Nome da máquina junto com a Porta e em seguida ( [EAISERVICE.apw?WSDL](http://localhost:89/EAISERVICE.apw?WSDL) )      agenteeagendamento  Para configurar o EAI Protheus com o TOTVS Educacional, precisamos cadastrar o JOB que irá monitorar a fila de integração. Esta configuração é feita no módulo SIGACFG do Protheus.  Inicie o appserver, em seguida  o smartclient. Informe usuário e senha.        Confirmar        Acesse: Ambiente | Schedule | Schedule. (  Após: Schedule | Agent | Cadastro )  Clique em Incluir para cadastrar o JOB. Insira as informações solicitadas e salve o cadastro.        Depois em Agendamento|Cadastro. Clique em incluir e informe a Rotina: FWEAI e Empresa/Filial: Informe a empresa        Após o cadastro do Agendamento , clicar no Local indicado para configurar a execução do mesmo !!!        **NESSE DOCUMENTO FALA SOBRE O DE/PARA DE EMPRESA  E TAMBÉM ADAPTER**  Cadastrar De Para ( Protheus / RM )  Ambiente | Shedule | Emp. Filial Mensage...                                  Cadastrando os Adapters ( Que serão utilizados na Integração com TOTVS Educacional )  Ambiente | Shedule | Adpater E.a.i                                Versão divergente – Editar no Protheus o Adapter para que fique na mesma Versão do Adpater cadastrado no TOTVS Educacional          Selecionar o Adpter , Alterar e mudar a versão. |
| **Observações:** |  |

divs
