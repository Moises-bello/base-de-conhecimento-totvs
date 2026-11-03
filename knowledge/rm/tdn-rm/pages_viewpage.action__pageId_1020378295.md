---
content_hash: bbc5faec17a5c91b08708da1a810bb703169e3d9238c74cf5a0cd7a0454e7f2d
fetched_at: '2026-06-29T00:05:47.967033+00:00'
page_id: '1020378295'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Aluguel - APIs e WebServices TCGI.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1020378295
version: 40
---

PrincipalconfiguracaoConfiguração APISpropostasAPI de Propostas

# Sumário

---

Sumário

# Visão Geral

Esse documento tem o objetivo de exemplificar o uso da API utilizando os métodos implementados.

A API de propostas permite o gerenciamento dos contratos de aluguel de imóveis, abrangendo:

* Criação
* Alteração
* Exclusão
* Consulta
* Upload de documentos

Todos os recursos exigem autenticação e estão protegidos por mecanismos internos de segurança do sistema.

# 1 - Recursos Disponíveis

## 1.1 - Criar / Alterar Contrato

false

**POST**

**Máscara de Url:**http://{domínio}:{porta}/api/imb/v1/pvi/proposals-external

Cria ou altera contrato de aluguel.

**Body:** ProposalPortalModelEntity

**Respostas:**

* Retorna ProposalPortalModelEntity;
  + Primay key contrato: company e code.
* 201 Created – Sucesso;
* 500 para erros internos.

Ver body JSON

{  
     "listOfProperties": [  
        {  
            "company": 2,  
            "propertyCode": 194  
        }  
    ],  
    "broker": {  
        "companyBroker": 0,  
        "codeBroker": "0000546"  
    },  
    "listOfTenants": [  
        {  
            "codeCfo": "0000560",  
            "name": "Sarah Brasil",  
            "company": 2,  
            "cgccpf": "67291674670",  
            "principal": 1  
        },  
        {  
            "codeCfo": "0000561",  
            "name": "Zarah Xpto",  
            "company": 2,  
            "cgccpf": "395.694.730-45",  
            "principal": 0  
        }  
    ],  
    "contractModel": {  
        "companyContractModel": 2,  
        "codeContractModel": "2",  
        "descriptionContractModel": "Contrato Padrão",  
        "typePayment": 0,  
        "isRequiredFieldsFilled": true  
    },  
    "contractPeriods": {  
        "contractNumber": "PVI-87",  
        "dateContract": "2025-01-01T00:00:00Z",  
        "dateExpiration": "2025-02-12T00:00:00Z",  
        "effectiveDate": "2025-01-01T00:00:00Z",  
        "finalDate": "2030-12-31T00:00:00Z",  
        "initialRental": "2025-01-01T00:00:00Z",  
        "initialPeriod": "2025-01-31T00:00:00Z",  
        "carenceDays": 0  
    },  
    "escalationList": [],  
    "contractProposal": {  
        "company": 0,  
        "rentalCode": 0,  
        "rentalNumber": "",  
        "dueDayRule": 0,  
        "statusProposal": 1  
    }  
}

Ver JSON retorno

{  
    "code": 59,  
    "company": 2,  
    "listOfProperties": [  
        {  
            "company": 2,  
            "propertyCode": 194,  
            "areaCode": null,  
            "description": null  
        }  
    ],  
    "guarantee": null,  
    "broker": {  
        "companyBroker": 0,  
        "codeBroker": "0000546"  
    },  
    "listOfTenants": [  
        {  
            "codeCfo": "0000560",  
            "name": "Sarah Brasil",  
            "company": 2,  
            "cgccpf": "67291674670",  
            "principal": 1  
        },  
        {  
            "codeCfo": "0000561",  
            "name": "Zarah Xpto",  
            "company": 2,  
            "cgccpf": "395.694.730-45",  
            "principal": 0  
        }  
    ],  
    "contractModel": {  
        "companyContractModel": 2,  
        "codeContractModel": "2",  
        "descriptionContractModel": "Contrato Padrão",  
        "dueDate": null,  
        "typePayment": 0,  
        "isRequiredFieldsFilled": true,  
        "requiredFieldsNotFilled": null  
    },  
    "contractPeriods": {  
        "contractNumber": "PVI-87",  
        "dateContract": "2024-12-31T21:00:00-03:00",  
        "dateExpiration": "2025-02-11T21:00:00-03:00",  
        "effectiveDate": "2024-12-31T21:00:00-03:00",  
        "finalDate": "2030-12-30T21:00:00-03:00",  
        "initialRental": "2024-12-31T21:00:00-03:00",  
        "initialPeriod": "2025-01-30T21:00:00-03:00",  
        "carenceDays": 0  
    },  
    "escalationList": [],  
    "contractProposal": {  
        "company": 0,  
        "rentalCode": 0,  
        "rentalNumber": "",  
        "dueDayRule": 0,  
        "properties": null,  
        "statusProposal": 1,  
        "statusProposalPVI": null,  
        "typeRangeComposite": null,  
        "inform\_gross\_revenue\_value": null  
    }  
}

## 1.2 - Alterar Proposta

false

**PUT**

**Máscara de Url:**http://{domínio}:{porta}/api/imb/v1/pvi/proposals-external

Altera uma proposta existente.

**Body:** ContratoLocEntity

Campos obrigatórios: company, rentalCode , statusProposal e statusProposalPVI.

**Respostas:**

* 200 OK – Sucesso;
* 500 para erros internos.

## 1.3 - Excluir Contrato

false

**DELETE**

**Máscara de Url:**http://{domínio}:{porta}/api/imb/v1/pvi/proposals-external?company={company}&proposal={proposal}

**Parâmetros:**

* company (int) – Código da empresa
* proposal (int) – Código do Contrato

**Respostas:**

* 200 OK – Sucesso;
* 500 para erros internos.

## 1.4 - Listar Contratos por Corretor

false

**POST**

**Máscara de Url:** http://{domínio}:{porta}/api/imb/v1/pvi/proposals-external/broker/{codBroker}

**Parâmetro de rota:**

* codBroker (string) – Código do corretor

**Retorno:**  
ApiResult.Items → ProposalPortalModelEntity

## 1.5 - Upload de Documento

false

**POST**

**Máscara de Url:** http://{domínio}:{porta}/api/imb/v1/pvi/proposals-external/upload

**Body:** UploadDocumentoTAE

**Retorno:** UploadDocumentoTAE

# 2 - Segurança

false

Todos os recursos desta API exigem **autenticação baseada em token**.

A autenticação deve ser enviada no cabeçalho da requisição utilizando o padrão **Bearer Token**.

**Http**  
Content-Type: application/json

# 3 - Objetos da API

## 3.1 - ProposalPortalModelEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| code | int | Código do Contrato - **Obrigatório na alteração** |
| company | int | Código da empresa - **Obrigatório na alteração** |
| listOfProperties | Lista<ImovelEntity> | Lista de imóveis |
| guarantee | GarantiaEntity | Dados da garantia |
| broker | CorretorEntity | Dados do corretor |
| listOfTenants | Lista<LocatarioEntity> | Locatários |
| contractModel | ContractModelEntity | Modelo de contrato (tem api?) |
| contractPeriods | PeriodosContratoLocEntity | Períodos |
| escalationList | Lista<EscalonamentoEntity> | Escalonamentos |
| contractProposal | ContratoLocEntity | Contrato vinculado |

## 3.2 - ImovelEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| company | int | Código da empresa |
| propertyCode | int | Código do imóvel |
| areaCode | int? | Código da área |
| description | string | Descrição |

## 3.3 - GarantiaEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| warrantyId | int | ID da garantia |
| companyInstitution | int | Código da empresa da instituição |
| codeInstitution | string | Código da instituição |
| nameInstitution | string | Nome da instituição |
| warrantyNumber | string | Número |
| warrantyType | enum | Tipo de garantia (TipoGerantiEnum) |
| warrantyValue | decimal | Valor |
| bindContract | bool | Vincula ao contrato |
| paymentdate | DateTime? | Data de pagamento |
| initialValidity | DateTime | Validade inicial |
| FinalValidity | DateTime | Validade final |
| note | string | Observações |

## 3.4 - CorretorEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| companyBroker | int? | Código da empresa |
| codeBroker | string | Código do corretor |

## 3.5 - LocatarioEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| codeCfo | string | Código do locatário |
| name | string | Nome |
| company | int? | Empresa |
| cgccpf | string | CPF/CNPJ |
| principal | int | Se é o principal |

## 3.5 - ContractModelEntity

| **Propriedade JSON** | **Tipo** | **Descrição** |
| --- | --- | --- |
| companyContractModel | int? | Código da empresa |
| codeContractModel | int | Código do modelo |
| descriptionContractModel | string | Descrição |
| dueDate | string | Dia de vencimento |
| typePayment | int | Tipo de pagamento |
| isRequiredFieldsFilled | bool | Campos obrigatórios preenchidos |
| requiredFieldsNotFilled | string | Lista dos não preenchidos |

## 3.7 - PeriodosContratoLocEntity

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| contractNumber | string | Nº do contrato |
| dateContract | dateTime | Data do contrato |
| dateExpiration | dateTime | Data de Vencimento |
| effectiveDate | dateTime | Início de vigência |
| finalDate | dateTime | Fim de vigência |
| initialRental | dateTime | Início da locação |
| initialPeriod | dateTime | Fim Primeiro período |
| carenceDays | int | Dias de carência |

## 3.8 - ContratoLocEntity

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| company | int | Código da empresa |
| rentalCode | int | Código do contrato |
| rentalNumber | string | Número |
| dueDayRule | int | Regra do vencimento |
| properties | array ImovelEntity | Imóveis |
| statusProposal | int | Situação - ver 3.11.1 Status Contrato |
| statusProposalPVI | int | Situação PVI - ver 3.11.1 Status Contrato |
| typeRangeComposite | int? | Tipo de faturamento |
| inform\_gross\_revenue\_value | int? | Informa faturamento bruto |

## 3.9 - UploadDocumentoTAE

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| codColigada | int | Código da coligada |
| codProposta | int | Código da proposta |
| token | string | Token |
| nomeEnvelope | string | Nome do envelope |
| solicitarAssinaturaManuscrita | bool | Solicitar assinatura física |
| listaDocumentosBinarios | array TaeDocumento | Documentos |
| assinantes | array string | Assinantes |
| validadores | array string | Validadores |

## 3.10 - Taedocumento

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| nomeDocumento | string | Nome |
| documentoBinario | string | Conteúdo Binário |

## 3.11 - ApiResult

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| count | int | Total de registros |
| hasNext | bool | Indica se tem mais registros |
| items | array object | Registros |

## 3.12 - Enumerados

### 3.12.1 - Status do Contrato

| Descrição | Valor |
| --- | --- |
| Efetivado | 0 |
| Em Elaboração | 1 |
| Rescindido | 2 |
| Suspenso | 3 |
| Encerrado | 4 |
| Em Aprovação | 5 |
| Proposta | 6 |
| Paralisado | 7 |

### 3.12.2 - Tipo de Garantia

| Descrição | Valor |
| --- | --- |
| Caução | 0 |
| Carta de Fiança | 1 |
| Seguro Fiança | 2 |
| Título de Capitalização | 3 |
| Fiador | 4 |
| Sem Garantia | 5 |
| Cessão Fiduciária | 6 |

# 4 - Tratamento de Erros

false

* Utiliza códigos HTTP padrão.
* 500 para erros internos.
* Recursos não implementados lançam exceções.

# 5 - Guia de Solução de Problemas

false

**Os dados do corretor não estão cadastrados no TCGI da Linha RM.**  
Código do Cliente Fornecedor do corretor (CODEBROKER) precisa estar relacionado a um usuário do sistema.   
O código do Cliente / Fornecedor, deve possuir o código relacionado no cadastro do corretor (XALGCORRETOR). No RM no módulo “Gestão de Imóveis”, acesse o menu “Aba ALUGUEL | Agrupador CADASTRO |Cadastro de Aluguel | Corretor”
