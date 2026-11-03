---
content_hash: e34413c00a438c270dbd3dfe4634c6ee48dc2f58d308a14c4d2ad7df51e2d130
fetched_at: '2026-06-28T21:35:24.669167+00:00'
page_id: '271178681'
product: fluig
source: tdn-fluig
title: Eventos de Documentos
type: documentation
url: https://tdn.totvs.com/display/fluig/Eventos+de+Documentos
version: 50
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam manipular os eventos de documentos. O objetivo é apresentar o seu funcionamento e a descrição dos campos utilizados.

# Pré-requisitos

---

Conhecer o conceito e as orientações sobre o .

# Eventos globais JavaScript

---

Os eventos de documentos são um conjunto de scripts carregados pela API de Documentos, os quais são desenvolvidos utilizando JavaScript e são chamados durante a execução de ação em Documentos ou em momentos específicos de interação em Documentos.

### AddDocumentConvertionExt

Este evento permite personalizar a conversão de documento realizada pelo TOTVS Fluig Plataforma. Mais informações sobre ele podem ser encontradas no guia [Conversores de Documentos](http://tdn.totvs.com/display/fluig/Conversores+de+Documentos).

### ValidateUpload

A partir da versão: 1.8.1- **[Silver Mist](https://tdn.totvs.com/x/hCFzL)**

Este evento sempre é disparado antes de realizar upload de arquivo para a plataforma, seja por API Rest, Soap/Webservices ou FTP. Através dele é possível validar o MIMEType ou Extensão do arquivo que está sendo feito upload e poder bloquear. O evento não recebe parâmetros, porém temos acesso à função getValue.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao arquivo que está sendo feito upload através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKCompany | Código da Empresa | int |
| WKFileName | Nome do arquivo com extensão | String |
| WKFileSize | Tamanho do arquivo em bytes | long |
| WKFilePath | Caminho absoluto do arquivo | String |
| WKFileMimeType | MimeType dos bytes do arquivo, ou seja, independente da extensão | String |
| WKUser | Usuário logado | String |

### ValidateCustomMetadata

Este evento sempre é disparado antes de salvar os valores dos campos customizados de um documento, tanto na publicação como edição. Através dele é possível alterar ou validar os valores dos campos customizados dos metadados de um documento. O evento recebe como parâmetro uma referência aos campos customizados.

**Exemplo:**

jstrue

No contexto deste evento a variável *fields* pode ser usada para consultar ou modificar os valores dos campos customizados de um documento. Não permitindo adicionar novos campos.  
Para inserir novos campos em um documento existe varias maneiras disponíveis.

* Pela herança da pasta pai.
* No cadastro de Campos Customizados, marcando a opção **Mostrar em todos documentos** ou da forma padrão.
* Através do *WebService CustomFieldsService*.
* Na edição dos metadados do documento, pelo usuário.

Para consultar o valor de um campo customizado neste evento, utiliza-se o *fields.getValue* passando como parâmetro o código do campo desejado. Retornando *null*, caso o campo não esteja disponível para este documento.

**Exemplo:**

jstrue

Já para realizar a edição utiliza-se o *fields.setValue*, passando como parâmetro, primeiro o nome do campo, em seguida o valor.

**Exemplo:**

jstrue

Alem dos valores dos campos customizados disponibilizamos algumas informações do documento que está sendo criado ou editado, porém somente para consulta através do método *getValue*.

|  |  |
| --- | --- |
| WKUser | Código do usuário |
| WKCompany | Número da empresa |
| WKNumParentDocument | Número da pasta pai |
| WKDocumentType | Tipo do documento |
| WKDocumentTypeId | ID do tipo de documento |
| WKPrivateDocument | Se o documento esta sendo publicado na pasta particular (true/false) |
| WKNumAcess | Número de acessos |
| WKComments | Comentários do documento |
| WKAuthor | Código do autor do documento |
| WKCreateDate | Data de criação do documento |
| WKDescription | Descrição do documento |
| WKNumDocument | Número do documento |
| WKNumVersion | Número da versão do documento |
| WKExpirationDate | Data de expiração do documento |
| WKExpires | Documento expira? (true/false) |
| WKFileSize | Tamanho do documento em bytes |
| WKKeyWord | Palavras chaves do documento |
| WKVolume | Volume do documento |
| WKSubject | Assunto relacionado ao documento |

Veja o exemplo em nosso repositório [aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse).

**Exemplo:**

jstrue

As exceções podem ser tratadas utilizando o comando *throw*. Este comando retornará uma mensagem ao usuário ao tentar salvar o documento.

**Exemplo:**

jstrue

### BeforeDocumentPublisher

Utilizado quando é preciso fazer validação customizada nas propriedades da tela de publicação/edição de documentos antes de salva-lo no banco de dados. Dentre todas as propriedades da tela de publicação/edição de documentos não serão tratados os campos customizados, pois já existe um evento que trata esta situação.

São disponibilizadas algumas propriedades referentes ao documento que está sendo criado ou editado, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKDocument | Objeto do Documento | [DocumentDto](https://tdn.totvs.com/x/EIl8B#DesenvolvimentodeEventos-DocumentDto) |
| WKDocumentEdit | Objeto do Documento | [DocumentEditDto](https://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentEditDto) |
| WKSubject | Descrição do Assunto do documento | String |
| WKListApprover | Lista dos Aprovadores do documento | List<[ApproverDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-ApproverDto)> |
| WKListSecurity | Lista com a segurança do documento | List<[DocumentSecurityConfigDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentSecurityConfigDto)> |
| WKListRelatedDocument | Lista com os documentos relacionados ao documento | List<[RelatedDocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-RelatedDocumentDto)> |
| WKState | Estado da ação: PUBLISH ou MODIFY | String |
| WKUser | Usuário logado | String |
| WKCompany | Código da Empresa | int |

O produto retorna *null* quando for necessário pegar umas das propriedades do documento que não exista.

Por exemplo: Nem todos os documentos publicados tem aprovador, logo a variável *WKListApprover* só terá informações quando realmente existirem aprovadores na publicação.

**Exemplos de implementação:**

falseExemplos beforeDcoumentPublisher1- Validar informações do documento

É possível usar vários objetos e fazer validações e é muito comum validar permissões específicas ao negócio do cliente e não permitir a inclusão do documento.

No exemplo abaixo, o trecho de código está mostrando todos os possíveis atributos, declara os possíveis objetos, exibe no log algumas informações desses objetos, depois verifica os aprovadores, validando que não pode conter um usuário administrador como aprovador e exibe todos documentos relacionados.

jstrue2- Impedir publicação com descrição repetida

Exemplo de evento que impede o usuário de publicar um documento com descrição repetida em uma determinada pasta.

jstrue 0
&& (datasetDocumentActive.getValue(0, "documentDescription") == doc.getDocumentDescription());
var isExistDocDeleted = datasetDocumentDeleted != null && datasetDocumentDeleted.rowsCount > 0
&& (datasetDocumentDeleted.getValue(0, "documentDescription") == doc.getDocumentDescription());
if (isExistDoc || isExistDocDeleted) {
throw "Já existe um documento com a mesma descrição informada";
}
}
}
}
]]>3- Tornar campo descrição/versão/revisão obrigatório

Exemplo de como tornar o campo 'Descrição/Versão/Revisão' de preenchimento obrigatório, apresentado no momento do check-in do documento.

jstrue 0) {
throw "Para efetuar o checkin é necessário informar a Descrição da Versão!";
}
}
}]]>4- Parametrizar keyword do documento

Exemplo de uso do parâmetro WKDocumentEdit no evento, para que seja possível atualizar o campo keyWord do documento.

jstrue5- Impedir publicação pela extensão do arquivo físico

Exemplo de como impedir a publicação pela extensão do arquivo físico.

jstrue6- Controlando a versão manualmente em novos documentos

Exemplo de uso do parâmetro WKDocumentEdit no evento para que seja possível controlar as propriedades version, validationStartDate e expirationDate do documento.

jstrue

### **AfterDocumentPublisher**

Utilizado quando é preciso fazer alguma manipulação customizada nas propriedades da tela de publicação/edição de documentos depois que ele foi salvo no banco de dados. Dentre todas as propriedades da tela de publicação/edição de documentos não serão tratados os campos customizados.

**Exemplo:**

jstrue

As propriedades recuperadas através do método *getValue*() são as mesmas do eventos *beforeDocumentPublisher* e a forma de manipulação das propriedades pode ser vista no exemplo do evento *beforeDocumentPublisher*.

### BeforeDocumentRemove

Este evento é executado antes do documento ir para a lixeira.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que está removido, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKSubject | Descrição do Assunto do documento | String |
| WKListApprover | Lista dos Aprovadores do documento | List<[ApproverDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-ApproverDto)> |
| WKListSecurity | Lista com a segurança do documento | List<[DocumentSecurityConfigDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentSecurityConfigDto)> |
| WKListRelatedDocument | Lista com os documentos relacionados ao documento | List<[RelatedDocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-RelatedDocumentDto)> |
| WKState | Estado da ação: PUBLISH ou MODIFY | String |
| WKUser | Usuário logado | String |
| WKCompany | Código da Empresa | int |

### AfterDocumentRemove

Este evento é executado logo após o documento ir para a lixeira.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que foi removido, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKSubject | Descrição do Assunto do documento | String |
| WKListApprover | Lista dos Aprovadores do documento | List<[ApproverDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-ApproverDto)> |
| WKListSecurity | Lista com a segurança do documento | List <[DocumentSecurityConfigDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentSecurityConfigDto)> |
| WKListRelatedDocument | Lista com os documentos relacionados ao documento | List<[RelatedDocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-RelatedDocumentDto)> |
| WKState | Estado da ação: PUBLISH ou MODIFY | String |
| WKUser | Usuário logado | String |
| WKCompany | Código da Empresa | int |

### BeforeDocumentRestore

Este evento é executado antes do documento ser restaurado da lixeira.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que está sendo restaurado, porém somente para consulta através do método *getValue*.

| Propriedade | Descrção | Tipo |
| --- | --- | --- |
| WKUser | Código do usuário | String |
| WKCompany | Número da empresa | int |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKUserLocale | Idioma do Usuário logado | String |
| WKSubject | Assunto do documento | String |

### AfterDocumentRestore

Este evento é executado logo após o documento ser restaurado da lixeira.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que foi restaurado, porém somente para consulta através do método *getValue*.

| Propriedade | Descrção | Tipo |
| --- | --- | --- |
| WKUser | Código do usuário | String |
| WKCompany | Número da empresa | int |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKUserLocale | Idioma do Usuário logado | String |
| WKSubject | Assunto do documento | String |

### BeforeDocumentRemovePermanently

Este evento é executado antes do documento ser excluído permanentemente

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que está sendo excluído permanentemente, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKUser | Código do usuário | String |
| WKCompany | Número da empresa | int |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKUserLocale | Idioma do Usuário logado | String |

### **AfterDocumentRemovePermanently**

Este evento é executado logo após o documento ser excluído permanentemente.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que foi excluído permanentemente, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKUser | Código do usuário | String |
| WKCompany | Número da empresa | int |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKUserLocale | Idioma do Usuário logado | String |

### BeforeDocumentViewer

Este evento é utilizado quando é preciso fazer validação customizada antes da visualização de algum documento.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que está sendo visualizado, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKUser | Usuário logado | String |
| WKCompany | Código da Empresa | int |

**Exemplo:**

jstrue0){
throw "Este documento está em check-out e não pode ser visualizado. Foi gerado o documento " + ds.getValue(0,"allocatedDocumentPK.destinationDocument") + " que está sob responsabilidade do usuário com matrícula "+ ds.getValue(0,"colleagueId");
}
}]]>

Veja o exemplo (**event-document-expiration-date-validation**) no [repositorio do TOTVS Fluig Plataforma](https://git.fluig.com/projects/SAMPLES) clicando [aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/event-document-expiration-date-validation).

### **BeforeDownloadContent**

Este evento é utilizado quando é preciso fazer validação customizada antes do download de algum documento.

**Exemplo:**

jstrue

São disponibilizadas algumas propriedades referentes ao documento que está sendo visualizado, porém somente para consulta através do método *getValue*.

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| WKDocument | Objeto do Documento | [DocumentDto](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) |
| WKSubject | Descrição do Assunto do documento | String |
| WKUserLocale | Idioma do Usuário logado | String |
| WKUser | Usuário logado | String |
| WKCompany | Código da Empresa | int |

**Exemplo:**

jstrue 0) {
var parent = ds.getValue(0, "parentDocumentId");
if (parent == 43) {
throw "Download não permitido!";
}
}
}]]>

### AfterSaveCard

Este evento é utilizado quando ao criar/salvar os dados de um registro de formulário pela Navegação de Documentos ou por movimentações *Workflow* se deseja salvar os dados do registro de formulário de uma forma externa. Por exemplo, ao criar um registro de formulário, enviar os dados do mesmo para um *Webservice* de outro produto.

**Exemplo:**

jstrue

Sendo os parâmetros:

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| formId | Código do Formulário | int |
| cardId | Código do Registro de Formulário | int |
| versionId | Versão do Registro de Formulário | int |
| cardData | Dados do Registro de Formulário | Hashmap <String, String> |

**Exemplo:**

jstrue' + key + ': ' + cardData.get(key));
ar.push(field1);
}
var resultArr = serviceHelper.instantiate("com.totvs.technology.webdesk.forms.service.custom.CardKeyValueArray");
resultArr.setItem(ar);
service.create(companyId, formId, cardId, versionId, resultArr);
}]]>

### AfterDeleteCard

Este evento é utilizado como complemento do evento *afterSaveCard*. É chamado toda vez que um formulário ou um registro de formulário é eliminado da lixeira.

**Exemplo:**

jstrue

Sendo os parâmetros:

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| companyId | Código da Empresa | int |
| cardId | Código do Registro de Formulário | int |

**Exemplo:**

jstrue

### onApplyDocumentPrintProperties

Este evento é chamado ao realizar a impressão de documentos que utilizam variáveis de cópia controlada. Onde será possível alterar ou obter o valor das variáveis disponibilizadas para este evento que podem ser consultadas em [Impressão de Cópia controlada](http://tdn.totvs.com/x/F5MbCQ).

É necessário que a opção **Atualiza propriedades de cópia controlada?** esteja habilitada nas propriedades do documento.

**Exemplo:**

jstrue

São disponibilizados os seguintes parâmetros de consulta:

| Parâmetro | Descrição |
| --- | --- |
| WKUser | Usuário logado |
| WKUserLocale | Local do usuário |
| WKCompany | Id do tenant atual |
| WKNumAcess | Número de acessos ao documento |
| WKComments | Comentários do documento |
| WKAuthor | Autor do documento |
| WKCreateDate | Data de criação do documento |
| WKDescription | Descrição do documento |
| WKNumDocument | Número do documento |
| WKNumParentDocument | Número do documento pai |
| WKNumVersion | Numero da versão |
| WKDocumentType | Tipo do documento |
| WKExpirationDate | Data de expiração do documento |
| WKExpires | Se documento expira ou não |
| WKFileSize | Tamanho do documento |
| WKKeyWord | Palavras chave do documento |
| WKDocumentTypeId | Id do tipo do documento |
| WKPrivateDocument | Indica se é documento privado |
| WKSubject | Assunto do documento |
| WKVolume | Id do volume do documento |

Propriedades que são atualizadas quando o documento é **visualizado**:

| Variável | Descrição | Formato |
| --- | --- | --- |
| Document.LevelN.ApproverM\* | --- |  |
| Document.Author | Autor do documento | Matricula - Nome do autor |
| Document.Comments | Comentários do documento | Texto |
| Document.ID | Código do documento | Número |
| Document.FirstVersionDate | Data da primeira versão | DD/MM/YYYY |
| Document.LastUpdateDate | Data da última atualização | DD/MM/YYYY |
| Document.CreationDate | Data de criação do documento | DD/MM/YYYY |
| Document.ExpiresOn | Data de expiração do documento | DD/MM/YYYY |
| Document.ApprovedOn | Data que o documento foi aprovado | DD/MM/YYYY |
| Document.VersionDescription | Descrição da Versão/Revisão | Texto |
| Document.Description | Descrição do documento | Texto |
| Document.Active | Documento ativo | true ou false |
| Document.Author.ID | Matricula do autor do documento | número |
| Document.Publisher.ID | Matricula do publicador do documento | Número |
| Document.Author.Name | Nome do autor do documento | Texto |
| Document.Publisher.Name | Nome do publicador do documento | Texto |
| Document.Approvers1 | Primeiro aprovador do nível 1 | Nome do aprovador |
| Document.Publisher | Publicador do documento | Matricula - Nome do publicador |
| Document.Revision | Revisão do documento | Número da Revisão |
| Document.ApproversN | Segundo aprovador do nível 1 | Nome do aprovador |
| Document.Tag | Tags do documento | Texto |
| Document.Version | Versão do documento | Versão,Revisão |

### onApplyDocumentProtocolProperties

Este evento é chamado ao realizar a impressão com documento de protocolo. Onde será possível alterar ou obter o valor das variáveis disponibilizadas para este evento que podem ser consultadas em [Impressão de Cópia controlada](http://tdn.totvs.com/x/F5MbCQ).

**Exemplo:**

jstrue

São disponibilizados os seguintes parâmetros de consulta:

| Parâmetro | Descrição |
| --- | --- |
| WKUser | Usuário logado |
| WKUserLocale | Local do usuário |
| WKCompany | Id do tenant atual |
| WKNumAcess | Número de acessos ao documento |
| WKComments | Comentários do documento |
| WKAuthor | Autor do documento |
| WKCreateDate | Data de criação do documento |
| WKDescription | Descrição do documento |
| WKNumDocument | Número do documento |
| WKNumParentDocument | Número do documento pai |
| WKNumVersion | Numero da versão |
| WKDocumentType | Tipo do documento |
| WKExpirationDate | Data de expiração do documento |
| WKExpires | Se documento expira ou não |
| WKFileSize | Tamanho do documento |
| WKKeyWord | Palavras chave do documento |
| WKDocumentTypeId | Id do tipo do documento |
| WKPrivateDocument | Indica se é documento privado |
| WKSubject | Assunto do documento |
| WKVolume | Id do volume do documento |

Propriedades que são atualizadas quando o documento **protocolo** é **impresso:**

| Variável | Descrição |
| --- | --- |
| Document.PrintDate | Data da impressão |
| Document.PrintRequester | Requisitante/Solicitante |
| Document.PrintedDocument.AreaResponsible | Responsável pela área |
| Document.PrintedDocument.Description | Descrição do documento |
| Document.PrintedDocument.Comments | Comentários do documento |
| Document.PrintedDocument.VersionDescription | Descrição da Versão/Revisão |
| Document.PrintedDocument.Tag | Tags do documento |
| Document.DocumentNrDocumento | Número do documento |
| Document.PrintedDocument.Version | Versão do documento |
| Document.PrintedDocument.Revision | Revisão do documento |
| Document.DestinationArea | Área |
| Document.PrintedDocument.Publisher | Publicador do documento |
| Document.PrintedDocument.VersionDescription1 | Descrição da versão do documento |
| Document.PrintedDocument.VersionDescription2 | Continuação da descrição da versão do documento |
| Document.PrintedDocument.VersionDescription3 | Continuação da descrição da versão do documento |

### onApplyDocumentPublishProperties

Este evento é chamado na publicação ou alteração de documentos. Onde será possível alterar ou obter o valor das variáveis disponibilizadas para este evento que podem ser consultadas em [Impressão de Cópia controlada](http://tdn.totvs.com/x/F5MbCQ).

**Exemplo:**

jstrue

São disponibilizados os seguintes parâmetros de consulta:

| Parâmetro | Descrição |
| --- | --- |
| WKUser | Usuário logado |
| WKUserLocale | Local do usuário |
| WKCompany | Id do tenant atual |
| WKNumAcess | Número de acessos ao documento |
| WKComments | Comentários do documento |
| WKAuthor | Autor do documento |
| WKCreateDate | Data de criação do documento |
| WKDescription | Descrição do documento |
| WKNumDocument | Número do documento |
| WKNumParentDocument | Número do documento pai |
| WKNumVersion | Numero da versão |
| WKDocumentType | Tipo do documento |
| WKExpirationDate | Data de expiração do documento |
| WKExpires | Se documento expira ou não |
| WKFileSize | Tamanho do documento |
| WKKeyWord | Palavras chave do documento |
| WKDocumentTypeId | Id do tipo do documento |
| WKPrivateDocument | Indica se é documento privado |
| WKSubject | Assunto do documento |
| WKVolume | Id do volume do documento |

Propriedades que são atualizadas quando o documento é **visualizado**:

| Variável | Descrição | Formato |
| --- | --- | --- |
| Document.LevelN.ApproverM\* | --- |  |
| Document.Author | Autor do documento | Matricula - Nome do autor |
| Document.Comments | Comentários do documento | Texto |
| Document.ID | Código do documento | Número |
| Document.FirstVersionDate | Data da primeira versão | DD/MM/YYYY |
| Document.LastUpdateDate | Data da última atualização | DD/MM/YYYY |
| Document.CreationDate | Data de criação do documento | DD/MM/YYYY |
| Document.ExpiresOn | Data de expiração do documento | DD/MM/YYYY |
| Document.ApprovedOn | Data que o documento foi aprovado | DD/MM/YYYY |
| Document.VersionDescription | Descrição da Versão/Revisão | Texto |
| Document.Description | Descrição do documento | Texto |
| Document.Active | Documento ativo | true ou false |
| Document.Author.ID | Matricula do autor do documento | número |
| Document.Publisher.ID | Matricula do publicador do documento | Número |
| Document.Author.Name | Nome do autor do documento | Texto |
| Document.Publisher.Name | Nome do publicador do documento | Texto |
| Document.Approvers1 | Primeiro aprovador do nível 1 | Nome do aprovador |
| Document.Publisher | Publicador do documento | Matricula - Nome do publicador |
| Document.Revision | Revisão do documento | Número da Revisão |
| Document.ApproversN | Segundo aprovador do nível 1 | Nome do aprovador |
| Document.Tag | Tags do documento | Texto |
| Document.Version | Versão do documento | Versão,Revisão |

# Desenvolvimento de Eventos JMS

---

O TOTVS Fluig Plataforma suporta o desenvolvimento de eventos JMS, permitindo criar procedimentos de auditoria com base nas informações fornecidas pelo produto. O JMS (Java Message Service) é uma API Java™ que provê uma conexão assíncrona entre aplicações por meio de troca de mensagens.

O produto dispara um tipo de mensagem JMS personalizável, o **wdkDocument**. O **wdkDocument** será acionado quando houver manipulação nos documentos da plataforma.

Para a aplicação receber a mensagem com as informações do documento, a classe tem que estender o *MessageListener* e ter a seguinte linha:

java

O objeto de retorno será um *MapMessage* que conterá os seguintes parâmetros:

* **event (String):** Informa qual o tipo de evento que foi efetuado com o documento, conforme a tabela abaixo:

| Evento | Descrição |
| --- | --- |
| PUBLISH | Um novo documento publicado |
| MODIFY | Documento é modificado |
| DELETE | Documento é excluído da base de dados |
| SENDRECYCLE | Documento é enviado para lixeira |
| DELETEFOLDER | Uma pasta é excluída da base de dados |
| EXTERNALCONVERTION | Documento com conversão customizada |
| CONVERTIONLONGTERM | Documento convertido para longo prazo |
| MOVE | Um ou mais documento ou pastas foram movidos de uma pasta para outra |
| RESTORERECYCLE | Restaura documentos e pastas da Lixeira |

* **companyId (Integer):** Código da empresa em que o documento foi manipulado.
* **colleagueId (String):** Usuário que efetuou a ação.
* **documentId (Integer):** Código do documento que sofreu a ação.
* **version (Integer):** Número da versão do documento.
* **lhasCreatedDocument (Boolean):** Informa se criou o documento.
* **IhasIncreasedVersion (Boolean):** Informa se foi incrementada a versão.
* **changedApproval (Boolean):** Informa se o aprovador foi modificado.
* **documento (byte[ ]):** Array de bytes com o documento e suas propriedades.
