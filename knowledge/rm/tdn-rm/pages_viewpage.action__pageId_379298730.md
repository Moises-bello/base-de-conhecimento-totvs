---
content_hash: a69bfa4770cc6438b17c0d7afce064351ad0f244407789df6aefc2d9b1d5aac2
fetched_at: '2026-06-29T00:09:02.214937+00:00'
page_id: '379298730'
product: rm
source: tdn-rm
title: 2200146 EDUCACIONAL01-4091 DT Cadastro de Assinatura de Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379298730
version: 87
---

# CADASTRO DE ASSINATURA DE PERIÓDICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Cadastro de Assinatura de Periódicos* |
| **Situação/Requisito:** | *Ao vincular um Cliente/Fornecedor a um período de Assinatura (Periódicos), o sistema exibe mensagem de erro de chave estrangeira.*  *Outras mensagens de erro apresentada no cadastro de publicações:*  - Ao editar uma publicação do tipo periódico apresentava incorretamente a mensagem: “Ocorreu um erro ao efetuar a leitura do registro: Falha ao ativar restrições. Uma ou mais linhas contêm valores que violam as restrições non-null, unique ou foreign-key”.  - Ao editar qualquer campo das publicações no acervo da biblioteca apresentava a mensagem de erro "Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados.". |
| **Solução/Implementação:** | *Foi criado a coluna CODCOLCFO na tabela LASSINATURAPER para ser utilizada ao referenciar um Cliente/Fornecedor, ao invés de usar a coluna CODCOLIGADA padrão da tabela.*  Para solucionar este problema, se faz necessário também executar o script cuja marcação é BL.2018.06\_01, onde será criado a coluna CODCOLCFO na tabela de assinatura de periódicos (LASSINATURAPER). |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | EDUCACIONAL01-4091; EDUCACIONAL01-5907; EDUCACIONAL01-5909; EDUCACIONAL01-5904; EDUCACIONAL01-5922 |
| **Requisito (ISSUE):** | *N/A* |

divs
