---
content_hash: bcdceb724a98a225661b511a0c2340cd3892e64947a1fc917b00292333582584
fetched_at: '2026-06-29T00:12:00.311834+00:00'
page_id: '883062126'
product: rm
source: tdn-rm
title: Dados enviados e Pipelines - Integração Gesplan
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883062126
version: 1
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Data Models**
3. **Demais****informações**

## **01. VISÃO GERAL**

O Vídeo a seguir tem uma explicação mais detalhada do processo e seu funcionamento: <https://drive.google.com/file/d/1ymlxI7no7hncyFW-TqvduuLkcbD2FIB3/view?usp=sharing>

O Documento a frente é a apresentação utilizada na apresentação: 

A Carol possui uma área de armazenamento onde ficam as ***staging tables,*** que são as tabelas que armazenam os dados brutos provenientes do ERP. Os ***Data Models*** são estrutura de dados definidas dentro da Carol, e nessas estruturas são armazenadas as informações resultantes do processamento das pipelines.

No tópico 02 abaixo, é apresentado um modelo visual de como as informação são trabalhadas dentro da Carol, antes de serem enviadas à Gesplan. Cada quadro apresentado dentro da BigQuery, representa um conjunto nomeado e temporário de resultados, derivado de uma consulta sql (c*ommon table expression* - CTE). São utilizadas como alternativa à, por exemplo,  subquerys e views, para melhor organização e manutenção das consultas.

Cada CTE armazena um conjunto intermediário de registros que são utilizados pelas CTEs seguintes , até que por fim é gerado um CTE final, que contém os registros que atendem à regra de negócio e que serão levados para o Data Models.

false

Os scripts dos pipelines possuem a extensão **.csql** e estão armazenados no Azure DevOps, no projeto **Backoffice-RM** e repositório [carol-integracao-gesplan](https://dev.azure.com/totvstfs/Backoffice-RM/_git/carol-integracao-gesplan). A Carol busca automaticamente a última versão do script na branch main e executa conforme a recorrência cadastrada no ambiente.

## **02. DATA MODELS**

Os lançamentos que contenham contabilidade serão enviados somente uma perna deles, de acordo com a regra abaixo:

* Lançamento à receber, envia os lançamentos contábeis de crédito.
* Lançamento à pagar, envia os lançamentos contábeis de débito.

Principais tabelas e campos envolvidos:

Cenariofade1Previsãofade

Modelo de dados **Previsto**: contempla todos os lançamentos financeiros em aberto no RM.

Não são considerados previstos os seguintes tipos:

> "**pipelineName**": "fluxodecaixaprevisao\_pipeline"  
> "**pipelineDescription**": "Pipeline para processar o registros de fluxo de caixa da previsão"  
> "**outputDataModelName**": "fluxodecaixa"  
> "**processScript**": "FluxoDeCaixaPrevisao.csql"

2 Realizadofade

Modelo de dados **Realizado**:

3Campos 

**Campos dos Data Models do Financeiro**

Campos\_internofade1Previsão - Com Contabilidadefade

Modelo de dados **Previsto**: contempla todos os lançamentos financeiros em aberto no RM onde os mesmos possuem rateio e/ou contabilidade.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FLAN | CODCOLIGADA|IDLAN|PREV | 1|302205|PREV | Adicionar PREV para sinalizar que é uma previsão |
| externalCodeHeader |  |  |  |  | Deixar nulo |
| externalCodeDetail |  | FLAN | CODCOLIGADA|IDLAN | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro |  |  |  | Deixar nulo |
| externalCodeDetailC | Chave do rateio na contabilidade | FLAN/CPARTIDA | CODCOLIGADA|IDLAN|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FLAN | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | Realizar o depara: 2 = Contas à Pagar / 1 = Contas à Receber |
| dateOfIssue | Data de Emissão | FLAN | DATAEMISSAO | 2023/11/30 | Deixar nulo |
| description | Descrição | FLAN | HISTORICO | ES-0012714-1FLAVIO INACIO SILVEIRA | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura | FLAN -> FTDO |
| documentTypeName\_enUS | Descrição do Tipo de Documento em Inglês |  |  |  | Deixar nulo |
| documentTypeName\_esES | Descrição do Tipo de Documento em Espanhol |  |  |  | Deixar nulo |
| documentNumber | Número de documento | FLAN | NUMERODOCUMENTO | 0000006928 |  |
| observation | Observação |  |  |  | Deixar nulo |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ |  |
| scenario | Cenário |  |  |  | Deixar nulo |
| managementGroupHeader | Grupo Gerencial |  |  |  | Deixar nulo |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | 2023/11/30 |  |
| payday | Data Pagamento | FLAN | DATABAIXA | Null ou 2023/11/30 |  |
| invoiceIssuanceDate | Data de emissão da NF | FLAN | DATAEMISSAO | 2023/11/30 |  |
| invoicePostingDat | Data de lançamento da NF | FLAN | DATACRIACAO | 2023/11/30 |  |
| eventType | Tipo de Evento | FLAN | PAGREC | S | Realizar o depara: 2 = S / 1 = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | FLAN -> FCXA |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 | FLAN -> FCFO |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP | FLAN -> FCFO |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | Enviar campo fixo 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 | FLAN -> FCFO |
| motionWay | Forma de Movimento | FDADOSPGTO | CODCOLIGADA|IDPGTO | 1|1020 | No financeiro ele não é obrigatório |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | FDADOSPGTO | DESCRICAO | Null ou Dinheiro | FLAN -> FDADOSPGTO No financeiro ele não é obrigatório |
| motionWayName\_enUS | Descrição da Forma de Movimento em Inglês |  |  |  | Deixar nulo |
| motionWayName\_esES | Descrição da Forma de Movimento em Espanhol |  |  |  | Deixar nulo |
| paymentNumber | Número de Pagamento |  |  |  | Deixar nulo |
| value | Valor do Documento | FLAN | VALORORIGINAL | 64782.0000 | Em definição (Temos que colocar baixado?) |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| valueBusiness |  |  |  |  | Deixar nulo |
| conversionBusiness | Valor de Conversão para Unidade de Negócio | FLAN | FLAN.VALORORIGINAL \* GCOTACAO.FATOR | 259.128 | Pegar a cotação pela data de vencimento e o indexador do lançamento |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente | GCOTACAO | FATOR | 4.00 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| financialOrigin | Cód. Ext. da abertura financeira de origem (Código externo do lançamento da abertura Financeira) |  |  |  | Deixar nulo |
| divisionGroup | Divisão | FLAN | CODCOLIGADA|CODFILIAL | 1|25 |  |
| project | Projeto |  |  |  | Deixar nulo |
| accountingAccountPlan | Plano de Conta Contábil |  |  |  | Avaliar |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) -> CCONTA Tem que fazer o depara que está entre parenteses. 00 = Não informada (null)/ 01 = Contas de ativo (1) / 02 = Contas de passivo (2) / 03 = Patrimônio Líquido (null) / 04 = Contas de resultado (Credora = 4 e Devedora = 3)/ 05 = Contas de compensação (null) / 09 = Outras (null) Os campos nulos não foram mapeados pois não serão utilizados na integração |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) -> CCONTA |
| accountingAccountName\_enUS |  |  |  |  | Deixar nulo |
| accountingAccountName\_esES |  |  |  |  | Deixar nulo |
| costCenterPlan | Plano de Centro de Custo |  |  |  | Avaliar |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) -> GCCUSTO |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) -> GCCUSTO |
| costCenterName\_enUS | Descrição do Centro de Custo em Inglês |  |  |  | Deixar nulo |
| costCenterName\_esES | Descrição do Centro de Custo em Espanhol |  |  |  | Deixar nulo |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Quando for inclusão/edição vamos deixar em branco. Quando for uma deleção, vamos enviar 'E'. |
| flexField001 | Campo Flexível |  |  |  | Deixar nulo |
| flexField002 | Campo Flexível - Campos Opcional 1 | FLAN | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FLAN | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FLAN | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FLAN | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FLAN | CODTB5FLX | 0100 |  |

2Previsão - Sem Contabilidadefade

Modelo de dados **Previsto**: contempla todos os lançamentos financeiros em aberto no RM onde os mesmos não possuem rateio e/ou contabilidade.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FLAN | CODCOLIGADA|IDLAN|PREV | 1|302205|PREV | Adicionar PREV para sinalizar que é uma previsão |
| externalCodeHeader |  |  |  |  | Deixar nulo |
| externalCodeDetail |  | FLAN | CODCOLIGADA|IDLAN | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro | FLAN/FLANRATCCU | CODCOLIGADA|IDLAN|IDRATCCU | 1|302205|2502 |  |
| externalCodeDetailC | Chave do rateio na contabilidade |  |  |  | Deixar nulo |
| businessUnit | Unidade Negócio | FLAN | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | Realizar o depara: 2 = Contas à Pagar / 1 = Contas à Receber |
| dateOfIssue | Data de Emissão | FLAN | DATAEMISSAO | 2023/11/30 | Deixar nulo |
| description | Descrição | FLAN | HISTORICO | ES-0012714-1FLAVIO INACIO SILVEIRA | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura | FLAN -> FTDO |
| documentTypeName\_enUS | Descrição do Tipo de Documento em Inglês |  |  |  | Deixar nulo |
| documentTypeName\_esES | Descrição do Tipo de Documento em Espanhol |  |  |  | Deixar nulo |
| documentNumber | Número de documento | FLAN | NUMERODOCUMENTO | 0000006928 |  |
| observation | Observação |  |  |  | Deixar nulo |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ |  |
| scenario | Cenário |  |  |  | Deixar nulo |
| managementGroupHeader | Grupo Gerencial |  |  |  | Deixar nulo |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | 2023/11/30 |  |
| payday | Data Pagamento | FLAN | DATABAIXA | Null ou 2023/11/30 |  |
| invoiceIssuanceDate | Data de emissão da NF | FLAN | DATAEMISSAO | 2023/11/30 |  |
| invoicePostingDat | Data de lançamento da NF | FLAN | DATACRIACAO | 2023/11/30 |  |
| eventType | Tipo de Evento | FLAN | PAGREC | S | Realizar o depara: 2 = S / 1 = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | FLAN -> FCXA |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 | FLAN -> FCFO |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP | FLAN -> FCFO |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | Enviar campo fixo 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 | FLAN -> FCFO |
| motionWay | Forma de Movimento | FDADOSPGTO | CODCOLIGADA|IDPGTO | 1|1020 | No financeiro ele não é obrigatório |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | FDADOSPGTO | DESCRICAO | Null ou Dinheiro | FLAN -> FDADOSPGTO No financeiro ele não é obrigatório |
| motionWayName\_enUS | Descrição da Forma de Movimento em Inglês |  |  |  | Deixar nulo |
| motionWayName\_esES | Descrição da Forma de Movimento em Espanhol |  |  |  | Deixar nulo |
| paymentNumber | Número de Pagamento |  |  |  | Deixar nulo |
| value | Valor do Documento | FLAN | VALORORIGINAL | 64782.0000 | Em definição (Temos que colocar baixado?) |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| valueBusiness |  |  |  |  | Deixar nulo |
| conversionBusiness | Valor de Conversão para Unidade de Negócio | FLAN | FLAN.VALORORIGINAL \* GCOTACAO.FATOR | 259.128 | Pegar a cotação pela data de vencimento e o indexador do lançamento |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente | GCOTACAO | FATOR | 4.00 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| financialOrigin | Cód. Ext. da abertura financeira de origem (Código externo do lançamento da abertura Financeira) |  |  |  | Deixar nulo |
| divisionGroup | Divisão | FLAN | CODCOLIGADA|CODFILIAL | 1|25 |  |
| project | Projeto |  |  |  | Deixar nulo |
| accountingAccountPlan | Plano de Conta Contábil |  |  |  | Deixar nulo |
| accountingAccount | Conta Contábil |  |  |  | Deixar nulo |
| accountingAccountClassification | Tipo de Conta Contábil |  |  |  | Deixar nulo |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português |  |  |  | Deixar nulo |
| accountingAccountName\_enUS |  |  |  |  | Deixar nulo |
| accountingAccountName\_esES |  |  |  |  | Deixar nulo |
| costCenterPlan | Plano de Centro de Custo |  |  |  | Deixar nulo |
| costCenter | Centro de Custo |  |  |  | Deixar nulo |
| costCenterCategory | Categoria do Centro de Custo |  |  |  | Deixar nulo |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português |  |  |  | Deixar nulo |
| costCenterName\_enUS | Descrição do Centro de Custo em Inglês |  |  |  | Deixar nulo |
| costCenterName\_esES | Descrição do Centro de Custo em Espanhol |  |  |  | Deixar nulo |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Quando for inclusão/edição vamos deixar em branco. Quando for uma deleção, vamos enviar 'E'. |
| flexField001 | Campo Flexível - Centro de custo do financeiro | FLANRATCCU | CODCOLIGADA|CODCCUSTO | 1|01.01 | FLAN -> FLANRATCCU |
| flexField002 | Campo Flexível - Campos Opcional 1 | FLAN | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FLAN | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FLAN | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FLAN | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FLAN | CODTB5FLX | 0100 |  |

3Realizado

Modelo de dados **Realizado**: contempla todos os extratos de caixa do RM onde os mesmos podem ou não possuir um rateio e/ou contabilidade e vieram de um lançamento financeiro.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FXCX | CODCOLIGADA|IDXCX|REAL | 1|302205|REAL | Adicionar REAL para sinalizar que é uma previsão |
| externalCodeHeader |  |  |  |  | Deixar nulo |
| externalCodeDetail |  | FXCX | CODCOLIGADA|IDXCX | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro | FXCX/FLANRATCCU | CODCOLIGADA|IDXCX|IDRATCCU | 1|302205|2502 |  |
| externalCodeDetailC | Chave do rateio na contabilidade | FXCX/CPARTIDA | CODCOLIGADA|IDXCX|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FXCX | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | Realizar o depara: 2 = Contas à Pagar / 1 = Contas à Receber |
| dateOfIssue | Data de Emissão | FXCX | DATA | 2023/11/30 |  |
| description | Descrição | FXCX | HISTORICO |  | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 | FXCX -> FLANBAIXA -> FLAN -> FTDO |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura | FXCX -> FLANBAIXA -> FLAN -> FTDO |
| documentTypeName\_enUS | Descrição do Tipo de Documento em Inglês |  |  |  | Deixar nulo |
| documentTypeName\_esES | Descrição do Tipo de Documento em Espanhol |  |  |  | Deixar nulo |
| documentNumber | Número de documento | FXCX | NUMERODOCUMENTO |  |  |
| observation | Observação |  |  |  | Deixar nulo |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ | FXCX -> FLANBAIXA -> FLAN |
| scenario | Cenário |  |  |  | Deixar nulo |
| managementGroupHeader | Grupo Gerencial |  |  |  | Deixar nulo |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | NULL ou 2023/11/30 | FXCX -> FLANBAIXA -> FLAN |
| payday | Data Pagamento | FXCX | DATA | 2023/11/30 |  |
| invoiceIssuanceDate | Data de emissão da NF |  |  |  | Deixar nulo |
| invoicePostingDat | Data de lançamento da NF |  |  |  | Deixar nulo |
| eventType | Tipo de Evento | FLAN | PAGREC | S | Realizar o depara: 2 = S / 1 = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | FXCX -> FCXA |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 | FXCX -> FLANBAIXA -> FLAN |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP | FXCX -> FLANBAIXA -> FLAN -> FCFO |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | Enviar campo fixo 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | Realizar o depara: 2 = CP / 1 = CR FXCX -> FLANBAIXA -> FLAN |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 | FXCX -> FLANBAIXA -> FLAN -> FCFO |
| motionWay | Forma de Movimento | TFORMAPAGTO | CODCOLIGADA|IDFORMAPAGTO | 1|2 | FXCX -> TFORMAPAGTO |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | TFORMAPAGTO | DESCFORMAPAGTO | Dinheiro | FXCX -> TFORMAPAGTO |
| motionWayName\_enUS | Descrição da Forma de Movimento em Inglês |  |  |  | Deixar nulo |
| motionWayName\_esES | Descrição da Forma de Movimento em Espanhol |  |  |  | Deixar nulo |
| paymentNumber | Número de Pagamento |  |  |  |  |
| value | Valor do Documento | FXCX | VALOR | 524.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FXCX.IDOPERACAO -> CPARTIDA |
| valueBusiness |  |  |  |  |  |
| conversionBusiness | Valor de Conversão para Unidade de Negócio |  |  |  | Deixar nulo |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa |  |  |  | Deixar nulo |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente |  |  |  | Deixar nulo |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente |  |  |  | Deixar nulo |
| financialOrigin | Cód. Ext. da abertura financeira de origem (Código externo do lançamento da abertura Financeira) |  |  |  | Deixar nulo |
| divisionGroup | Divisão | FXCX | CODCOLIGADA|CODFILIAL | 1|2 |  |
| project | Projeto |  |  |  | Deixar nulo |
| accountingAccountPlan | Plano de Conta Contábil |  |  |  | Avaliar |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 | FXCX -> FLANBAIXA ->  CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | FLAN -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) -> CCONTA Tem que fazer o depara que está entre parenteses. 00 = Não informada (null)/ 01 = Contas de ativo (1) / 02 = Contas de passivo (2) / 03 = Patrimônio Líquido (null) / 04 = Contas de resultado (Credora = 4 e Devedora = 3)/ 05 = Contas de compensação (null) / 09 = Outras (null) Os campos nulos não foram mapeados pois não serão utilizados na integração |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza | FXCX -> FLANBAIXA -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| accountingAccountName\_enUS |  |  |  |  | Deixar nulo |
| accountingAccountName\_esES |  |  |  |  | Deixar nulo |
| costCenterPlan | Plano de Centro de Custo |  |  |  | Avaliar |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 | FXCX -> FLANBAIXA -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 | FXCX -> FLANBAIXA -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria | FXCX -> FLANBAIXA -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterName\_enUS | Descrição do Centro de Custo em Inglês |  |  |  | Deixar nulo |
| costCenterName\_esES | Descrição do Centro de Custo em Espanhol |  |  |  | Deixar nulo |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Quando for inclusão/edição vamos deixar em branco. Quando for uma deleção, vamos enviar 'E'. |
| flexField001 | Campo Flexível | FLANBAIXARATCCU | CODCCUSTO | 1|01.01 | FLANBAIXA -> FLANBAIXARATCCU |
| flexField002 | Campo Flexível - Campos Opcional 1 | FXCX | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FXCX | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FXCX | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FXCX | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FXCX | CODTB5FLX | 0100 |  |

4Realizado - Movimentações bancárias

Modelo de dados **Realizado**: contempla todos os extratos de caixa do RM onde os mesmos podem ou não possuir um rateio e/ou contabilidade e não vieram de um lançamento financeiro.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FXCX | CODCOLIGADA|IDXCX|REAL | 1|302205|REAL | Adicionar REAL para sinalizar que é uma previsão |
| externalCodeHeader |  |  |  |  |  |
| externalCodeDetail |  | FXCX | CODCOLIGADA|IDXCX | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro | FXCX/FLANRATCCU | CODCOLIGADA|IDXCX|IDRATCCU | 1|302205|2502 |  |
| externalCodeDetailC | Chave do rateio na contabilidade | FXCX/CPARTIDA | CODCOLIGADA|IDXCX|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FXCX | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem |  |  | EX | Enviar Valor fixo |
| originSystemName | Descrição do Sistema de Origem |  |  | Extrato de caixa | Enviar Valor fixo |
| dateOfIssue | Data de Emissão | FXCX | DATA | 2023/11/30 |  |
| description | Descrição | FXCX | HISTORICO |  | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FXCX | TIPO |  |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português |  |  | Saque manual | Case do enum FinXCXTipoExtratoEnum |
| documentTypeName\_enUS | Descrição do Tipo de Documento em Inglês |  |  |  | Deixar nulo |
| documentTypeName\_esES | Descrição do Tipo de Documento em Espanhol |  |  |  | Deixar nulo |
| documentNumber | Número de documento | FXCX | NUMERODOCUMENTO |  |  |
| observation | Observação |  |  |  | Deixar nulo |
| currency | Moeda | FCXA | CODMOEDA | NULL ou R$ | FXCX -> FCXA |
| scenario | Cenário |  |  |  | Deixar nulo |
| managementGroupHeader | Grupo Gerencial |  |  |  | Deixar nulo |
| dueDate | Data Vencimento | FXCX | DATA | NULL ou 2023/11/30 |  |
| payday | Data Pagamento | FXCX | DATA | 2023/11/30 |  |
| invoiceIssuanceDate | Data de emissão da NF |  |  |  | Deixar nulo |
| invoicePostingDat | Data de lançamento da NF |  |  |  | Deixar nulo |
| eventType | Tipo de Evento | FXCX | TIPO | S | Realizar o depara utilizando a tabela: Depara Tipo do Extrato |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | FXCX -> FCXA |
| beneficiary | Beneficiário |  |  |  | Deixar nulo |
| beneficiaryName | Nome do Beneficiário |  |  |  | Deixar nulo |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | Enviar campo fixo 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário |  |  |  | Deixar nulo |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário |  |  |  | Deixar nulo |
| motionWay | Forma de Movimento | TFORMAPAGTO | CODCOLIGADA|IDFORMAPAGTO | 1|2 | FXCX -> TFORMAPAGTO |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | TFORMAPAGTO | DESCFORMAPAGTO | Dinheiro | FXCX -> TFORMAPAGTO |
| motionWayName\_enUS | Descrição da Forma de Movimento em Inglês |  |  |  | Deixar nulo |
| motionWayName\_esES | Descrição da Forma de Movimento em Espanhol |  |  |  | Deixar nulo |
| paymentNumber | Número de Pagamento |  |  |  |  |
| value | Valor do Documento | FXCX | VALOR | 524.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FXCX.IDOPERACAO -> CPARTIDA |
| valueBusiness |  |  |  |  | Deixar nulo |
| conversionBusiness | Valor de Conversão para Unidade de Negócio |  |  |  | Deixar nulo |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa |  |  |  | Deixar nulo |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente |  |  |  | Deixar nulo |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente |  |  |  | Deixar nulo |
| financialOrigin | Cód. Ext. da abertura financeira de origem (Código externo do lançamento da abertura Financeira) |  |  |  | Deixar nulo |
| divisionGroup | Divisão | FXCX | CODCOLIGADA|CODFILIAL | 1|25 |  |
| project | Projeto |  |  |  | Deixar nulo |
| accountingAccountPlan | Plano de Conta Contábil |  |  |  | Avaliar |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) Tem que fazer o depara que está entre parenteses. 00 = Não informada (null)/ 01 = Contas de ativo (1) / 02 = Contas de passivo (2) / 03 = Patrimônio Líquido (null) / 04 = Contas de resultado (Credora = 4 e Devedora = 3)/ 05 = Contas de compensação (null) / 09 = Outras (null) Os campos nulos não foram mapeados pois não serão utilizados na integração |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| accountingAccountName\_enUS |  |  |  |  | Deixar nulo |
| accountingAccountName\_esES |  |  |  |  | Deixar nulo |
| costCenterPlan | Plano de Centro de Custo |  |  |  | Avaliar |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria | FXCX (IDOPERACAOCONT) -> CCONT (IDOPERACAO) -> CPARTIDA (IDPARTIDA) |
| costCenterName\_enUS | Descrição do Centro de Custo em Inglês |  |  |  | Deixar nulo |
| costCenterName\_esES | Descrição do Centro de Custo em Espanhol |  |  |  | Deixar nulo |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Quando for inclusão/edição vamos deixar em branco. Quando for uma deleção, vamos enviar 'E'. |
| flexField001 | Campo Flexível |  |  |  | Deixar nulo |
| flexField002 | Campo Flexível - Campos Opcional 1 | FXCX | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FXCX | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FXCX | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FXCX | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FXCX | CODTB5FLX | 0100 |  |

4Definiçõesfade

De acordo com o status do lançamento iremos modificar o evento de deleção

|  |  |  |
| --- | --- | --- |
| **Código** | **Status** | **Evento Gesplan** |
| 0 | Em Aberto | Inclusão/Modificação |
| 1 | Baixado | Deleção |
| 2 | Cancelado | Deleção |
| 3 | Baixado por Acordo | Deleção |
| 4 | Baixado parcialmente | Inclusão/Modificação |
| 5 | Borderô | Inclusão/Modificação |

Tipo do extrato - Enviado para Gesplan no campo Tipo de Documento.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tipo de extrato** | **Origem** | **Descrição** | **Código** | **Descricao** | **Tipo Gesplan** | **Tipo de Evento** |
| 1 - Saque Manual | Movimentação Bancária | Saque | 1 | Pagar | CR | E |
| 2 - Depósito Manual | Movimentação Bancária | Depósito | 2 | Receber | CP | S |
| 3 - Saque Transferência | Movimentação Bancária | Saque | 1 | Pagar | CR | E |
| 4 - Depósito Transferência | Movimentação Bancária | Depósito | 2 | Receber | CP | S |
| 5 - Depósito na Baixa | Título | Depósito | 2 | Receber | CP | E |
| 6 - Saque na Baixa | Título | Saque | 1 | Pagar | CR | S |
| 7 - Saque do Cheque | Título | Saque | 1 | Pagar | CR | E |
| 8 - Dep. Canc. de Baixa | Título | Depósito | 2 | Receber | CP | S |
| 9 - Saque Canc. Baixa | Título | Saque | 1 | Pagar | CR | E |
| 10 - Dep. Canc. de Cheque | Título | Depósito | 2 | Receber | CP | S |
| 11 - Saque CPMF | Movimentação Bancária | Saque | 1 | Pagar | CR | E |
| 12 - Recebimento via Cheque | Título | Depósito | 2 | Receber | CP | S |
| 13 - Saque Canc. Receb. Cheque | Título | Saque | 1 | Pagar | CR | E |
| 14 - Deb. Canc. CPMF | Movimentação Bancária | Depósito | 2 | Receber | CP | S |
| 15 - Desc. Em Aberto | Título | Depósito | 2 | Receber | CP | E |
| 16 - Desc. Efetivado | Título | Depósito | 2 | Receber | CP | E |
| 17 - Devolução de Desconto | Título | Saque | 1 | Pagar | CR | S |
| 18 - Saque Transferência Conciliação | Movimentação Bancária | Saque | 1 | Pagar | CR | E |
| 19 - Depóstio Transferência Conciliação | Movimentação Bancária | Depósito | 2 | Receber | CP | S |
| 20 - Saque Taxas Adm. Cartão | Movimentação Bancária | Saque | 1 | Pagar | CR | E |
| 21 - Rendimento Financeiro | Movimentação Bancária | Depósito | 2 | Receber | CP | S |
| 22 - Depósito Antecipação | Movimentação Bancária | Depósito | 2 | Receber | CP | E |
| 23 - Saque Antecipação | Movimentação Bancária | Saque | 1 | Pagar | CR | E |

## **03. DEMAIS INFORMAÇÕES**

* <https://docs.carol.ai/>
