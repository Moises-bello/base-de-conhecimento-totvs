---
content_hash: acdd7ff06887f7f0837aea8b2800f0c4f77c65c85aeae6e9f4a1963601bb61ef
fetched_at: '2026-06-28T21:35:17.168861+00:00'
page_id: '1022378520'
product: fluig
source: tdn-fluig
title: Outros Eventos Globais
type: documentation
url: https://tdn.totvs.com/display/fluig/Outros+Eventos+Globais
version: 4
---

2

# Eventos gerais disponíveis

---

A seguir, são apresentados os **eventos gerais** disponíveis no Fluig, que podem ser disparados independentemente de uma atividade específica de um card.

### DisplayCentralTasks

Este evento é disparado **sempre antes** da exibição da central de tarefas. Por meio dele, é possível **inserir**, **alterar** ou **remover** os links exibidos nessa central. O evento recebe como parâmetro um **LinkedHashMap** contendo os links disponíveis na central de tarefas.

#### **Exemplo de como adicionar um link customizado ao final dos itens da central de tarefas**

java

#### **Exemplo de alteração na ordem de exibição dos links padrão, com a adição de três novos links: um no início e dois ao final**

java

Disponibilizamos outras informações sobre o usuário e a empresa, porém essas informações podem ser consultadas somente via método **getValue**.

|  |  |
| --- | --- |
| **WKUser** | Código do usuário |
| **WKCompany** | Número da empresa |

javaExemplo

### DisplayCustomMetadata

Este evento é disparado antes da exibição dos campos customizados de um documento, tanto no momento da publicação quanto da edição. Por meio dele, é possível definir valores iniciais para os campos customizados dos metadados do documento. O evento recebe como parâmetro uma referência aos campos customizados do documento.

javaExemplo

No contexto deste evento a variável **fields** pode ser utilizada para consultar ou modificar os valores dos campos customizados de um documento. **Não permitindo adicionar novos campos**.

Para inserir novos campos em um documento, podem ser utilizadas as formas descritas abaixo.

* Pela herança da pasta pai;
* No cadastro de **Campos Customizados**, marcando a opção *Mostrar em todos documentos* ou da forma padrão;
* Através do WebService CustomFieldsService;
* Na edição dos metadados do documento, pelo usuário.

Para consultar o valor de um campo customizado neste evento, utiliza-se o **fields.getValue** passando como parâmetro o código do campo desejado. Retornando “null”, casso o campo não esteja disponível para este documento.

javaExemplo

Já pra a **edição** utiliza-se o fields.setValue, passando como parâmetro, **primeiro o nome do campo**, **em seguida o valor**.

javaExemplo

Além dos valores dos campos customizados, disponibilizamos outras informações do documento que está sendo criado ou editado, porém essas informações podem ser consultadas somente via método **getValue**.

|  |  |
| --- | --- |
| **WKUser** | Código do usuário |
| **WKCompany** | Número da empresa |
| **WKNumParentDocument** | Número da pasta pai |
| **WKDocumentType** | Tipo do documento |
| **WKPrivateDocument** | Se o documento esta sendo publicado na pasta particular (true/false) |

javaExemplo

### BeforeWatchContent

Este evento é utilizado quando, ao acompanhar um conteúdo, é necessário recuperar informações do registro **antes** da execução da ação de “acompanhar”. Por exemplo, ao acompanhar um documento, é possível obter suas informações e utilizá-las em um **dataset**.

javaExemplo

Sendo os parâmetros:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **companyId** | Código da Empresa | int |
| **watchDTO** | Dados do registro | WatchDTO |

javaExemplo0){
throw "Sua solicitação de notificação foi negada, pois o documento está em checkout." ;
}
}
}]]>

### AfterWatchContent

Este evento é utilizado quando, ao acompanhar um conteúdo, é necessário recuperar informações do registro **após** a execução da ação de “acompanhar”. Por exemplo, ao acompanhar um post, é possível recuperar suas informações e utilizá-las para informar o usuário sobre o autor da publicação.

javaExemplo

Sendo os parâmetros:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **companyId** | Código da Empresa | int |
| **watchDTO** | Dados do registro | WatchDTO |

javaExemplo

### BeforeUnwatchContent

Este evento é utilizado quando, ao deixar de acompanhar um conteúdo, é necessário recuperar informações do registro **antes** da execução da ação de “deixar de acompanhar”. Por exemplo, ao tentar deixar de acompanhar uma comunidade, é possível avaliar se o usuário pode ou não deixar de acompanhá-la.

javaExemplo

Sendo os parâmetros:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **companyId** | Código da Empresa | int |
| **watchDTO** | Dados do registro | WatchDTO |

javaExemplo

### AfterUnwatchContent

Este evento é utilizado quando, ao deixar de acompanhar um conteúdo, é necessário recuperar informações do registro **após** a execução da ação de “deixar de acompanhar”. Por exemplo, ao deixar de acompanhar um post, é possível recuperar suas informações e informar ao usuário que aquele post possui muitos seguidores.

javaExemplo

Sendo os parâmetros:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **companyId** | Código da Empresa | int |
| **watchDTO** | Dados do registro | WatchDTO |

javaExemplo

### beforeCreateUser

Evento disparado **antes da criação de um novo usuário**. Pode ser utilizado para realizar validações antes da criação do usuário ou para adicionar dados adicionais de forma programática.

js

Somente os atributos **firstName**, **lastName**, **fullName** podem ser modificados. Para adicionar dados adicionais é necessário utilizar o método **addData** do **UserEventVO**.

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **user** | Objeto que contém as informações do usuário |  |

#### **Exemplo de implementação**

jstrue

### afterCreateUser

Evento disparado depois da criação de um novo usuário. Pode ser utilizado quando for necessário realizar alguma rotina com o usuário criado, como exemplo a criação de recursos adicionais para o usuário.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **user** | Objeto que contém as informações do usuário |  |

#### **Exemplo de implementação**

jstrue

### beforeUpdateUser

Evento disparado antes da atualização de um usuário. Pode ser utilizado quando for necessário realizar validações no usuário antes da sua atualização ou adicionar dados adicionais programaticamente.

js

Somente os atributos **firstName**, **lastName**, **fullName** podem ser modificados. Para adicionar dados adicionais é necessário utilizar o método **addData** do **UserEventVO**.

Para verificar se a senha do usuário foi alterada basta utilizar o método **getPassword**, onde caso seja retornado algum valor significa que a senha foi alterada. Já para verificar se a atualização do usuário foi realizada por ele próprio, através da edição de perfil, é necessário comparar o login do usuário recebido como parâmetro, através do método **getLogin** com o login do usuário corrente, resgatado através da chamada **getValue("WKUser")**, onde caso sejam iguais significa que a atualização foi realizada pelo próprio usuário.

exemplo

jstrue

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **user** | Objeto que contém as informações do usuário |  |

#### **Exemplo de implementação**

jstrue

### afterUpdateUser

Evento disparado depois da atualização de um usuário, ou após a gravação de uma nova senha, pelo recurso de reset de senha da .

O evento *afterUpdateUser* será disparado no reset de senha pela tela de login somente na **atualização 1.6.5 ou superior**.

Este evento pode ser utilizado quando for necessário executar alguma rotina com o usuário atualizado, como, por exemplo, a atualização de recursos adicionais associados a esse usuário.

js

Para verificar se a senha do usuário foi alterada basta utilizar o método **getPassword**, onde caso seja retornado algum valor significa que a senha foi alterada. Já para verificar se a atualização do usuário foi realizada por ele próprio, através da edição de perfil, é necessário comparar o login do usuário recebido como parâmetro, através do método **getLogin** com o login do usuário corrente, resgatado através da chamada **getValue("WKUser")**, onde caso sejam iguais significa que a atualização foi realizada pelo próprio usuário.

exemplo

jstrue

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **user** | Objeto que contém as informações do usuário |  |

#### **Exemplo de implementação**

jstrue

### beforeDeactivateUser

Evento disparado antes da desativação de um usuário. Pode ser utilizado quando for necessário realizar validações no usuário antes da sua desativação.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário a ser desativado | String |

#### **Exemplo de implementação**

jstrue 0) {
throw "O usuário " + login + " não pode ser desativado por ser moderador nas comunidades: "
+ moderateCommunities.join(", ") + ".";
}
}]]>

### afterDeactivateUser

Evento disparado depois da desativação de um usuário. Pode ser utilizado quando for necessário realizar alguma rotina com o usuário desativado.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário desativado | String |

#### **Exemplo de implementação**

jstrue

### beforeActivateUser

Evento disparado antes da ativação de um usuário. Pode ser utilizado quando for necessário realizar validações no usuário antes da sua ativação.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário a ser ativado | String |

#### **Exemplo de implementação**

jstrue

### afterActivateUser

Evento disparado depois da ativação de um usuário. Pode ser utilizado quando for necessário realizar alguma rotina com o usuário ativado.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário ativado | String |

#### **Exemplo de implementação**

jstrue

### afterLogin

Evento disparado após o login de um usuário. Pode ser utilizado quando for necessário realizar alguma rotina  quando o usuário é autenticado no fluig.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário | String |

#### **Exemplo de implementação**

jstrue

O evento **afterLogin** funciona mesmo com a autenticação via Identity. O DesktopSSO ou a autenticação automática não interfere na execução do evento, porque ele é executado depois do login não importando como é feito.

### onLoginError

Evento disparado quando ocorrer um erro de login de um usuário. Este erro pode ser por login e senha inválidos ou usuário inativo. Pode ser utilizado quando for necessário realizar alguma rotina quando ocorrer um erro de login ou apresentar uma mensagem personalizada para o usuário.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário | String |
| **errorCause** | Motivo do erro de login, onde:  0 - Login e senha inválidos 1 - Usuário inativo | Integer |

#### **Exemplo de implementação**

jstrue 3) {
service.blockUser(login);
throw "Seu usuário foi bloqueado por ultrapassar 3 tentativas de login"
} else {
throw "Tentativa de login " + loginAttempts + " de 3"
}
}
}]]>

### onLogout

Evento disparado quando o usuário realizar logout. Pode ser utilizado quando for necessário realizar alguma rotina quando o usuário realiza o logout no portal através da opção Sair.

js

Parâmetro da função:

|  |  |  |
| --- | --- | --- |
| Propriedade | Descrição | Tipo |
| **login** | Login do usuário | String |

#### **Exemplo de implementação**

jstrue

### onNotify

Para interferir no envio de uma notificação padrão do fluig, deve ser utilizado o evento global *onNotify*, que é disparado no momento em que qualquer notificação do fluig é enviada. Nesse evento, podem ser feitas alterações como, por exemplo, adicionar outros destinatários ao e-mail, modificar os valores dos parâmetros utilizados no template de e-mail, etc.

**Abaixo disponibilizamos um exemplo de como implementar este evento**

javascriptEclipsetrueAtenção

A partir da versão 1.3.3 do Fluig, recomenda-se fazer a validação do template utilizando **template == "TPLDOCUMENT\_APPROVAL\_PENDING****"**ao invés da função match(), evitando assim redundâncias na customização, pois o match() pode retornar como válido para mais de um *template* em casos como TPLNEW\_TASK e TPLNEW\_TASK\_POOL\_GROUP.

Dica

A partir da versão Fluig 1.5.13 o fluigAPI estárá habilitado para este evento.

O evento onNotify está disponível na lista de eventos globais. Ao selecionar esse evento na lista de eventos disponíveis, a assinatura da função acima já será preenchida automaticamente. Este evento disponibiliza os seguintes parâmetros:

| Parâmetro | Descrição |
| --- | --- |
| **subject** | É o assunto do e-mail. A alteração desta variável irá implicar que todos os usuários recebam o e-mail com o novo assunto configurado. Exemplo de utilização: **subject.add("ASSUNTO");** |
| **receivers** | Lista de e-mails destinatários. Também é possível adicionar outros e-mails, de usuários que não participam do processo. Inclusive, podem ser adicionados e-mails de usuários que não estão cadastrados no fluig, caso seja necessário notificar uma pessoa que não tenha acesso ao sistema. |
| **template** | Permite validar qual tipo de e-mail está sendo enviado (por exemplo, template de documento em aprovação, documento expirando, etc). Com base nessa variável podemos distinguir quais e-mails queremos customizar. É recomendável que sempre seja verificado o código do template, para evitar que ocorram alterações em outros tipos de e-mail, que não necessitariam de customização. |
| **params** | É um mapa de dados que permite alterar/incluir parâmetros para que sejam apresentados no e-mail. O nome dos parâmetros informados nesse mapa devem ser os mesmos que são utilizados dentro do arquivo de template. |

No exemplo que foi apresentado acima é validado se o template se refere ao *"TPLDOCUMENT\_APPROVAL\_PENDING"* (que corresponde a documento pendente de aprovação). Em caso positivo, um novo e-mail será adicionado na lista de destinatários. Ou seja, além do responsável pela aprovação, outra pessoa será notificada, recebendo uma cópia do e-mail. Como está sendo validado o código do template, os demais tipos de e-mail não serão afetados.

Os templates podem ser consultados dentro do diretório do volume, em: *<VOLUME>\templates\tplmail*. Se for necessário adicionar algum parâmetro no e-mail padrão, os templates podem ser editados diretamente nesse diretório.

Importante

* O evento global onNotify possui bind de variáveis para acesso à log, datasetManager, DatasetFactory, DatasetBuilder, ConstraintType e ServiceManager.
* Recomenda-se verificar a lista de parâmetros (params) recebida antes de utilizá-los, pois estes variam de acordo com o template utilizado.
* Quando um workflow possuir evento onNotify, o evento global onNotify será ignorado para os e-mails daquele processo.
* É imprescindível a validação pelo código do template antes de qualquer implementação, pois TODOS os e-mails passarão por esta customização quando o evento estiver registrado.
Dica

Quando o evento onNotify for utilizado como evento global, é necessário informar uma constraint extra informando o usuário para fixar as permissões, já que o evento onNotify não é executado por nenhum usuário mas sim pelo sistema. Vale lembrar ainda que quando for utilizar algum dataset interno do fluig, é necessário tambem informar uma constraint.

exemplo

var constraintUser = DatasetFactory.createConstraint("userSecurityId", "nome\_do\_usuario", "nome\_do\_usuario", ConstraintType.MUST);

### beforeSendNotification

Evento disparado antes do envio de uma notificação ao usuário. Pode ser utilizado quando for necessário adicionar alguma informação à nota ou alterar a prioridade de uma notificação, possibilitando o cancelamento do envio da notificação caso seja definida uma prioridade através do evento.

Observação

Por questões de segurança, somente os campos *priority* e *note* podem ser alterados. Outras alterações não serão consideradas.

Importante

Caso seja lançada uma exceção através do evento a notificação não será enviada, mas esse não é o modo correto de cancelar o envio. Definir o campo *priority* como "NONE" impede que a notificação seja enviada sem a necessidade de lançar exceção.

**Abaixo temos um exemplo de como implementar esse evento**

javascriptEclipsetrue

São disponibilizadas algumas propriedades referentes à notificação que está sendo enviada.

|  |  |  |
| --- | --- | --- |
| **Propriedade** | **Descrição** | **Tipo** |
| **aliasSender** | Alias de quem enviou a notificação. Pode vir nulo nos casos em que a notificação é enviada pelo sistema. | String |
| **aliasReceiver** | Alias de quem vai receber a notificação. | String |
| **place** | Lugar onde foi feita a ação que gerou a notificação. Pode vir nulo quando não for um lugar socializavel. |  |
| **object** | Objeto sobre o qual foi feita a ação que gerou o alerta. |  |
| **eventType** | Tipo do evento que gerou a notificação. | String |
| **metadata** | Metadados da notificação. | Hashmap <String, String> |
| **priority** | Prioridade da notificação. Valores válidos:  NONE, LOW, NORMAL, HIGH. | String |
| **note** | Nota enviada junto à notificação. | String |

Veja o exemplo (**event-notification**) no repositório do fluig clicando **[aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-notification)**.

### afterSendNotification

Evento disparado após o envio de uma notificação ao usuário. Pode ser utilizado quando for necessário registrar alguma informação, para auditoria, por exemplo.

Abaixo segue um exemplo de como implementar etse evento:

javascriptEclipsetrue

São disponibilizadas algumas propriedades referentes à notificação que foi  enviada.

|  |  |  |
| --- | --- | --- |
| **Propriedade** | **Descrição** | **Tipo** |
| **aliasSender** | Alias de quem enviou a notificação. Pode vir nulo nos casos em que a notificação é enviada pelo sistema. | String |
| **aliasReceiver** | Alias de quem vai receber a notificação. | String |
| **place** | Lugar onde foi feita a ação que gerou a notificação. Pode vir nulo quando não for um lugar socializavel. |  |
| **object** | Objeto sobre o qual foi feita a ação que gerou o alerta. |  |
| **eventType** | Tipo do evento que gerou a notificação. | String |
| **metadata** | Metadados da notificação. | Hashmap <String, String> |
| **priority** | Prioridade da notificação. | String |
| **note** | Nota enviada junto à notificação. | String |

Veja o exemplo (**event-notification**) no [repositório do fluig](http://tdn.totvs.com/display/fluig/htt) clicando [aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-notification).

### onDisplayTasks

Este evento é disparado antes de serem exibidas as tarefas das aba "Tarefas a concluir" , "Minhas solicitações", "Tarefas em pool", "Tarefas em consenso" e "Minhas tarefas sob gerência" na central de tarefas. Através dele é possível inserir, alterar ou remover itens da central de tarefas. O evento recebe como parâmetro uma lista de das tarefas existentes.

#### **Exemplo de como adicionar, editar e remover uma tarefa personalizada ao final da lista de tarefas**

js

Disponibilizamos algumas informações para consulta através do método getValue.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| **WKUser** | Código do usuário logado. | String |
| **WKUserLocale** | Idioma do usuário logado. | String |
| **WKCompany** | Número da empresa. | Int |
| **taskUserId** | Código do usuário substituído, em caso de visualização da central como substituto. Nos demais casos retorna o usuário logado. | String |
| **taskType** | Indicador do tipo de tarefas que estão sendo exibidas, “open” tarefas a concluir e “requests” para minhas solicitações. | String |
| **filter** | Filtros utilizados. | Map<String, Object> |
| **order** | Ordenação aplicada. | String |
| **maxResult** | Número de resultados por página. | Int |
| **page** | Número da página atual. | Int |
| **taskId** | Em caso de pool,  quando o taskType for pool, o taskId trará uma string contendo o tipo no caso ‘Role’ para papel ou ‘Group‘ para grupo e seu código. Exemplo: ‘Pool:Role:admin’ para um pool do papel ‘admin’. | String |

jsExemplo

### onDisplayTasksSummary

Este evento é disparado antes de serem exibidos os contadores das abas e gráficos da central de tarefas e widgets de BPM. Através dele é possível alterar números de tarefas pendentes de cada tipo.

#### **Exemplo alterando o número de tarefas abertas e no prazo**

js

O objeto recebido como parâmetro contém:

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| **expiredTasks** | Solicitações atrasadas. | Int |
| **openTasks** | Solicitações no prazo. | Int |
| **myRequests** | Minhas solicitações. | Int |
| **toApprover** | Aprovação de documentos pendentes. | Int |
| **myDocuments** | Documentos aguardando aprovação. | Int |
| **checkout** | Documento em checkout. | Int |
| **learningTasks** | Atividades de Aprendizado. | Int |

js

Disponibilizamos algumas informações para consulta através do método getValue.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| **WKUser** | Código do usuário logado. | String |
| **WKUserLocale** | Idioma do usuário logado. | String |
| **WKCompany** | Número da empresa. | Int |
| **taskUserId** | Código do usuário substituído, em caso de visualização da central como substituto. Nos demais casos retorna o usuário logado. | String |

jsExemplo

# Objetos utilizados nos eventos

---

Existem alguns objetos disponibilizados pelo produto que são utilizados nos eventos, nas próximas sessões eles serão explicados seus métodos e seus retornos.

#### **DocumentDto**

Este objeto representa o documento e suas propriedades, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getDocumentId()** | Retorna o número do documento. | int |
| **getVersion()** | Retorna o número da versão do documento. | int |
| **getCompanyId()** | Retorna o código da empresa em que o documento foi publicado. | Int |
| **getUUID()** | Retorna o UUID (identificador Único Global) do documento. | String |
| **getDocumentTypeId()** | Retorna o tipo do arquivo físico, se retornar branco ou nulo é porque esse tipo não é conhecido pelo fluig. | String |
| **getLanguageId()** | Retorna o código do Idioma do documento. | String |
| **getIconId()** | Retorna o código do Ícone do documento. | int |
| **getTopicId()** | Retorna o código do assunto do documento. | int |
| **getColleagueId()** | Retorna a matricula do usuário que criou o documento. | String |
| **getDocumentDescription()** | Retorna a descrição do documento. | String |
| **getAdditionalComments()** | Retorna os comentários adicionais do documento. | String |
| **getPhisicalFile()** | Retorna o nome do arquivo físico atrelado ao documento. | String |
| **getCreateDate()** | Retorna a data de criação. | java.util.Date |
| **getApprovedDate()** | Retorna a data de Aprovação. | java.util.Date |
| **getLastModifiedDate()** | Retorna a Data da última modificação. | java.util.Date |
| **getDocumentType()** | Retorna o tipo do documento, onde:  0 à Pasta raiz  1 à Pasta  2 à Documento normal  3 à Documento externo**1**  4 à Formulário  5 à Registro de formulário  7 à Anexo Workflow  8 à Novo Conteúdo  9 à Aplicativo  10 à Relatório  portal à Site  portalPage à Página de Site  **1** → A partir da atualização **2.0.0-26XXXX**, o recurso Documento externo foi desabilitado para novas empresas. | String |
| **getExpirationDate()** | Retorna a data de expiração. | java.util.Date |
| **getParentDocumentId()** | Retorna o número da Pasta/Formulário pai | int |
| **getRelatedFiles()** | String com o nome do arquivo físico principal e anexos. | String |
| **getActiveVersion()** | Retorna se a versão é ativa. | boolean |
| **getVersionDescription()** | Retorna a descrição da versão. | String |
| **getDownloadEnabled()** | Retorna se o documento permite Download | boolean |
| **getApproved()** | Retorna se o documento está em aprovação. | boolean |
| **getValidationStartDate()** | Retorna a partir de que data em que o documento poderá ser visualizado. | java.util.Date |
| **getPublisherId()** | Retorna a matricula do usuário que publicou o documento. | String |
| **getCardDescription()** | Retorna a descrição do registro de formulário, para documento do tipo 5. | String |
| **getDocumentPropertyNumber()** | Retorna o formulário que foi usado como base para criação do registro de formulário, por isso só tem um valor quando o documento é do tipo 5 (registro de formulário). | int |
| **getDocumentPropertyVersion()** | Retorna a versão do formulário em que o registro de formulário foi criado. | int |
| **getPrivateDocument()** | Retorna se o documento/pasta está abaixo da pasta particular. | boolean |
| **getPrivateColleagueId()** | Se é um documento particular retorna a matricula do usuário onde este documento está alocado. | String |
| **getIndexed()** | Retorna se o documento já foi indexado. | boolean |
| **getPriority()** | Retorna a prioridade do documento. | int |
| **getUserNotify()** | Retorna se notifica os usuários que tenham esse assunto de interesse. | boolean |
| **getExpires()** | Retorna se o documento está expirado. | boolean |
| **getVolumeId()** | Retorna o volume onde o documento foi publicado, se estiver em branco ele utiliza o volume do pai. | String |
| **getInheritSecurity()** | Retorna se herda segurança do pai. | boolean |
| **getUpdateIsoProperties()** | Retorna se atualiza as propriedades da cópia controlada. | boolean |
| **getLastModifiedTime()** | Retorna a hora da última modificação em milissegundos. | String |
| **getDeleted()** | Retorna se o documento está na lixeira. | boolean |
| **getDatasetName()** | Retorna o documento do dataset , se o documento é um formulário. | String |
| **getKeyWord()** | Retorna as palavras chaves do documento. Cada palavra é separada por vírgula. | String |
| **getImutable()** | Retorna se a versão/revisão é inalterável. | boolean |
| **getDraft()** | Retorna se o documento está em edição, para documento do tipo “Novo Conteúdo”. | boolean |
| **getInternalVisualizer()** | Retorna se utiliza visualizador interno. | boolean |
| **getPhisicalFileSize()** | Retorna o tamanho físico do documento principal e anexos. | float |
| **getVersionOption()** | Retorna a condição de versionamento do documento:  0 = Será mantida a versão  1 = Será criado nova revisão  2 = Será criado nova versão  **Importante lembrar que no momento da criação de um novo documento o valor sempre será 0.** | int |

javaExemplo

#### **DocumentEditDto**

Este objeto representa as propriedades editáveis de um documento, na tabela abaixo consta mais informações sobre ele:

| Função | Descrição da função | Tipo do retorno |
| --- | --- | --- |
| **setKeyWord** | Adiciona Palavras chaves no documento. Cada palavra é separada por vírgula. | void |
| **setExpires** | Define se o documento deve expirar | void |
| **setExpirationDate** | Define a data de expiração. | void |
| **setValidationStartDate** | Define a data a partir da qual o documento poderá ser visualizado. | void |

javaExemploAtenção

Lembrando que no javascript, no construtor new Date, o valor do "Mês" começa com o index 0, sendo 0 = Janeiro e 11 = Dezembro, veja outros exemplos [clicando aqui](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/Date).

#### **ApproverDto**

Este objeto representa os aprovadores e suas propriedades, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| **Função** | **Descrição da Função** | **Tipo do Retorno** |
| **getDocumentId()** | Retorna o número do documento. | int |
| **getVersion()** | Retorna o número da versão do documento. | int |
| **getCompanyId()** | Retorna o código da empresa em que o documento foi publicado. | Int |
| **getColleagueId()** | Retorna a matricula de um usuário ou o código do grupo que está aprovando este documento. É possível saber se vai retornar um usuário ou um grupo pelo tipo de aprovação. | String |
| **getApproverType()** | Retorna o tipo da aprovação, onde:  0 à Usuário  1 à Grupo | int |
| **getLevelId()** | Retorna o nível de aprovação, no caso de aprovação em níveis. | int |

javaExemplo

        

#### **DocumentSecurityConfigDto**

Este objeto representa a segurança de um documento e suas propriedades, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getDocumentId()** | Retorna o número do documento. | int |
| **getVersion()** | Retorna o número da versão do documento. | int |
| **getCompanyId()** | Retorna o código da empresa em que o documento foi publicado. | Int |
| **getAttributionValue()** | Retorna a matricula de um usuário ou o código do grupo que está na segurança deste documento. É possível saber se vai retornar um usuário ou um grupo pelo tipo da segurança.  Obs.: Retorna em branco quando o tipo é todos os usuários. | String |
| **getAttributionType()** | Retorna o tipo da segurança, onde:  1 à Usuário;  2 à Grupo;  3 à Todos os Usuários. | int |
| **getPermission()** | Retorna se é uma permissão.  Obs.: Se não é uma permissão é uma restrição. | boolean |
| **getShowContent()** | Retorna se lista o conteúdo. | boolean |
| **getSecurityLevel()** | Retorna no nível de permissão/restrição, onde:  -1 à sem permissão/restrição (nega acesso);  0 à Leitura;  1 à Gravação;  2 à Modificação;  3 à Total. | int |
| **getSequence()** | Retorna a sequência da permissão/restrição. | int |
| **getSecurityVersion()** | Retorna se ele utiliza a segurança deste versão nas demais. | boolean |

javaExemplo

#### **RelatedDocumentDto**

Este objeto representa os documentos relacionados e suas propriedades, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getDocumentId()** | Retorna o número do documento. | int |
| **getVersion()** | Retorna o número da versão do documento. | int |
| **getCompanyId()** | Retorna o código da empresa em que o documento foi publicado. | int |
| **getRelatedDocumentId()** | Retorna o número do documento que está relacionado ao documento publicado. | int |

javaExemplo

#### **ProcessDefinitionVersionDtoProcessDefinitionVersionDto**

Este objeto representa a definição de um processo e seus atributos. A tabela abaixo apresenta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getCompanyId()** | Retorna o código da empresa | Long |
| **getProcessId()** | Retorna o código do processo | Long |
| **getProcessDescription()** | Retorna a descrição do processo | String |
| **getVersion()** | Retorna a versão do processo | Integer |
| **getVersionDescription()** | Retorna a descrição da versão do processo | String |
| **getFormId()** | Retorna o código do formulário do processo | Integer |
| **getCategoryStructure()** | Retorna a categoria do processo | String |
| **getFullCategoryStructure()** | Retorna a estrutura completa da categoria do processo | String |

**UserEventVO****UserEventVO**

Este objeto representa um usuário e seus atributos, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getId()** | Retorna o identificador do usuário | Long |
| **getTenantId()** | Retorna o código da empresa | Long |
| **getLocationId()** | Retorna o código da localização à qual o usuário pertence | Long |
| **getFirstName()** | Retorna o nome do usuário | String |
| **getLastName()** | Retorna o sobrenome do usuário | String |
| **getFullName()** | Retorna o nome completo do usuário | String |
| **getEmail()** | Retorna se lista o conteúdo | String |
| **getLogin()** | Retorna o e-mail do usuário | String |
| **getPassword()** | Retorna a senha do usuário | String |
| **getIdpId()** | Retorna o identificador associado ao fluig Identity | String |
| **getUserCode()** | Retorna o código do usuário | String |
| **getUserType()** | Retorna o tipo do usuário, onde:  0 - Normal 3 - Aplicativo | Integer |
| **getState()** | Retorna o estado do usuário, onde:  0 - Não confirmado 1 - Ativo 2 - Bloqueado 3 - Removido | Integer |
| **getTimeZone()** | Retorna o Fuso Horário do usuário | String |
| **getRoles()** | Retorna a lista dos códigos dos papéis aos quais o usuário pertence | List<String> |
| **getGroups()** | Retorna a lista dos códigos dos grupos aos quais o usuário pertence | List<String> |
| **getData()** | Retorna os dados adicionais do usuário | Map<String, String> |
| **setFirstName(String firstName)** | Informa o nome do usuário | void |
| **setLastName(String lastName)** | Informa o sobrenome do usuário | void |
| **setFullName(String fullName)** | Informa o nome completo do usuário | void |
| **putData(String key, String value)** | Adiciona um novo dado adicional ao usuário. Só pode ser utilizado em eventos ***before**.* | void |

#### **WatchDTO**

Este objeto representa as notificações de acompanhamento de comentários e suas propriedades, na tabela abaixo consta mais informações sobre ele:

|  |  |  |
| --- | --- | --- |
| Função | Descrição da Função | Tipo do Retorno |
| **getEntityId()** | Retorna o código do Conteúdo. | String |
| **getUserId()** | Retorna o código do usuário. | String |
| **getUserAlias()** | Retorna o alias do usuário. | String |
| **getSociableId()** | Retorna ocódigo sociable. | String |
| **getCreationDate()** | Retorna a data de criação. | String |
| **getLastUpdateDate()** | Retorna a data da última atualizaçã. | String |
| **getNumberComments()** | Retorna o número de comentários. | String |
| **getNumberLikes()** | Retorna o número de apoios. | String |
| **getNumberShares()** | Retorna o número de compartilhamentos. | String |
| **getNumberWatchers()** | Retorna o número de acompanhamentos. | String |
| **getNumberDenouncements()** | Retorna o número de denúncias. | String |
| **getSocialWatchType()** | Retorna o tipo (social) | String |
| **getPostAuthor()** | Retorna o autor do conteúdo. | String |
| **getTags()** | Retorna as tags. | String |
| **getText()** | Retorna o texto. | String |
| **getDescription()** | Retorna a descrição. | String |
| **getObjectClass()** | Retorna a classe do objeto. | String |
| **getObjectId()** | Retorna o objectId. | String |
| **getThumbURL()** | Retorna a url do thumb | String |

#### **SocialPostEventVO** **SocialPostEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialPostEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getText()** | texto do post | String |
| **getUser()** | alias do usuário que está postando | String |
| **getVisibility()** | visibilidade do post | String |
| **getPostId()** | identificador do post | String |
| **getCreationDate()** | data de criação do post | String |
| **getLastUpdateDate()** | data de ultima atualização do post | String |
| **getSociables()** | objetos sociables relacionado a esse post. Ex: Imagens, Vídeos, Artigos, etc... | List<> |
| **getSocial()** | objeto social onde o post foi feito. Pode ser timeline de um usuario ou um comunidade |  |
| **\*getAttributes()** | Atributos do Analytics em formato de Lista de Strings. Limite de 3 itens | List<String> |
| **\*getFacts()** | Fatos dos atributos do Analytics em formato de Lista de Strings. Limite de 3 itens | List<String> |
| **customData** | Mapa em formato JSON onde pode-se persistir dados extras da publicação | Map JSON |

#f2f2f2#f2f2f2

**\*Somente enviado no evento beforSocialPost e afterSocialPost, esses valores não são persistidos no Fluig**

#### **SociableEventVO** **SociableEventVO**

|  |  |  |
| --- | --- | --- |
| **SociableEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getId()** | identificador do objeto | String |
| **getCreationDate()** | data de criação do objeto | String |
| **getLastUpdateDate()** | ultima atualização do objeto | String |
| **getNumberLikes()** | quantidade de curtidas | String |
| **getNumberShares()** | quantidade de compartilhamentos | String |
| **getNumberComments()** | quantidade de comentários | String |
| **getNumberDenouncements()** | quantidade de denúncias | String |
| **getNumberWatchers()** | quantidade de acompanhamentos | String |
| **getTags()** | nomes marcadores | String |
| **getUrl()** | endereço do objeto | String |
| **getSociableType()** | tipo do objeto social | String |
| **getRemoved()** | informa se o objeto foi removido | String |
| **\*getPostAuthor()** | retorna o alias do autor da publicação que foi comentada | String |
| **\*getText()** | retorna o texto da publicação que foi comentada | String |
| **\*\*getDescription()** | Nome do objeto comentado | String |
| **\*\*getThumbURL()** | url de ícone do objeto comentado. | String |
| **getSocial()** | local aonde o comentário foi efetuado | SocialEvent |

#f2f2f2#f2f2f2

**\* Retornados apenas quando o comentário é sobre um post.**

**\*\*Retornado para os comentários de documentos e etc.**

#### **SocialEventVO** **SocialEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getId()** | identificador do objeto | String |
| **getCreationDate()** | data de criação do objeto | String |
| **getLastUpdateDate()** | ultima atualização do objeto | String |
| **getAlias()** | apelido do objeto social | String |
| **getName()** | nome do objeto social | String |
| **getDescription()** | descrição do objeto social | String |
| **getType()** | tipo do objeto social | String |
| **getState()** | status do objeto social | String |
| **getHidden()** | informa se o objeto é oculto | String |
| **getPrivateContent()** | informa se o conteúdo é privado | String |
| **getApprovalRequired()** | informa se aprovação é requerida | String |
| **getCustomPage()** | informação de página customizada | String |

#### **SocialShareEventVO** **SocialShareEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialShareEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSociable()** | objeto sendo compartilhado |  |
| **getSocialPlace()** | objeto que recebe o compartilhamento |  |
| **getUser()** | alias do usuario que compartilha | String |
| **getText()** | texto informado no compartilhamento | String |
| **getType()** | tipo do objeto | String |

#### **SocialCommentEventVO** **SocialCommentEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialCommentEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSociable()** | objeto sendo compartilhado |  |
| **getUser()** | alias do usuário que comenta | String |
| **getText()** | texto informado no comentário | String |
| **getCommentId()** | id do comentário | String |

#### **SocialDenounceEventVO** **SocialDenounceEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialDenounceEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSociable()** | objeto sendo compartilhado |  |
| **getUser()** | alias do usuário que comenta | String |
| **getText()** | texto informado no comentário | String |
| **getType()** | Tipo de denúncia | String |

#### **SocialLikeEventVO** **SocialLikeEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialLikeEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSociable()** | objeto sendo compartilhado |  |
| **getUser()** | alias do usuário que comenta | String |

#### **SocialCommunityRelationEventVO****SocialCommunityRelationEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialCommunityRelationEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSocial()** | Social relacionado à comunidade |  |
| **getCommunity()** | Social que representa a Comunidade |  |

#### **SocialFollowEventVO****SocialFollowEventVO**

|  |  |  |
| --- | --- | --- |
| **SocialFollowEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getSocial()** | Social que seguirá |  |
| **getFollowed()** | Social que está sendo seguido |  |

#### **SocialPictureEventVOSocialPictureEventVO**

|  |  |  |
| --- | --- | --- |
| SocialPictureEventVO | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **getLoggedUser()** | Alias do usuário autenticado | String |
| **getAlias()** | Alias do local aonde se está mudando a imagem (usuário| comunidade) | String |
| **getPath()** | Path do diretório onde a imagem foi salva | String |
| **getPictureName()** | Nome da imagem salva | String |
| **getWidth()** | Largura da imagem | int |
| **getHeight()** | Altura da imagem | int |

#### **GenericAlertEventVOGenericAlertEventVO**

|  |  |  |
| --- | --- | --- |
| **GenericAlertEventVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **objectId** | Id do objeto relacionado | String |
| **objectClass** | Classe que identifica o objeto relacionado | String |
| **link** | Link que está disponível no objeto. Pode vir nulo nos casos em que não existe um link de acesso | String |

#### **WorkflowTasksVOWorkflowTasksVO**

|  |  |  |
| --- | --- | --- |
| **WorkflowTasksVO** | | |
| Propriedade / Método | Descrição | Tipo / Retorno |
| **url** | Url destino para tarefas personalizadas | String |
| **code** | Código para tarefas personalizadas | String |
| **processId** | Código do processo | String |
| **processDescription** | Descrição do processo | String |
| **requesterId** | Código do usuário de abertura | String |
| **requesterName** | Nome do usuário de abertura | String |
| **stateDescription** | Descrição da atividade atual | String |
| **colleagueName** | Nome do usuário responsável pela tarefa atual | String |
| **dateExpires** | Data de expiração | String |
| **attachDescription** | Descrição do anexo principal | String |
| **expired** | Tarefa expirada? | boolean |
| **know** | Usuário já visualizou a tarefa? | boolean |
| **fieldValue1** | Campo do formulário | String |
| **fieldValue2** | Campo do formulário | String |
| **fieldValue3** | Campo do formulário | String |
| **fieldValue4** | Campo do formulário | String |
| **fieldValue5** | Campo do formulário | String |
| **fieldValue6** | Campo do formulário | String |
| **fieldValue7** | Campo do formulário | String |
| **fieldValue8** | Campo do formulário | String |
| **fieldValue9** | Campo do formulário | String |
| **fieldValue10** | Campo do formulário | String |
| **fieldValue11** | Campo do formulário | String |
| **fieldValue12** | Campo do formulário | String |
| **fieldValue13** | Campo do formulário | String |
| **fieldValue14** | Campo do formulário | String |
| **fieldValue15** | Campo do formulário | String |

## Exemplo com usuário de aplicação

---

No exemplo abaixo, a mensagem "**Post criado via evento**" é postada no mural:

js

Exemplo com usuário logado

---

js

# Atualização do Analytics

---

## Definição

É possível enviar dados ao **Analytics** a partir dos eventos de customização. Os dados recebidos no evento **não são persistidos no Fluig**, porém podem ser **alterados antes do envio** para o Analytics. Esses valores são transmitidos por meio do objeto **SocialPostEventVO**.

## Exemplo de uso

jsAssinatura do métodojsUtilização no Evento
