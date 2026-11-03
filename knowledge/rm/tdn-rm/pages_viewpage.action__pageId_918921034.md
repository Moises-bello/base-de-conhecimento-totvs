---
content_hash: aa11ea653821c19ead9c0f22b9c6b0dc5e3c70f0206fba14862abfddb2e8c7e0
fetched_at: '2026-06-29T00:12:07.033501+00:00'
page_id: '918921034'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan - Extrato de caixa (Envio da Gesplan para o RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918921034
version: 30
---

Conteúdo:

# 1. Dicionário

| RM | Gesplan |
| --- | --- |
| [Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=275587649) | Unidade Operacional |
| Filial | Divisão |
| [Conta / Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) | Banco | Agência | Conta |
| [Extrato de Caixa](https://tdn.totvs.com/display/LRM/FIN+-+Extratos+de+Caixa) | Eventos que afetam conta /corrente |

# 2. Definições

Para garantir o sucesso da integração e evitar a quebra das regras de negócios, foram necessárias algumas definições e ajustes prévios entre o ERP e a Gesplan.

**Conta/Caixa:** O cliente deve informar o código da [conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837) que representa cada conta/corrente que será movimentada na integração. Nos casos onde a conta/caixa é global, a identificação da coligada da conta/caixa deve ser como "0" zero (***tag: CodColCxa***). Quando a conta/caixa não é global,  a identificação da coligada da conta/caixa passa a respeitar a mesma coligada do extrato. (***tag: CodColigada***)

**Identificação da origem:** Os extratos de caixa gerados pela Gesplan, serão classificados como origem do próprio módulo financeiro.

**Moeda**: A Gesplan sempre vai enviar as movimentações bancárias na moeda da empresa, quando houver uso de outras moedas, a Gesplan vai realizar a conversão e enviar o valor já convertido.

**Natureza Orçamentária / Financeira**: Cliente deve informar se usa o próprio cadastro de [natureza orçamentária financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=423937949), ou uma [tabela opcional](https://tdn.totvs.com/display/LRM/FIN+-+Tabelas+Opcionais) para a classificação do título.

**Tabelas Opcionais**: As tabelas opcionais podem ser utilizadas de maneira customizada, pois cada cliente pode definir o nome de cada uma das 5 tabelas disponíveis, nos [parâmetros](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar).

**Evento Contábil**: O cliente deve informar o código do evento a ser utilizado em cada evento da Gesplan que tenha interesse de contabilizar através do extrato de caixa.

# 3. Mapemento de Campos

Para facilitar a identificação dos campos trafegados entre as plataformas, disponibilizamos abaixo o mapeamentos dos campos:

Mapemento dos campos para INCLUSÃO de um Extrato de Caixa no RM

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome do campo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada da movimentação bancária |
| IdXCX | int | Identificador do extrato | Sim |  | Fixo: -1 |
| CodFilial | int | Código da filial | Sim |  | Código da Filial da movimentação bancária |
| NumeroDocumento | string | Número do documento | Sim |  | Número de identificação da movimentação bancária |
| NomeEmitente | string | Origem da informação | Sim |  | Fixo: Gesplan   (informação será usada para identificar extratos gerados pela gesplan, e não integrar novamente para o fluxo de caixa) |
| Tipo | int | Tipo de extrato | Sim |  | 1 - Saída monetária da conta/caixa origem da movimentação 2 - Entrada monetária da conta/caixa origem da movimentação 3 - Transferência monetária entre contas. |
| Contabil | int | Tipo Contábil | Não |  | 0 - Não Contábil 1 - Contábil 3 - A Contabilizar |
| CodEvento | short | Código do evento contábil | Não |  | Informar o código do evento contábil, caso a informação do Tipo Contábil estiver como 1 |
| CodColCxa | int | Coligada da Conta/Caixa | Sim |  | Informar o código da coligada responsável pela conta/caixa origem da movimentação.  (Quando este campo for diferente do atributo CodColigada caracteriza Mútuo) |
| CodCxa | string | Código da conta caixa | Sim | 10 | Informar o código da conta/caixa origem da movimentação. |
| Data | DateTime | Data do extrato | Sim |  | Data da movimentação |
| Valor | decimal | Valor do extrato | Sim |  |  |
| UsuarioCriacao | string | Usuário de criação | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| Historico | string | Histórico |  | 255 |  |
| Status | int | Status do extrato | Não |  | Informar 1, caso o extrato seja gerado como compensado |
| DataCompensacao | DateTime | Data de Compensacao | Não |  | Se Status = 1, informar a data da compensação |
| CodColNatFinanceira | int | Coligada da natureza orçamentária financeira | Não |  | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da coligada responsável pela natureza orçamentária financeira |
| CodNatFinanceira | string | Código da natureza orçamentária financeira | Não | 40 | Pode ser obrigatório a depender da parametrização do cliente. Informar o código da natureza orçamentária financeira |
| CodCCusto | string | Código de centro de custo | Não | 25 | Pode ser obrigatório a depender da parametrização do cliente. |
| CodColCxaTransf | int | Código da coligada da conta caixa - Transf. | Não |  | Se tipo = 3, obrigatório informar dados da transferência  Código da coligada da conta/caixa destino da transferência. |
| CodFilialTransf | int | Código da filial de transferência | Não |  | Se tipo = 3, obrigatório informar dados da transferência  Código da filial da conta/caixa destino da transferência. |
| CodCxaTransf | string | Código da conta caixa - Transf. | Não | 20 | Se tipo = 3, obrigatório informar dados da transferência  Código da conta/caixa destino da transferência. |
| CodTabOp1 | string | Código da Tabela Opcional 1 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp2 | string | Código da Tabela Opcional 2 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp3 | string | Código da Tabela Opcional 3 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp4 | string | Código da Tabela Opcional 4 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |
| CodTabOp5 | string | Código da Tabela Opcional 5 | Não |  | Pode ser obrigatório a depender da parametrização do cliente, e em cada cliente pode ter um nome diferente. |

Mapemento dos campos para CANCELAMENTO de um Extrato de Caixa no RM

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nome do campo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |  |
| CodColigada | int | Código da coligada | Sim |  | Código da coligada da movimentação bancária |  |
| IdXCX | int | Identificador do extrato | Sim |  | Identificador da movimentação bancária que será cancelada. |  |
| UsuarioAlteracao | string | Usuário que fez a alteração | Sim | 20 |  |  |
| DataCancelamento | Date | Data de Cancelamento | Sim |  |  |  |

# 4. Exemplo de utilização

Modelo de mensagens

xmlJson - Inclusão Extrato de CaixatruexmlJson - Retorno inclusão de Extrato de CaixatruexmlJson - Cancelamento de Extrato de CaixatrueImportante!

Os campos "externalSystem", "ExternalKey" não serão gravados no ERP, eles são somente informações de controle da Gesplan, que chegará na requisição e serão enviados na resposta do processamento, indicando sucesso ou falha da inclusão do registro.
