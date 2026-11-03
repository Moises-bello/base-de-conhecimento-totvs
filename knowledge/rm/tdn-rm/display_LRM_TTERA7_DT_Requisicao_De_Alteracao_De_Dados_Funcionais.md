---
content_hash: 87005c0c67c3702a96ff8f433845be60c704691619671930ec54095f59be93be
fetched_at: '2026-06-29T00:08:11.213871+00:00'
page_id: '242385297'
product: rm
source: tdn-rm
title: TTERA7_DT_Requisicao_De_Alteracao_De_Dados_Funcionais
type: documentation
url: https://tdn.totvs.com/display/LRM/TTERA7_DT_Requisicao_De_Alteracao_De_Dados_Funcionais
version: 111
---

# REQUISIÇÃO DE ALTERAÇÃO DE DADOS FUNCIONAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Requisição de Alteração de Dados Funcionais* |
| **Situação/Requisito:** | *Quando tenho um funcionário horista, vinculado a uma requisição de alteração de dados funcionais, ao fazer a alteração de função e/ou salário no cadastro do funcionário, antes de efetivar a requisição e tenha alterado os dados da requisição no processo de efetivação da requisição, retorna o erro: "ORA-01427: a subconsulta de uma única linha retorna mais de uma linha".* |
| **Solução/Implementação:** | *Ajuste no cadastro de Funcionário. Ao alterar dados de um funcionário, que possam causar cancelamento de uma requisição com mais de um parecer "Aprovado", não ocorre erro.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTERA7* |
| **Requisito (ISSUE):** |  |

divs
