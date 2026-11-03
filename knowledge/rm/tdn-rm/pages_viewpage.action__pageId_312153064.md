---
content_hash: 3bd69b606fd68d1b16f81714714ebaaae67c76225699c126667ef0460fc91104
fetched_at: '2026-06-29T00:08:45.678247+00:00'
page_id: '312153064'
product: rm
source: tdn-rm
title: DT Inativação/Ativação de Contas Gerenciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312153064
version: 12
---

# Processo de Inativação/Ativação de Contas Gerenciais

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | ****Gestão Contábil**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inativação/Atvação de Conta Gerencial* | **Inativação/Atvação de Conta Gerencial** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de contas gerenciais** | *CtbGerenciaAction* | | *Inativação/Atvação de Conta Gerencial* | CtbInativarAtivarContasGerenciaisAction | |
| **Cadastros Iniciais:** | *Cadastro de conta gerencial* |
| **Parâmetro(s):** | ***Não se aplica*.** |
| **Ponto de Entrada:** | **Não se aplica*.* |
| **Tickets relacionados** | **Não se aplica*.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [CONTROLADORIA01-576](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-576)  [CONTROLADORIA01-723](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-723)  [CONTROLADORIA01-345](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-345) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | ***SQL Server e Oracle*.** |
| **Tabelas Utilizadas:** | ***CGERENCIA*** |
| **Sistema(s) Operacional(is):** | ***Windows*** |

## Descrição

A inativação/ativação de contas gerenciais surgiu através da necessidade de maior controle interno acerca das contas e suas movimentações, possibilitando barrar a utilização de determinas contas em novas movimentações contábeis, não perdendo, porém os saldos e os registros das movimentações anteriormente realizadas nestas contas. Desta forma as contas gerenciais inativadas não poderão mais ser utilizadas em novos lançamentos, sejam estes feitos diretamente no sistema de Gestão Contábil ou naqueles que têm origem em sistemas externos, porém as movimentações anteriores existentes para estas contas comporão normalmente os saldos e as informações dos relatórios e rotinas legais.

Se, a qualquer momento, for necessário liberar novamente a utilização destas contas na realização das movimentações contábeis, basta executar este processo marcando a opção ‘Ativar Conta Gerencial’. Durante a execução do processo é possível determinar que o sistema envie um email aos usuários selecionados, informando-os sobre as contas gerenciais que foram inativadas ou ativadas e um complemento para tal ação.

Além disto contas gerenciais inativas poderão ser utilizadas normalmente nos filtros dos relatórios padrões do TOTVS Gestão Contábil.

**Observações**

Esse processo somente poderá ser executado para contas gerenciais analíticas e que tenham status (ativa/inativa) contrário ao tipo de alteração selecionado.

Para envio de emails na realização do processo, os cadastros dos usuários devem estar preenchidos com os respectivos endereços de email e as informações para Envio de Emails devidamente preenchidas nos Parâmetros Globais.

A maioria dos recursos existentes no sistema permite a indicação de contas gerenciais ativas ou inativas, com exceção daqueles que resultam na inclusão de novos lançamentos, tais como Inclusão de Lançamentos Contábeis.

O acesso ao processo de Inativação / Ativação de Contas Gerenciais é definido no perfil associado ao usuário.
