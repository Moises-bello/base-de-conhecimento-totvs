---
content_hash: 78b8a1d5757c7486a274a161c858bfeb0b6053203e0c1842809469e9246b8969
fetched_at: '2026-06-29T00:06:04.825767+00:00'
page_id: '200911664'
product: rm
source: tdn-rm
title: TSGWUY_DT_Estorno_Item_Nao_Cotado
type: documentation
url: https://tdn.totvs.com/display/LRM/TSGWUY_DT_Estorno_Item_Nao_Cotado
version: 8
---

# Estorno de Item não Cotado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Estornar Item Não Cotado* | CmpEstornarItemCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cotação* | CmpCotacaoAction | |  |  | |
| **Cadastros Iniciais:** | * *Solicitação de Compras gerada através do RMSolum.* * *Cotação* * *Ordem de compra gerada através da cotação.* |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | Não se Aplica |
| **Chamados relacionados** | Não se Aplica |
| **Requisito (ISSUE):** | Não se Aplica |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas utilizadas:** | * TCCOTACAO * TCCOTACAOITMMOV * TMOV * TITMMOV |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | *12.1.7* |

# **Objetivo**

Permitir que o usuário estorne itens que estão participando do processo de cotação e, caso a solicitação de compra correspondente tenha sido gerada através da integração RMSolum x RMNucleus, a quantidade estornada deverá ser informada ao RMSolum.

# **Descrição**

Foi criado o processo responsável por Estornar Itens Não Cotados, este possui como objetivo estornar os itens previamente selecionados de uma determinada cotação e realizar a baixa da solicitação de compras:

Para a utilização do processo citado, o usuário deverá fazer parte de um perfil que possui uma permissão específica, foi criado o item “Estornar Item Não Cotado” na aba “Acesso a Menus” da tela de edição do perfil de usuário.  
 **Caminho Completo**: Edição do Perfil de Usuário -> Acesso a Menus -> Gestão de Estoque, Compras e Faturamento -> Compras -> Gestão de Compras -> Cotação -> Estornar Item Não Cotado

Durante a execução do processo, para cada item selecionado serão aplicadas as seguintes rotinas:

* **Baixa da Solicitação de Compras**: Será realizada a baixa da solicitação de compra que possui o item em questão, a quantidade do item no movimento será alterada para 0 e serão executadas todas as rotinas parametrizadas no tipo de movimento, exemplo: Integração Financeira, Integração Contábil, Estoque, WorkFlow, Orçamento, etc...
* **Status da Cotação**: O campo Status de cada item selecionado será alterado para “Estornado”, caso todos os registros sejam selecionados, ou seja, não existam mais itens Ativos, a cotação será Concluída.
* **Estorno no RMSolum**: Caso a solicitação de compra tenha sido gerada através do módulo de Projetos “IntegraAplicacao = M”, o sistema será responsável por retornar o saldo estornado para o RMSolum.

**Notas:**

* Não será possível selecionar mais de uma cotação para a execução do processo.
* O processo estará disponível apenas para cotações com o status “Ordem de Compra Parcialmente Gerada”.
* Na tela do processo serão exibidos apenas os itens ativos da cotação “STATUS = 1”.
* Pelo menos um item deverá ser selecionado para a execução do processo.
* Nesta primeira versão, não será possível estornar itens de cotações que estejam integradas ao Paradigma ou ClicBusiness.
