---
content_hash: 4223d08ecd277b7c5a30fd549890daafa4fe5d606c860edf576e810dd1c2b3aa
fetched_at: '2026-06-29T00:08:18.159356+00:00'
page_id: '263193232'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-107_EngineEAI2
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-107_EngineEAI2
version: 112
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo EAI** |  |
| **Segmento Executor** | Framework | | |
| **Projeto1** | 1. [Framework BH - 004](http://jiraproducao.totvs.com.br/browse/FRW_FRW002) | **IRM1** |  |
| **Requisito1** | 1. [FRW\_FRW002-93](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-93) | **Subtarefa1**  [FRW\_FRW002-107](http://jiraproducao.totvs.com.br/browse/FRW_FRW002-107) |  |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

  

### Objetivo

 

* As regras atuais de manipulação das mensagens existentes atualmente no EAI (*handle de dataServers,  handles de process e handle de WebServices*) devem ser escritas pelas equipes dos segmentos.
* A equipe de frame fornecerá funções (API's genéricas) para serem utilizadas pelos adapters.
* As regras atuais de réplica entre coligadas existentes atualmente no EAI devem ser escritas pelas equipes dos segmentos (API's serão fornecidas);
* O EAI não armazenará os xslts (de saída, entrada e retorno) . A transformação das mensagens de entrada e saída ficará sob a responsabilidade dos adapters dos segmentos..
* Os fontes localizados nos extensions (GS*ourceCodes*) devem ser migrados para estruturas de adapters.
* Informações de contexto (coligada, filial, etc) não serão manipuladas pelo EAI, as mesmas devem ser manipuladas dentro dos adapters.
* O recurso de fórmula visual não deve ser usado para enviar as mensagens para o EAI. O EAI deve ser chamado dentro dos objetos de negócio dos produtos para envio das mensagens;
* Não será permitido o envio de mensagens síncronas para múltiplas rotas, sendo permitido somente mensagens assíncronas.

 

## Definição da Regra de Negócio

# Modelo de solução

Abaixo será definido o modelo de solução para a criação do EAI 2.0.

# 1 - Modelo de dados

,

GEAICONFIG (Configurações gerais do EAI)

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| TipoEAI | Tipo do EAI - Define a engine a ser executada no ambiente do cliente. | 0 ou Null –EAI 1.0  1 – EAI 2.0 |
| ProxyUsr | usuário proxy rede interna |  |
| ProxyPassword | senha proxy rede interna |  |
| Timeout | Tempo máximo de envio da mensagem. | Será utilizado o valor default em caso de não preenchimento |
| ValidaXsd | Habilita/desabilita validação xsd | Permite validar xml no recebimento/envio de mensagens usando o xsd (perda de performance)  0 ou NULL– Não valida  1 - valida |
| UsaLog | Habilita/desabilita gravação de log do EAI | 0 OU NULL – NÃO USA  1 - USA LOG |
| UsaDebugLog | Habilita/desabilita gravação de informações de objetos de debug | DataSet e outros objetos serializados poderão ser gravados na tabela de log (perda de performance);  0 OU NULL – NÃO USA  1 - Usa |
| UsaContextoLog | Habilita/desabilita gravação do objeto de contexto do EAI na execução da mensagem | Perda de performance e espaço.  0 OU NULL – NÃO USA  1 - USA |
| UrlMonitorInterno | Endereço do monitor interno |  |
| UrlWSDLInterno | Endereço WSDL interno |  |
| NumTentativasExec | Número de tentativas de execução da mensagem em caso de mensagens assíncronas com erro | Valor maior que 0 informará o número de tentativas de execução.  Valor NULL ou 0 - Será executado uma única vez |
| IntervaloDeExecucao | Tempo de intervalo de execução (em milissegundos) | Valor NULL ou 0: será executado imediatamente |
| DesabilitaCustomizacao | Desabilita a execução das extensões de customização | 0 ou NULL - Habilitado  1 - Desabilitado |
|  |  |  |

GEAIAPP (cadastro de aplicativos)

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| Id (pk) | Identificador do aplicativo | autoinc |
| Nome | Nome do aplicativo |  |
| Descricao | Descrição longa do aplicativo |  |
| AppHost | Define se o app em questão é o app host (app interno) | Só haverá um app interno por instalação  0 – interno  1 - externo |
| SourceApplication | Informação enviada no protocolo “TotvsMessage” do atributo “MessageInformation/SourceApplication”. | No aplicativo interno, esse valor será o nome da instância do RM (Inicialmente será “RM”). Não será permitido o cadastro de mais de um aplicativo com o mesmo SourceApplication/CodProduto. |
| CodProduto | Nome do produto. Corresponde ao atributo “ProductName” enviado através do protocolo TotvsMessage. | Ex: Protheus, DataSul, Logix, RM.  No aplicativo interno, esse valor terá o nome “RM”.  Em se tratando de recebimento de mensagens, os valores “Sourceapplication” e “CodProduto“ enviados na mensagem definirão o aplicativo correto.  Caso não seja encontrado o aplicativo, a mensagem não será executada, retornando erro. |
| UrlWSDLExterno | Endereço WSDL do aplicativo externo |  |
| UsrWSDLExterno | Usuário para conectar na url  WSDL do aplicativo externo |  |
| PassWSDLExterno | senha para conectar nas url WSDL do aplicativo externo |  |
| Ativo | Ativo: ativa / desativa  um app | 0 ou null – inativo  1 - ativo |
| RMColigadaNoProtheus | Mapeamento da coligada com o Protheus (em caso de aplicativo Protheus) | Grupo de empresa - 1  Unidade de negócio- 2  Empresa - 3 |

GEAITRANSACAO (cadastro de transação)

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| Id (pk) | Identificador da transação | Ex: COSTCENTER, BANK, CUSTOMERVENDOR, ORDER, etc. |
| Descricao | Descrição da transação |  |
| ModoSuportado | Modo suportado pela transação, ou seja, são as formas possíveis de uso da mesma | 1 [envio\_habilitado]: A transação só pode ser usada no aplicativo para enviar mensagens;  2 [recebimento\_habilitado]: A transação só pode ser usada no aplicativo para receber mensagens;  3 [ambos\_habilitado]: A transação pode ser usada tanto para envio quanto para recebimento; |
| SyncAsyncEnvio | Informa se a transação é síncrona ou assíncrona (em caso de envio) | 0 – Sincrona  1 – Assincrona  Default é 0 |
| PermiteRecAsync | Permite recebimento assíncrono em caso de recebimento? | 0 – permite  1 – Não permite.  Default é 0 |

GEAITRANSACAOVERSAO: Mapeamento transação / versão

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| IdTransacao (pk) (fk) | Identificador da transação | chave estrangeira para tabela GEAITransacao |
| Versao (pk) | Versão da transação |  |
| NomeClasseAdapterCst | Nome da classe (fullName) do adapter de customização (se existir). Se estiver vazio (default) será usado o adapter nativo carregado automaticamente. |  |

 

GEAITRANSACAOAPP: Cadastro de rotas (mapeamento entre app/transação/versão)

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| IdApp (pk)(fk) | Identificador do app | Chave estrangeira para tabela GEAIApp |
| IdTransacao (pk)(fk) | Identificador da transação. | Chave estrangeira para tabela GEAITransacaoVersao |
| Versao (fk) | Versão da mensagem ativada para o aplicativo em questão | * Não será permitido cadastrar mais de um app/transação em versões diferentes. * Chave estrangeira para tabela GEAITransacaoVersao; * Não faz parte da chave primária; * Preenchimento obrigatório. |
| IdSourceCode (fk) | Identificador do código fonte customizado | Chave estrangeira para tabela GSourceCode; |
| IncluiMensagemOriginal | Indica se na mensagem de resposta de uma transação/versão será adicionado a mensagem original no corpo da mensagem de resposta | **0 OU NULL –INCLUI**  **1 – Não INCLUI** |
| ModoHabilitado | Modo habilitado da transação, ou seja, o que de fato está habilitado no momento. | 1 [envio\_habilitado]: A transação só pode ser usada no aplicativo para enviar mensagens;  2 [recebimento\_habilitado]: A transação só pode ser usada no aplicativo para receber mensagens;  3 [ambos\_habilitados]: A transação pode ser usada tanto para envio quanto para recebimento ;  4 [Não\_habilitado]: a transação não está habilitada para essa versão de mensagem no app em questão; |

GEAIPACOTEINSTALADO: pacotes instalados

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Regras** |
| IdPacote (pk) | identificador do pacote instalado | Número do Guid incluído nos arquivos de configuração de  integração (json) |
| NomePacote | nome do pacote instalado |  |
| NomeReduzido | Nome reduzido do pacote instalado |  |
| AppId (fk) | Identificador do aplicativo instalado | Chave estrangeira para tabela GEAIAPP |

 

GEAIGRUPOMENSAGEM: Agrupador de mensagens

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| Id (pk) | identificador único do grupo  autoinc |
| Grupo | Identificador do grupo de mensagens. Deve ser enviado um guid que representará um grupo de mensagens |
| NomeGrupo | Nome do grupo. Ex: Pedido de compra |
| InfoGrupo | Informações complementares do grupo |
|  |  |

GEAIMENSAGEM: representará uma mensagem (business, response ou receipt). Cada mensagem recebida, enviada ou respondida será uma nova linha nessa tabela.

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| Id (pk) | identificador da mensagem (gautoinc) |
| UUID | Armazenará o UUID da mensagem.  Exemplo:  a)        Ao receber uma mensagem do Protheus, será gravado nesse campo o UUID gerado lá no sistema do Protheus (TotvsMessage.MessageInformation.UUID)  b)        Ao enviar uma mensagem, será gravado nesse campo o UUID (GUID) gerado para a mensagem de envio. |
| TipoEntrega | Tipo de entrega (Assíncrono e síncrono).  0 – Sync  1 - Async |
| EntradaSaida | Tipo de entrada/saída (envio ou recebimento). |
| Evento | Tipo do evento de mensagem.  BusinessEvent  Request |
| Tipo | Tipo da mensagem  0 – BusinessMessage  1 – ResponseMessage  2 - ReceiptMessage |
| TransactionId (fk) | Identificador da transação. Chave estrangeira para tabela GEAITRANSACAO |
| Versao | Versão da mensagem |
| XMLOriginal | XML contendo a mensagem original.  Se for uma mensagem de recebimento, será o TotvsMessage enviado.  Se for uma mensagem de envio, será o dataSet de origem serializados. |
| IdGrupo | Identificador do grupo de mensagem mensagem (chave estrangeira para tabela GEAIGrupoMensagem). |
| IdMensagemPai | Armazenará o identificador (Id) da mensagem pai.  Ex:  1)        Quando o RM enviar uma mensagem de forma assíncrona, imediatamente será retornada uma mensagem de recibo (receiptMessage). Essa será gravada em uma nova linha nessa tabela. Nessa nova linha, no campo “IdMensagemRelac” será gravado o Id da mensagem origem.  2)        O destino ao enviar a resposta (responseMessage) da mensagem para o RM, essa será gravada em uma nova linha. Será gravado nessa linha o id da mensagem pai. |
| RMSContexto | Armazena o objeto RMSContext |

GEAIROTAMENSAGEM: Rotas geradas para execução das mensagens

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| Id (pk) | Identificador da rota/mensagem (gautoinc) |
| IdMensagem (fk) | identificador da mensagem  Chave estrangeira para tabela GEAIMensagem |
| IdApp (fk) | Armazenará o aplicativo da mensagem.  Se o RM estiver recebendo uma mensagem, o IdApp será do aplicativo externo (quem enviou a mensagem);  Se o RM estiver enviando uma mensagem, o IdApp será do aplicativo de destino da mensagem  Chave estrangeira para tabela GEAIApp |
| EstadoMensagem | Estado da mensagem:  0: Received (recebida)  1: Recognized (reconhecida)  2: Validated (validada)  3: Delivering (entregaando)  4: Processing (processando)  5: Delivered (entregue)  6: Processed (processada com sucesso)  7: Refused (negada)  8: Malformed (mal formatada)  9: NotDelivered (não entregue)  10: BusinessError (erro de negócio) |

GEAIROTALOGMENSAGEM: Log gerado pela execução da rota da mensagem

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| Id (pk) | Identificador do log (gautoinc) |
| IdRotaMensagem (fk) | Identificador da rota/mensagem.  Chave estranheira para GEAIRotaMensagem |
| TipoLog | 0 - Info  1   - Warning  1          Error |
| InfoLog | Texto contendo informações do log |
| InfoDebugVar | Informações de debug de variaveis |
| InfoDebugObj | Informações de debug de objetos. |

GEAIEXECROTAMENS: Informações de execução da rota da mensagem. 

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| Id (pk) | Identificador da execução (gautoinc) |
| IdRotaMensagem | Identificador da rota/mensagem.  Chave estrangeira para tabela GEAIRotaMensagem |
| XmlMensTransformada | XML contendo a mensagem transformada |
| MensagemExecucao | Mensagem da execução |
| CodigoExecucao | Código da execução |
| EAIContext | Armazenará o objeto EAIContext serializado através do “DataContractSerialization”. Todas as informações de contexto de execução da mensagem naquele momento serão gravadas nesse campo.  Essa gravação ocorrerá somente se o parâmetro *GEAIParams.UsaContextoLog = true*) estiver setado. |
| DeParaInfo | Informações de de/para |
| RMSContexto | Contexto RM usado para a execução da mensagem |

GEAIJOBMENSAGEM: Mapeamento entre job / mensagem (usada somente para mensagens assíncronas)

|  |  |
| --- | --- |
| **Coluna** | **Descrição** |
| IdMensagem (pk) | identificador da mensagem  Chave estranheira para tabela GEAIMensagem |
| IdJob (pk) | Identificador do Job gerado para processar a mensagem assíncrona.  Não possui chave estranheira com a tabela GJob |

HCINTEGRACAOID (alterações na tabela de DE DE/PARA)

 

* Essa será a única tabela compartilhada entre os dois EAI’s, ou seja, não será criada uma nova tabela para armazenar valores de “de/para” do eai 2.0.
* Atualmente não é armazenado nessa tabela o “sourceApplication” correspondente ao mapeamento da chave. Sendo assim, caso RM integre com dois sistemas Protheus (dois sourceApplications diferentes para o mesmo sistema), o RM não saberá de qual sourceApplication aquele mapeamento corresponderá.
* Atualmente esse erro não ocorreu nos nossos clientes porque até o momento não existe nenhuma implantação na qual o RM integre com dois sourceAppliaction diferentes para o mesmo sistema.
* Para resolver a situação acima, será criada uma nova coluna nessa tabela chamada “AppID” (não será criada chave estrangeira para tabela GEAIApp).
* Será armazenado nessa coluna o identificador do aplicativo externo correspondente a integração.
* A coluna “SistemaIntegrado” não será usada pelo EAI 2.0 (ela não será removida da tabela para compatibilizar com o EAI 1.0).
* No processo de conversão para o novo EAI, será criado um script para preencher esse campo com o AppId correspondente ao “SistemaIntegrado”.
* Será removida dessa tabela sua chave primária (pkhcintegracaoid). Essa tabela não possuirá chave primária;
* A coluna "SISTEMAINTEGRADO" passa a aceitar valores nulos;
* Serão criados nessa tabela dois índices não únicos, entre eles:
  + IX\_HCINTE\_APPID (TABELARM, IDNOMERM, IDVALORRM, APPID)
  + IX\_HCINTE\_SISTINTEG (TABELARM, IDNOMERM, IDVALORRM, SISTEMAINTEGRADO)

# 2 - Detalhamento dos processos

|  |  |  |  |
| --- | --- | --- | --- |
| **RM RECEBE MENSAGENS SÍNCRONAS**    **1)****Serviço de recebimento de mensagens do EAI RM é chamado**  Grava mensagem nas tabelas GEAIMensagem e GEAIRotaMensagem    **2)****Serviço de execução de mensagens é chamado**  Grava informações na tabela de execução GEAIExecMens;   1. **SUCESSO?**                      i.      [ESTADO: Processed];                      ii.      COMMIT;                      iii.      Grava mensagem de resposta de sucesso (nova linha nas tabelas “GEAIMensagem” e “GEAIRotaMensagem”)  [ESTADO RESPOSTA: Delivered]    Caso o destino não receba a mensagem de resposta (timeout), ele não será capaz de atualizar os de/paras.  Sendo assim, um RollBabck será realizado no aplicativo externo e um commit será realizado no RM.  No RM a mensagem original foi marcada como “Processed”.  E no aplicativo externo a mensagem será marcada “BusinessError”.  Essa situação deve ser apontada na ferramenta de diagnóstico.        2. **ERRO?**                    i.      [ESTADO: BusinessError];                     ii.      ROLLBACK;                     iii.      Grava mensagem de resposta de erro;  [ESTADO RESPOSTA: Delivered];  Caso o aplicativo externo não receba a mensagem de resposta ou receba com erro, ele não será capaz de atualizar os De/Paras.  Nesse caso, um RollBabck será realizado em ambos os lados;  Nesse caso, não apresentará inconsistências; | | |  |
| Definição dos estados da mensagem: | | | |
| **BusinessMessage** | | | |
| **Post da mensagem** | | | |
| Inclusão da mensagem | Received | EAI da RM recebe a mensagem. | |
| Validação | Validated/Refused | EAI do RM valida mensagem.  Verifica correto preenchimento das tabelas de integração. | |
| **Execução da mensagem** | | | |
| Validação | Validated/Refused |  | |
| Envio da mensagem ao adapter para processamento | Processing | Nesse momento os adapters serão chamados para gravação dos dados no RM. | |
| Execução da mensagem nos adapters | Processed/BusinessError | Os dados da mensagem serão processados pelos objetos de negócio do RM | |
| **ResponseMessage** | | | |
| Retorna mensagem de resposta | Delivered |  | |

|  |  |  |
| --- | --- | --- |
| ***RM ENVIA MENSAGENS SÍNCRONAS***    1)        **Serviço de recebimento de mensagens do EAI RM é chamado**  VALIDAÇÃO: Verifica se existe mais de uma rota para envio da mensagem. Caso positivo, o EAI apresentará uma mensagem de erro não aceitando a mensagem.  **2)****Serviço de execução de mensagens é disparado;**   1. **Serviço de envio de mensagens é executado;**   **i.****Sucesso no envio da mensagem?**  **Sucesso no retorno da mensagem?**  a) [ESTADO: Delivered];  b) Grava De/Para;  c) COMMIT;  d) Grava mensagem de resposta contendo sucesso;  [ESTADO reposta: processed]  **Erro no retorno da mensagem?**  a) [ESTADO: Delivered]  b) Não grava informações de De/Para;  c) Grava mensagem de resposta contendo erro;  d) [ESTADO: BusinessError];  f) ROLLBACK;  **ii.****Erro no envio da mensagem (ex: timeout)?**  a) [ESTADO: NotDelivered];  b) Não Grava informações de De/ParaGrava mensagem de resposta;  c) Não existe resposta;  d) ROLLBACK;      Se por algum motivo (timeout no lado Rm) o aplicativo destino recebeu a mensagem,  nesse caso, a informação poderá ter sido gravada em seus de/paras;  Na origem o processo efetuou rollback.  Essa situação será apontada na ferramenta de diagnóstico. | | |
|  | | |
|  |  |  |
| **BusinessMessage** | | |
| **Post da mensagem** | | |
| Inclusão da mensagem | Received | EAI da RM recebe a mensagem de envio. |
| Validação | Validated/Refused | Verifica correto preenchimento das tabelas de integração. |
| **Execução da mensagem** | | |
| Validação | Validated/Refused |  |
| Envio da mensagem para o aplicativo externo | Processing | Nesse momento a mensagem é enviada para o aplicativo externo |
| Sucesso/Erro no envio da mensagem para o aplicativo externo | Delivered/NotDelivered | A mensagem foi enviada com sucesso para o aplicativo externo.  Erro no envio da mensagem. |
| **ResponseMessage** |  | |
| Mensagem de resposta foi retornada com sucesso | Processed |  |
| Mensagem de resposta foi retornada com erro | BusinessError |  |

# 3 - Interfaces de customização

ICUSTOMADAPTERDATASERVER - Interface de adapter de dataServer

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Fase EAI 1.0** | **Interface EAI 1.0** | **Método EAI 1.0** | **Fase EAI 2.0** | **Interface EAI 2.0** | **Método EAI 2.0** |
| Antes de transformar o xml recebido para o xml gerado | IExtensionTransformReceive | BeforeTransformReceive | **Usada para transformar  o businessContent Original antes de solicitar a transformação pelos  adapters** | **ICustomAdapterDataServer** | **AntesTransformarDataServer** |
| Depois de transformar o xml recebido para o xml gerado após xslt | IExtensionTransformReceive | AfterTransformReceive | **Usada para realizar alguma alteração no xml transformado após a transformação pelos adapters.** | **ICustomAdapterDataServer** | **DepoisTransformarDataServer** |
| Antes de executar os manipuladores de recebimento e envio | IExtensionMessage | BeforeExecuteHandle | **Usada para alterar o dataSet transformado antes de enviar o dataSet para o DataServer.**  **obs: Esse método é chamado uma única vez independente da quantidade de dataServers a serem executados pelo adapter para a transação em questão.** | **ICustomAdapterDataServer** | **AntesExecutarDataServer** |
| Depois de executar os manipuladores de recebimento e envio | IExtensionMessage | AfterExecuteHandle | **Usado para efetuar a leitura nos dataSets enviados aos dataServers executados pelos adapters.**  **Esse método é chamado uma única vez independente da quantidade de dataServers a serem executados pelo adapter para a transação em questão.** | **ICustomAdapterDataServer** | **DepoisExecutarDataServer** |
| Depois de criar a resposta para as mensagens recebidas | IExtensionResponse | CreateResponse | **Depois de ciar a tag de returnContent para as respostas de dataServer.** | **ICustomAdapterDataServer** | **DepoisGerarReturnContentRespostaDataServer** |

 

ICUSTOMADAPTERPROCESS- Interface de adapter de process

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Fase EAI 1.0** | **Interface EAI 1.0** | **Método EAI 1.0** | **Fase EAI 2.0** | **Interface EAI 2.0** | **Método EAI 2.0** |
| Antes de transformar receive | IExtensionTransformReceive | BeforeTransformReceive | **Antes de gerar a classe paramsProc** | **ICustomAdapterProcess** | **AntesTransformarProcesso** |
|  | **Nova** |  | **Deposi de gerar o paramsProc** | **ICustomAdapterProcess** | **DepoisTransformarProcesso** |
| Antes de executar um processo RMSProcess | IExtenisonProcess | BeforeExecute | **Antes de enviar para o método execute do process** | **ICustomAdapterProcess** | **BeforeExecuteProcess** |
| Depois de executar um processo RMSprocess | IExtenisonProcess | AfterExecute | **Depois da execução** | **ICustomAdapterProcess** | **AfterExecuteProcess** |
| Depois de criar a resposta para as mensagens recebidas | IExtensionResponse | CreateResponse | **Depois de ciar a tag de returnContent para as respostas de process.** | **ICustomAdapterProcess** | **DepoisGerarReturnContentRespostaProcess** |

ICUSTOMADAPTERWEBSERVICES- Interface de Webservices

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Fase EAI 1.0** | **Interface EAI 1.0** | **Método EAI 1.0** | **Fase EAI 2.0** | **Interface EAI 2.0** | **Método EAI 2.0** |
| Antes de transformar | IExtensionWebService | BeforeTransformSend | **Antes de transformar** | **ICustomAdapterWebServices** | **AntesTransformarWebServices** |
| Depois de transformar | IExtensionWebService | AfterTransformSend | **Depois de transformar** | **ICustomAdapterWebServices** | **DepoisTransformarWebServices** |
| Antes de executar o handle | IExtensionMessage | BeforeExecuteHandle | **Antes de enviar o totvsMessage para o ws** | **ICustomAdapterWebServices** | **AntesExecutarWebServices** |
| Depois de enviar o totvsmessage para o webServices | IExtensionWebService | AfterSendWebServices | **Depois de enviar o totvsMessage para o ws** | **ICustomAdapterWebServices** | **DepoisExecutarWebServices** |

Interfaces descontinuadas

 

|  |  |  |
| --- | --- | --- |
| **Interface** | **Método** | **Comentários** |
| IExtensionDataServer | AfterTransformDataSet | Deve-se utilizar a interface ICustomAdapterDataServer BeforeExecuteDataServer. |
| IExtensionDataServer | BeforeSave | *A manipulação dos dataServers a partir de agora ficará sob responsabilidade dos adapters dos produtos.*  *Sendo assim, caso exista necessidade, essa interface de customização deverá ser criada dentro do adapter do produto e chamado dentro do próprio método do adapter do produto..*  *Na interface antiga, esse método é executado dentro de um foreach para cada nome de Dataserver.* |
| IExtensionDataServer | AfterSave | *A manipulação dos dataServers a partir de agora ficará sob responsabilidade dos adapters dos produtos.*  *Sendo assim, caso exista necessidade, essa interface de customização deverá ser criada dentro do adapter do produto e chamado dentro do próprio método do adapter do produto..*  *Na interface antiga, esse método é executado dentro de um foreach para cada nome de Dataserver.* |
| IExtensionModule | BeforeExecuteMethodParams | *Será removida pois não é utilizada* |
| IExtensionModule | AfterExecuteMethod | *Será removida pois não éutilizada* |

# 4 - Adapters

 

|  |  |
| --- | --- |
| **Classe** | **Descrição** |
| AdapterBase | Classe ancestral usada para definir regras comuns para todos os adapters. |
| AdapterReceiveBase | Classe ancestral usada para definir regras comuns para todos os adapters de recebimento de mensagens |
| AdapterSendBase | Classe ancestral usada para definir regras comnus para todos os adpaters de envio de mensagens |

 

|  |  |
| --- | --- |
| **Classe** | **Descrição** |
| AdapterDataServerBase | Classe ancestral usada para definir comportamentos de manipulação de mensagens usando estruturas de dataServers |
| AdapterProcessBase | Classe ancestral usada para definir comportamentos de manipulação de mensagens usando estruturas de RMProcess |

|  |  |
| --- | --- |
| **Classe** | **Descrição** |
| AdapterWebServiceBase | Classe ancestral usada para definir comportamentos de manipulação de mensagens a serem enviadas por webServices |

 

|  |
| --- |
| **Exemplo: Regra de recebimento da mensagem de recebimento CostCenter** |
| 1) -Adicionar referencia para as dlls abaixo:  [RM.Eai.TotvsMessage.Intf, RM.Eai.TotvsMessage.IService, RM.Eai.TotvsMessage.Lib, Rm.Eai.TotvsMessage.Adapter](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=RM.Eai.TotvsMessage.Intf%2C+RM.Eai.TotvsMessage.IService%2C+RM.Eai.TotvsMessage.Lib%2C+Rm.Eai.TotvsMessage.Adapter&linkCreation=true&fromPageId=261062751)  **2) - Criar a classe com a seguinte característica:**  **a)** Nome da classe: CostCenter\_Receive\_2000  **b)**Herdar da classe "***AdapterDataServerBase*****"**  **Ex: public class **CostCenter\_Receive\_2000**: AdapterDataServerBase**  **c)**Usar o atributo de classe "***AdapterAttr*****":**esse atributo irá "carimbar" a classe com informações do adapter.  **Ex: [AdapterAttr("COSTCENTER", "1.000")]****public class ****CostCenter\_Receive\_2000****: AdapterDataServerBase**     | **Exemplo: Regra de envio da mensagem CostCenter** | | --- | | 1) -Adicionar referencia para as dlls abaixo:  [RM.Eai.TotvsMessage.Intf, RM.Eai.TotvsMessage.IService, RM.Eai.TotvsMessage.Lib, Rm.Eai.TotvsMessage.Adapter](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=RM.Eai.TotvsMessage.Intf%2C+RM.Eai.TotvsMessage.IService%2C+RM.Eai.TotvsMessage.Lib%2C+Rm.Eai.TotvsMessage.Adapter&linkCreation=true&fromPageId=261062751)  **2) - Criar a classe com a seguinte característica:**  **a)** Nome da classe: CostCenter\_Send\_2000  **b)**Herdar da classe "***AdapterWebServicesBase*****"**  **Ex: public class **CostCenter\_Send\_2000**: AdapterWebServicesBase**  **c)**Usar o atributo de classe "***AdapterAttr*****":**esse atributo irá "carimbar" a classe com informações do adapter.  **Ex: [AdapterAttr("COSTCENTER", "1.000")]****public class ****CostCenter\_Send\_2000****: AdapterWebservicesBase** | |

# 5 - API

API de manipulação por dataServer

 

|  |  |
| --- | --- |
| **Nome Serviço** | **Descrição** |
| CreateDataServer | Criar um instancia do DataServer |
| Readrecord | Executa o método ReadRecord do Dataserver |
| SaveRecord | Salva um dataSet no dataServer; |
| GetDeParaItem | Retorna um objeto "EAIMsgDeParaItem" referente a um item de depara |
| GetPKValues | Recupera valores de chave primária data row passada como parametro |
| GetPKValuesByDePara | Recupera valores de chave primária baseado na tela de de/para |
| CopyDataRow | Copia valores da linha de origem para tabela de destino |
| UpdateRowValue | Atualiza valores da linha corrente |
| GetReplaceCompanyIdBranchId | Troca a coligada e filial de todo o xml |

API de manipulação da tabela de DE/PARA

 

|  |  |
| --- | --- |
| **Nome Serviço** | **Descrição** |
| GetChaveRM | Retorna um valor da chave primária |
| ExistsDePara | Verifica a existencia de um de/para |
| SaveDePara | Salva valores na tabela de de/para |

API de manipulação de processos

 

|  |  |
| --- | --- |
| **Nome Serviço** | **Descrição** |
| Execute | Executa um rmsprocess |
| ExecuteWithParams | Executa um rmsProcess com parametros. Passan do um xmlDeParametros |
| ExecuteWithParams | Executa um rmsProcess com parametros passando umparamsProc. |
|  |  |

API de manipulação de webServices

|  |  |
| --- | --- |
| **Nome Serviço** | **Descrição** |
| SendWebServices | Envia o xml TotvsMessage para o destino via webServices |
| GetDeParaByListOfInternalId | Retrona uma lista de informações de de/para localizadas no xml de responseMessage |
| RemoveRMEntityName | Remove a coluna "'EntityName" criada no dataSet |
| PrepareInternalFields | Adiciona campos de InternalId nas tabelas do dataSet |

|  |
| --- |

divs
