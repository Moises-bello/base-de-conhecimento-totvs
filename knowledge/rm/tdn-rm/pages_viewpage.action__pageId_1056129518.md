---
content_hash: 55046fd4d1d52039b45d69ca829abc0eb7726178158bb45c3f095176da119612
fetched_at: '2026-06-29T00:05:51.818550+00:00'
page_id: '1056129518'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan - Contas a Pagar (Envio da Gesplan para o RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056129518
version: 6
---

Conteúdo:

ATENÇÃO

EM CONSTRUÇÃO... ainda sem prazo de liberação para o mercado

# 1. Dicionário

| RM | Gesplan |
| --- | --- |
| [Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=275587649) | Unidade Operacional |
| Filial | Divisão |
| [Conta / Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) | Banco | Agência | Conta |
| [Lançamento](https://tdn.totvs.com/pages/viewpage.action?pageId=421388578) | Contas a Pagar |

# 2. Definições

Para garantir o sucesso da integração e evitar a quebra das regras de negócios, foram necessárias algumas definições e ajustes prévios entre o ERP e a Gesplan.

**Conta/Caixa:** O cliente deve informar o código da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) que representa cada conta/corrente que será movimentada na integração. Nos casos onde a conta/caixa é global, a identificação da coligada da conta/caixa deve ser como "0" zero (***tag: CodColCxa***). Quando a conta/caixa não é global,  a identificação da coligada da conta/caixa passa a respeitar a mesma coligada do extrato. (***tag: CodColigada***)

**Identificação da origem:** Os lançamentos gerados pela Gesplan, serão classificados como origem do próprio módulo financeiro.

**Moeda**: A Gesplan sempre vai enviar as movimentações bancárias na moeda da empresa, quando houver uso de outras moedas, a Gesplan vai realizar a conversão e enviar o valor já convertido.

**Tabelas Opcionais**: As tabelas opcionais podem ser utilizadas de maneira customizada, pois cada cliente pode definir o nome de cada uma das 5 tabelas disponíveis, nos [parâmetros](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar).

**Evento Contábil**: O cliente deve informar o código do evento a ser utilizado em cada evento da Gesplan que tenha interesse de contabilizar através do lançamento.

**Tipo de documento**: O cliente deve informar o código do [tipo de documento](https://tdn.totvs.com/pages/viewpage.action?pageId=421388695) a ser utilizado em cada lançamento da Gesplan.

# 3. Mapeamento de Campos

Para facilitar a identificação dos campos trafegados entre as plataformas, disponibilizamos abaixo o mapeamentos dos campos:

Mapemento dos campos para INCLUSÃO de um Contas a Pagar no RM

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome do campo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| **Lançamento Financeiro** | | | | | |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada do lançamento |
| IdLan | int | Identificador do lançamento | Sim |  | Fixo: -1 |
| CodAplicacao | string | Identificação da aplicação | Sim |  | Fixo: " F " |
| PagRec | int | tipo do lançamento | Sim |  | Fixo = 2 (A Pagar) |
| CodFilial | int | Código da filial | Sim |  | Código da Filial do lançamento |
| NumeroDocumento | string | Número do documento | Sim |  | Número de identificação do lançamento |
| CodColCfo | int | Código da coligada do fornecedor | Sim |  | Código da Coligada do fornecedor Se o fornecedor for global, o código é zero "0" |
| CodCfo | string | Código do fornecedor | Sim |  | Código do fornecedor |
| CodTdo | string | Código do tipo de documento | Sim |  | Cadastro previamente realizado pelo cliente para classificar o lançamento |
| TipoContabil | int | Tipo Contábil | Não |  | 0 - Não Contábil 1 - Contábil 2 - Baixa Contábil |
| CodEvento | short | Código do evento contábil | Não |  | Informar o código do evento contábil, caso a informação do Tipo Contábil estiver como 1 ou se não tiver evento informado na tabela default pra evento |
| CodColCxa | int | Coligada da Conta/Caixa | Sim |  | Informar o código da coligada responsável pela conta/caixa do lançamento |
| CodCxa | string | Código da conta caixa | Sim | 10 | Informar o código da conta/caixa do lançamento |
| DataEmissao | DateTime | Data de emissão | Sim |  | Data de emissão do lançamento |
| DataVencimento | DateTime | Data de vencimento | Sim |  | Data de vencimento do lançamento |
| DataPrevBaixa | DateTime | Data de previsão de baixa | Sim |  | Data de previsão de baixa do lançamento |
| ValorOriginal | decimal | Valor original | Sim |  | Valor original do lançamento |
| UsuarioInclusao | string | Usuário de inclusão | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| Historico | string | Histórico | Não | 255 |  |
| CodColNatFinanceira | int | Coligada da natureza orçamentária financeira | Não |  | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da coligada responsável pela natureza orçamentária financeira |
| CodNatFinanceira | string | Código da natureza orçamentária financeira | Não | 40 | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da natureza orçamentária financeira |
| CodCCusto | string | Código de centro de custo | Não | 25 | Pode ser obrigatório a depender da parametrização do cliente. |
| CodDepartamento | string | Código do departamento. | Não |  | Pode ser obrigatório a depender da parametrização do cliente. |
| ValorOp1 | decimal | Valor opcional 1 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp2 | decimal | Valor opcional 2 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp3 | decimal | Valor opcional 3 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp4 | decimal | Valor opcional 4 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp5 | decimal | Valor opcional 5 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp6 | decimal | Valor opcional 6 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp7 | decimal | Valor opcional 7 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp8 | decimal | Valor opcional 8 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| CodTabOp1 | string | Código da Tabela Opcional 1 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp2 | string | Código da Tabela Opcional 2 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp3 | string | Código da Tabela Opcional 3 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp4 | string | Código da Tabela Opcional 4 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp5 | string | Código da Tabela Opcional 5 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| **Rateio por centro de custo / natureza financeira** | | | | | |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada do lançamento |
| IdLan | int | Identificador do lançamento | Sim |  | Fixo: -1 |
| CodCCusto | string | Código de centro de custo | Sim |  |  |
| Valor | decimal | Valor associado ao centro de custo. | Sim |  |  |
| CodColNatFinanceira | int | Coligada da natureza orçamentária financeira | Não |  | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da coligada responsável pela natureza orçamentária financeira |
| CodNatFinanceira | string | Código da natureza orçamentária financeira | Não | 40 | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da natureza orçamentária financeira |
| Historico | string | Histórico | Não | 255 |  |
| Idprj | int | Identificador do projeto associado ao rateio por centro de custo. | Não |  |  |
| Idtrf | int | Identificador da tarefa associada ao rateio por centro de custo. | Não |  |  |
| **Rateio por departamento** | | | | | |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada do lançamento |
| IdLan | int | Identificador do lançamento | Sim |  | Fixo: -1 |
| CodFilial | int | Código da filial | Sim |  |  |
| CodDepartamento | string | Código do departamento. | Sim |  |  |
| Valor | decimal | Valor associado ao departamento | Sim |  |  |

Mapemento dos campos para ALTERAÇÃO de um Contas a Pagar no RM

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome do campo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada do lançamento |
| IdLan | int | Identificador do lançamento | Sim |  | Identificador do lançamento |
| CodColCxa | int | Coligada da Conta/Caixa | Sim |  | Informar o código da coligada responsável pela conta/caixa do lançamento |
| CodCxa | string | Código da conta caixa | Sim | 10 | Informar o código da conta/caixa do lançamento |
| DataVencimento | DateTime | Data de vencimento | Sim |  | Data de vencimento do lançamento |
| DataPrevBaixa | DateTime | Data de previsão de baixa | Sim |  | Data de previsão de baixa do lançamento |
| ValorOriginal | decimal | Valor original | Sim |  | Valor original do lançamento |
| Historico | string | Histórico | Não | 255 |  |
| CodColNatFinanceira | int | Coligada da natureza orçamentária financeira | Não |  | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da coligada responsável pela natureza orçamentária financeira |
| CodNatFinanceira | string | Código da natureza orçamentária financeira | Não | 40 | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da natureza orçamentária financeira |
| CodCCusto | string | Código de centro de custo | Não | 25 | Pode ser obrigatório a depender da parametrização do cliente. |
| ValorOp1 | decimal | Valor opcional 1 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp2 | decimal | Valor opcional 2 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp3 | decimal | Valor opcional 3 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp4 | decimal | Valor opcional 4 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp5 | decimal | Valor opcional 5 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp6 | decimal | Valor opcional 6 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp7 | decimal | Valor opcional 7 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| ValorOp8 | decimal | Valor opcional 8 | Não |  | Valores opcionais, em cada cliente pode ter um nome diferente. |
| CodTabOp1 | string | Código da Tabela Opcional 1 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp2 | string | Código da Tabela Opcional 2 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp3 | string | Código da Tabela Opcional 3 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp4 | string | Código da Tabela Opcional 4 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp5 | string | Código da Tabela Opcional 5 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |

Importante!

Os campos "externalSystem", "ExternalKey" não serão gravados no ERP, eles são somente informações de controle da Gesplan, que chegará na requisição e serão enviados na resposta do processamento, indicando sucesso ou falha da inclusão do registro.
