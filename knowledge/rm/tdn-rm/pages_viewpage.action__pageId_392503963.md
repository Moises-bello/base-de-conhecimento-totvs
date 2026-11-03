---
content_hash: 92cf7b51b1470fc25072891187aa649940c9888b5857412f483464ad404f557a
fetched_at: '2026-06-29T00:09:09.188151+00:00'
page_id: '392503963'
product: rm
source: tdn-rm
title: DT Data de Vencimento do Adiantamento maior que Data de Liberação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392503963
version: 1
---

# DATA DE VENCIMENTO DO ADIANTAMENTO MAIOR QUE DATA DE LIBERAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Adiantamento de Contratos | Adiantamento de Contratos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Liberação de Adiantamento | Liberação de Adiantamento | |
| **Cadastros Iniciais:** | Projeto, Contrato, Adiantamento |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Informe o requisito relacionado (Issue). |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Consistência da Data de Vencimento do Adiantamento do Contrato em relação à Data de Liberação do mesmo.

## Procedimento para Utilização

No processo de Liberação de Adiantamentos de Contratos é verificado se a Data de Vencimento do Adiantamento é maior ou igual à Data de Liberação do mesmo para que o processo possa ser executado com sucesso.

Em caso de negativa, uma mensagem de erro é exibida na tela, e para que o adiantamento seja liberado a data de vencimento deverá ser alterada:
