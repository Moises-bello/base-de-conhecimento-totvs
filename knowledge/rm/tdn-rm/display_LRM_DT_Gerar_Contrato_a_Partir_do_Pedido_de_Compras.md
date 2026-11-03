---
content_hash: d986af87d0a57b30df8f9cbb071ad8d9d84f1b4238cfecb9f58bcdf2d7782985
fetched_at: '2026-06-29T00:06:04.696040+00:00'
page_id: '200910441'
product: rm
source: tdn-rm
title: DT_Gerar_Contrato_a_Partir_do_Pedido_de_Compras
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Gerar_Contrato_a_Partir_do_Pedido_de_Compras
version: 6
---

# GERAR CONTRATO A PARTIR DO PEDIDO DE COMPRAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar Contrato | CtrGeraContratoMovimentoProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | MovMovimentoAction | | Manutenção de Contrato | CtrCntAction | |
| **Parâmetro(s):** | Gera Contrato |
| **Requisito (ISSUE):** | PCREQ-6379 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | TITMCNTMOVRELAC |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.7 |

## Descrição

Gerar contrato através de movimentos de Pedido de compra gerados por cotação ou manualmente. Esse novo processo será elaborado para atender tanto a geração de contrato a partir da cotação como também a geração de contrato através de Pedidos de compra simples.

## Importante

1. * **Exclusão do Contrato Gerado por Ordem de Compra**

   Não será permitido excluir um contrato gerado a partir do pedido de compras. Esse contrato só poderá ser cancelado.

   * **Cancelamento do Contrato Gerado por Ordem de Compra**

   Ao efetuar o cancelamento de um contrato gerado por ordem de compra não será feita alteração no status do movimento de origem. Isso acontece pois o contrato pode ser “descancelado” e essa característica dificulta o tratamento do movimento de origem.

## Procedimento para Configuração

**Configuração de Segurança**

Para utilizar o novo recurso de **Gerar Contrato**é necessário habilitar a permissão **Gerar Contrato**  para o tipo de movimento que irá executar o processo no anexo **Permissão por Tipo de Movimento** do cadastro de Usuários.

**CONFIGURAÇÃO DE PARÂMETROS**

Para atender as condições desse novo processo o parametrizador deverá ser configurado da seguinte forma:

1. Para que o tipo de movimento esteja apto a ser utilizado para gerar o Contrato, o tipo de movimento deve ser do tipo 1.1.xx e estar parametrizado como **GERAR MOVIMENTO DE COMPRA na etapa COMPRA/VENDA – CARACTERÍSTICAS.**
2. E também deve estar parametrizado como ****Pedido de Compra** na **Etapa 49 -  Compra/Venda – Outros Dados Tipo de movimento de Compra**.**
3. Além disso, o tipo de movimento não poderá afetar estoque (nenhum saldo) na ****Etapa 39 - Estoque - Estoque 1/3****
4. O tipo de movimento também não poderá afetar o orçamento na **Etapa 45 - Orçamento**
5. Nos parâmetros do tipo de movimento que se deseja parametrizar para gerar Contrato é necessário acessar a****Etapa 51 – Contratos** e marcar a opção Gera Contrato.**Esse parâmetro será responsável por habilitar no menu de PROCESSOS da visão do movimento o assistente de Geração de Contrato(s).

## Procedimento para Utilização

       1.            Gerar Contrato a partir de uma Ordem de Compras:

Na visão do tipo de movimento parametrizado para Gerar Contrato (Vide Procedimento para Configuração) selecione os movimentos que irão gerar os contratos e execute o **Processo Gerar Contrato.** A seguinte tela é apresentada:

       2.            Caso necessário é possivel agrupar os movimentos por Cliente/Fornecedor marcando a opção **Agrupar por Cliente/Fornecedor**

       3.            Clique em **Executar**

       4.            A tela de Edição do Contrato é apresentada com todos os dados carregados do movimento, para que as informações pertinentes ao Contrato sejam informadas.

       5.            Ao salvar o contrato será realizada a baixa do movimento, que terá seu status atualizado para Recebido/Parcialmente Recebido e será relacionado ao contrato gerado através da tabela TITMCNTMOVRELAC. Esse relacionamento permitirá a rastreabilidade de movimentos que deram origem a contratos e vice-versa. A visualização desse relacionamento acontece apenas através da tabela não existindo interface para consulta.
