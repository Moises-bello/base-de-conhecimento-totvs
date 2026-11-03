---
content_hash: 7827685d0796cb4c691dd492a96d23a5c897fedc0050d28632a26210f0a7dea3
fetched_at: '2026-06-29T00:06:26.342304+00:00'
page_id: '225215347'
product: rm
source: tdn-rm
title: TTOTG8_DT_Exclusao_de_Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOTG8_DT_Exclusao_de_Pessoa
version: 119
---

# EXCLUSÃO DE PESSOA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Pessoas* |
| **Função:** | *Exclusão de Pessoas* |
| **Situação/Requisito:** | *Sistema apresenta a mensagem de erro abaixo ao tentar excluir uma pessoa que foi cadastrada incorretamente.*  *Excluindo: Identificador = XXXX*  *A pessoa XXXX - NOME DA PESSOA possui associação com o cadastro de "Especialização da PPessoa" e o processo de exclusão da pessoa somente é possível após a exclusão desse relacionamento no módulo correspondente.* |
| **Solução/Implementação:** | *Adicionada validação quanto à existência de relacionamento da Pessoa com o Endereço Profissional ( *Especialização da PPessoa -* PPESSOA X SPESSOA), possibilitando assim a exclusão da pessoa quando não houver relacionamento com o Educacional (Aluno e Professor).* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTOTG8* |
| **Requisito (ISSUE):** |  |

divs
