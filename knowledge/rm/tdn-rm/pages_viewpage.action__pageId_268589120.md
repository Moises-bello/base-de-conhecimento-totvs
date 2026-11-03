---
content_hash: 7c56f47f7dda7c40ad2fdce485aa273f677b5b66c499148ce2ec6fa5e23d6a4f
fetched_at: '2026-06-29T00:08:20.882128+00:00'
page_id: '268589120'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-182_Melhorias_License_Server_Versão_1.03.010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268589120
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | FRAMEWORK |
| **Segmento Executor** | FRAMEWORK | | |
| **Projeto1** | FRW\_FRW002 | **IRM1** |  |
| **Requisito1** | FRW\_FRW002-182 | **Subtarefa1** | FRW\_FRW002-191 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Melhorias na comunicação com o License Server, enviando novos dados requeridos pela versão 1.03.010.

### Definição da Regra de Negócio

Requisitos das linhas de produto

1) A Mensagem SetInfo de usuário deverá ser enviada quando solicitada pelo LS ( requisito em vigência ) e toda a vez um usuário for incluído ou modificado em nossos softwares.

Para atender a este item, o envio de informação de usuário deve ser acionado no SaveRecord do GlbUsuarioData, enviando os dados do usuário que foi incluído/atualizado.

2) A Mensagem SetInfo de usuário terá sua estrutura alterada (Json) para incluir as seguintes informações: Id do Identity e email. Estas informações serão utilizadas para que não haja duplicação de consumo entre nossos softwares.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Envio da Solicitação de detalhamento do usuário** | | | | | | | |  |
| **Atributo** | **Tipo do Atributo** | **Ocorrência** | **Pai** | **Tipo** | **Tamanho** | **Decimal** | **Descrição** |  |
| method | Singular | 1 | **-** | Character | 255 | 0 | Informar o valor - "setInfo" |  |
| code | Singular | 1 | **-** | Character | 6 | 0 | LS001 |  |
| **User** | **Multi-valued** | **1** | **-** | **-** | - | - |  |  |
| id | Singular | 1 | User | Character | 36 | 0 | Id do usuário |  |
| name | Singular | 1 | User | Character | 80 | 0 | Nome do usuário |  |
| mail | Singular | 0 | User | Character | 240 | 0 | email do usuário | new |
| idIdentity | Singular | 0 | User | Character | 36 | 0 | UUID do usuário no Fluig Identity | new |

No CorporePrincipal existe o e-mail do usuário. Deve ser acrescentado também o Id do Fluig Identity e este deve ser alimentado nas rotinas que alimentam os dados do usuário no Principal. Alterar o método GetUserInfo da RMSLoginServer acrescentando o retorno do Id do Fluig Identity e nos pontos onde este método é chamado, alimentar a propriedade IdFluigIdentity no principal.

3) A mensagem SetInfo de Instalação da linha de produto, foi alterada para incluir informações extras que são especificas da linha e serão enviadas para o GCAD local. O uso desta informação não é obrigatório e deverá ser acordado entre o GDP de Framework e o Gerente de GCAD.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Envio da Solicitação de detalhamento da instalação da linha de produto** | | | | | | | |  |
| **Atributo** | **Tipo do Atributo** | **Ocorrência** | **Pai** | **Tipo** | **Tamanho** | **Decimal** | **Descrição** |  |
| method | Singular | 1 | **-** | Character | 255 | 0 | Informar o valor - "setInfo" |  |
| ProductLine | Singular | 1 | **-** | Character | 2 | 0 | Código da linha de produto. Exemplo: 01 - Logix, 02 - Microsiga, 03 - RM, 04 - First, 05 - Vitrine, 06 - Datasul, 07 - Personal Med,08 - Proxima |  |
| code | Singular | 1 | **-** | Character | 6 | 0 | LS003 |  |
| **ApplicationServer** | **Multi-valued** | **1** | **-** | **-** | **-** | **-** | **Estrutura do application Server** |  |
| OperationSystem | Singular | 1 | ApplicationServer | Character | 255 | 0 | Descrição do sistema operacional |  |
| Memory | Singular | 1 | ApplicationServer | Inteiro | 12 | 2 | Memoria fisica em Mbytes |  |
| Processor | Singular | 0-1 | ApplicationServer | Inteiro | 12 | 2 | Numero de processadores |  |
| Core | Singular | 0-1 | ApplicationServer | Inteiro | 12 | 2 | Numero de núcleos |  |
| Clock | Singular | 0-1 | ApplicationServer | Inteiro | 12 | 2 | Mhz do processador |  |
| Idioma | Singular | 0-1 | ApplicationServer | Character | 5 | 0 | Id de identificação do idioma do sistema operacional. Exemplo: 'pt-br' |  |
| ProcessorModel | Singular | 0-1 | ApplicationServer | Character | 255 | 0 | Descrição com o modelo do processado |  |
| IPAddress | Singular | 1 | ApplicationServer | Character | 16 | 0 | endereço IP do aplication server |  |
| **DBMS** | **Multi-valued** | **0-1** | **-** | **-** | **-** | **-** | **Estrutura do SGBD** |  |
| OperationSystem | Singular | 0-1 | DMS | Character | 255 | 0 | Descrição do sistema operacional |  |
| Memory | Singular | 0-1 | DMS | Inteiro | 12 | 2 | Memoria fisica em Mbytes |  |
| Processor | Singular | 0-1 | DMS | Inteiro | 12 | 2 | Numero de processadores |  |
| Core | Singular | 0-1 | DMS | Inteiro | 12 | 2 | Numero de núcleos |  |
| Clock | Singular | 0-1 | DMS | Inteiro | 12 | 2 | Mhz do processador |  |
| ProcessorModel | Singular | 0-1 | DMS | Character | 255 | 0 | Descrição com o modelo do processado |  |
| IPAddress | Singular | 0-1 | DMS | Character | 16 | 0 | endereço IP do aplication server |  |
| Database | Singular | 1 | DMS | Character | 255 | 0 | Descrição do banco de dados |  |
| Version | Singular | 0-1 | DMS | Character | 255 | 0 | Versão do banco de dados |  |
| **WorkStation** | **Multi-valued** | **0-1** | **-** | **-** | **-** | **-** | **Estrutura da estaçäo de trabalho** |  |
| OperationSystem | Singular | 1 | WorkStation | Character | 255 | 0 | Descrição do sistema operacional |  |
| Memory | Singular | 1 | WorkStation | Inteiro | 12 | 2 | Memoria fisica em Mbytes |  |
| Processor | Singular | 0-1 | WorkStation | Inteiro | 12 | 2 | Numero de processadores |  |
| Core | Singular | 0-1 | WorkStation | Inteiro | 12 | 2 | Numero de núcleos |  |
| Clock | Singular | 0-1 | WorkStation | Inteiro | 12 | 2 | Mhz do processador |  |
| Idioma | Singular | 0-1 | WorkStation | Character | 5 | 0 | Id de identificação do idioma do sistema operacional. Exemplo: 'pt-br' |  |
| Browse | Singular | 0-1 | WorkStation | Character | 255 | 0 | Idenficação do vendor do Browse. IE,CHROME,FIREFOX, SAFARI, etc... |  |
| BrowseVersion | Singular | 0-1 | WorkStation | Character | 255 | 0 | Versão do Browse Instalado |  |
| ProcessorModel | Singular | 0-1 | WorkStation | Character | 255 | 0 | Descrição com o modelo do processado |  |
| IPAddress | Singular | 1 | WorkStation | Character | 16 | 0 | Endereço IP do aplication server |  |
| **ProductLine** | **Multi-valued** | **1** | **-** | **-** | **-** | **-** | **Estrutura da linha de produto** |  |
| DbScriptVersion | Singular | 0-1 | ProductLIne | Character | 255 | 0 | Versão da estrutura de dados do produto |  |
| BOVersion | Singular | 0-1 | ProductLIne | Character | 255 | 0 | Identificação da versão da linha de produto |  |
| AppSrvVersion | Singular | 0-1 | ProductLIne | Character | 255 | 0 | Identificação da versão do Application Server |  |
| FWVersion | Singular | 0-1 | ProductLIne | Character | 255 | 0 | Identificação da versão do Framework utilizado |  |
| **ExtraContent** | Singular | 0-1 | - | Character | 524288 | 0 | Informação adicional não padronizada | new |

Acrescentar novo campo no objeto de envio do LS003.

Criar um nova interface que implemente **IRMSServer**:

Interface: **IRMSProductLineExtraContent**

Método: **GetProductLineExtraContent**

Tipo de Retorno: **String**

Criar nova server que implemente **IRMSProductLineExtraContent**:

Este server será responsável por buscar, agrupar, preparar a informação que será enviada no campo ExtraContent e será de reponsabilidade do GCAD implementar o conteúdo necessário. A implementação base irá retornar um conteúdo vazio.

4) As linhas de produto deverão se adequar a uma conexão SSL/TLS over TCP, onde verificaremos a origem do certificado, porém deveremos permitir certificados vencidos, uma vez que não controlamos a atualização de nossos softwares.

O LS 2014 ainda não suporta SSL/TLS na comunicação com os ERPs. Este recurso será desenvolvido em breve e assim que estiver disponível, serão feitos os ajustes necessários na linha RM.

5) Incluir mecanismo de controle do consumo de licenças pelos WebServices SOAP e REST expostos pelo RM.Host.

Para permitir esta implementação, será necessário padronizar o mecanismo de autenticação dos WebServices, pois a autenticação é pré-requisito para o consumo de licenças.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
