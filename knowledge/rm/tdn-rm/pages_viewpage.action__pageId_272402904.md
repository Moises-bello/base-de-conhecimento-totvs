---
content_hash: ebeb4990db5cbdeded5c8e6a68cecef26ab2ab2a7920c49a8a8960508e5b498b
fetched_at: '2026-06-29T00:08:30.136709+00:00'
page_id: '272402904'
product: rm
source: tdn-rm
title: 631243 MRH-8618 DT Cadastro de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272402904
version: 107
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Pessoas |
| **Função:** | Cadastro de Funcionário |
| **Situação/Requisito:** | Ao tentar cadastrar um novo funcionário, e informar o CPF 224.893.448-38 na tela de pré-cadastro, ocorre o erro ao salvar os dados do novo funcionário (com todos os campos obrigatórios preenchidos):  Referência de objeto não definida para uma instância de um objeto. |
| **Solução/Implementação:** | Realizado ajuste no cadastro de Funcionário de forma a evitar inconsistências quando o funcionário a ser cadastrado estiver vinculado a uma requisição de substituição gerada por uma requisição de outra coligada. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 631243 |
| **Requisito:** |  |

divs
