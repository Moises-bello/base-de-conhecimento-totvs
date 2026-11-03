---
content_hash: 3db64d7497e1d3c2b1841708e434b22f5572bfe3a85bb6184a6f51d64a8c6bd3
fetched_at: '2026-07-02T19:24:25.889480+00:00'
page_id: '514447254'
product: protheus
source: tdn-tec
title: Application Server - Guia de Abertura de chamado
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+Guia+de+Abertura+de+chamado
version: 15
---

Guia de Abertura de chamado

Guia de abertura de issues no Jira para atendimento do time de Tecnologia Clients, no projeto TOTVS | Platform - Servers (**DTAPPSRV**).

Abaixo são descritos o padrão, os requisitos e informações necessários por tipo de Issue:

FieldTab,nFeedFieldTab,nFeedyesFieldTabManutenção,Melhoria,Apoio,Documentação,Teste SistêmicoManutenção,Melhoria,Apoio,Documentação,Teste SistêmicoyesManutenção

Para abertura de chamados de manutenção é obrigatório seguir o guia abaixo.

Devolução para Atendimento

As issues que não atenderem o padrão descrito ou que não tenha as informações solicitadas nesse guia **serão rejeitadas para atendimento**.

**Guia de Abertura de manutenção:**

* Issue Type

Selecione o tipo **Manutenção** para a issue que será criada.

* Resumo (Summary) :

  Descreva resumidamente o problema que está acontecendo. Evite títulos genéricos como: Erro no AppServer.

  ---
* Descrição (Description) :

  Descrição]]>
* Affected Version:

       A informação do Application Server utilizada pode ser obtida das seguintes formas:

1. Cabeçalho do arquivo console.log
2. Executando o comando appserver.exe -version

Versionamento

A versão do Application Server não está relacionada a versão dos produtos TOTVS (Protheus, Logix). Dúvidas sobre o versionamento do Application Server podem ser esclarecidas .

* ---

  Componente (Component/s) :

Selecione o componente na qual se encaixa o erro reportado, conforme abaixo:

| Componente | Descrição | Componente | Descrição |
| --- | --- | --- | --- |
| 4GL | Problemas relacionados a linguagem 4GL (Logix). | Preprocessador | Problemas relacionados ao preprocessador. |
| ADVPL | Problemas relacionados a linguagem ADVPL. | SSL | Problemas relacionados a segurança e criptografia. |
| AppServer Command Line | Problemas relacionados aos recursos por linha de comando. | TELNET | Problemas relacionados ao serviço de TELNET. |
| EMAIL | Problemas relacionados ao serviços de envio e recebimento de e-mail. | TLPP | Problemas relacionados a linguagem TLPP. |
| FTP | Problemas relacionados ao serviço de FTP. | WSDL | Problemas relacionados a WSDL. |
| HTTP | Problemas relacionados ao serviço de HTTP. | LockServer | Problemas relacionados ao serviço LockServer. |

---

* Anexos (Attachment) **obrigatórios**:

Conteúdo dos anexos

console.log: Geração do [console.log](http://tdn.totvs.com.br/display/tecen/ConsoleLog), desde o momento do inicio do AppServer (com o \*\*\* [www.totvs.com.br](http://www.totvs.com.br) \*\*\*)

Exemplo de um POC:

cppModelo de POCCaso não tenha um POC

Caso não tenha um POC identicando o problema, verifique o fluxo abaixo para que seu chamado não seja rejeitado:

truetruefalseDORfalse6514

noMelhoria

Para abertura de chamados de melhoria é obrigatório seguir o guia abaixo.

Devolução para Atendimento

As issues que não atenderem o padrão descrito neste guia serão rejeitadas para atendimento.

Requisitos de RoadMap

* Para solicitações internas de Segmento: Existência de RoadMap de produto com a necessidade da melhoria.
* Para solicitações de Clientes: Existência de no minimo 1 ticket de cliente, associado ou vinculada direto a issue.

**Guia de Abertura de melhoria:**

* Issue Type:

* Resumo (Summary) :  
       

  ---
* Descrição (Description) :

  ---
* Componente (Component/s) :

Selecione o componente na qual se encaixa a melhoria, conforme abaixo:

| Componente | Descrição | Componente | Descrição |
| --- | --- | --- | --- |
| 4GL | Problemas relacionados a linguagem 4GL. | Preprocessador | Problemas relacionados ao preprocessador. |
| ADVPL | Problemas relacionados a linguagem ADVPL. | SSL | Problemas relacionados a segurança e criptografia. |
| AppServer Command Line | Problemas relacionados aos recursos por linha de comando. | TELNET | Problemas relacionados ao serviço de TELNET. |
| EMAIL | Problemas relacionados ao serviços de envio e recebimento de e-mail. | TLPP | Problemas relacionados a linguagem TLPP. |
| FTP | Problemas relacionados ao serviço de FTP. | WSDL | Problemas relacionados a WSDL. |
| HTTP | Problemas relacionados ao serviço de HTTP. | LockServer | Problemas relacionados ao serviço LockServer. |

---

* Anexos (Attachment) :

Especificação.doc: Especificação da sugestão de melhoria e a necessidade.

POC.prw:

cppModelo de POCnoApoio

* Issue Type:

* Resumo (Summary):

* Descrição (Description):

noTeste SistêmiconoDocumnetação
