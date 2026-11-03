---
content_hash: 0d97f8984f825734a9df251a2576fe983a3602d6903b1ddb1c1f4beb0da5eacb
fetched_at: '2026-06-29T00:08:54.794532+00:00'
page_id: '346495802'
product: rm
source: tdn-rm
title: DT Geração de movimento por competência para o responsável do contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346495802
version: 3
---

# Geração de movimento por competência para o responsável do contrato

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Gerar Movimento por competência | Gerar Movimento por competência | |  |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Responsável financeiro do contrato | Responsável financeiro do contrato | |  |  | |
| **Cadastros Iniciais:** | *Cadastrar o responsável financeiro para o contrato informando o responsável financeiro do movimento* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *DEDUINTEGRACOES-1835* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SRESPONSAVELCONTRATO* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Com o objetivo de flexibilizar geração de movimento por competência foi acrescentada uma opção para que seja possível gerar os movimentos para o responsável do contrato. Dessa forma, o processo de geração de movimento recebeu um novo campo para que o cliente consiga informar o tipo do responsável financeiro que será gerado nos movimentos.

## Procedimento para Utilização

Ao selecionar o processo geração de movimento por competência a seguinte tela será apresentada para o usuário com a nova opção de tipo de responsável financeiro:

* **Responsável financeiro do aluno:**   
  Ao selecionar essa opção o sistema irá gerar os movimentos buscando a informação do cliente/fornecedor no cadastro de responsável do aluno, como na imagem a baixo:
* **Responsável financeiro do contrato:**  
  Ao selecionar essa opção o sistema irá gerar os movimentos buscando a informação do cliente/fornecedor no cadastro de responsável do contrato. Para que o sistema consiga identificar qual dos responsáveis do contrato será o responsável financeiro do movimento foi criado o campo "Responsável financeiro do movimento" no cadastro do responsável do contrato. Na imagem a baixo segue o exemplo de um responsável financeiro do contrato que também é responsável financeiro do movimento:

Caso a opção do tipo de responsável financeiro, selecionada no processo, seja a de responsável financeiro do contrato e o contrato não tenha nenhum responsável financeiro para o movimento, o sistema irá buscar no responsável financeiro do aluno os dados de cliente/fornecedor.
