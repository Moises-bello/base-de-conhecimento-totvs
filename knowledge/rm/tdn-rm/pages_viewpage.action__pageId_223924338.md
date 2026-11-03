---
content_hash: 1f4665de1d706a47a6c25df3220cb9adc3de51de399793218a31910d7147c780
fetched_at: '2026-06-29T00:06:22.641072+00:00'
page_id: '223924338'
product: rm
source: tdn-rm
title: DT_Melhorias_no_processo_Gerar Contrato_através_do_pedido_de_compras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223924338
version: 123
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar Contrato | CtrGeraContratoMovimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | MovMovimentoAction | | Contrato | CtrContratoAction | |
| **Cadastros Iniciais:** | Movimento de Pedido de Compas devidamente parametrizado para Gerar Contrato |
| **Parâmetro(s):** | Gerar Contrato |
| **Ponto de Entrada:** | Movimento / Processo / Gerar Contrato |
| **Chamados Relacionados** | N/A |
| **Requisito (ISSUE):** | * [PCREQ-8870](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8870 "PCREQ-8870") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER EXPRESS 2012 |
| **Tabelas Utilizadas:** | * TITMCNTMOVRELAC * TITMCNT |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.10 |
| **Versão Corrigida:** | 12.1.10 |
| **Versão Expedida:** | 12.1.10 |

## Descrição

Este documento visa detalhar as melhorias realizadas no processo Gerar Contrato a partir de um Pedido de compras. Todas as melhorias visam melhorar a usabilidade do módulo.

**Exclusão de Contrato Gerado a partir de um pedido**

Será permitida a exclusão de um contrato criado a partir de um pedido de compras que ainda não sofreu nenhum faturamento.

* O serviço de exclusão do contrato irá desfazer todas a(s) movimentações(s) de estoque e orçamento necessárias e o retorno do status do movimento para pendente.
* No caso de exclusão de itens de contrato será realizado o tratamento para não permitir que os itens vinculados a pedidos de compra sejam excluídos.

**Orçamento**

Será removida a restrição de parametrização para o movimento que será utilizado para gerar contrato. Com isto também serão realizados os tratamentos necessários para que o a rotina de geração de contratos copie os dados do item de orçamento para os itens de contrato.

 - Ao gerar o contrato a partir de um pedido o orçamento do movimento em questão será desfeito, e só afetará no contrato se o usuário informar um tipo de contrato que afete o orçamento e faça os devidos ajustes no contrato para que isto ocorra.

**Rastreabilidade de Contratos Gerados a partir de um pedido**

Foi adicionado na tela de rastreabilidade do movimento uma aba para que sejam apresentados os dados dos contratos gerados a partir do movimento.

## Procedimento para Implantação

Para utilizar o recurso de **Gerar Contrato**é necessário habilitar a permissão **Gerar Contrato**para o tipo de movimento que irá executar o processo no anexo **Permissão por Tipo de Movimento** do cadastro de Usuários no Módulo de Serviços Globais.

*Para atender as condições desse processo o tipo de movimento deve ser parametrizado da seguinte forma:*

1. *O movimento deve ser do tipo 1.1.XX e estar parametrizado como **Pedido de Compra** na **Etapa 49 -  Compra/Venda – Outros Dados Tipo de movimento de Compra**.*
2. *O tipo de movimento não poderá afetar estoque (nenhum saldo) na **Etapa 39 - Estoque - Estoque 1/3***
3. *Não poderá usar Faturamento parcial por valor (nem por item nem por movimento)*
4. *O parâmetro**Gerar Contrato**deverá ser marcado,**Etapa 51 – Contratos e marcar a opção Gera Contrato.**Esse parâmetro será responsável por habilitar no menu de Processos da visão do movimento o assistente de Geração de Contrato(s).*

## Procedimento para Utilização

```
Para gerar um contrato a partir de um pedido de compras o procedimento a seguir deve ser realizado:
```

* *Na visão do tipo de movimento parametrizado para Gerar Contrato selecione o movimento e execute o Processo Gerar Contrato.. A tela de Edição do Contrato é apresentada com todos os dados carregados do movimento, para que as informações pertinentes ao Contrato sejam informadas*.
* *Caso necessário, é possível agrupar os itens por Cliente/Fornecedor marcando a opção **Agrupar por Cliente/Fornecedor**no Assistente de Geração de Contratos.*
* *Após a inclusão do contrato será criado o relacionamento entre o movimento e o contrato gerado através da tabela TITMCNTMOVRELAC. Esse relacionamento permitirá a rastreabilidade do movimento que deu origem ao contrato e vice-versa. A visualização desse relacionamento pode ser feita através da tela de Rastreamento do movimento acessando a aba **Contrato**.*
* *Ao salvar o contrato, o pedido de compras ficará "Recebido".*

divs
