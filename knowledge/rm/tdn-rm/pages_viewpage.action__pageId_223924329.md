---
content_hash: 5850f3badd27a9c403dd05f373203bd5b93637f608d265cddf73757bae4a43cc
fetched_at: '2026-06-29T00:06:22.626858+00:00'
page_id: '223924329'
product: rm
source: tdn-rm
title: DT_Melhorias_no_processo_Gerar Contrato_através_do_pedido_de_compra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223924329
version: 122
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
| **Versões/Release:** | 12.1.9 |
| **Versão Corrigida:** | 12.1.9 |
| **Versão Expedida:** | 12.1.9 |

## Descrição

Este documento visa detalhar as melhorias realizadas no processo Gerar Contrato a partir de um Pedido de compras. Todas as melhorias visam melhorar a usabilidade do módulo.

**Agrupamento por Fornecedores**

O processo Gerar Contrato agrupando os itens por Fornecedor passa a considerar os dados de cada movimento não apenas os dados no primeiro movimento computado, assim a informação de cada movimento será copiada para cada item de contrato como por exemplo a condição de pagamento do movimento será copiada para cada item de contrato referente ao seu movimento de origem.

Os campos que serão tratados nesse caso são:

* Local de Estoque (CODLOC)
* Condição de pagamento (CODCPG)
* Representante (CODRPR)
* Comissão do Representante (COMISSAOREPRES)
* Município (CODMUNICIPIOSERV)
* Estado (CODETDMUNSERV)
* Natureza do Movimento(IDNATMOV)
* Tipo de Frete (TIPOFRETE)
* Comprador (CODVEN1)
* Percentual de comissão do Comprador (PERCENTCOMISSAO)

Durante a geração do contrato o sistema verifica se o campo está preenchido no item de movimento e caso positivo o mesmo é copiado para o item de contrato, caso contrario (a informação não esta no item de movimento mas está no movimento) a informação é copiada do movimento de origem para o item de contrato correspondente.

**Unidade de Medida**

O item de contrato passa a ter a informação de unidade de medida. Isso se faz necessário, pois o movimento de origem pode ter itens iguais com unidades distintas ou mesmo agrupar itens de movimentos distintos com unidades diferentes em um mesmo item de contrato.

Nesse caso será criado o campo CODUND na tabela TITMCNT e será realizada a alteração na rotina de faturamento para que o mesmo passe a considerar a unidade de medida do item de contrato na geração de movimentos.

*Consistências:*

* Este campo não será preenchido com nenhum default vindo do cadastro do produto,
* Será filtrado de acordo com a unidade base da unidade de controle do produto selecionado.
* Não será possível alterar o campo CODUND caso o item de contrato seja do tipo medição e tenha alguma medição já faturada.
* Durante o faturamento de um item de contrato serão feitas as mesmas consistências que já são realizadas pelo serviço do movimento.

## Procedimento para Implantação

Para utilizar o recurso de **Gerar Contrato**é necessário habilitar a permissão **Gerar Contrato**para o tipo de movimento que irá executar o processo no anexo**Permissão por Tipo de Movimento** do cadastro de Usuários no Módulo de Serviços Globais.

*Para atender as condições desse processo o tipo de movimento deve ser parametrizado da seguinte forma:*

1. *O movimento deve ser do tipo 1.1.XX e estar parametrizado como **Pedido de Compra** na **Etapa 49 -  Compra/Venda – Outros Dados Tipo de movimento de Compra**.*
2. *O tipo de movimento não poderá afetar estoque (nenhum saldo) na **Etapa 39 - Estoque - Estoque 1/3***
3. *Não poderá usar aturamento parcial por valor (nem por item nem por movimento)*
4. *O parâmetro**Gerar Contrato**deverá ser marcado,**Etapa 51 – Contratos e marcar a opção Gera Contrato.**Esse parâmetro será responsável por habilitar no menu de Processos da visão do movimento o assistente de Geração de Contrato(s).*

## Procedimento para Utilização

```
Para gerar um contrato a partir de um pedido de compras o procedimento a seguir deve ser realizado:
```

* *Na visão do tipo de movimento parametrizado para Gerar Contrato selecione o movimento e execute o Processo Gerar Contrato.. A tela de Edição do Contrato é apresentada com todos os dados carregados do movimento, para que as informações pertinentes ao Contrato sejam informadas*.
* *Caso necessário, é possível agrupar os itens por Cliente/Fornecedor marcando a opção **Agrupar por Cliente/Fornecedor**no Assistente de Geração de Contratos.*
* *Será criado o relacionamento entre o movimento e o contrato gerado através da tabela TITMCNTMOVRELAC. Esse relacionamento permitirá a rastreabilidade do movimento que deu origem ao contrato e vice-versa. A visualização desse relacionamento acontece apenas através da tabela não existindo interface para consulta.*
* *Ao salvar o contrato, o pedido de compras ficará "Recebido".*

divs
