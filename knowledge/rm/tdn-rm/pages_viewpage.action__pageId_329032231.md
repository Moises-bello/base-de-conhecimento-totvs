---
content_hash: 6e41d130761fe69f9e03b0995c292279a657c1294139b7b032a1177ef6998ead
fetched_at: '2026-06-29T00:08:48.969847+00:00'
page_id: '329032231'
product: rm
source: tdn-rm
title: DT Sobrepor defaults do template sobre lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329032231
version: 2
---

# Template de Acordo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Template de Acordo* | *Template de Acordo* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de Acordo*  *Negociação Online* | *Geração de Acordo.*  *Negociação Online* | |  |  | |
| **Cadastros Iniciais:** | *Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito.* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Ponto de Entrada:** | *Informe o ponto de entrada relacionado (link).* |
| **Tickets relacionados** | *Informe o(s) chamado(s) relacionado(s).* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4130> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql-Server e Oracle* |
| **Tabelas Utilizadas:** | *FTEMPLATEACORDO* |
| **Sistema(s) Operacional(is):** | MS-Windows |

## Descrição

Disponibilizado no cadastro de Template de Acordo o parâmetro "Sobrepor defaults do template sobre lançamento" que terá a seguinte ação:

Desmarcado – Considera primeiramente os default do lançamento de origem se preenchido, caso esteja vazio irá considerar os default do template.

Marcado – Sempre considera os default do template caso esteja preenchido, caso contrário, considera os default do lançamento.

Obs.: Para múltiplos lançamento de origem só será considerado o default do lançamento caso tenha o mesmo default entre eles, caso seja diferente então irá considerar o default do template e caso o default do template esteja vazio, o default do lançamento de destino também ficará vazio.

## Procedimento para Utilização

       1.            No TOTVS Gestão Financeira, acesse o  menu "Contas a Pagar/Receber | Acordo | Template de Acordo", edite um template e na aba "Default" marque ou desmarque o parâmetro "Sobrepor default do template sobre o lançamento".

       2.            No cadastro de Lançamento ao efetuar um acordo com o parâmetro "Sobrepor default do template sobre o lançamento" marcado os default do lançamento de destino será o mesmo do cadastro de Template de acordo, no qual o usuário poderá modificar.

       3.            No cadastro de Lançamento ao efetuar um acordo com o parâmetro "Sobrepor default do template sobre o lançamento" desmarcado os default do lançamento de destino será o mesmo do lançamento de Origem, no qual o usuário poderá modificar.

       5.            No Portal do Aluno, funcionalidade "Negociação Online" o parâmetro "Sobrepor default do template sobre o lançamento" terá o mesmo efeito, sendo que esses campos não são visíveis para que o aluno possa mudar.

## Vídeo

600400
