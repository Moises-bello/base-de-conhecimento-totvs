---
content_hash: b4ed598cd1f1c2a57c2ef925a6f583f76909dd9d127cec469d899dd94ba98467
fetched_at: '2026-06-29T00:12:07.093649+00:00'
page_id: '919061335'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan - Previsão Financeira (Envio do RM para a Gesplan)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=919061335
version: 11
---

Conteúdo:

# 1. Dicionário

| RM | Gesplan |
| --- | --- |
| [Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=275587649) | Unidade Operacional |
| Filial | Divisão |

# 2. Definições

Para garantir o sucesso da integração e evitar a quebra das regras de negócios, foram necessárias algumas definições e ajustes prévios entre o ERP e a Gesplan.

**Valor**: Sempre será sempre o Valor Original do lançamento financeiro

**Natureza Orçamentária / Financeira**: A [natureza orçamentária financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=423937949), será enviada em um campo flexível (7)

**Tabelas Opcionais**: Como as [tabela opcional](https://tdn.totvs.com/display/LRM/FIN+-+Tabelas+Opcionais) são usadas para objetivos diferentes por cada cliente, as informações serão enviadas em campos flexíveis (2 a 6).

**Contabilidade:** Para lançamentos a receber, será enviada apenas as partidas a crédito. Para lançamentos a pagar, serão enviadas apenas as partidas a débito.

# 3. Gatilhos

O envio de informações para Gesplan acontece de forma automática, os status dos lançamentos financeiros são responsáveis por disparar gatilhos de eventos na Gesplan.

| Status RM | Evento Gesplan |
| --- | --- |
| Em aberto | Inclusão / Modificação |
| Baixado | Deleção da previsão |
| Cancelado | Deleção da previsão |
| Baixado por Acordo | Deleção da previsão |
| Baixado parcialmente | Inclusão/Modificação |
| Borderô | Inclusão/Modificação |

# 3. Mapemento de Campos

Para facilitar a identificação dos campos trafegados entre as plataformas, disponibilizamos abaixo o mapeamentos dos campos:

**PREVISTO**: O envio da previsão financeira considera todos os lançamentos (a pagar e a receber) em aberto ou parcialmente baixado.

Modelo de dados Previsto (com contabilidade)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FLAN | CODCOLIGADA|IDLAN|PREV | 1|302205|PREV | PREV para sinalizar que é uma previsão |
| externalCodeDetail |  | FLAN | CODCOLIGADA|IDLAN | 1|302205 |  |
| externalCodeDetailC | Chave do rateio na contabilidade | FLAN/CPARTIDA | CODCOLIGADA|IDLAN|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FLAN | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | 2 - A Pagar = CP  1 - A Receber = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | 2 - A Pagar = Contas à Pagar 1 - A Receber = Contas à Receber |
| dateOfIssue | Data de Emissão | FLAN | DATAEMISSAO | 2023/11/30 |  |
| description | Descrição | FLAN | HISTORICO | ES-0012714-1FLAVIO INACIO SILVEIRA | Se for null, enviado o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura |  |
| documentNumber | Número de documento | FLAN | NUMERODOCUMENTO | 0000006928 |  |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ |  |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | 2023/11/30 |  |
| payday | Data Pagamento |  |  |  |  |
| invoiceIssuanceDate | Data de emissão da NF | FLAN | DATAEMISSAO | 2023/11/30 |  |
| invoicePostingDat | Data de lançamento da NF | FLAN | DATACRIACAO | 2023/11/30 |  |
| eventType | Tipo de Evento | FLAN | PAGREC | S | 2 - A Pagar = S  1 - A Receber = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | Se o cadastro for global, a coligada virá como 0(zero) |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 | Se o cadastro for global, a coligada virá como 0(zero) |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP |  |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | 2 - A Pagar = CP 1 - A Receber = CR |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 |  |
| motionWay | Forma de Movimento | FDADOSPGTO | CODCOLIGADA|IDPGTO | 1|1020 |  |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | FDADOSPGTO | DESCRICAO | Null ou Dinheiro |  |
| value | Valor do Documento | FLAN | VALORORIGINAL | 64782.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 |  |
| conversionBusiness | Valor de Conversão para Unidade de Negócio | FLAN | FLAN.VALORORIGINAL \* GCOTACAO.FATOR | 259.128 | Pegar a cotação pela data de vencimento e o indexador do lançamento |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente | GCOTACAO | FATOR | 4.00 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| divisionGroup | Divisão | FLAN | CODCOLIGADA|CODFILIAL | 1|25 |  |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 | Se o cadastro for global, a coligada virá como 0(zero) |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | 00 = Não informada 01 = Contas de ativo 02 = Contas de passivo 04 = Contas de resultado (Credora = 4 e Devedora = 3) |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza |  |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 |  |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 |  |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria |  |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Inclusão/edição = em branco Deleção = E |
| flexField001 | Campo Flexível | FLANRATCCU | CODCOLIGADA|CODCCUSTO |  |  |
| flexField002 | Campo Flexível - Campos Opcional 1 | FLAN | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FLAN | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FLAN | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FLAN | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FLAN | CODTB5FLX | 0100 |  |
| flexField007 | Campo Flexível - Natureza Orçamentária Financeira | FLANRATCCU | CODCOLNATFINANCEIRA|CODNATFINANCEIRA | 0|02.001.0001 | Se o cadastro for global, a coligada virá como 0(zero) |
| flexField008 | Campo Flexível - Data Previsão de Baixa | FLAN | DATAPREVBAIXA | 2023/11/30 |  |
| flexField009 | Campo Flexível - Período Letivo | FLAN | PERLETIVO |  |  |
| flexField010 | Campo Flexível - Valor Opcional 1 | FLAN | VALOROP1 |  |  |
| flexField011 | Campo Flexível - Valor Opcional 2 | FLAN | VALOROP2 |  |  |
| flexField012 | Campo Flexível - Valor Opcional 3 | FLAN | VALOROP3 |  |  |
| flexField013 | Campo Flexível - Valor Opcional 4 | FLAN | VALOROP4 |  |  |
| flexField014 | Campo Flexível - Valor Opcional 5 | FLAN | VALOROP5 |  |  |
| flexField015 | Campo Flexível - Valor Opcional 6 | FLAN | VALOROP6 |  |  |
| flexField016 | Campo Flexível - Valor Opcional 7 | FLAN | VALOROP7 |  |  |
| flexField017 | Campo Flexível - Valor Opcional 8 | FLAN | VALOROP8 |  |  |

Modelo de dados Previsto (sem contabilidade)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FLAN | CODCOLIGADA|IDLAN|PREV | 1|302205|PREV | PREV para sinalizar que é uma previsão |
| externalCodeDetail |  | FLAN | CODCOLIGADA|IDLAN | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro |  | FLAN/FLANRATCCU | CODCOLIGADA|IDLAN|IDRATCCU | 1|302205|2502 |
| businessUnit | Unidade Negócio | FLAN | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | 2 - A Pagar = CP  1 - A Receber = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | 2 - A Pagar = Contas à Pagar 1 -A Receber = Contas à Receber |
| dateOfIssue | Data de Emissão | FLAN | DATAEMISSAO | 2023/11/30 |  |
| description | Descrição | FLAN | HISTORICO | ES-0012714-1FLAVIO INACIO SILVEIRA | Se for null, enviado o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura |  |
| documentNumber | Número de documento | FLAN | NUMERODOCUMENTO | 0000006928 |  |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ |  |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | 2023/11/30 |  |
| payday | Data Pagamento | FLAN | DATABAIXA | Null ou 2023/11/30 |  |
| invoiceIssuanceDate | Data de emissão da NF | FLAN | DATAEMISSAO | 2023/11/30 |  |
| invoicePostingDat | Data de lançamento da NF | FLAN | DATACRIACAO | 2023/11/30 |  |
| eventType | Tipo de Evento | FLAN | PAGREC | S | 2 - A Pagar = S  1 - A Receber = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 | Se o cadastro for global, a coligada virá como 0(zero) |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 | Se o cadastro for global, a coligada virá como 0(zero) |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP |  |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | 2 - A Pagar = CP 1 - A Receber = CR |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 |  |
| motionWay | Forma de Movimento | FDADOSPGTO | CODCOLIGADA|IDPGTO | 1|1020 |  |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | FDADOSPGTO | DESCRICAO | Null ou Dinheiro |  |
| value | Valor do Documento | FLAN | VALORORIGINAL | 64782.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 |  |
| conversionBusiness | Valor de Conversão para Unidade de Negócio | FLAN | FLAN.VALORORIGINAL \* GCOTACAO.FATOR | 259.128 | Pegar a cotação pela data de vencimento e o indexador do lançamento |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente | GCOTACAO | FATOR | 4.00 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente | FLAN | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) | 1 | Pegar a cotação pela data de vencimento e a moeda do lançamento |
| divisionGroup | Divisão | FLAN | CODCOLIGADA|CODFILIAL | 1|25 |  |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 | Se o cadastro for global, a coligada virá como 0(zero) |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | 00 = Não informada 01 = Contas de ativo 02 = Contas de passivo 04 = Contas de resultado (Credora = 4 e Devedora = 3) |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza |  |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 |  |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 |  |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria |  |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Inclusão/edição = em branco Deleção = E |
| flexField001 | Campo Flexível |  |  |  | Deixar nulo |
| flexField002 | Campo Flexível - Campos Opcional 1 | FLAN | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FLAN | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FLAN | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FLAN | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FLAN | CODTB5FLX | 0100 |  |
| flexField007 | Campo Flexível - Natureza Orçamentária Financeira | FLANRATCCU | CODCOLNATFINANCEIRA|CODNATFINANCEIRA |  | Se o cadastro for global, a coligada virá como 0(zero) |
| flexField008 | Campo Flexível - Data Previsão de Baixa | FLAN | DATAPREVBAIXA | 2023/11/30 |  |
| flexField009 | Campo Flexível - Periodo Letivo | FLAN | PERLETIVO |  |  |
| flexField010 | Campo Flexível - Valor Opcional 1 | FLAN | VALOROP1 |  |  |
| flexField011 | Campo Flexível - Valor Opcional 2 | FLAN | VALOROP2 |  |  |
| flexField012 | Campo Flexível - Valor Opcional 3 | FLAN | VALOROP3 |  |  |
| flexField013 | Campo Flexível - Valor Opcional 4 | FLAN | VALOROP4 |  |  |
| flexField014 | Campo Flexível - Valor Opcional 5 | FLAN | VALOROP5 |  |  |
| flexField015 | Campo Flexível - Valor Opcional 6 | FLAN | VALOROP6 |  |  |
| flexField016 | Campo Flexível - Valor Opcional 7 | FLAN | VALOROP7 |  |  |
| flexField017 | Campo Flexível - Valor Opcional 8 | FLAN | VALOROP8 |  |  |
