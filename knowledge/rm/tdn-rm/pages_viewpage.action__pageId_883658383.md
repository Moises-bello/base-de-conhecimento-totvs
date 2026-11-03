---
content_hash: 9c9f3444108006abd0552dfe6bf95ebed723c6946845f8c1b037dd4276dc156b
fetched_at: '2026-06-29T00:12:00.673774+00:00'
page_id: '883658383'
product: rm
source: tdn-rm
title: Linha RM (Integração Gesplan) - Dados recebidos pelo ERP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883658383
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Data Models**
3. **Testando via Postman**
4. **Demais****informações**

## **01. VISÃO GERAL**

Esse documento tem como objetivo apresentar como a Gesplan envia registros para o RM.

## **02. DATA MODELS**

O propósito desta seção é apresentar os campos disponíveis para adicionar registros no RM.

Para as solicitações de alteração, não é necessário submeter todos os campos; apenas os obrigatórios e aqueles que estão sendo modificados precisam ser enviados.

Este documento está dividido em duas partes: a primeira parte lista os campos disponíveis para cada tipo de solicitação, enquanto a segunda parte fornece um exemplo de Json que ilustra como os dados devem ser estruturados.

cenario1Lanc. Financeiro - Inclusãofade

Modelo de dados para à inclusão de um lançamento financeiro no RM.  
A subscrição que deverá ser utilizada: **FinLanIncDataCommand**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | ****Tamanho**** | **Observação** |
| FinLanInclusaoConsumer | CodColigada | int | Coligada | Sim |  |  |
| FinLanInclusaoConsumer | IdLan | int | Referência do lançamento | Sim |  |  |
| FinLanInclusaoConsumer | UsuarioInclusao | string | Usuário do sistema de inclusão do Lançamento | Sim | 20 |  |
| FinLanInclusaoConsumer | PagRec | FinLanPagRecEnum | A pagar/receber | Sim |  | 0 - WCF 1 - Receber 2 - Pagar |
| FinLanInclusaoConsumer | CodFilial | int | Código da Filial | Sim |  |  |
| FinLanInclusaoConsumer | CodColCfo | int | Coligada do Cliente/Fornecedor | Sim |  |  |
| FinLanInclusaoConsumer | CodCfo | string | Código do Cli/For | Sim | 25 |  |
| FinLanInclusaoConsumer | CodTdo | string | Código do Tipo de Documento | Sim | 10 |  |
| FinLanInclusaoConsumer | NumeroDocumento | string | Número do documento | Sim | 40 |  |
| FinLanInclusaoConsumer | DataEmissao | DateTime | Data de Emissão | Sim |  |  |
| FinLanInclusaoConsumer | DataVencimento | DateTime | Data de vencimento | Sim |  |  |
| FinLanInclusaoConsumer | ValorOriginal | decimal | Valor Original | Sim |  |  |
| FinLanInclusaoConsumer | Historico | string | Histórico | Não | 255 |  |
| FinLanInclusaoConsumer | SerieDocumento | string | Série do documento | Não | 8 |  |
| FinLanInclusaoConsumer | Reutilizacao | int? | Reutilização do bloco de notas fiscais | Não |  |  |
| FinLanInclusaoConsumer | CodCCusto | string | Código do centro de custo | Não | 25 |  |
| FinLanInclusaoConsumer | Moeda | string | Moeda valor original | Não | 10 |  |
| FinLanInclusaoConsumer | ValorJuros | decimal | Valor dos juros | Não |  |  |
| FinLanInclusaoConsumer | ValorDesconto | decimal | Valor do desconto | Não |  |  |
| FinLanInclusaoConsumer | ValorMulta | decimal | Valor multa | Não |  |  |
| FinLanInclusaoConsumer | TipoContabil | FinLanContabilEnum | Tipo Contábil | Não |  | 0 - Não Contábil 1 - Contábil 2 - Baixa Contábil 3 - A Contabilizar 4 - Contábil com Baixa a Contabilizar 5 - Baixa a Contabilizar |
| FinLanInclusaoConsumer | CodEvento | short? | Código do Evento Contábil | Não |  |  |
| FinLanInclusaoConsumer | Contabilizacao | ObjectList<FinLanContInclusaoConsumer> | Contabilização | Não |  |  |
| FinLanInclusaoConsumer | RateioCCusto | ObjectList<FinLanRatCCuInclusaoConsumer> | Rateio por centro de custo | Não |  |  |
| FinLanInclusaoConsumer | RateioDepto | ObjectList<FinLanRatDepInclusaoConsumer> | Rateio por departamento | Não |  |  |
| **Classes de lista da FinLanInclusaoConsumer** | | | | | | |
| FinLanContInclusaoConsumer | Tipo | FinLanDebitoCreditoEnum | Tipo Contábil (Débito ou Crédito) | Sim |  | Os campos só serão obrigatórios se o objeto for preenchido.  0 - WCF  1 - Débito  2 - Crédito |
| FinLanContInclusaoConsumer | CodColConta | int | Coligada da Conta Contábil | Sim |  |  |
| FinLanContInclusaoConsumer | CodConta | string | Código da Conta Contábil | Sim |  |  |
| FinLanContInclusaoConsumer | CodFilial | int | Código da Filial | Sim |  |  |
| FinLanContInclusaoConsumer | CodCCusto | string | Código do Centro de Custo | Não | 25 |  |
| FinLanContInclusaoConsumer | ComplHistorico | string | Complemento de histórico | Não | 250 |  |
| FinLanContInclusaoConsumer | Valor | decimal | Valor | Sim |  |  |
| FinLanRatCCuInclusaoConsumer | CodCCusto | string | Código do centro de custo | Sim | 25 |  |
| FinLanRatCCuInclusaoConsumer | Valor | decimal | Valor atribuído ao centro de custo | Sim |  |  |
| FinLanRatCCuInclusaoConsumer | Historico | string | Histórico associado ao rateio | Não | 255 |  |
| FinLanRatDepInclusaoConsumer | CodFilial | int | Código identificador da filial | Sim |  | Os campos só serão obrigatórios se o objeto for preenchido. |
| FinLanRatDepInclusaoConsumer | CodDepartamento | string | Código identificador do departamento | Sim | 25 |  |
| FinLanRatDepInclusaoConsumer | Valor | decimal | Valor atribuído ao rateio por departamento | Sim |  |  |

2Lanc. Financeiro - Alteraçãofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

A subscrição que deverá ser utilizada: **FinLanAltDataCommand**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| FinLanAlteracaoConsumer | UsuarioAlteracao | string | Define o usuário de alteração do Lançamento. | Sim | 20 |  |
| FinLanAlteracaoConsumer | CodColigada | int | Coligada. | Sim |  |  |
| FinLanAlteracaoConsumer | IdLan | int | Ref. do Lançamento. | Sim |  |  |
| FinLanAlteracaoConsumer | DataSistema | DateTime | DataSistema. | Sim |  |  |
| FinLanAlteracaoConsumer | PagRec | FinLanPagRecEnum | A pagar/receber. | Não |  | 0 - WCF 1 - Receber 2 - Pagar |
| FinLanAlteracaoConsumer | CodFilial | int | Código da Filial. | Sim |  |  |
| FinLanAlteracaoConsumer | CodColCfo | int | Coligada do Cli/For. | Não | 25 |  |
| FinLanAlteracaoConsumer | CodCfo | string | Código do Cli/For. | Não | 10 |  |
| FinLanAlteracaoConsumer | CodTdo | string | Código do Tipo de Documento. | Não | 40 |  |
| FinLanAlteracaoConsumer | NumeroDocumento | string | Número do Documento. | Não | 20 |  |
| FinLanAlteracaoConsumer | SegundoNumero | string | Segundo número. | Não |  |  |
| FinLanAlteracaoConsumer | DataEmissao | DateTime | Data de emissão. | Não |  |  |
| FinLanAlteracaoConsumer | ValorOriginal | decimal | Valor original. | Não |  |  |
| FinLanAlteracaoConsumer | Historico | string | Histórico. | Não | 255 |  |
| FinLanAlteracaoConsumer | Moeda | string | Moeda. | Não | 10 |  |
| FinLanAlteracaoConsumer | SerieDocumento | string | Série do documento. | Não | 8 |  |
| FinLanAlteracaoConsumer | ValorJuros | decimal | Valor de juros. | Não |  |  |
| FinLanAlteracaoConsumer | ValorDesconto | decimal | Valor de desconto. | Não |  |  |
| FinLanAlteracaoConsumer | ValorMulta | decimal | Valor de multa. | Não |  |  |
| FinLanAlteracaoConsumer | Reutilizacao | int | Reutilização do bloco de notas fiscais. | Não |  |  |
| FinLanAlteracaoConsumer | TipoContabil | FinLanContabilEnum | Tipo Contábil. | Não |  | 0 - Não Contábil 1 - Contábil 2 - Baixa Contábil 3 - A Contabilizar 4 - Contábil com Baixa a Contabilizar 5 - Baixa a Contabilizar |
| FinLanAlteracaoConsumer | ContabilizacaoInclusao | List<FinLanContAlteracaoConsumer> | Contabilização de Inclusão. | Não |  |  |
| FinLanAlteracaoConsumer | RateioCCusto | ObjectList<FinLanRatCCuAlteracaoConsumer> | Rateio por centro de custo. | Não |  |  |
| FinLanAlteracaoConsumer | RateioDepto | ObjectList<FinLanRatDepAlteracaoConsumer> | Rateio por departamento. | Não |  |  |
| **Classes de lista da FinLanAlteracaoConsumer** | | | | | | |
| FinLanContAlteracaoConsumer | IdLanCont | int | Identificador do lançamento contábil. | Sim |  | Os campos só serão obrigatórios se o objeto for preenchido. |
| FinLanContAlteracaoConsumer | Tipo | FinLanDebitoCreditoEnum | Tipo do lançamento (débito ou crédito). | Sim |  | 0 - WCF 1 - Débito 2 - Crédito |
| FinLanContAlteracaoConsumer | Valor | decimal | Valor do lançamento. | Sim |  |  |
| FinLanContAlteracaoConsumer | CodFilial | int | Código da filial. | Sim |  |  |
| FinLanContAlteracaoConsumer | CodCCusto | string | Código do centro de custo. | Não | 25 |  |
| FinLanContAlteracaoConsumer | ComplHistorico | string | Complemento de histórico. | Não | 250 |  |
| FinLanContAlteracaoConsumer | CodColConta | int | Coligada da conta contábil. | Sim |  |  |
| FinLanContAlteracaoConsumer | CodConta | string | Código da conta contábil. | Sim |  |  |
| FinLanRatCCuAlteracaoConsumer | IdRatCCU | int | Identificador do centro de custo. | Sim |  | Os campos só serão obrigatórios se o objeto for preenchido. |
| FinLanRatCCuAlteracaoConsumer | CodCCusto | string | Código do centro de custo. | Sim | 25 |  |
| FinLanRatCCuAlteracaoConsumer | Valor | decimal | Valor associado ao centro de custo. | Sim |  |  |
| FinLanRatCCuAlteracaoConsumer | Historico | string | Histórico associado ao rateio por centro de custo. | Não | 255 |  |
| FinLanRatCCuAlteracaoConsumer | CodColNatFinanceira | int? | Coligada da natureza financeira. | Não |  |  |
| FinLanRatCCuAlteracaoConsumer | CodNatFinanceira | string | Código da natureza financeira. | Não | 40 |  |
| FinLanRatCCuAlteracaoConsumer | Percentual | decimal | Percentual do valor total do lançamento atribuído ao centro de custo. | Não |  |  |
| FinLanRatCCuAlteracaoConsumer | IdLan | int | Referência do lançamento financeiro associado ao rateio por centro de custo. | Sim |  |  |
| FinLanRatCCuAlteracaoConsumer | CodColigada | int | Coligada do lançamento financeiro associado ao rateio por centro de custo. | Sim |  |  |
| FinLanRatDepAlteracaoConsumer | CodFilial | int | Código da filial. | Sim |  |  |
| FinLanRatDepAlteracaoConsumer | CodDepartamento | string | Código do departamento. | Sim | 25 |  |
| FinLanRatDepAlteracaoConsumer | Valor | decimal | Valor atribuído ao departamento no rateio. | Sim |  |  |
| FinLanRatDepAlteracaoConsumer | IdLan | int | Referência do lançamento financeiro associado ao rateio por departamento. | Sim |  |  |
| FinLanRatDepAlteracaoConsumer | CodColigada | int | Coligada do lançamento financeiro associado ao rateio por departamento. | Sim |  |  |

3Extrato de caixa - Inclusãofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

A subscrição que deverá ser utilizada: **FinXCXIncDataCommand**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| FinXCXInclusaoConsumer | CodColigada | int | Código da coligada | Sim |  | Código da coligada da movimentação bancária |
| FinXCXInclusaoConsumer | IdXCX | int | Identificador do extrato | Sim |  | Fixo: -1 |
| FinXCXInclusaoConsumer | CodFilial | int | Código da filial | Sim |  | Código da Filial da movimentação bancária |
| FinXCXInclusaoConsumer | NumeroDocumento | string | Número do documento | Sim |  | Número de identificação da movimentação bancária |
| FinXCXInclusaoConsumer | Tipo | int | Tipo de extrato | Sim |  | 1 - Saída monetária da conta/caixa origem da movimentação 2 - Entrada monetária da conta/caixa origem da movimentação 3 - Transferência monetária entre contas. |
| FinXCXInclusaoConsumer | Contabil | int | Tipo Contábil | Não |  | 0 - Não Contábil 1 - Contábil 3 - A Contabilizar |
| FinXCXInclusaoConsumer | CodColCxa | int | Coligada da Conta/Caixa | Sim |  | Informar o código da coligada responsável pela conta/caixa origem da movimentação.  (Quando este campo for diferente do atributo CodColigada caracteriza Mútuo) |
| FinXCXInclusaoConsumer | CodCxa | string | Código da conta caixa | Sim | 10 | Informar o código da conta/caixa origem da movimentação. |
| FinXCXInclusaoConsumer | Data | DateTime | Data do extrato | Sim |  | Data da movimentação |
| FinXCXInclusaoConsumer | Valor | decimal | Valor do extrato | Sim |  |  |
| FinXCXInclusaoConsumer | UsuarioCriacao | string | Usuário de criação | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| FinXCXInclusaoConsumer | Historico | string | Histórico |  | 255 |  |
| FinXCXInclusaoConsumer | CodColNatFinanceira | int | Coligada da natureza orçamentária financeira | Não |  | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da coligada responsável pela natureza orçamentária financeira |
| FinXCXInclusaoConsumer | CodNatFinanceira | string | Código da natureza orçamentária financeira | Não | 40 | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da natureza orçamentária financeira |
| FinXCXInclusaoConsumer | CodCCusto | string | Código de centro de custo | Não | 25 | Pode ser obrigatório a depender da parametrização do cliente. |
| FinXCXInclusaoConsumer | CodColCxaTransf | int | Código da coligada da conta caixa - Transf. | Não |  | Se tipo = 3, obrigatório informar dados da transferência  Código da coligada da conta/caixa destino da transferência. |
| FinXCXInclusaoConsumer | CodFilialTransf | int | Código da filial de transferência | Não |  | Se tipo = 3, obrigatório informar dados da transferência  Código da filial da conta/caixa destino da transferência. |
| FinXCXInclusaoConsumer | CodCxaTransf | string | Código da conta caixa - Transf. | Não | 20 | Se tipo = 3, obrigatório informar dados da transferência  Código da conta/caixa destino da transferência. |

4Extrato de caixa - Alteraçãofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

A subscrição que deverá ser utilizada: **FinXCXAltDataCommand**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| FinXCXAlteracaoConsumer | CodColigada | int | Código da coligada | Sim |  | Código da coligada da movimentação bancária |
| FinXCXAlteracaoConsumer | IdXCX | int | Id do extrato | Sim |  | Identificador da movimentação bancária que será alterada. |
| FinXCXAlteracaoConsumer | UsuarioAlteracao | string | Usuário que fez a alteração | Sim | 20 |  |
| FinXCXAlteracaoConsumer | Status | int | Status do extrato | Não |  | Para cancelar o extrato Fixo: 2 - Cancelado |

5Extrato de caixa - Cancelamentofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

A subscrição que deverá ser utilizada: **FinXCXCancelDataCommand**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| FinXCXAlteracaoConsumer | CodColigada | int | Código da coligada | Sim |  | Código da coligada da movimentação bancária |
| FinXCXAlteracaoConsumer | IdXCX | int | Id do extrato | Sim |  | Identificador da movimentação bancária que será cancelado. |
| FinXCXAlteracaoConsumer | Usuario | string | Usuário que fez a alteração | Sim | 20 |  |
| FinXCXAlteracaoConsumer | DataCancelamento | Date | Data de cancelameno | Sim |  |  |

6Lanc. Contábil - Inclusãofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

A subscrição que deverá ser utilizada: **CtbLanIncDataCommand**

Código do lote

O cliente deverá informar a Gesplan qual o código do lote que eles vão utilizar para a inclusão do lançamento contábil e qual o lote para o estorno do lançamento contábil.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| CtbAccountingEntriesEntity | IntegraAplicacao | string | Identificador da aplicação/processo que está originando a contabilidade; deve ser diferente para sistemas com múltiplos processos de contabilização. | Sim |  | Fixo = C |
| CtbAccountingEntriesEntity | CodColigada | int | Código da coligada. | Sim |  | Código da coligada do lançamento contábil |
| CtbAccountingEntriesEntity | IdLancamento | int | Id. Lançamento contábil; será gerado pelo serviço de inclusão de lançamento. | Sim |  | Fixo = -1 |
| CtbAccountingEntriesEntity | CodLote | int | Código do lote em que o lançamento será incluído. | Sim |  | Código previamente cadastrado pelo cliente dentro do TOTVS Gestão Contábil. |
| CtbAccountingEntriesEntity | Descricao | string | Descrição do lançamento contábil. | Sim | 100 |  |
| CtbAccountingEntriesEntity | CodUsuario | string | Usuário que está incluindo o lançamento contábil. | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| CtbAccountingEntriesEntity | Partidas | ObjectList<CtbAccountEntryEntity> | Lista com as partidas do lançamento. | Sim |  | Não é possível inserir lançamento sem partidas |
| **Classes de lista da CtbLancamentoInclusaoConsumer** | | | | | | |
| CtbAccountEntryEntity | CodColigada | int | Código da coligada. | Sim |  | Código da coligada do lançamento contábil |
| CtbAccountEntryEntity | CodLote | int | Código do lote. | Sim |  | Código definido pelo cliente.  Obrigatoriamente tem que ser o mesmo código da classe *CtbAccountingEntriesEntity* |
| CtbAccountEntryEntity | IdLancamento | int | Id. do lançamento. O id. do lançamento será gerado pelo serviço. | Sim |  | Fixo = -1 |
| CtbAccountEntryEntity | IdPartida | int | Id. da partida. O id. da partida será gerado pelo serviço. | Sim |  | Fixo = -1 |
| CtbAccountEntryEntity | CodFilial | int | Código da filial. | Sim |  | Código da Filial do lançamento contábil |
| CtbAccountEntryEntity | CodDepartamento | string | Código do departamento. | Não | 25 | Pode ser obrigatório a depender da parametrização TOTVS Gestão Contábil. |
| CtbAccountEntryEntity | CodCCusto | string | Código do centro de custo. | Não | 25 | Pode ser obrigatório a depender da parametrização TOTVS Gestão Contábil. |
| CtbAccountEntryEntity | Documento | string | Número do documento. | Sim | 20 |  |
| CtbAccountEntryEntity | Data | DateTime | Data da contabilização. | Sim |  | A data deve ser a mesma para todas as partidas de um lançamento. |
| CtbAccountEntryEntity | CodColDebito | int | Coligada da conta a débito. | Sim |  | Código da coligada da conta contábil de débito |
| CtbAccountEntryEntity | Debito | string | Conta débito. | Sim | 40 | Ao inserir a conta débito, é necessário enviar a coligada da conta Débito. É necessário que pelo menos uma conta seja enviada, débito, crédito ou ambas. |
| CtbAccountEntryEntity | CodColCredito | int | Código da coligada da conta crédito. | Sim |  | Código da coligada da conta contábil de crédito |
| CtbAccountEntryEntity | Credito | string | Conta a crédito. | Sim | 40 | Ao inserir a conta crédito, é necessário enviar a coligada da conta Crédito. É necessário que pelo menos uma conta seja enviada, débito, crédito ou ambas. |
| CtbAccountEntryEntity | Valor | decimal | Valor da partida. | Sim |  |  |
| CtbAccountEntryEntity | Usuario | string | Usuário responsável pela inclusão da partida. | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| CtbAccountEntryEntity | UsuarioAlter | string | Usuário responsável pela alteração da partida. | Não | 20 | Obrigatório quando for uma alteração. |
| CtbAccountEntryEntity | CodHistp | string | Código do histórico. | Não |  | Pode ser obrigatório a depender do parâmetro.  Código previamente cadastrado pelo cliente dentro do TOTVS Gestão Contábil. |
| CtbAccountEntryEntity | Complemento | string | Descrição do complemento de histórico. | Não |  | Pode ser obrigatório a depender do parâmetro.  Texto Livre |
| CtbMultiCurrencyEntryEntity | CodColigada | int | Código da coligada. | Sim |  | Usado quando o cliente utiliza multimoedas Grupo obrigatório quando a conversão multimoedas for do tipo Fixa. |
| CtbMultiCurrencyEntryEntity | IdPartida | int | Id. da partida associada à moeda e valor. | Sim |  | Fixo = -1 |
| CtbMultiCurrencyEntryEntity | Moeda | string | Código ou identificador da moeda. | Sim | 10 | Código da moeda previamente cadastrada no TOTVS Gestão Financeira. |
| CtbMultiCurrencyEntryEntity | Valor | decimal | Valor associado à moeda especificada. | Sim |  |  |

7Lanc. Contábil - Alteraçãofade

Modelo de dados para à alteração de um lançamento contábil no RM.

A subscrição que deverá ser utilizada: **CtbLanAltDataCommand**

Código do lote

O cliente deverá informar a Gesplan qual o código do lote que eles vão utilizar para a inclusão do lançamento contábil e qual o lote para o estorno do lançamento contábil.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Classe** | **Nome do Atributo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| CtbAccountingEntriesEntity | IntegraAplicacao | string | Identificador da aplicação/processo que está originando a contabilidade; deve ser diferente para sistemas com múltiplos processos de contabilização. | Sim |  |  |
| CtbAccountingEntriesEntity | CodColigada | int | Código da coligada. | Sim |  | Se não enviar esse campo, o default é 0, nesse caso daria erro de período contábil |
| CtbAccountingEntriesEntity | IdLancamento | int | Id. Lançamento contábil; será gerado pelo serviço de inclusão de lançamento. | Sim |  |  |
| CtbAccountingEntriesEntity | CodLote | int | Código do lote em que o lançamento será incluído. | Sim |  | Importante enviar para lotes de origem contábil ou diretamente ao lote zero |
| CtbAccountingEntriesEntity | Descricao | string | Descrição do lançamento contábil. | Sim | 100 |  |
| CtbAccountingEntriesEntity | CodUsuario | string | Usuário que está incluindo o lançamento contábil. | Sim | 20 |  |
| CtbAccountingEntriesEntity | Partidas | ObjectList<CtbAccountEntryEntity> | Lista com as partidas do lançamento. | Sim |  | Não é possível inserir lançamento sem partidas |

Abaixo temos um modelo do Json de envio para cada uma das subscrições.

cenario1Lanc. Financeiro - Inclusãofade

Modelo de dados para à inclusão de um lançamento financeiro no RM.

{  
    "header": {  
        "type": "FinLanIncDataCommand",  
        "tenantId": "",  
        "externalSystem": "4321"  
    },  
    "data":[  
        {        
        "CodColigada": 1,  
        "IdLan": -1,  
        "CodigoExterno": "GESP001",  
        "UsuarioInclusao": "mestre",  
        "CodUsuario": "mestre",  
        "PagRec": "2",  
        "CodFilial": 1,  
        "CodColCfo": 0,  
        "CodCfo": "00111075",  
        "CodTdo": "01",  
        "NumeroDocumento": "0000020013",  
        "DataEmissao": "2024-05-27",  
        "DataVencimento": "2024-06-22",  
        "ValorOriginal": 10.00,  
        "Historico": "Teste Behavior 28\_05",  
        "SerieDocumento": "@@@",  
        "CodCCusto": "",  
        "Moeda": "R$",  
        "ValorJuros": 1.00,  
        "ValorDesconto": 1.00,  
        "ValorMulta": 1.00,  
        "RateioCCusto":  
        [  
            {  
            "CodCCusto": "01.1",  
            "Valor": 5.00  
            },  
            {  
            "CodCCusto": "01.2",  
            "Valor": 5.00  
            }  
        ]  
        },  
        {        
        "CodColigada": 1,  
        "IdLan": -1,  
        "CodigoExterno": "GESP002",  
        "UsuarioInclusao": "mestre",  
        "CodUsuario": "mestre",  
        "PagRec": "2",  
        "CodFilial": 1,  
        "CodColCfo": 0,  
        "CodCfo": "00111075",  
        "CodTdo": "01",  
        "NumeroDocumento": "0000020014",  
        "DataEmissao": "2024-05-27",  
        "DataVencimento": "2024-06-22",  
        "ValorOriginal": 10.00,  
        "Historico": "Teste Behavior segundo da lista",  
        "SerieDocumento": "@@@",  
        "CodCCusto": "",  
        "Moeda": "R$",  
        "ValorJuros": 1.00,  
        "ValorDesconto": 1.00,  
        "ValorMulta": 1.00,  
        "RateioCCusto":  
        [  
            {  
            "CodCCusto": "01.1",  
            "Valor": 5.00  
            },  
            {  
            "CodCCusto": "01.2",  
            "Valor": 5.00  
            }  
        ]  
        }  
    ]  
}

2Lanc. Financeiro - Alteraçãofade

Modelo de dados para à alteração de um lançamento financeiro no RM.

{  
    "header": {  
        "type": "FinLanAltDataCommand",  
        "tenantId": "",  
        "externalSystem": "4321"  
    },  
    "data": {  
        "CodColigada": 1,  
        "CodFilial": 1,  
        "IdLan": 6985,  
        "CodigoExterno": "GESP002",  
        "UsuarioAlteracao": "mestre",  
        "DataSistema": "2024-02-27",  
        "ValorOriginal": 12.00,  
        "Historico": "Teste Consumer de alteração"  
    }  
}

3Extrato de caixa - Inclusãofade

Modelo de dados para à inclusão de um extrato de caixa no RM.

{  
    "header": {  
        "type": "FinXCXIncDataCommand",  
        "tenantId": "",  
        "externalSystem": "4321"  
    },  
    "data":[  
        {  
            "CodColigada": 1,  
            "IdXCX": -1,  
            "CodigoExterno": "GESP001",  
            "CodFilial": 1,  
            "NumeroDocumento": "0000009042",  
            "Tipo": "2",  
            "CodColCxa": 0,  
            "CodCxa": "0006",  
            "Data": "2024-05-28",  
            "Valor": 29,  
            "UsuarioCriacao": "mestre"  
        },  
        {  
            "CodColigada": 1,  
            "IdXCX": -1,  
            "CodigoExterno": "GESP002",  
            "CodFilial": 1,  
            "NumeroDocumento": "0000009043",  
            "Tipo": "2",  
            "CodColCxa": 0,  
            "CodCxa": "0006",  
            "Data": "2024-05-28",  
            "Valor": 29,  
            "UsuarioCriacao": "mestre"  
        }  
    ]  
}

4Extrato de caixa - Alteraçãofade

Modelo de dados para à alteração de um extrato de caixa  no RM.

{  
    "header": {  
        "type": "FinXCXAltDataCommand",  
        "tenantId": "",  
        "externalSystem": "4321"  
    },  
    "data":{  
      "CodColigada": 1,  
      "IdXCX": 1860,  
      "CodigoExterno": "GESP001",  
      "CodFilial": 1,  
      "Historico": "Teste Consumer de alteração",  
      "UsuarioAlteracao": "mestre"  
  }  
}

5Extrato de caixa - Cancelamentofade

Modelo de dados para o cancelamento de um extrato de caixa  no RM.

{  
    "header": {  
        "type": "FinXCXCancelDataCommand",  
        "tenantId": "b99",  
        "externalSystem": "4321"  
    },  
    "data": [{  
            "CodColigada": 1,  
            "IdXCX": 1943,  
            "CodigoExterno": "GESP001",  
            "DataCancelamento": "2024-08-28",  
            "Usuario": "mestre"  
        }  
    ]  
}

6Lanc. Contábil - Inclusãofade

Modelo de dados para à inclusão de um lançamento contábil no RM.

{  
    "header": {  
        "type": "CtbLanIncDataCommand",  
        "tenantId": "dd6b2ceb-2393-4e6f-a5b4-1487d5330c4e",  
        "externalSystem": "4321"  
    },  
    "data": [{  
        "IntegraAplicacao": "C",  
        "CodColigada": 1,  
        "IdLancamento": -1,  
        "CodigoExterno": "GESP\_EXT001",  
        "CodLote": 99,  
        "Descricao": "Teste Consumer de inclusão 31",  
        "CodUsuario": "mestre",  
        "Partidas":[  
            {  
                "CodColigada": 1,  
                "CodLote": 99,  
                "CodigoExterno": "GESP001",  
                "IdLancamento": -1,  
                "IdPartida": -1,  
                "CodFilial": 1,  
                "Documento": "0000011036",  
                "Data": "2024-05-24",  
                "Valor": 10.00,  
                "Usuario": "Mestre",  
                "CodColDebito": 1,  
                "Debito": "1.1.1.1.001",  
                "CodColCredito": 1,  
                "Credito": "2.1.1.1.002"  
            }  
        ]  
    },  
    {  
        "IntegraAplicacao": "C",  
        "CodColigada": 1,  
        "IdLancamento": -1,  
        "CodigoExterno": "GESP\_EXT002",  
        "CodLote": 99,  
        "Descricao": "Teste Lista Consumer de inclusão 2",  
        "CodUsuario": "mestre",  
        "Partidas":[  
            {  
                "CodColigada": 1,  
                "CodLote": 99,  
                "CodigoExterno": "GESP002",  
                "IdLancamento": -1,  
                "IdPartida": -1,  
                "CodFilial": 1,  
                "Documento": "0000012001",  
                "Data": "2024-05-24",  
                "Valor": 11.00,  
                "Usuario": "Mestre",  
                "CodColDebito": 1,  
                "Debito": "1.1.1.1.001",  
                "CodColCredito": 1,  
                "Credito": "2.1.1.1.002"  
            }  
        ]  
    }]  
}

7Lanc. Contábil - Alteraçãofade

Modelo de dados para à alteração de um lançamento contábil no RM.

{  
    "header": {  
        "type": "CtbLanAltDataCommand",  
        "tenantId": "b991502e-6faa-4e3a-aaf4-967c4fe2a196",  
        "externalSystem": "4321"  
    },  
    "data": {  
        "IntegraAplicacao": "Fin",  
        "CodColigada": 1,  
        "IdLancamento": 2751,  
        "IntegraChave": "GESP\_EXT002",  
        "CodLote": 99,  
        "Descricao": "Teste Consumer de alteração 5",  
        "CodUsuario": "mestre",  
        "Partidas":[  
            {  
                "CodColigada": 1,  
                "CodLote": 99,  
                "IntegraChave": "GESP002",  
                "IdLancamento": 2751,  
                "IdPartida": 11691,  
                "CodFilial": 1,  
                "Valor": 11.00,  
                "Usuario": "Mestre",  
                "UsuarioAlter": "Mestre",  
                "CodColDebito": 1,  
                "Debito": "3.1.1.1.001",  
                "RateioDebito": [  
                    {  
                        "CodColigada": 1,  
                        "CodGerencial": "5.03",  
                        "CodColGerencial": 1,  
                        "VlrDebito": 11,  
                        "IdPartida": 11691  
                    }  
                ],  
                "CodColCredito": 1,  
                "Credito": "4.1.1.1.008",  
                "RateioCredito": [  
                    {  
                        "CodColigada": 1,  
                        "CodGerencial": "5.03",  
                        "CodColGerencial": 1,  
                        "VlrCredito": 11,  
                        "IdPartida": 11691  
                    }  
                ]  
            }  
        ]  
    }  
}

Abaixo temos um modelo do Json de retorno.

cenario1Lançamento Financeirofade

{  
    "specversion": "1.0",  
    "tenantId": "",  
    "time": "2024-05-28 11:23:57",  
    "type": "FinLanIncDataCommandResp",  
    "externalSystem": "4321",  
    "Error": null,  
    "data": [{  
            "BranchId": "1",  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": "GESP001",  
            "Key": "1;7024"  
        }, {  
            "BranchId": "1",  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": "GESP002",  
            "Key": "1;7025"  
        }  
    ]  
}

2Extrato Financeirofade

{  
    "specversion": "1.0",  
    "tenantId": "",  
    "time": "2024-05-28 13:44:17",  
    "type": "FinXCXIncDataCommandResp",  
    "externalSystem": "4321",  
    "Error": null,  
    "data": [{  
            "BranchId": null,  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": "GESP001",  
            "Key": "1;1889"  
        }, {  
            "BranchId": null,  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": "GESP002",  
            "Key": "1;1890"  
        }  
    ]  
}

3Lançamento Contábilfade

{  
    "specversion": "1.0",  
    "tenantId": "",  
    "time": "2024-05-27 08:49:47",  
    "type": "CtbLanIncDataCommandResp",  
    "externalSystem": "4321",  
    "Error": null,  
    "data": [{  
            "BranchId": null,  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": null,  
            "Key": "1;2829",  
            "Partidas": [{  
                    "BranchId": "1",  
                    "CompanyId": "1",  
                    "Error": null,  
                    "ExternalKey": "GESP001",  
                    "Key": "1;1;11911"  
                }  
            ]  
        }, {  
            "BranchId": null,  
            "CompanyId": "1",  
            "Error": null,  
            "ExternalKey": null,  
            "Key": "1;2830",  
            "Partidas": [{  
                    "BranchId": "1",  
                    "CompanyId": "1",  
                    "Error": null,  
                    "ExternalKey": "GESP002",  
                    "Key": "1;1;11912"  
                }  
            ]  
        }  
    ]  
}
