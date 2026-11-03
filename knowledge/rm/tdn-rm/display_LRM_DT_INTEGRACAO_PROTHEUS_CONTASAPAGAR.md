---
content_hash: 39b0539d9fb5a6da9c859ab37e4bf5f88dd5863e95a8c1391e11837482be8849
fetched_at: '2026-06-29T00:06:17.064379+00:00'
page_id: '212904191'
product: rm
source: tdn-rm
title: DT_INTEGRACAO_PROTHEUS_CONTASAPAGAR
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_INTEGRACAO_PROTHEUS_CONTASAPAGAR
version: 126
---

# Integração de Contas a Pagar através da integração por Mensageria Única

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Patrimonial* |
| **Módulo:** | *BackOffice* |
|  |  |

## Descrição

Foi disponibilizado através do pacote de integração "TOTVS Educacional x BackOffice Protheus" o envio de lançamentos a pagar para o sistema Protheus através de Mensageria Única.

Módulo Integração: **Ferramentas | Configurar**

As informações serão trafegadas utilizando a estrutura da mensagem única "AccountPayableDocument" na versão 2.001:

| Campo | Tag XML | Descrição | Tamanho | Observações |
| --- | --- | --- | --- | --- |
| FLAN/CODCOLIGADA | FLAN/IDLAN | InternalId | InternalId da chave completa do lançamento |  |  |
| FLAN/CODCOLIGADA | CompanyId | Código da empresa |  |  |
| FLAN/CODFILIAL | BranchId | Código da filial |  |  |
| FLAN/CODCOLIGADA | FLAN/CODFILIAL | CompanyInternalId | InternalId da chave completa de empresa |  |  |
| FLAN/SERIEDOCUMENTO | DocumentPrefix | Série do documento | 3 |  |
| FLAN/NUMERODOCUMENTO | DocumentNumber | Código do documento | 9 |  |
| FLAN/PARCELA | DocumentParcel | Número da parcela do documento | 1 |  |
| FLAN/CODTDO | DocumentTypeCode | Tipo do documento | 3 |  |
| FLAN/DATAEMISSAO | IssueDate | Data de emissão do documento |  |  |
| FLAN/DATAVENC | DueDate | Data de vencimento do documento |  |  |
| FLAN/DATAVENC | RealDueDate | Data de vencimento do documento |  |  |
| FLAN/CODCFO | VendorCode | Código do fornecedor |  |  |
| FLAN/CODCOLCFO | FLAN/CODCFO | VendorInternalId | InternalId do VendorCode |  |  |
|  | StoreId | Loja |  | Obs.: O TOTVS Gestão Financeira não possui essa informação. |
| FLAN/VALORORIGINAL | NetValue | Valor líquido |  |  |
| FLAN/VALORORIGINAL | GrossValue | Valor bruto |  |  |
| FLAN/CODMOEDA | CurrencyCode | Código da moeda |  |  |
| FLAN/CODMOEDA | CurrencyInternalId | InternalId do CurrencyCode |  |  |
|  | CurrencyRate | Taxa da moeda |  |  |
| ListOfSourceDocument | | | | |
| Taxes | | | | |
| ApportionmentDistribution | | | | |
| FLANRATCCU | Apportionment | Rateio | | |
| FLANRATCCU/CODCOLIGADA | FLANRATCCU/IDLAN | FLANRATCCU/IDRATCCU | InternalId | InternalId do rateio |  |  |
| FLANRATCCU/CODCOLIGADA | FLANRATCCU/CODCCUSTO | CostCenterInternalId | InternalId do CostCenterCode |  |  |
| FLANRATCCU/CODCCUSTO | CostCenterCode | Código do Centro de Custo |  |  |
|  | ProjectInternalId | InternalId do Projeto |  |  |
|  | TaskInternalId | InternalId da Tarefa |  |  |
| FLANRATCCU/VALOR | Value | Valor do rateio |  |  |
| FLANRATCCU/PERCENTUAL | Percentual | Percentual do rateio |  |  |
| FLANRATCCU/OBSERVACAO | Observation | Observações |  |  |
| FLAN/OBSERVACAO | Observation | Observações | 200 |  |
|  |  |  |  |  |
| FLAN/CODSISTEMA | Origin | Sistema de origem | 10 |  |
| FLAN/CODCOLNATFINANCEIRA | FLAN/CODNATFINANCEIRA | FinancialNatureInternalId | InternalId da natureza financeira |  |  |
| FLAN/NUMBANCO | BankCode | Número do banco |  |  |
| FLAN/NUMAGENCIA | BankBranch | Número da agência |  |  |
|  | BranchKey | Dígito verificador da agência |  |  |
| FLAN/NUMCONTA | CheckingAccountNumber | Número da conta |  |  |
|  | CheckingAccountNumberKey | Dígito verificador da conta |  |  |

##### **Importante:**

O lançamentos a pagar gerados no TOTVS Gestão Financeira serão enviados, automaticamente, para o BackOffice do Protheus, se a integração "TOTVS Educacional x BackOffice Protheus" estiver ativa.

Os lançamentos serão, apenas, enviados. Quaisquer alterações relacionadas ao lançamento, serão realizadas estritamente no BackOffice do Protheus e não serão retornadas para o TOTVS Gestão Financeira.

## Procedimento para Implantação

1. No arquivo de configuração do Host, inserir as tags "**DefaultDB**" e "**HttpPort**" para definição do Alias e da porta de comunicação que serão utilizados pelo Webservice da integração.  

   ***<add key="DefaultDB" value="NomeAlias" />***  
   ***<add key="HttpPort" value="8051" /> (Porta Padrão)***
2. Reiniciar o Host para que as alterações tenham efeito
3. Instalar o pacote de integração "***TOTVS Educacional x BackOffice Protheus***" através do processo de configuração de integração.
4. Configurar e ativar a integração para que reconheça o envio da mensagem "AccountPayableDocument".

#### Manual da integração

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Integração 
   1. Integração "TOTVS Educacional x BackOffice Protheus":
      1. O campo "Ativo?" deve ser marcado para ativar a integração
      2. O campor "URL WebService" deve ser preenchido com o endereço WSDL do webservice do Protheus.
      3. O campo "Usuário Autenticação" deve conter o usuário de acesso as funcionalidades do WebService informado.
      4. O campo "Senha Autenticação" deve conter a senha do usuário informado.

divs
