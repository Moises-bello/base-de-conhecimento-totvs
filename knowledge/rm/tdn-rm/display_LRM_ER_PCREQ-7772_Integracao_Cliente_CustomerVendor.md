---
content_hash: 6c3eb125643889c6d30f20ca99c37b1e72055ea256b9427985adcf842a013bcd
fetched_at: '2026-06-29T00:06:07.644196+00:00'
page_id: '201736649'
product: rm
source: tdn-rm
title: ER_PCREQ-7772_Integracao_Cliente_CustomerVendor
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7772_Integracao_Cliente_CustomerVendor
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Financeiro |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7772 | **Subtarefa1** | PDR\_CP\_MOV008-2 |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

```
 Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Cliente com o PDV, viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração.
```

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Cliente (CustomerVendor), estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito.

 

A análise e o desenvolvimento do adapter será efetuado considerando a integração com o PDV Protheus, mas também viabilizará a integração com outras fontes de dados desde que respeitado o layout da mensagem.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cliente/Fornecedor | Inclusão/Alteração/Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Financeiros \ Clientes / Fornecedores | - |

Os campos considerados obrigatórios no envio para o correto recebimento no PDV são:

* Código do Cliente
* Loja - Campo mapeado para a Coligada do Cli/For
* Nome
* Nome Fantasia
* Endereço
* Entidade: pessoa física ou pessoa jurídica
* Município.
* Estado.
* País.

O gatilho de integração será executado sempre que a **Classificação** do registro for **Cliente** ou **Ambos.** Por padrão estes registros sempre serão integrados ao realizar qualquer ação no registro de Cliente/Fornecedor, caso a integração BackOffice RM x PDV Protheus esteja ativa.

Como o endereço é uma informação obrigatória para inclusão/alteração de Cliente do lado PDV, sugerimos que no diálogo do Cliente/Fornecedor do RM seja marcada a opção **Preenchimento Obrigatório** para os campos de **Endereço Principal.**

**Cliente Padrão**

No PDV existem parâmetros para definir qual será o Consumidor Final quando não for informado os dados do Cliente na Compra. Com isso, será necessário cadastrar este Cliente no RM e alterar os parâmetros ***MV\_CLIPAD** e ***MV\_LOJAPAD**** no configurador PROTHEUS (SIGACFG) informando o código do cliente.

**Fórmula Visual**

Está sendo disponibilizado uma fórmula visual para que possa realizar customizações na integração da entidade Cliente/Fornecedor. Caso deseje utilizar este recurso será necessário importar a fórmula visual que encontra-se disponível na pasta “Fórmulas Visuais”, interna à pasta “ObjetosGerenciais” no ambiente instalado do sistema (“../CorporeRM/ObjetosGerenciais/Fórmulas Visuais”). Ao importar a fórmula visual deverá ser marcado para cada fórmula o parâmetro “Importar Gatilho” na rotina de Importação de Fórmula Visual.

Como para o PDV devem ser enviados os registro Cliente ou Ambos do cadastro de Cliente/Fornecedor, nesta fórmula visual foi criado um contra-gatilho no gatilho "**Pode executar o contexto?"** para os assinantes de Inclusão, Alteração e Exclusão de Cliente/Fornecedor via mensagem única (FinCFOTotvsMessageSbc).

**Observação:**

* Quando a integração Manutenção de Ativos (SigaMNT) x BackOffice RM estiver sendo utilizada juntamente com a integração BackOffice RM x PDV Protheus deve ser removido da fórmula visual utilizada para o PDV o contra-gatilho, uma vez que para a integração do Manutenção de Ativos deve-se enviar Cliente, Fornecedor e Ambos. Para isso você pode proceder com uma das seguintes maneiras abaixo:
  + Alterar o retorno do método "CustomCanExecute\_ExecuteCode" para ser sempre "**true"** na fórmula visual de "01\_PDV\_Cliente.TotvsWF".
  + Editar a fórmula visual para considerar também os registros que possuem a classificação de Cliente/Fornecedor igual a Fornecedor
  + Desativar o gatilho da fórmula visual "01\_PDV\_Cliente.TotvsWF".

**Carga Inicial**

Visando facilitar a sincronização das bases de dados RM e PDV foi desenvolvida uma atividade de fórmula visual que se responsabiliza por, a partir de alguns parâmetros, obter os dados necessários e solicitar o envio da Mensagem Única TOTVS CustomerVendor\_2.002.

Basicamente é necessário informar a esta atividade somente a lista de chaves dos registros que se deseja integrar, qual a Mensagem Única a enviar e qual o objeto de negócio (DataServer) responsável por retornar as informações do registro. A partir destas informações a atividade se responsabiliza pela leitura, transformação e envio dos dados ao sistema de destino, oferecendo como retorno o Log de integração.

Por padrão a consulta seleciona para envio registros do tipo Cliente ou Ambos que ainda não foram enviados para o Protheus ou que estejam desatualizados no mesmo (data de último envio anterior a data da última modificação do registro).

Todas as mensagens trafegadas também constarão no monitor da fila de integração, para posterior conferência.

**Implantação do Adapter na Integração com PDV**

Ao executar o configurador da integração será verificado se a base de dados do cliente utiliza a integração de Cliente/Fornecedor na versão 1.000 da mensagem CustomerVendor e caso positivo será apresentada mensagem de erro informando que não será feita a atualização para o uso da versão 2.002 pois existe uma incompatibilidade entre estas e este fato deve ser verificado juntamente com o Suporte.

A verificação será efetuada através da Fila de Mensagens do cliente, considerando que o mesmo possui a versão 1.000 sem conversão prévia caso as três condições abaixo sejam satisfeitas:

1. Existem registros na Fila de Mensagens para a versão 1.XXX da mensagem CustomerVendor.
2. Não existem registros na Fila de Mensagens para a versão 2.XXX da mensagem CustomerVendor.
3. Não existe Adapter em versão 2.XXX para nenhuma integração.

**Utilização do campo StoreId (Loja)**

Visando evitar erros de chave duplicada caso o usuário cadastre Cliente/Fornecedor global com mesmo código de um outro registro por coligada, o código da Coligada do registro (zero em caso de registro global) será enviado ao Protheus a partir do campo StoreId (Loja) ao invés de enviar o valor '01' fixo.

**Listagem de Fórmula Visual:**

|  |  |  |  |
| --- | --- | --- | --- |
|  | **Rotina** | **Operação** | **Fórmula Visual** |
| **Cadastro** | ``` Cliente ``` | ``` Inclusão / Alteração / Exclusão ``` | ``` 01_PDV_Cliente.TotvsWF ``` |
| ``` Cliente ``` | ``` Carga inicial ``` | 01.Sincronização de Cliente.TotvsWF |

**Tabelas Utilizadas**

* FCFO – Cadastro de Clientes / Fornecedor.
* HCINTEGRACAOID – Tabela de-para dos identificadores de cada integração.
* HCFILAMENSAGEM – Armazena dados da fila de mensageria única.

**Entidades de Integração**

* DataServer envolvido
  + FinCFODataBR
* Transformação
  + Id: CustomerVendor
  + Versão: 2.002
* Extension: 4d87df6a-0c52-43d1-bff2-f0cf4c498875

**Restrições e Pontos de Atenção**

* Mesmo que a empresa não utilize Cliente/Fornecedor global no RM, deve-se compartilhar a tabela referente no Protheus por empresa.
* No Protheus o código do cliente/fornecedor será composto pelo código do cliente/fornecedor e da coligada, conforme a mascara “[CODCOLIGADA]|[CODCFO]”.
* Como o código do País no Protheus é baseado na tabela de classificação do IBGE, deve-se cadastrar esta tabela no RM e definir nos parâmetros de integração qual será o código desta tabela.
  + No cadastro de **Classificação de País** incluir uma tabela de classificação.
  + No cadastro de **País** abrir o anexo **Codificação de País** e incluir a tabela de classificação informando o **Código País.**
  + Nos **Parâmetros de Integração** informar no parâmetro "**CODCLASSIFICPAIS**" o código da tabela de classificação utilizada e associado ao país.
* A informação de Condição de Pagamento padrão não é trafegada no adapter de envio.
  + Caso esta informação passe a ser considerada é importante que seu envio seja efetuado somente se o cadastro de condição de pagamento também for integrado (mensagem PaymentCondition), caso contrário haverá erro de "De-Para não encontrado".
  + Para a integração com PDV Protheus este campo deve ser desconsiderado pois o mesmo não possui uso no mesmo e assim sendo o cadastro de Condição de Pagamento não é sincronizado entre os sistemas.
* Uma vez que já foi feito consenso que Cliente e Fornecedor são tratados na mesma mensagem (CustomerVendor), é responsabilidade do destinatário processar a mensagem da melhor forma possível para garantir a consistência dos dados na origem e no destino. Se o destino implementa uma única tabela, terá que manipular apenas um registro. Se implementa mais de uma tabela, tem que manipular até 2 registros.  
    
  Exemplo1: <TOTVSMessage ... CustomerVendor...>…<Event>upsert</Event>…<Type>Customer<Type>…  
    
  Como não dá para saber se este Cliente (<Type>Customer) é uma inclusão ou uma alteração (<Event>upsert), tem que verificar no de/para.
  + Se o EAI destino é capaz de cadastrar um único registro como ambos: deve verificar se já existe um registro com este ID, caso afirmativo fazer alteração deste registro para Cliente e alterar os demais campos, senão fazer inclusão.
  + Se o EAI destino NÃO é capaz de cadastrar um único registro como ambos: primeiro deve verificar se já existe um Fornecedor com este ID, caso afirmativo deve tentar excluir este Fornecedor (não conseguindo gerar uma exceção semelhante a “o código xx já é um fornecedor não pode ser excluído/alterado para tipo cliente.”). Segundo, deve verificar se já existe um registro de Cliente com este ID, caso afirmativo fazer alteração dos demais campos, senão fazer inclusão.  
  Exemplo 2: <TOTVSMessage ... CustomerVendor...>…<Event>upsert</Event>…<Type>Both<Type>…
  + Se o EAI destino é capaz de cadastrar um único registro como ambos, deve verificar se o ID já existe para definir se faz alteração ou inclusão.
  + Se o EAI destino tem 2 tabelas distintas, deve incluir/alterar um Cliente. E ainda incluir/alterar um fornecedor.

## Fluxo do Processo

## Mapeamento dos Campos

 

* **Mensagem CustomerVendor 2.002**

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da coligada | FCFO | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | FCFO | CODFILIAL |
| **CompanyInternalId** | InternalId da filial | FCFO | CODCOLIGADA e CODFILIAL |
| **Code** | Código do Cliente/Fornecedor | FCFO | CODCFO |  |
| **StoreId** | Loja | FCFO | CODCOLIGADA |  |
| **InternalId** | Chave primária do registro | FCFO | CODCOLIGADA|CODCFO |  |
| **ShortName** | Nome Reduzido | FCFO | NOMEFANTASIA | Envia os primeiros 12 caracteres. |
| **Name** | Nome do Cliente/Fornecedor | FCFO | NOME | Envia os primeiros 40 caracteres. |
| **Type** | Tipo do Registro | FCFO | PAGREC | Fixo “Customer”: Cliente  Fixo “Vendor”: Fornecedor  Fixo “Both”: Ambos |
| **EntityType** | Tipo de Pessoa | FCFO | PESSOAFISOUJUR | Fixo “Person”: Física  Fixo “Company”: Jurídica |
| **MarketSegment** | Segmento de Mercado | FCFO | CODTCF | Ver MarketSegmentType |
| **RegisterDate** | Data de registro | FCFO | DATACRIACAO | Não utilizado pela linha RM |
| **RegisterSituation** | Situação | FCFO | ATIVO | Fixo “Active”: Ativo  Fixo “Inactive”: Inativo  Fixo “Canceled”: Cancelado  Fixo “Pending”: Pendente Fixo “Suspended”: Suspenso |
| **Comments** | Observações |  |  | Não utilizado pela linha RM |
| **GovernmentalInformation** |  |  |  | Ver GovernmentalInformationType |
| **Address** |  |  |  | Ver AddressType |
| **ShippingAddress** |  |  |  | Ver ShippingAddress \ AddressType |
| **ListOfCommunicationInformation** |  |  |  | Ver CommunicationInformationType |
| **ListOfContacts** |  |  |  | Ver ContactInformationType |
| **ListOfBankingInformation** |  |  |  | Ver ListOfBankingInformation \ BankingInformation |
| **BillingInformation** | | | | |
| BillingCustomerCode |  |  |  | Não utilizado pela linha RM |
| BillingCustomerInternalId |  |  |  | Não utilizado pela linha RM |
| Address |  |  |  | Ver AddresType |
| **VendorInformation** |  |  |  | Ver VendorInformationType |
| **FiscalInformation** | | | | |
| Category |  |  |  | Não utilizado no RM |
| IsRetentionAgent |  |  |  | Não utilizado no RM |
| **CreditInformation** | | | | |
| CreditIndicator |  |  |  | Não utilizado no RM |
| CreditEvaluation |  |  |  | Não utilizado no RM |
| ShipmentCreditEvaluation |  |  |  | Não utilizado no RM |
| CreditLimit |  | FCFO | LIMITECREDITO |  |
| CreditLimitCurrency |  |  |  | Não utilizado no RM |
| CreditLimitDate |  |  |  | Não utilizado no RM |
| AdditionalCreditLimit |  |  |  | Não utilizado no RM |
| AdditionalCreditLimitCurrency |  |  |  | Não utilizado no RM |
| AdditionalCreditLimitDate |  |  |  | Não utilizado no RM |
| LatePeriods |  |  |  | Não utilizado no RM |
| BalanceOfCredit |  |  |  |  |
| PaymentConditionCode |  |  |  | Campo não utilizado na integração. |
| PaymentConditionInternalId |  |  |  | Campo não utilizado na integração. |
| PriceListHeaderItemCode | Código da Tabela de Preço |  |  | Não utilizado pela linha RM |
| PriceListHeaderItemInternalId | InternalId do PriceListHeaderItemCode |  |  | Não utilizado pela linha RM |
| CarrierCode | Código da Transportadora default do Cliente |  |  | Não utilzado nesta integração. |
| **ContactInformationType** | | | | |
| Code | Código do Contato | FCFOCONTATO | IDCONTATO |  |
| Title | Título do Contato |  |  | Não utilizado pela linha RM |
| Name | Nome do Contato | FCFOCONTATO | NOME |  |
| Department | Departamento do Contato |  |  |  |
| **ListOfContact\Contact\CommunicationInformationType** | | | | |
| PhoneNumber | Número do telefone | FCFOCONTATO | TELEFONE |  |
| PhoneExtension | Ramal | FCFOCONTATO | RAMAL |  |
| FaxNumber | Número do FAX | FCFOCONTATO | FAX |  |
| FaxNumberExtension | Ramal do FAX |  |  | Não utilizado no RM |
| HomePage | Página da WEB |  |  | Não utilizado no RM |
| Email | Correio Eletrônico | FCFOCONTATO | EMAIL |  |
| **ListOfContact\Contact\ ContactInformationAddress** | | | | |
| Address | Rua, Avenida, Rodovia, etc | FCFOCONTATO | RUA |  |
| Number | Número do Endereço | FCFOCONTATO | NUMERO |  |
| Complement | Informações complementares do endereço | FCFOCONTATO | COMPLEMENTO |  |
| City \ CityCode | Código do Município | FCFOCONTATO | CODMUNICIPIO |  |
| City\ CityDescription | Descrição do Município | FCFOCONTATO | CIDADE |  |
| District | Bairro |  |  | Não utilizado no RM |
| State \ StateCode | Código do Estado | FCFOCONTATO | CODETD |  |
| State \ StateDescription | Descrição do Estado | FCFOCONTATO | DESCETDCONTATO | Extension: DESCETDCONTATO |
| Country \ CountryCode | Código do País | FCFOCONTATO | CODPAISCONTATO | Extension: CODPAISCONTATO |
| Country \ CountryDescription | Descrição do País | FCFOCONTATO | PAIS |  |
| ZIPCode | CEP | FCFOCONTATO | CEP |  |
| Region | Região |  |  | Não utilizado no RM |
| POBox | Caixa Postal |  |  | Não utilizado no RM |
| **ListOfBankingInformation \ BankingInformation** | | | | Esta informações serão enviadas somente se a mensagem Bank estiver mapeada para a integração e existir as informações completas dos dados bancários, ou seja, Banco, Agência, Dígito, Nome da Agência, Conta Corrente e Dígito devem ser informados no RM. Se ao menos um destes campos estiver vazio a lista não será enviada. |
| BankCode | Código do banco | FDADOSPGTO | NUMEROBANCO |  |
| BankInternalId | InternalId do BankCode | FDADOSPGTO | CODCOLIGADA|CODCOLCFO|CODCFO|IDPGTO |  |
| BankName | Nome do banco | FDADOSPGTO | DESCRICAO | Valor texto tamanho 30 |
| BranchCode | Agência | FDADOSPGTO | CODIGOAGENCIA |  |
| BranchKey | Dígito agência | FDADOSPGTO | DIGITOAGENCIA |  |
| CheckingAccountNumber | Numero conta | FDADOSPGTO | CONTACORRENTE |  |
| CheckingAccountNumberKey | Dígito conta | FDADOSPGTO | DIGITOCONTA |  |
| **MarketSegmentType** | | | | Será enviado quando existir a informação de Tipo de Cliente/Fornecedor (FCFO.CODTCF) cadastrado e no cadastro de Tipo de Cliente Fornecedor existir um Segmento associado ao Tipo de Cliente/Fornecedor. |
| MarketSegmentCode |  | TSEGMENTO | CODSEGM |  |
| MarketSegmentInternalId |  | TSEGMENTO | CODSEGM |  |
| MarketSegmentDescription |  | TSEGMENTO | DESCRICAO |  |
| **VendorInformationType** | | | | |
| VendorClassification |  |  |  | Não utilizado no RM |
| VendorType |  |  |  | Não utilizado no RM |
| **VendorTypeType** | | | | |
| VendorTypeCode |  |  |  | Não utilizado no RM |
| VendorTypeInternalId |  |  |  | Não utilizado no RM |
| VendorTypeDescription |  |  |  | Não utilizado no RM |
| **TaxPayerType** | | | | |
| TaxName |  |  |  | Não utilizado no RM |
| isPayer |  |  |  | Não utilizado no RM |
| Mode |  |  |  | Não utilizado no RM |
| **GovernmentalInformationType** | | | | |
| Id | Identificação Governamental | FCFO | CGCCFO, INSCRESTADUAL INSCRMUNICIPAL | Quando Escopo = “Federal” e Nome = (“CPF” ou “CNPJ”) busca-se a informação na coluna CGCCFO;  Quando Escopo = “State” e Nome = “Inscricao Estadual” busca-se a informação na coluna INSCRESTADUAL;  Quando Escopo = “Municipal” e Nome = “Inscricao Municipal” busca-se a informação na coluna INSCRMUNICIPAL. |
| @scope | Escopo (Federal, State, Municipal) |  |  | Explicação de como será preenchido na tag Id |
| @name | Nome da identificação (Ex.: CNPJ, CPF, etc.) |  |  | Explicação de como será preenchido na tag Id |
| @issueOn | Data em que a identificação foi expedida (quando aplicável) |  |  | Não utilizado no RM. |
| @expiresOn | Data de expiração da identificação. |  |  | Não utilizado no RM. |
| **AddressType** | | | | |
| Address | Rua, Avenida, Rodovia, etc | FCFO | RUA |  |
| Number | Número do Endereço | FCFO | NUMERO |  |
| Complement | Informações complementares do endereço | FCFO | COMPLEMENTO |  |
| City |  |  |  | Ver CityType |
| District | Bairro | FCFO | BAIRRO |  |
| State |  |  |  | Ver StateType |
| Country |  |  |  | Ver CountryType |
| ZIPCode | CEP | FCFO | CEP |  |
| Region | Região |  |  | Não utilizado no RM |
| POBox | Caixa Postal | FCFO | CAIXAPOSTAL |  |
| **CityType** | | | | |
| CityCode | Código do município | FCFO | CODMUNICIPIO |  |
| CityInternalId | InternalId do CityCode | FCFO | CODMUNICIPIO |  |
| CityDescription | Descrição do município | FCFO | CIDADE |  |
| **StateType** | | | | |
| StateCode | Código da Unidade Federativa | FCFO | CODETD |  |
| StateInternalId | InternalId do StateCode | FCFO | CODETD |  |
| StateDescription | Descrição da Unidade Federativa | GETD | NOME |  |
| **CountryType** |  |  |  |  |
| CountryCode | Código do país | FCFO | IDPAIS | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| CountryInternalId | InternalId do CountryCode | FCFO | IDPAIS | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| CountryDescription | Descrição do país | FCFO | PAIS |  |
| **CommunicationInformationType** | | | | |
| PhoneNumber | Número do telefone | FCFO | TELEFONE |  |
| PhoneExtension | Ramal |  |  | Não utilizado no RM |
| FaxNumber | Número do FAX | FCFO | FAX |  |
| FaxNumberExtension | Ramal do FAX |  |  | Não utilizado no RM |
| HomePage | Página da WEB |  |  | Não utilizado no RM |
| Email | Correio Eletrônico | FCFO | EMAIL |  |
| **ShippingAddress \ AddressType** | | | | Estas tags serão enviadas somente se o campo RUAENTREGA possui valor. |
| Address | Rua, Avenida, Rodovia, etc | FCFO | RUAENTREGA |  |
| Number | Número do Endereço | FCFO | NUMEROENTREGA |  |
| Complement | Informações complementares do endereço | FCFO | COMPLEMENTREGA |  |
| City | Cidade |  |  | Ver CityType \ ShippingAddress \ AddressType |
| District | Bairro | FCFO | BAIRROENTREGA |  |
| State | Estado |  |  | Ver StateType \ ShippingAddress \ AddressType |
| ZIPCode | CEP | FCFO | CEPENTREGA |  |
| Region | Região |  |  | Não utilizado no RM |
| POBox | Caixa Postal | FCFO | CAIXAPOSTALENTREGA |  |
| **CityType \ ShippingAddress \ AddressType** | | | | |
| CityCode | Código do município | FCFO | CODMUNICIPIOENTREGA |  |
| CityDescription | Descrição do município | FCFO | CIDADEENTREGA |  |
| **StateType \ ShippingAddress \ AddressType** | | | | |
| StateCode | Código da Unidade Federativa | FCFO | CODETDENTREGA |  |
| StateDescription | Descrição da Unidade Federativa | GETD | DESCETDENTREGA |  |
| **CountryType \ ShippingAddress \ AddressType** | | | | |
| CountryCode | Código do município | FCFO | IDPAISENTREGA | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| CountryInternalId | InternalId do CountryType | FCFO | IDPAISENTREGA | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| CountryDescription | Descrição do município | FCFO | PAISENTREGA |  |
| **BillingInformation \ AddressType** | | | | Estas tags serão enviadas somente se o campo RUAPAGTO possui valor. |
| Address | Rua, Avenida, Rodovia, etc | FCFO | RUAPGTO |  |
| Number | Número do Endereço | FCFO | NUMEROPGTO |  |
| Complement | Informações complementares do endereço | FCFO | COMPLEMENTOPGTO |  |
| City | Cidade |  |  | Ver CityType \ BillingInformation\ AddressType |
| District | Bairro | FCFO | BAIRROPGTO |  |
| State | Estado |  |  | Ver StateType \ BillingInformation \ AddressType |
| Country | País |  |  | Ver CountryType \ BillingInformation \ AddressType |
| ZIPCode | CEP | FCFO | CEPPGTO |  |
| Region | Região |  |  | Não utilizado no RM |
| POBox | Caixa Postal | FCFO | CAIXAPOSTALPAGAMENTO |  |
| **CityType \ BillingInformation \ AddressType** | | | | |
| CityCode | Código do município | FCFO | CODMUNICIPIOPGTO |  |
| CityDescription | Descrição do município | FCFO | CIDADEPGTO |  |
| **StateType \ BillingInformation \ AddressType** |  |  |  |  |
| StateCode | Código da Unidade Federativa | FCFO | CODETDPGTO |  |
| StateDescription | Descrição da Unidade Federativa | FCFO | DESCETDPGTO |  |
| **CountryType \ BillingInformation \ AddressType** | | | | |
| CountryCode | Código do país | FCFO | IDPAISPGTO | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| CountryInternalId | InternalId do CountryCode | FCFO | IDPAISPGTO | Preenchido via Extension com base na tabela de classificação definida para País nos parâmetros de integração. |
| Description | Descrição do município | FCFO | PAISPAGTO |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
