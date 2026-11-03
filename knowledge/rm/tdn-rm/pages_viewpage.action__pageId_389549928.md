---
content_hash: b2ed7f45342b1e66b8817b7177096c7e25a13a4c2da8b7339b8c7b24429e5f1c
fetched_at: '2026-06-29T00:09:08.494486+00:00'
page_id: '389549928'
product: rm
source: tdn-rm
title: DT Nova Opção de Usa TEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389549928
version: 4
---

# Nova opção para 'Usa TEF' obrigatório na sessão de caixa.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | TEF | Integração com pagamento com TEF |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Baixa. | Baixa. quitação de lançamentos | | Sessão de Caixa | Sessão de Caixa | |
| **Cadastros Iniciais:** | Parametrização para Utilizar TEF |
| **Parâmetro(s):** | 02.02.05.01 - Módulo de Caixa |
| **Tickets relacionados** | 3211286 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7687> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | FLAN, FPARAM, FSESSAOCAIXA, FFILIALPARAM |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.22 |

## Descrição

Nova opção nas parametrizações de integração com TEF por filial ou por coligada para usar a integração com o TEF obrigatoriamente na sessão de caixa.

## Procedimento para Utilização

* Dentre as opções para utilização do TEF será disponibilizado mais uma opção para que a integração do TEF seja obrigatória nos pagamentos via sessão de caixa.
* Tal parametrização terá a regra de definir na abertura da sessão de caixa se deve utilizar ou não a integração do TEF. Caso a opção de obrigatório esteja selecionada, não será possível desmarcar a opção de utilização do TEF.

Por Coligada

Por Filial
