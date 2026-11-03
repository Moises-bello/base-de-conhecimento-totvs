---
content_hash: d56ceb887b4f2ab72e6561d1cea08a7013e70dffda01fad78546d0efd3dce2f2
fetched_at: '2026-06-29T00:06:12.083280+00:00'
page_id: '204968264'
product: rm
source: tdn-rm
title: ER_PCREQ-7764_Sincronizador_Integracao_Educacional_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7764_Sincronizador_Integracao_Educacional_Protheus
version: 15
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Gestão Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_CTB004 | **IRM** | PCREQ-7762 |
| **Requisito** | PCREQ-7764 | **Subtarefa** | PDR\_EDU\_CTB003-565 |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

 Permitir a criação do de/para para as entidades da integração Educacional x Protheus via Stored Procedure para o novo modelo de integração que usa Mensagem Única.

O usuário poderá escolher as seguintes entidades:

* Centro de Custo
* Unidade de Medida
* Cliente/Fornecedor
* Banco/Agência/Conta
* Lançamento a Receber
* Moeda
* Classe de Valor
* Item Contábil

## Definição da Regra de Negócio

**Mensagem InternalIdLoad**

Foi desenvolvida uma nova mensagem única TOTVS, **IntenalIdLoad(1.000)**,  para permitir a conversão dos códigos da integração atual para o novo formato de de/para utilizado nas integrações via mensagem única. Fica a cargo do RM o envio dos registros a serem sincronizados para o Protheus. O Protheus deve receber esta nova mensagem, consultar se o código passado existe na base de dados de acordo com a regra de geração de código da integração atual e retornar o status desta pesquisa para o RM. Caso o registro seja encontrado na base de dados do Protheus o mesmo deverá gerar um InternalID único para este registro, gravá-lo na tabela de de/para (XXF) e retornar o InternalID para o RM. Devido limitações de tamanho de mensagem existente no EAI do Protheus a mensagem será enviada com no máximo 300 registros, sendo que esses registros serão agrupados por Coligada, Filial e Entidade.

 A mensagem recebida terá a seguinte estrutura:

* **CompanyId:**Este campo armazena a coligada do RM.   
  Obs: No Protheus não é possível alterar o grupo de empresas logado dentro do adapter e por isto a mensagem deve conter somente registros de um mesmo grupo de empresas do Protheus.

* **BranchId:**Este campo armazena a filial do RM.
* **CompanyInternalId:**Este campo é a junção dos campos CompanyId e BranchId separados por | (pipe).
* **ExecutionIdentifier:**Este campo armazena um código de execução gerado pelo RM.
* **ListOfEntity:**Este campo armazena uma lista de entidades enviadas pelo RM.
* **Entity:**Este campo representa uma entidade integrada. Ex.: Produto, Fornecedor, etc.

        Ele é formado pelos campos:

* + **EntityName:**Armazena o nome da entidade integrada. Ex.: Item, CustomerVendor, etc.
  + **ListOfInternalIdLoad:**Armazena uma lista de registros (InternalIdLoad).
  + **InternalIdLoad:**Representa um registro de uma determinada entidade sincronizado anteriormente. Ele é formado pelos campos:
  + **IntegrationId:**Código externo do RM que corresponde ao código do registro no Protheus.
  + **New IntegrationId:**Código único gerado pelo RM para identificar o registro nas transações via mensagem única TOTVS.

É necessário que a Integração Educacional x BackOffice Protheus no novo modelo esteja configurado e funcionando, caso a integração não seja configurado de forma correta o conversor não poderá funcionar.

**XSD da mensagem**

**Exemplo do XML de envio (BusinessContent)**

**Exemplo do XML de retorno (ReturnContent)**

**Processo para sincronização de Entidade**

O sincronizador de entidades deverá ser acessado através do Menu Integração | Ferramentas | Conversão | Converter Integração e a utilização é dividida em 4 passos, sendo:

1. Seleção da Conversão Utilizada: o usuário deverá selecionar a integração a ser utilizada, sendo nosso caso a “EducacionalxProtheus Stored Procedure para Mensagem Única”.
2. Seleção das Entidades para converter: o usuário deverá selecionar as entidades que serão convertidas de forma automática com o conversor, caso alguma entidade a critério do usuário seja feita de forma manual ou em outro momento, é necessário apenas deixar desmarcado a entidade, o conversor pode ser utilizado várias vezes, mas caso seja repetido o processo de conversão em entidades que já foram convertidas o conversor irá envia-las novamente ao Protheus.
3. Seleção das Coligadas: o usuário deverá selecionar para quais coligadas (empresas) serão filtrados os registros para conversão.
4. Seleção das Filiais: o usuário deverá selecionar para quais filiais serão filtrados os registros para conversão.

**Log do Conversor de Entidade**

A conversão de entidades gera log de todos os registros que foram enviados ao Protheus que pode ser acessado através do Menu : Integração | Ferramentas | Conversão | Log de Conversão. Quando executado o processo de conversão, é gerado um novo “Id Execução” que pode ser visualizado ao final do processo na tela de log do processo, o usuário deve usar esse id para filtrar os resultados na tela de log.

**Entidades**

**Unidade de Medida**

As Unidades de Medida serão enviadas para o Protheus através do campo CODUND. No sistema RM pode existir unidades de medidas que não foram criadas no Protheus, nesses casos o usuário deve cria-las no Protheus antes de executar o conversor. Caso exista alguma Unidade de Medida no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. As Unidades de Medida convertidas não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | - |
| BranchId | - |
| CompanyInternalId | - |
| EntityName | Fixo: UnitOfMeasure |
| IntegrationId | TUND.CODUND |
| InternalId | TUND.CODUND |

Será enviado somente as unidades de medidas com o código de tamanho menor ou igual a 2, devido ao código da tabela de unidade de medida do Protheus ter esse tamanho. Para os demais registros se necessário deverá ser feito o De/Para manualmente.

**Centro de Custo**

Os Centros de Custo serão enviados para o Protheus através do campo CODCCUSTO. Caso exista algum Centro de Custo no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. Os Centros de Custos convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | GCCUSTO. CODCOLIGADA |
| BranchId | - |
| CompanyInternalId | - |
| EntityName | Fixo: CostCenter |
| IntegrationId | GCCUSTO. CODCCUSTO |
| InternalId | GCCUSTO. CODCOLIGADA| GCCUSTO. CODCCUSTO |

**Moeda**

As Moedas serão enviadas para o Protheus através do campo SÍMBOLO. Caso exista alguma Moeda no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. As Moedas convertidas não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | - |
| BranchId | - |
| CompanyInternalId | - |
| EntityName | Fixo: Currency |
| IntegrationId | GMOEDA. SIMBOLO |
| InternalId | GMOEDA. SIMBOLO |

**Cliente/Fornecedor**

Os Clientes/Fornecedores serão enviados para o Protheus através do campo composto pelo Cod.Loja (fixo '01'); Tipo (C - Cliente, F-Fornecedor) + Código. Caso exista algum Cliente ou Fornecedor no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. Os clientes/fornecedores convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | FCFO.CODCOLIGADA |
| BranchId | - |
| CompanyInternalId | - |
| EntityName | Fixo: CustomerVendor |
| IntegrationId | '01';C ou F + FCFO.CODFCFO |
| InternalId | FCFO.CODCOLIGADA | FCFO.CODFCFO |

**Lançamento a Receber**

Os Lançamentos a Receber serão enviados para o Protheus através dos campos composto pelo Número do título (IdLan com tam. 9 e 0 a esq.); Parcela; Prefixo (Serie documento); Tipo documento; Cod. Loja (fixo '01'); Tipo (C - Cliente) + Código. A criação de lançamentos a receber é realizada no RM e caso o Protheus não tenha o título a receber cadastrado o conversor irá gerar um log informando os títulos não cadastradas no Protheus. Os lançamentos a receber convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | FLAN.CODCOLIGADA |
| BranchId | FLAN.CODFILIAL |
| CompanyInternalId | FLAN.CODCOLIGADA| FLAN.CODFILIAL |
| EntityName | Fixo: AccountReceivableDocument |
| IntegrationId | FLAN.IDLAN;FLAN.PARCELA;FLAN.SERIEDOCUMENTO;FLAN.CODTDO;'01';C;FLAN.CODCFO |
| InternalId | FLAN.CODCOLIGADA | FLAN.IDLAN |

Para os lançamentos que o campo PARCELA estiverem NULO, será considerado o valor 1.

**Banco/Agência/Conta**

As contas correntes serão enviados para o Protheus através dos campos NUMBANCO + NUMAGENCIA + NROCONTA. Caso exista alguma conta corrente no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. As contas correntes convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | FCONTA.CODCOLIGADA |
| BranchId | - |
| CompanyInternalId | - |
| EntityName | Fixo: Bank |
| IntegrationId | FCONTA.NUMBANCO | FCONTA.NUMAGENCIA | FCONTA.NROCONTA |
| InternalId | FCONTA.CODCOLIGADA|FCONTA.NUMBANCO|FCONTA.NUMAGENCIA|FCONTA.NROCONTA |

No RM serão criados também o De/Para para Conta Caixa e Convênio cadastrados para os respectivos Banco/Agencia/Conta.

**Classe de Valor**

As classes de valores serão enviados para o Protheus através do campo CLASSEVALOR. Caso exista alguma classe de valor no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. As contas correntes convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | SCLASSEVALORPROTHEUS.CODCOLIGADA |
| BranchId | SCLASSEVALORPROTHEUS.CODFILIAL |
| CompanyInternalId | SCLASSEVALORPROTHEUS.CODCOLIGADA | SCLASSEVALORPROTHEUS.CODFILIAL |
| EntityName | Fixo: ClassValue |
| IntegrationId | SCLASSEVALORPROTHEUS.CLASSEVALOR |
| InternalId | SCLASSEVALORPROTHEUS.CODCOLIGADA | SCLASSEVALORPROTHEUS.IDCLASSEVALOR |

**Item Contábil**

Os itens contábeis serão enviados para o Protheus através do campo ITEMCONTABIL. Caso exista alguma classe de valor no RM que não foi criado no Protheus o conversor irá gerar log com as informações retornadas do Protheus. As contas correntes convertidos não irão sofrer alterações nos seus dados nos dois produtos utilizados.

|  |  |
| --- | --- |
| **Campo Mensagem** | **Campo RM** |
| CompanyId | SITEMCONTABILPROTHEUS.CODCOLIGADA |
| BranchId | SITEMCONTABILPROTHEUS.CODFILIAL |
| CompanyInternalId | SITEMCONTABILPROTHEUS.CODCOLIGADA| SITEMCONTABILPROTHEUS.CODFILIAL |
| EntityName | Fixo: AccountingItem |
| IntegrationId | SITEMCONTABILPROTHEUS.ITEMCONTABIL |
| InternalId | SITEMCONTABILPROTHEUS.CODCOLIGADA | SITEMCONTABILPROTHEUS.IDITEMCONTABIL |

Obs: O  'Cod. Loja'  que compõem o campo IntegrationId para as mensagens CustomerVendor e AccountReceivableDocument na integração Educacional x BackOffice Protheus não é enviado pelo RM conforme o manual de integração.

 

***Tabelas Utilizadas***

* *TUND – Unidade de medida*
* *GCCUSTO - Centro de custo*
* *GMOEDA - Moeda*
* *FCFO - Cliente/Fornecedor*
* *FLAN - Lançamento*
* *FCONTA - Conta corrente*
* *SCLASSEVALORPROTHEUS - Classe de valor*
* *SITEMCONTABILPROTHEUS - Item contábil*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
