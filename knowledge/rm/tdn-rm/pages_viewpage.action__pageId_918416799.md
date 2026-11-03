---
content_hash: 395ef4414679b4363bc776ac2fef59cd56b42e3f3af47357c4aa1817988162c8
fetched_at: '2026-06-29T00:12:06.980977+00:00'
page_id: '918416799'
product: rm
source: tdn-rm
title: Linha RM - Integração Gesplan - Lançamentos Contábeis (Envio da Gesplan para
  o RM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918416799
version: 26
---

Conteúdo:

**4**

# 1. Dicionário

| RM | Gesplan |
| --- | --- |
| [Coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=275587649) | Unidade Operacional |
| Filial | Divisão |

# 2. Definições

Para garantir o sucesso da integração e evitar a quebra das regras de negócios, foram necessárias algumas definições e ajustes prévios entre o ERP e a Gesplan.

**Lote**: Deverá existir previamente um [lote](https://tdn.totvs.com/pages/viewpage.action?pageId=423938593) para controle dos lançamentos contábeis gerados pela Gesplan. (***tag:*** ***CodLot**e***)

**Identificação da origem**: Os lançamentos contábeis gerados pela Gesplan, serão classificados como origem do próprio módulo contábil. (***tag:*** ***IntegraAplicacao = C***)

**Histórico Padrão**: A Gesplan não tem o conceito de [histórico padrão](https://tdn.totvs.com/pages/viewpage.action?pageId=423938455), nos casos em que este campo é obrigatório no RM, deve ser definido quais códigos serão utilizados na integração. Além disse esse campo pode ser obrigatório a depender da parametrização de cada cliente. (***tag:*** ***CodHistp***)

**Usuário:** Deverá ser definido pelo cliente um usuário que será utilizado na integração (***tag: CodUsuario***). Este usuário deverá ter permissão no módulo contábil e estar com [acesso liberado](https://tdn.totvs.com/pages/viewpage.action?pageId=624765998) para incluir, alterar ou excluir lançamentos contábeis. 

**Plano de Contas**: O [plano de contas](https://tdn.totvs.com/pages/viewpage.action?pageId=423938354) pode ser compartilhado com todas as coligadas, sendo classificado como global. Nesse caso a identificação da coligadas das contas contábeis deve ser como "0" zero. (***tags: CodColDebito e CodColCredito***). Quando não é global, a identificação da coligadas das contas passa a respeitar a mesma coligada do lançamento contábil (***tag: CodColigada***)

**Rateio Gerencial**: Se o RM estiver parametrizado para usar rateio gerencial, obrigatoriamente precisa definir a distribuição gerancial nas [contas contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=423938354), porque a Gesplan não utiliza este conceito.

**Moeda**: A Gesplan sempre vai enviar os lançamentos contábeis na moeda da empresa, quando houver uso de outras moedas, a Gesplan vai realizar a conversão e enviar o valor já convertido.

**Estorno**: O processo de estorno realizado no Gesplan sempre irá gerar um lançamento de contra partida, não vai cancelar o lançamento contábil existente.

# 3. Mapemento de Campos

Para facilitar a identificação dos campos trafegados entre as plataformas, disponibilizamos abaixo o mapeamentos dos campos:

Modelo de dados para inclusão de lançamento contábil no RM

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome do Campo** | **Tipo** | **Descrição** | **Obrigatório** | **Tamanho** | **Observação** |
| **Lançamento Contábil** | | | | | |
| IntegraAplicacao | string | Identificador da aplicação/processo que está originando a contabilidade; deve ser diferente para sistemas com múltiplos processos de contabilização. | Sim |  | Fixo = C |
| CodColigada | int | Código da coligada. | Sim |  | Código da coligada do lançamento contábil |
| IdLancamento | int | Id. Lançamento contábil; será gerado pelo serviço de inclusão de lançamento. | Sim |  | Fixo = -1 |
| CodLote | int | Código do lote em que o lançamento será incluído. | Sim |  | Código previamente cadastrado pelo cliente dentro do TOTVS Gestão Contábil. |
| Descricao | string | Descrição do lançamento contábil. | Sim | 100 |  |
| CodUsuario | string | Usuário que está incluindo o lançamento contábil. | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| **Partidas** | | | | | |
| CodColigada | int | Código da coligada. | Sim |  | Código da coligada do lançamento contábil |
| CodLote | int | Código do lote. | Sim |  | Código definido pelo cliente.  Obrigatoriamente tem que ser o mesmo código do Lançamento Contábil |
| IdLancamento | int | Id. do lançamento. O id. do lançamento será gerado pelo serviço. | Sim |  | Fixo = -1 |
| IdPartida | int | Id. da partida. O id. da partida será gerado pelo serviço. | Sim |  | Fixo = -1 |
| CodFilial | int | Código da filial. | Sim |  | Código da Filial do lançamento contábil |
| CodDepartamento | string | Código do departamento. | Não | 25 | Pode ser obrigatório a depender da parametrização TOTVS Gestão Contábil. |
| CodCCusto | string | Código do centro de custo. | Não | 25 | Pode ser obrigatório a depender da parametrização TOTVS Gestão Contábil. |
| Documento | string | Número do documento. | Sim | 20 |  |
| Data | DateTime | Data da contabilização. | Sim |  | A data deve ser a mesma para todas as partidas de um lançamento. |
| CodColDebito | int | Coligada da conta a débito. | Sim |  | Código da coligada da conta contábil de débito, caso o plano de contas seja global deve ser informado 0 |
| Debito | string | Conta débito. | Sim | 40 | Ao inserir a conta débito, é necessário enviar a coligada da conta Débito. É necessário que pelo menos uma conta seja enviada, débito, crédito ou ambas. |
| CodColCredito | int | Código da coligada da conta crédito. | Sim |  | Código da coligada da conta contábil de crédito, caso o plano de contas seja global deve ser informado 0 |
| Credito | string | Conta a crédito. | Sim | 40 | Ao inserir a conta crédito, é necessário enviar a coligada da conta Crédito. É necessário que pelo menos uma conta seja enviada, débito, crédito ou ambas. |
| Valor | decimal | Valor da partida. | Sim |  |  |
| Usuario | string | Usuário responsável pela inclusão da partida. | Sim | 20 | Usuário usado para integração definido pelo cliente. |
| UsuarioAlter | string | Usuário responsável pela alteração da partida. | Não | 20 | Obrigatório quando for uma alteração. |
| CodHistp | string | Código do histórico padrão. | Não |  | Pode ser obrigatório a depender do parâmetro.  Código previamente cadastrado pelo cliente dentro do TOTVS Gestão Contábil. |
| Complemento | string | Descrição do complemento de histórico. | Não |  | Pode ser obrigatório a depender do parâmetro. Texto Livre |

# 4. Exemplo de utilização

Modelo de mensagem enviada pela Gesplan

xmlJson - Recebimento lançamentos contábeistrue

Modelo de mensagem de resposta enviado pelo RM

xmlJson - Recebimento lançamentos contábeistrueImportante!

Os campos "externalSystem", "ExternalKey" não serão gravados no ERP, eles são somente informações de controle da Gesplan, que chegará na requisição e serão enviados na resposta do processamento, indicando sucesso ou falha da inclusão do registro.
