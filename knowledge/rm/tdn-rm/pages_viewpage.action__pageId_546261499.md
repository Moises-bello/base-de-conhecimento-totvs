---
content_hash: f2768433da1f8f56d8dd0def671326330f44084f54cd5d989f76e60ea704749f
fetched_at: '2026-06-29T00:10:41.655060+00:00'
page_id: '546261499'
product: rm
source: tdn-rm
title: Permissão de Segurança nas Medições do Item de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546261499
version: 63
---

# Implementação de permissão de segurança nas medições do item de contrato

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | CtrCntAction | Contrato | |
| **Tickets relacionados** | -- |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** | TCNT, TITMCNT, TITMCNTMEDICAO |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementado permissão de segurança na medição de item de contrato, assim como seus processos: faturamento, exclusão de faturamento e cancelamento de faturamento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de 12.1.29. Por padrão, as novas permissões serão concedidas ou negadas conforme pré-condição de permissibilidade no perfil do usuário, para Inclusão e Edição na "Manutenção de Contrato.

Disponível no cadastro de Perfil do Usuário em: "Acesso a Menus | Contratos | Gestão de Contratos | Manutenção de Contrato":

* Inserir Medição - Excluir Medição - Editar Medição.
* Faturar Medição - Excluir Faturamento de Medição - Cancelar Faturamento de Medição.

## Procedimento para Utilização

-- Acessar o Contrato.

-- Acessar o Item de Contrato.

-- Verificar a permissão de medição (Incluir / Alterar / Excluir) ao tentar incluir um item de contrato com tipo de faturamento igual a medição.

* Os itens serão apresentados conforme as permissões concedidas no perfil do usuário.
* Todo usuário que possua permissão para Incluir uma nova medição, por padrão também poderá editá-la, mesmo que a permissão de edição esteja negada.
* As ações via atalho no teclado para Incluir / Editar / Excluir obedecem às regras de permissão.

-- Verificar a permissão de processos (faturamento, exclusão de faturamento e cancelamento de faturamento) no anexo de medições do contrato.

* Os botões de ação e a listagem dos processos no menu de Processos do anexo: "Visualizar Medições do Contrato", será disponibilizada conforme permissões concedidas.

|  |  |
| --- | --- |
| **Todas as Permissões NEGADAS** | **Todas as permissões CONCEDIDAS** |
|  |  |

divs
