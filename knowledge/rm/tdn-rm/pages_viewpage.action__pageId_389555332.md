---
content_hash: 2d146384ba7a344237715f06c40bcf59c28a4a8cba180eb9fce4e847f50fc1af
fetched_at: '2026-06-29T00:09:08.585099+00:00'
page_id: '389555332'
product: rm
source: tdn-rm
title: DT Verificação de objetos gerenciais impactados pelo novo SICRO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389555332
version: 2
---

# VERIFICAÇÃO DE OBJETOS GERENCIAIS IMPACTADOS PELO NOVO SICRO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | ***RM*** |
| **Segmento:** | ***Construção e Projeto*** |
| **Módulo:** | ****Gestão de Obras e Projetos**** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Verificação de objetos gerenciais impactados pelo novo SICRO | Verificação de objetos gerenciais impactados pelo novo SICRO |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Reports |  | | Relatórios Delphi |  | | Planilhas |  | | Fórmulas |  | | Consultas SQL |  | | Cubos |  | | Gráficos |  | |
| **Cadastros Iniciais:** | Não se aplica |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [TOPORCAPLAN001-](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-3573)[4032](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-4032) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Devido à necessidade de adequação à terceira versão do SICRO (Sistema de Custos Referenciais de Obras), alguns impactos podem ocorrer em Objetos Gerenciais, Fórmulas ou Consultas SQL.

## Procedimento para Utilização

O SICRO é uma ferramenta criada e aperfeiçoada pelo DNIT para manter atualizada a definição de custos, apta para estabelecer os melhores parâmetros para referenciar a elaboração dos orçamentos de projetos rodoviários e licitação de obras.

Sendo assim, alguns Objetos Gerenciais (Reports, Relatórios Delphi, Cubos, Gráficos), Fórmulas ou Consultas SQL podem sofrer impactos devido aos novos grupos DNIT, Atividades Auxiliares e Tempo Fixo, e principalmente pela mudança do grupo de Materiais que passa a ser representado pela letra "C".

Através da funcionalidade de "Verificação de objetos gerenciais impactados pelo novo SICRO" é possível visualizar quais objetos sofrem impactos com as alterações. A busca é feita a partir dos campos GRUPODNER, PERCSOBREGRPDNER E FLAGTIPOCMP,  que armazenam os grupos DNIT.

Uma mensagem será exibida ao entrar no TOTVS Obras e Projetos, informando da necessidade de utilização dessa nova rotina:
