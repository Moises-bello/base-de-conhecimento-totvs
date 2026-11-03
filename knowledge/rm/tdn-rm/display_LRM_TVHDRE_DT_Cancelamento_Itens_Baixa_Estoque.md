---
content_hash: c475241bba14fcd21409ddb9262e062280c1e0f9c8e53488f110add192598890
fetched_at: '2026-06-29T00:08:14.739725+00:00'
page_id: '244715019'
product: rm
source: tdn-rm
title: TVHDRE_DT_Cancelamento_Itens_Baixa_Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/TVHDRE_DT_Cancelamento_Itens_Baixa_Estoque
version: 125
---

# Integração Protheus SigaMNT x BackOffice RM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamentos* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV000171.* | *Integração Protheus SigaMNT x BackOffice RM* | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *Necessário realizar a atualização do SOURCECODE referente a mensagem de CANCELREQUEST (Cancelamento da baixa) e em seguida executar o CONFIGURADOR DA INTEGRAÇÃO novamente.*  *Descrito na seção ->***Procedimento para configuração - Atualização de Source Code** |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | *TVEFUT* |
| **Requisito (ISSUE):** | MATESTCNTFTOF01-370. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | *SQL Server, ORACLE* |
| **Tabelas Utilizadas:** | RM:  *TMOV, TITMMOV, TMOVRELAC, TITMMOVRELAC, HCINTEGRACAOID*  *PROTHEUS: XXF, SD3, SCP, STJ* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Implementação da rotina de cancelamento de itens em movimentações de baixa de estoque no RM, para mensagem de cancelamento enviada pelo Manutenção de Ativos (SigaMnt).

Dados do adapter de integração:

**Cancelar Solicitação:**

* **Tipo de Fluxo:** Protheus -> RM
* **Mensagem:** CancelRequest
* **Versão:** 1.000
* **Tipo do server:** ProcessServer
* **DataServer:** MovExclusaoCancelamentoMovProc
* **SourceCode:**
  + **UUID:** 76546dcc-b9af-4f89-9e73-779b2c62104c
  + **Nome:** ConCancelRequestExt

## Procedimento para Implantação

Liberado a partir da versão específica 12.1.12.100

## Procedimento para configuração - Atualização de Source Code

1. No BackOffice RM acessar Integração -> Mensagem Única -> Integrações
2. Selecionar a integração Manutenção de Ativos x BackOffice RM -> clicar em anexos -> Mapeamento de entidades.
3. Em seguida editar a TransactionId CANCELREQUEST.
4. Realize a exclusão do evento "ConCancelRequestExt" que é referente a TransactionId CANCELREQUEST. (Para que seja possível realizar a exclusão/edição/inclusão de source codes, é necessário que o campo READONLY da tabela HCINTEGRACAO esteja com o valor "F", caso contrário o sistema exibirá um erro não permitindo a operação).
5. Realize a exclusão da TransactionId CANCELREQUEST.
6. Ainda no contexto de Integração selecionar a aba Ferramentas -> Configurar.
7. Executar a configuração referente ao manutenção de ativos para que o mesmo recrie o evento "ConCancelRequestExt" atualizado e recrie o mapeamento de entidades para a CancelRequest.

## Procedimento para Utilização

       1.            No SigaMnt efetue a criação de uma OS corretiva, que possua 2 insumos previstos.

       2.            Assim que a OS estiver salva, o gatilho de integração será disparado e no BackOffice RM será criado o movimento referente a OS e o movimento referente a SA/SC com os 2 insumos cadastrados.

       3.            Fature a SA/SC para o movimento parametrizado para baixa de estoque, selecionando os 2 itens.

       4.            Assim que a baixa for criada, no SigaMnt acesse a tela -> RETORNO MOD.2 -> E filtre a OS criada anteriormente.

Os itens da OS estarão como INSUMOS FINALIZADOS (tela no canto direito).

       5.            Exclua um item para que o mesmo volte a ser um INSUMO PREVISTO. Ao salvar será disparado o gatilho de integração e no RM o item referente ao insumo excluído também deve ser removido da movimentação de baixa de estoque.

       6.           Caso todos os insumos sejam excluídos ou a OS possuir apenas um insumo, o movimento de baixa deve ser cancelado no RM.

divs
