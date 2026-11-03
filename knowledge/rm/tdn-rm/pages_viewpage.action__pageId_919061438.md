---
content_hash: 9e59df9673d697019286696bccf6554b3fb10e616bf2acedd2130cee9ed56865
fetched_at: '2026-06-29T00:12:07.136818+00:00'
page_id: '919061438'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan - Realizado (Envio do RM para a Gesplan)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=919061438
version: 15
---

Conteúdo:

# 1. Dicionário

| RM | Gesplan |
| --- | --- |
| [Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=275587649) | Unidade Operacional |
| Filial | Divisão |
| [Conta / Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) | Banco | Agência | Conta |

# 2. Definições

**Valor**: Sempre será enviado o valor do extrato.

**Conta/Caixa**: Será enviado as informações de Banco / Agência / Conta Corrente, informados na [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) utilizada na baixa do lançamento financeiro. 

**Rateio**: Rateio será enviado como campo flexível (1).

**Tabelas Opcionais**: Como as [tabela opcional](https://tdn.totvs.com/display/LRM/FIN+-+Tabelas+Opcionais) são usadas para objetivos diferentes por cada cliente, as informações serão enviadas em campos flexíveis (2 a 6).

**Contabilidade:**Para lançamentos a receber, será enviada apenas as partidas a crédito. Para lançamentos a pagar, serão enviadas apenas as partidas a débito.

# 3. Gatilhos

O envio de informações para Gesplan acontece de forma automática, os tipos dos extratos de caixa são responsáveis por disparar os tipos de de eventos na Gesplan.

Tipo Extrato RM

| Tipo Extrato RM | Origem RM | Descrição Documento | Código | Origem Gesplan | Tipo Gesplan | Tipo de Evento Gesplan |
| --- | --- | --- | --- | --- | --- | --- |
| 1 - Saque Manual | Movimentação Bancária | Saque | 1 | Pagar | CP | S |
| 2 - Depósito Manual | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 3 - Saque Transferência | Movimentação Bancária | Saque | 1 | Pagar | CP | S |
| 4 - Depósito Transferência | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 5 - Depósito na Baixa | Título | Depósito | 2 | Receber | CR | E |
| 6 - Saque na Baixa | Título | Saque | 1 | Pagar | CP | S |
| 7 - Saque do Cheque | Título | Saque | 1 | Pagar | CP | S |
| 8 - Dep. Canc. de Baixa | Título | Depósito | 2 | Receber | CR | E |
| 9 - Saque Canc. Baixa | Título | Saque | 1 | Pagar | CP | S |
| 10 - Dep. Canc. de Cheque | Título | Depósito | 2 | Receber | CR | E |
| 11 - Saque CPMF | Movimentação Bancária | Saque | 1 | Pagar | CP | S |
| 12 - Recebimento via Cheque | Título | Depósito | 2 | Receber | CR | E |
| 13 - Saque Canc. Receb. Cheque | Título | Saque | 1 | Pagar | CP | S |
| 14 - Deb. Canc. CPMF | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 15 - Desc. Em Aberto | Título | Depósito | 2 | Receber | CR | E |
| 16 - Desc. Efetivado | Título | Depósito | 2 | Receber | CR | E |
| 17 - Devolução de Desconto | Título | Saque | 1 | Pagar | CP | S |
| 18 - Saque Transferência Conciliação | Movimentação Bancária | Saque | 1 | Pagar | CP | S |
| 19 - Depóstio Transferência Conciliação | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 20 - Saque Taxas Adm. Cartão | Movimentação Bancária | Saque | 1 | Pagar | CP | S |
| 21 - Rendimento Financeiro | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 22 - Depósito Antecipação | Movimentação Bancária | Depósito | 2 | Receber | CR | E |
| 23 - Saque Antecipação | Movimentação Bancária | Saque | 1 | Pagar | CP | S |

3. Mapemento de Campos

Para facilitar a identificação dos campos trafegados entre as plataformas, disponibilizamos abaixo o mapeamentos dos campos:

**REALIZADO**: Contempla todos os extratos de caixa do RM, independente da sua origem.

Realizado (extratos por baixa de lançamentos financeiro)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FXCX | CODCOLIGADA|IDBAIXA|REAL | 1|302205|REAL | REAL para sinalizar que é um realizado |
| externalCodeDetail |  | FXCX | CODCOLIGADA|IDBAIXA | 1|302205 |  |
| externalCodeDetailF | Chave do rateio no financeiro | FLANBAIXA/FLANBAIXARATCCU | CODCOLIGADA|IDBAIXA|IDRATCCU | 1|302205|2502 |  |
| externalCodeDetailC | Chave do rateio na contabilidade | FLANBAIXA/CPARTIDA | CODCOLIGADA|IDBAIXA|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FXCX | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem | FLAN | PAGREC | CP | 2 - A Pagar = CP 1 - A Receber = CR |
| originSystemName | Descrição do Sistema de Origem | FLAN | PAGREC | Contas à Pagar | 2 - A Pagar = Contas à Pagar 1 - A Receber = Contas à Receber |
| dateOfIssue | Data de Emissão | FXCX | DATA | 2023/11/30 |  |
| description | Descrição | FXCX | HISTORICO |  | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FTDO | CODCOLIGADA|CODTDO | 1|01 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FTDO | DESCRICAO | NF- Serviço - Fatura |  |
| documentNumber | Número de documento | FXCX | NUMERODOCUMENTO |  |  |
| currency | Moeda | FLAN | CODMOEVALORORIGINAL | R$ |  |
| dueDate | Data Vencimento | FLAN | DATAVENCIMENTO | NULL ou 2023/11/30 |  |
| payday | Data Pagamento | FXCX | DATA | 2023/11/30 |  |
| payday | Data Compensacao | FXCX | DATACOMPENSACAO | 2023/11/30 |  |
| eventType | Tipo de Evento | FLAN | PAGREC | S | 2 - A Pagar = S 1 - A Receber = E |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 |  |
| beneficiary | Beneficiário | FCFO | CODCOLIGADA|CODCFO | 1|00111075 |  |
| beneficiaryName | Nome do Beneficiário | FCFO | NOMEFANTASIA | FERSHOP |  |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | 6 - Outros |
| beneficiaryOrigin | Origem do Beneficiário | FLAN | PAGREC | CP | 2 - A Pagar = CP 1 - A Receber = CR |
| beneficiaryFederalCode | Identificação Nacional do Beneficiário | FCFO | CGCCFO | 111.111.111-11 |  |
| motionWay | Forma de Movimento | TFORMAPAGTO | CODCOLIGADA|CODFORMAPAGTO | 1|2 |  |
| motionWayName\_ptBR | Descrição da Forma de Movimento em Português | TFORMAPAGTO | DESCFORMAPAGTO | Dinheiro |  |
| value | Valor do Documento | FXCX | VALOR | 524.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FXCX.IDOPERACAO -> CPARTIDA |
| valueBusiness |  |  |  |  |  |
| conversionBusiness | Valor de Conversão para Unidade de Negócio | GCOTACAO | FATOR |  | Se moeda for diferente, mandar fator da moeda da Coligada na data do pagamento |
| fixedRateBusiness | Taxa Fixa Moeda da Empresa | 1 | IF( (FLAN.VALORORIGINAL \* GCOTACAO.FATOR) <> 0 , '1' , '0' ) |  |  |
| conversionAccount | Taxa de Conversão Fixa para Conta Corrente | GCOTACAO | FATOR |  | Se moeda for diferente, mandar fator da moeda da conta/caixa na data do pagamento |
| fixedRateAccount | Taxa Fixa Moeda Conta Corrente | 1 |  |  |  |
| divisionGroup | Divisão | FXCX | CODCOLIGADA|CODFILIAL | 1|2 |  |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 |  |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | 01 = Contas de ativo 02 = Contas de passivo 04 = Contas de resultado (Credora = 4 e Devedora = 3) |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza |  |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 |  |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 |  |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria |  |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Inclusão/edição = em branco. Deleção  E |
| flexField001 | Campo Flexível | FLANBAIXARATCCU | CODCOLIGADA|CODCCUSTO | 1|01.01 | FLANBAIXA -> FLANBAIXARATCCU |
| flexField002 | Campo Flexível - Campos Opcional 1 | FXCX | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FXCX | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FXCX | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FXCX | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FXCX | CODTB5FLX | 0100 |  |
| flexField007 | Campo Flexível - Natureza Orçamentária Financeira | FLANBAIXARATCCU | CODCOLNATFINANCEIRA|CODNATFINANCEIRA | 1|004.003 | FLANBAIXA -> FLANBAIXARATCCU |
| flexField008 | Campo Flexível - Data Previsão de Baixa | FLAN | DATAPREVBAIXA |  |  |
| flexField009 | Campo Flexível - Período Letivo | FLAN | PERLETIVO |  |  |
| flexField010 | Campo Flexível - Valor Opcional 1 | FLAN | VALOROP1 |  |  |
| flexField011 | Campo Flexível - Valor Opcional 2 | FLAN | VALOROP2 |  |  |
| flexField012 | Campo Flexível - Valor Opcional 3 | FLAN | VALOROP3 |  |  |
| flexField013 | Campo Flexível - Valor Opcional 4 | FLAN | VALOROP4 |  |  |
| flexField014 | Campo Flexível - Valor Opcional 5 | FLAN | VALOROP5 |  |  |
| flexField015 | Campo Flexível - Valor Opcional 6 | FLAN | VALOROP6 |  |  |
| flexField016 | Campo Flexível - Valor Opcional 7 | FLAN | VALOROP7 |  |  |
| flexField017 | Campo Flexível - Valor Opcional 8 | FLAN | VALOROP8 |  |  |

Realizado (extratos manuais)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo Gesplan** | **Descrição Gesplan** | **Tabela RM** | **Campo RM** | **Exemplo Envio** | **Observação** |
| externalCode | Código Externo | FXCX | EX|CODCOLIGADA|IDXCX|REAL | EX|1|302205|REAL | REAL para sinalizar que é um realizado |
| externalCodeDetail |  | FXCX | CODCOLIGADA|IDXCX | 1|302205 |  |
| externalCodeDetailF |  | FXCX | CODCOLIGADA|IDXCX | 1|302205 |  |
| externalCodeDetailC | Chave do rateio na contabilidade | FXCX/CPARTIDA | CODCOLIGADA|IDXCX|IDPARTIDA | 1|302205|23999 |  |
| businessUnit | Unidade Negócio | FXCX | CODCOLIGADA | 1 |  |
| originSystem | Sistema de Origem |  |  | EX | Valor Fixo = EX |
| originSystemName | Descrição do Sistema de Origem |  |  | Extrato de caixa | Valor Fixo = Extrato de caixa |
| dateOfIssue | Data de Emissão | FXCX | DATA | 2023/11/30 |  |
| description | Descrição | FXCX | HISTORICO |  | Se for null, enviar o texto: Sem descrição |
| documentType | Tipo de Documento | FXCX | TIPO | 1|1 |  |
| documentTypeName\_ptBR | Descrição do Tipo de Documento em Português | FXCX | TIPO | Saque manual | De acordo com o mapeamento de tipos |
| documentNumber | Número de documento | FXCX | NUMERODOCUMENTO |  |  |
| currency | Moeda | FCXA | CODMOEDA | R$ |  |
| dueDate | Data Vencimento | FXCX | DATA | NULL ou 2023/11/30 |  |
| payday | Data Pagamento | FXCX | DATA | 2023/11/30 | Se extrato compensado, Data Compensação, Senão Data do extrato |
| eventType | Tipo de Evento | FXCX | TIPO | S | De acordo com o mapeamento de tipos |
| currentAccount | Conta Corrente | FCXA | CODCOLIGADA|NUMBANCO|NUMAGENCIA|NROCONTA | 0|0023|1020-1|10203 |  |
| beneficiaryType | Tipo do Beneficiário |  |  | 6 | 6 - Outros |
| value | Valor do Documento | FXCX | VALOR | 524.0000 |  |
| proratedValue |  | CPARTIDA | VALOR | 30.00 | FXCX.IDOPERACAO -> CPARTIDA |
| divisionGroup | Divisão | FXCX | CODCOLIGADA|CODFILIAL | 1|2 |  |
| accountingAccount | Conta Contábil | CPARTIDA | CODCOLCREDITO|CREDITO OU CODCOLDEBITO|DEBITO | 1|1.1.1.1.003 |  |
| accountingAccountClassification | Tipo de Conta Contábil | CCONTA | CODCOLIGADA|NATSPED | 1|01 | 01 = Contas de ativo 02 = Contas de passivo 04 = Contas de resultado (Credora = 4 e Devedora = 3) |
| accountingAccountName\_ptBR | Descrição da Conta Contábil em Português | CCONTA | DESCRICAO | Caixa Filial Fortaleza |  |
| costCenter | Centro de Custo | CPARTIDA | CODCOLIGADA|CODCCUSTO | 1|01.1 |  |
| costCenterCategory | Categoria do Centro de Custo | GCCUSTO | CODCOLIGADA|CODCLASSIFICA | 1|01 |  |
| costCenterName\_ptBR | Descrição do Centro de Custo em Português | GCCUSTO | NOME | Controladoria |  |
| integrationType | Branco ou 'E' e 'E' indicando exclusão do registro/movimento |  |  |  | Inclusão/edição = em branco. Deleção  E |
| flexField001 | Campo Flexível - Centro de Custo do Extrato | FXCX | CODCCUSTO | 01.01 |  |
| flexField002 | Campo Flexível - Campos Opcional 1 | FXCX | CODTB1FLX | 0001 |  |
| flexField003 | Campo Flexível - Campos Opcional 2 | FXCX | CODTB2FLX | 2010 |  |
| flexField004 | Campo Flexível - Campos Opcional 3 | FXCX | CODTB3FLX | 0010 |  |
| flexField005 | Campo Flexível - Campos Opcional 4 | FXCX | CODTB4FLX | 10.20 |  |
| flexField006 | Campo Flexível - Campos Opcional 5 | FXCX | CODTB5FLX | 0100 |  |
| flexField007 | Campo Flexível - Natureza Orçamentária Financeira | FXCX | CODCOLNATFINANCEIRA|CODNATFINANCEIRA | 1|004.003 |  |
