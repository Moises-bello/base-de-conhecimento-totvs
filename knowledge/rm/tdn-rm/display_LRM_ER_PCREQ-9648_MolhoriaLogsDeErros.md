---
content_hash: b31926b75d9a4aeec03e5e8ec945d3402da931dcc264ec1202b220169120d30d
fetched_at: '2026-06-29T00:08:05.208351+00:00'
page_id: '235586657'
product: rm
source: tdn-rm
title: ER_PCREQ-9648_MolhoriaLogsDeErros
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9648_MolhoriaLogsDeErros
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo:** | EAI |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_FRW\_FRW002 | **IRM** | PCREQ-9646 |
| **Requisito1** | PCREQ-9648 | **Subtarefa:** | PDR\_FRW\_FRW002-52 |
| **Chamado2** |  | | |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo:

Melhorar as mensagens de erro do EAI e propor um mecanismo de geração e gravação de logs de execução de mensagens do EAI. 

## Introdução

Será utilizado o padrão de SysLog para geração dos Logs do EAI.

Trata-se de um padrão definido pela Totvs para implementação de mecanismos de geração de logs.

Esse padrão foi implementado na Lib RM,  e atualmente diversos recursos da Lib utilizam o mesmo. ex: DataServers, Host, Process, Jobs, etc.

## Definição da Regra de Negócio

****1) - Regras para ativação do log do EAI:****

****a) Atributo "TRACESYSLOG":****

O atributo "TRACESYSLOG" (disponível nos arquivos de configuração do Host) deve ser ativado (TRACESYSLOG" = true).

Isso possibilitará o uso do padrão SysLog nos processos do ERP, inclusive nas rotinas do EAI.

****b) - ****Atributo "TRACESYSLOGDEBUG****":************

O atributo "TRACESYSDEBUG" (disponível nos arquivos de configuração do Host) permitirá que informações de debug sejam também logadas.

A ativação desse atributo permitirá a produção de logs mais detalhados, aumentando assim o volume dos logs gerados.

****c) Atributo "****TRACESYSLOGEAI":********

Será criado o atributo "TRACESYSLOGEAI" nos arquivos de configuração do Host.

Por default, esse atributo estará desligado = "false".

Quando estiver ligado = "true", as mensagens de log do EAI serão geradas e gravadas na nova tabela de Log do EAI "HcLogMensagem".

Caso contrário, nenhum log será gravado na tabela de log do EAI.

****2) - Estrutura de tabelas****

a) **- Criação da tabela: HCMonitor.**

      Uma linha nessa tabela indicará um "monitoramento de uma determinada ação no EAI". Basicamente essa tabela será usada para agrupar mensagens relacionadas;

        Informações principais:

*ID- Identificador do monitor*  
*IDPROCESSO Identificador do processo*

Cenário:

      - Em um determinado cliente existem duas integrações mapeadas para a mensagem  "COSTCENTER 2.000" (mensagem de centro de custo);

               Integração A: RM ---> Protheus

               Integração B: RM —> DataSul

      - Ao cadastrar um centro de  custo no RM, ocorrerá o seguinte:

* O EAI RM será chamado para executar o envio da mensagem de centro de custo;
* Será gerada uma única linha na tabela HCMonitor (responsável em agrupar as mensagens geradas na fila);
* Serão geradas duas linhas na fila HCFilaMensagem (uma linha para cada integração mapeada);

**b)-   Criação da coluna "MonitorID" na tabela "HCFilaMensagem" com referência para tabela HCMonitor;**

     As mensagens gravadas na fila (HCFilaMensagem) estarão vinculadas a uma informação de monitor (HCMonitor).

**c) - Criação da tabela: HCLogMensagem.**

Todos os logs gerados para uma determinada mensagem serão gravados nessa tabela.

     Uma linha nessa tabela indicará uma única mensagem de log, ou seja, várias linhas serão incluídas nessa tabela para cada tentativa de execução da mensagem.

      Informações principais:

*UUID- Identificador da mensagem na fila*  
*SEQUENCIAL- Compor chave primária*

*DATAMENSAGEM: Data e hora da geração do log*

*LOCALIZACAO: região do eai que gerou a mensagem*

*TIPOLOG : Tipo da mensagem de log [error, warning, info]*

**Info: 0 - Mensagem de informação**

*Warning: 1 - Mensagem de aviso*

*Error: 2 - Mensagem de erro*

*INFOLOG: mensagem de log.*

*INFO*DEBUG*: Informações de debug. Nesse campo serão gravadas informações de valores de variáveis, propriedades de objetos, contextos existentes no momento da geração do log.*

**3) - Geração de logs customizados:**

a) - Será disponibilizada na classe "**HandleServices**" (localizada no projeto: *RM.Con.TotvsMessage.IServices*" uma instância para o objeto "LogServices".

Um objeto da classe "HandleServices" está disponível atualmente nos *extensions* e estará disponível nas futuras classes de adapters.

b) - Será disponibilizado no objeto "LogServices" três métodos:

       - WriteTraceInformation: responsável pelo envio de mensagens de informação;

       - WriteTraceError: responsável pelo envio de mensagens de erro;

      - WriteTraceWarning: responsável pelo envio de mensagens de aviso;

        Esses métodos recebem como parâmetro os seguintes dados:

* + Identificador do monitor : disponível no contexto global do EAI. (this.TotvsMessageContext.Monitor.MonitorId);
  + Mensagem de log: texto contendo a mensagem de log;
  + Informações de debug: Devem ser enviadas no seguinte formato: "Identificação da inf. de debug", "Valor da informação de debug";

   Segue abaixo um exemplo de criação customizada de logs nos adapters / extensions:

**4) - Mapeamento dos logs gerados pela engine do EAI**

Abaixo serão listados todos os logs a serem disponibilizados durante o processo de gravação e execução da mensagem.

Todas as mensagens de erro logadas serão acompanhadas de seus respectivos erros técnicos (exceções geradas).

A coluna "Todas as marcas" indicará se o log deve ou não ser implementado nos EAIs das outras marcas.

a) - Informações de log disponibilizadas durante o processo de "Recebimento de mensagens":

|  |  |  |  |
| --- | --- | --- | --- |
| **Localização** | **Mensagem** | **Tipo de menagem**  **E -**  **A -**  **I -** | **Todas as marcas** |
| Fila | INÍCIO DO PROCESSO DE SALVAR MENSAGEM DE RECEBIMENTO NA FILA | I | Sim |
| Fila | Xml recebido é válido | I | Sim |
| Fila | Xml recebido não é válido | E | Sim |
| Fila | Integrações recuperadas. | I | Sim |
| Fila | Id da integração recuperada | I | Não |
| Fila | Não foi possível localizar nenhuma integração. | E | Sim |
| Fila | Não foi encontrada nenhuma entidade mapeada. | E | Não |
| Fila | Mapa de integração carregado. | I | Não |
| Fila | Erro ao carregar mapa de integração. | E | Não |
| Fila | XSLT de entrada não foi preenchido. | E | Não |
| Fila | Recebimento de mensagem assíncrona. | I | Sim |
| Fila | Evento CanSaveQueue será executado. | I | Não |
| Fila | Mensagem gravada na fila. | I | Sim |
| Fila | Erro ao salvar mensagem na fila. | E | Sim |
| Fila | FIM DO PROCESSO DE SALVAR MENSAGEM NA FILA. | I | Sim |
| Inicializando execução | INÍCIO DO PROCESSO DE EXECUÇÃO DA MENSAGEM DE RECEBIMENTO. | I | Sim |
| Inicializando execução | Mensagem recuperada da fila. | I | Sim |
| Validação de execução | Não foi encontrada nenhuma entidade mapeada. | E | Não |
| Validação de execução | Mapa de integração carregado. | I | Não |
| Validação de execução | Erro ao carregar mapa da integração. | E | Não |
| Validação de execução | Evento CanExecuteQueue executado | I | Não |
| Validação de execução | Entidade não mapeada | E | Não |
| Validação de execução | XSLT de entrada não foi preenchido. | E | Não |
| Preparação de contexto | Preparação de contexto. | I | Não |
| Preparação de contexto | Coligada e filial recuperados. | I | Não |
| Preparação de contexto | Alterando código de todas as coligadas e filiais encontradas. | I | Não |
| Preparação da execução | Evento BeforeExecuteHandle será executado. | I | Não |
| Preparação da execução | Início da execução do manipulador (handle) | I | Não |
| Preparação da execução | Manipulador (Handle) de 'DataServer' definido! | I | Não |
| Preparação da execução | Manipulador (Handle) de 'Process' definido! | I | Não |
| Preparação da execução | Manipulador (Handle) de 'Module' definido! | I | Não |
| Preparação da execução | Manipulador (Handle) de 'CustomHandle' definido! | I | Não |
| Preparação da execução | Contexto da RM (RMSContext) criado: | I | Não |
| Preparação da execução | Inicio do processo de transformação via xslt! | I | Não |
| Preparação da execução | Evento BeforeTransformReceive será executado! | I | Não |
| Preparação da execução | Evento BeforeTransformReceive será executado! | I | Não |
| Preparação da execução | Evento AfterTransformReceive será executado! | I | Não' |
| Preparação da execução | Evento AfterTransformDataSet será executado! | I | Não |
| Preparação da execução | Fim do processo de transformaçaõ via xslt | I | Não |
| Preparação da execução | DataSet está vazio | E | Não |
| Executando handle de dataServer | Início da execução do manipulador de Dataserver! | I | Não |
| Executando handle de dataServer | Executando o dataServer + "Nome do dataServer" | I | Não |
| Executando handle de dataServer | Evento BeforeSave será executado! | I | Não |
| Executando handle de dataServer | Schema do dataServer recuperado! | I | Não |
| Executando handle de dataServer | Início da recuperação dos valores da chave primária | I | Não |
| Executando handle de dataServer | Valor Chave primária:[serão informados os valores da chave primária" | I | Não |
| Executando handle de dataServer | Fim da recuperação dos valores da chave primária | I | Não |
| Executando handle de dataServer | Preechimento dos relacionamentos! | I | Não |
| Executando handle de dataServer | Linha principal do dataSet em estado de exclusão! | I | Não |
| Executando handle de dataServer | Linha principal do dataSet em estado de alteração! | I | Não |
| Executando handle de dataServer | Linha principal do dataSet em estado de inclusão! | I | Não |
| Executando handle de dataServer | Método 'SaveRecord' do dataServer executado: | I | Não |
| Atualização De/Para | Atualizando De/Para da tabela + "Nome da tabela" | I | Sim |
| Atualização De/Para | A coluna 'INTERNALID' não existe no dataSet a ser enviado para o DataServer. O De/Para não será atualizado! | A | Não |
| Atualização De/Para | Não existe chave primária na tabela. O De/Para não será atualizado! | A | Não |
| Atualização De/Para | Informações do De/Para a serem gravados:[dados do de/para] | I | Sim |
| Atualização De/Para | Informações do De/Para serão excluídas | I | Sim |
| Atualização De/Para | Erro ao atualizar De/Para | E | Sim |
| Executando handle de dataServer | Evento AfterSave será executado | I | Não |
| Executando handle de dataServer | Fim da execução do manipulador de Dataserver! | I | Não |
| Executando handle de Processo | Início da execução do manipulador de processo. | I | Não |
| Execução de handle de Processo | Evento BeforeExecute será executado | I | Não |
| Execução de handle de Processo | Fim da execução do manipulador de process | I | Não |
| Execução de handle de Processo | Evento AfterExecute será executado | I | Não |
| Execução de handle de módule | Início da execução do manipulador de module | I | Não |
| Execução de handle de módule | Evento BeforeExecuteMethod será executado | I | Não |
| Execução de handle de módule | Evento AfterExecuteMethod será executado | I | Não |
| Execução de handle de módule | Fim da execução do manipulador de module! | I | Não |
| Finalizando execução | Erro ao executar manipulador (handle) | E | Não |
| Gerrando resposta | Início da recuperação do xml de resposta | I | Não |
| Gerrando resposta | Evento CreateResponse será executado | I' | Não |
| Gerrando resposta | Início da construção da tag ReturnContent do dataServer! | I | Não |
| Gerrando resposta | Informações do internalId. | I | Sim |
| Gerrando resposta | Fim da construção da tag ReturnContent do dataServer | I | Não |
| Gerrando resposta | Fim da recuperação do xml de resposta | I | Sim |
| Finalizando execução | Fim da execução do manipulador (handle) | I | Não |
| Finalizando execução | Evento AfterExecuteHandle será executado! | I | Não |
| Finalizando execução | Informações de execução da mensagem foram gravadas na fila | I | Não |
| Finalizando execução | Informações de execução da mensagem. | I | Sim |
| Finalizando Execução | FIM DO PROCESSO DE EXECUÇÃO DA MENSAGEM DE RECEBIMENTO! | I | Sim |
|  |  |  |  |

b) - Informações de log disponibilizadas durante o processo de "Envio de mensagens":

|  |  |  |  |
| --- | --- | --- | --- |
| **Localização** | **Mensagem** | **Tipo de menagem**  **(E) -**  **A - (**  **I - ()** | **Todas as marcas** |
| Fila | INÍCIO DO PROCESSO DE SALVAR MENSAGEM DE ENVIO NA FILA | I | Sim |
| Fila | Recuperação das integrações | I | Sim |
| Fila | Mensagem não foi gravada na fila, pois não existe integração mapeada! | I | Sim |
| Fila | Entidade não foi mapeada | E | Não |
| Fila | Mapa de integração carregado. | I | Não |
| Fila | Erro ao carregar mapa de integração | E | Não |
| Fila | Executando mensagem da integração. [Serão listados os dados da integração] | I | Não |
| Fila | Evento CanSaveQueue será executado! | E | Não |
| Fila | Mensagem gravada na fila | I | Sim |
| Fila | Erro ao salvar mensagem na fila | E | Sim |
| Fila | Dados da mensagem gravada. [Serão listados os dados da mensgem gravada na fila] | I | Sim |
| Fila | FIM DO PROCESSO DE SALVAR MENSAGEM DE ENVIO NA FILA | I | Sim |
| Inicializando execução | INICIO DO PROCESSO DE EXECUÇÃO DA MENSAGEM DE ENVIO NA FILA! | I | Sim |
| Inicializando execução | Mensagem recuperada da fila! | I | Sim |
| Inicializando execução | Execução da mensagem de forma sincrona! | I | Sim |
| Inicializando execução | Execução da mensagem de forma assincrona! | I | Sim |
| Validação de execução | Entidade não mapeada | E | Não |
| Validação de execução | Mapa de integração carregado. | I | Não |
| Validação de execução | Erro na carga de informações | E | Não |
| Validação de execução | Evento CanExecuteQueue será executado! | I | Não |
| Preparação de contexto | Coligada não foi encontrada no dataSet enviado pelo produto! | A | Não |
| Preparação de contexto | Filial não foi encontrada no dataSet enviado pelo produto! | A | Não |
| Preparação de contexto | Coligada e filial recuperados | I | Não |
| Preparação de contexto | Início da execução do manipulador (handle) | I | Não |
| Preparação de contexto | Inicio do processo de transformação via xslt! | I | Não' |
| Preparação de contexto | Evento BeforeTransformSend será executado! | I | Não |
| Preparação de contexto | Evento AfterTransformSend será executado! | I | Não |
| Preparação de contexto | Fim do processo de transformação via xslt! | I | Não |
| Execução handle WebServices | Início da execução do manipulador de WebServices! | I | Não |
| Execução handle WebServices | Evento BeforeSendWebService será executado! | I | Não |
| Execução handle WebServices | Inicio da execução do webServices! | I | Não |
| Execução handle WebServices | Objeto wsdl não gerado! | E | Não |
| Execução handle WebServices | Informações do assemblyProxy não encontradas! | E | Não |
| Execução handle WebServices | Proxy não recuperado! | E | Não |
| Execução handle WebServices | Fim da execução do webServices! | I | Sim |
| Execução handle WebServices | Evento AfterSendWebService será executado! | I | Não |
| Execução handle WebServices | Erro ao executar manipulador (handle): | E | Não |
| Validação da resposta | A resposta da execução do WebServices foi bem sucedida! | I | Sim |
| Validação da resposta | Erro ao realizar parser da resposta da mensagem (ResponseMessage): | E | Sim |
| Validação da resposta | Informações retornadas na resposta da mensagem:[Serão listadas as informações retornas de InternalId] | I | Sim |
| Atualização De/Para | Início do processo de salvar De/para! | I | Sim |
| Atualização De/Para | Atributo 'ListOfInternalId' retornado no conteúdo da resposa da mensagem! | I | Sim |
| Atualização De/Para | Informações do De/Para a ser gravado:[Serão listados dados do De/para] | I | Sim |
| Atualização De/Para | Tabela não existente no dataSet original da mensagem: | A | Não |
| Atualização De/Para | De/para não atualizado. Indentificador do internalId não localizado na lista! | A | Não |
| Atualização De/Para | De/Para excluído com sucesso! | I | Sim |
| Atualização De/Para | Exclusão de De/Para não retornou nenhum valor! | A | Sim |
| Atualização De/Para | Não foi possível encontrar valores no de/para para exclusão! | A | Sim |
| Atualização De/Para | Valor do 'internalId' não foi encontrado! | A | Não |
| Atualização De/Para | Campo 'InternalId' não foi encontrado no dataSet de transformação! | A | Não |
| Atualização De/Para | Campos chaves do De/Para não foram informados! | A | Não |
| Atualização De/Para | Não foi encontrada a tabela no dataSet original | A | Não |
| Atualização De/Para | Tabela não encontrada no dataSet original: | A | Não |
| Atualização De/Para | De/para não atualizado. Atributo 'ListOfInternalId' não retornado no conteúdo da resposa da mensagem! | I | Sim |
| Atualização De/Para | Conteúdo da mensagem (ReturnContent) não retornado na resposta da mensagem. De/para não atualizado. | A | Sim |
| Atualização De/Para | Fim do processo de salvar De/para! | I | Sim |
| Atualização De/Para | Erro ao salvar tabela De-Para: | E | Sim |
| Finalizando execução | Fim da execução do manipulador (handle) | I | Não |
| Finalizando execução | Evento AfterExecuteHandle será executado! | I | Não |
| Finalizando execução | Mensagem não foi executada. | I | Sim |
| Finalizando execução | Informações de execução da mensagem [ Serão listados dados de status da execução] | I | Sim |
| Finalizando execução | FIM DO PROCESSO DE EXECUÇÃO DA MENSAGEM DE ENVIO NA FILA! | I | Si |

## Dicionário de Dados

***HCMONITOR***

| CAMPO | DESCRIÇÃO | TIPO |
| --- | --- | --- |
| ID | Identificador do monitor | int |
| IDPROCESSO | Identificador do processo | varchar(255) |
| RECCREATEDBY | Usuário de criação | varchar(50) |
| RECCREATEDON | Data de criação | datetime |
| RECMODIFIEDBY | Usuário de alteração | varchar(50) |
| RECMODIFIEDON | Data de alteração | datetime |

**HCLOGMENSAGEM**

| CAMPO | DESCRIÇÃO | TIPO |
| --- | --- | --- |
| UUID | Identificador da mensagem na fila | varchar(255) |
| SEQUENCIAL | Sequencial | int |
| DATAMENSAGEM | Data de geração da mensagem | datetime |
| TIPOLOG | Tipo do Log  0 - Information  1 - Warning  2 - Error | int |
| LOCALIZACAO | localização do log na engine do eai | varchar(100) |
| INFOLOG | dados do log | text |
| INFODEBUG | dados do debugger | text |
| RECCREATEDBY | usuário de criação | varchar(50) |
| RECCREATEDON | Data de criaçaõ | datetime |
| RECMODIFIEDBY | usuário de alteração | varchar(50) |
| RECMODIFIEDON | data de alteração | datetime |

Scripts:

CREATE TABLE HCMONITOR -- Monitor do EAI  
(  
 ID VARCHAR(255) NOT NULL,--Identificador do nonitor  
 IDPROCESSO VARCHAR(255) NULL, --Identicador do processo  
 RECCREATEDBY VARCHAR(50) NULL,  
 RECCREATEDON DATETIME NULL,  
 RECMODIFIEDBY VARCHAR(50) NULL,  
 RECMODIFIEDON DATETIME NULL,  
)

ALTER TABLE HCMONITOR  
ADD CONSTRAINT PK\_HCMONITOR PRIMARY KEY (ID)

CREATE TABLE HCLOGMENSAGEM -- Log de mensagens.  
(  
 UUID VARCHAR(255) NOT NULL,--Identificador do log  
 SEQUENCIAL INT NOT NULL,--Número sequencial  
 DATAMENSAGEM DATETIME NULL, --Data de inclusão da mensagem.  
 TIPOLOG INT NULL, --Tipo do log [error, warning, info, danger]

LOCALIZACAO VARCHAR(100) NULL, --localização dolog na engine do eai  
 INFOLOG TEXT NULL,--Informações de Log do monitor

INFODEBUG TEXT NULL, --Informações de debug  
 RECCREATEDBY VARCHAR(50) NULL,  
 RECCREATEDON DATETIME NULL,  
 RECMODIFIEDBY VARCHAR(50) NULL,  
 RECMODIFIEDON DATETIME NULL,   
)

ALTER TABLE HCLOGMENSAGEM  
ADD CONSTRAINT PK\_HCLOGMENSAGEM PRIMARY KEY(UUID, SEQUENCIAL)

ALTER TABLE HCLOGMENSAGEM  
ADD CONSTRAINT FK\_HCLOGMENSAGEM\_HCFILAMENSAGEM FOREIGN KEY(UUID)  
REFERENCES HCFILAMENSAGEM (UUID)

--ALTERAÇÕES NA TABELA DE FILA DE MENSAGEM  
ALTER TABLE HCFILAMENSAGEM  
ADD MONITORID VARCHAR(255) NULL --Identificador do monitor.

ALTER TABLE HCFILAMENSAGEM  
ADD CONSTRAINT FK\_HCFILAMENSAGEM\_HCMONITOR FOREIGN KEY (MONITORID)  
REFERENCES HCMONITOR(ID)

ALTER TABLE HCFILAMENSAGEM  
ADD STATUSMENSAGEM INT NULL --Status da mensagem.

 

---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
