---
content_hash: 397e9ac76a900bee4029978affcad289c009aabdcaf563965fea869153023114
fetched_at: '2026-06-28T21:35:24.542248+00:00'
page_id: '270919174'
product: fluig
source: tdn-fluig
title: Método getValue
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270919174
version: 30
---

O método **getValue** é utilizado para obter dados específicos associados aos eventos de personalização. Através deste método, é possível acessar diferentes propriedades dependendo do tipo de evento.

Esta documentação fornece uma visão geral do método getValue e orientações sobre como utilizá-lo com base nas propriedades de diversos tipos de eventos.

# Parâmetros nos eventos de documentos e formulário

Os eventos de formulário possuem bastante variações nos parâmetros disponíveis por evento, por isso, consulte a documentação do evento para conhecer os parâmetros disponíveis.

# Parâmetros específicos para eventos de processo

| Parâmetro | Descrição |
| --- | --- |
| WKDef | Código do processo. |
| WKVersDef | Versão do processo. |
| WKNumProces | Número da solicitação de processo. |
| WKNumState | Número da atividade. Importante Para realizar a busca pelo número da atividade, indica-se o uso do parâmetro WKNumState.  Caso utilize um campo de formulário, uma segunda chamada pode ser feita para atualizar este campo, o que pode causar inconsistências inesperadas. |
| WKCompany | Número da empresa. |
| WKUser | Código do usuário corrente. |
| WKUserComment | A partir do fluig 1.5 é possível adicionar Complementos em uma solicitação. Este recurso permite inserir diversas observações na mesma solicitação. Ou seja, não temos mais apenas um comentário por atividade. Os complementos em solicitações permitem que um usuário adicione comentários ou anexos em uma solicitação aberta sendo ou não responsável pela tarefa corrente com a finalidade de evitar comunicação por outros meios que não ficarão registrados no histórico do processo.  Por isso a forma de retornar a informação mudou para a variável WKUserComment. Agora ela recebe um texto com todas as observações feitas pelos usuários na atividade corrente. Exemplo do valor atual da variável WKUserComment: " Nome do usuário - 09/03/2017 - 10:46 - Observação feita pelo usuário  Nome do usuário - 09/03/2017 - 10:45 - Nova observação feita pelo usuário "  OBS: Esse parâmetro irá retornar apenas os comentários da atividade corrente.    A partir da Atualização 1.5, para resgatar os complementos (observação) de uma tarefa, deve ser utilizado o método da API Pública: <https://api.fluig.com/resource_WorkflowRest.html#path__2.0_workflows_findObservations_-processInstanceId-_-stateSequence-_-threadSequence-.html>  Documentação indicada para auxiliar na utilização da API publica em eventos: <http://tdn.totvs.com/x/0Xo-Dg> |
| WKCompletTask | Se a tarefa foi completada ("true"/"false"). |
| WKNextState | Número da próxima atividade (destino). |
| WKCardId | Código do registro de formulário do processo. |
| WKFormId | Código do formulário do processo. |
| WKIdentityCompany | Identificador da empresa selecionada para Experiências de uso TOTVS.  Esse parâmetro corresponde à empresa que está selecionada quando as experiências de uso TOTVS estão ativas.  Nesse cenário, quando o usuário clica na imagem do perfil (canto superior direito), uma das opções que aparece é "Trocar empresa". Ao clicar nessa opção aparecerá uma ou mais empresas nas quais o usuário está configurado no Identity.  O parâmetro WKIdentityCompany corresponde à empresa selecionada nessa opção de Trocar empresa, e uma forma de verificar o valor que está definido é através do painel de controle, nos dados adicionais do usuário, com a chave "UX-APP-COMPANY". |
| WKMobile | Identifica se a ação foi realizada através de um dispositivo *mobile*. |
| WKIsService | Identifica se a solicitação de cancelamento foi realizada através de um serviço. Esta variável só pode ser consultada nos eventos *beforeCancelProcess* e *afterCancelProcess*. |
| WKUserLocale | Identifica o idioma corrente do usuário. |
| WKManagerMode | Identifica se o processo está sendo movimentado pela visão do gestor do processo ou não. Importante notar que esse parâmetro apenas retorna true/false caso o formulário esteja sendo movimentado por um processo *workflow*. Caso ele esteja sendo aberto e alterado pela navegação de documentos este parâmetro é nulo. |
| WKReplacement | Código do usuário substituto Observação Para processos que estejam sendo acessados por um usuário substituto, o usuário logado será o retorno do parâmetro WKReplacement |
| WKIsTransfer | Permite verificar se o usuário está ou não transferindo uma tarefa. |
| WKCurrentMovto | Permite a movimentação do processo. |
| WKActualThread | Retorna a Thread atual do processo. |
| takeTask | Identifica se a atividade foi assumida. |

0.5falsesamplesfadetrue1Exemplo 1

Para validar se o usuário está completando uma atividade corretamente, basta utilizar o evento **beforeTaskSave** e retornar alguma mensagem caso queira disparar um erro. Por exemplo, segue parte de um código de desenvolvimento de um processo sob a plataforma:

javascriptEclipse1true3Exemplo 3

Para iniciar uma nova solicitação de um outro processo ao finalizar uma solicitação podem ser executados os seguintes procedimentos:

1. Cadastrar um serviço no fluig em que a URL seja o WSDL do serviço ECMWorkflowEngineService.
2. Implementar o evento **afterProcessFinish** utilizando o exemplo abaixo, sendo ‘process2’ o novo processo a ser inicializado.

jsEclipse1true/webdesk/ECMWorkflowEngineService?wsdl
// Busca o webservice cadastrado com o código "WorkflowEngineService"
var workflowEngineServiceProvider = ServiceManager.getServiceInstance(serviceName);
var workflowEngineServiceLocator = workflowEngineServiceProvider.instantiate("com.totvs.technology.ecm.workflow.ws.ECMWorkflowEngineServiceService");
var workflowEngineService = workflowEngineServiceLocator.getWorkflowEngineServicePort();
 
// Cria o ProcessAttachmentDtoArray
var processAttachmentDtoArray = workflowEngineServiceProvider.instantiate("com.totvs.technology.ecm.workflow.ws.ProcessAttachmentDtoArray");
// Cria o ObjectFactory
var objectFactory = workflowEngineServiceProvider.instantiate("net.java.dev.jaxb.array.ObjectFactory");
// Cria um String[][]
var cardData = objectFactory.createStringArrayArray();
   // Cria uma solicitação
workflowEngineService.simpleStartProcess(user, pass, companyId, processId, "Comment", processAttachmentDtoArray, cardData);
}]]>

Existem outros métodos parar iniciar uma solicitação, consulte-os [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=73084007#UtilizaçãodeWebservices-ECMWorkflowEngineService).

Lembre-se de consultar a classe ObjectFactory do serviço, essa classe possui diversos métodos para criar instância de objetos necessários para utilização do serviço.

4Exemplo 4

Exemplo para barrar o usuário de movimentar a solicitação com o campo "nome" vazio. Caso o mesmo salve a solicitação, a ação será permitida.

jsEclipse1trueExemplo 5

Exemplo que permite verificar se o usuário está ou não transferindo uma tarefa:

jsEclipsetrue
