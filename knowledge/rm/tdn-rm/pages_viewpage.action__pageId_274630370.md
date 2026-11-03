---
content_hash: 3569a56db4805a0485b082ad0357b6dcde8c1f5f8107b48f8ef2e7de1046a124
fetched_at: '2026-06-29T00:08:33.940396+00:00'
page_id: '274630370'
product: rm
source: tdn-rm
title: 721463 EDUCACIONAL01-749 DT Portal do Professor Diário de classe ordenado pelo
  Nome Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274630370
version: 98
---

# DIARIO DE CLASSE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Diário de Classe no Portal |
| **Situação/Requisito:** | A ordenação na lista de frequência diária não está considerando o nome social, ordenando pelo número diário + nome civil. |
| **Solução/Implementação:** | Otimizado no Portal do Professor, link Diário de Classe, a ordenação da frequência diária do aluno que poderá ser Por Nome (inclusive nome social).  Foi criado novo parâmetro Educacional de Matrícula para Tipo de Numeração, com a opção “Por nome (inclusive nome social)”. Caso seja marcado, o sistema irá ordenar os alunos pelo nome, inclusive o nome social. Na opção Tipo de Numeração igual a “Por Nome”, a ordenação é feita pelo nome civil apenas.  Importante: Como a ordenação do aluno observa também o número do diário, caso opte pelo novo parâmetro, será necessário gerar novamente o processo “Numeração de turma”. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** |  |

divs
