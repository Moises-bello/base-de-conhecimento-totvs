---
content_hash: a48b5f6c98785f37084a48a884add030421b38d4a8b131038c70bf41fb90d690
fetched_at: '2026-06-29T00:08:33.812714+00:00'
page_id: '274326863'
product: rm
source: tdn-rm
title: 594278 FINANCEIRO01-312 Integração Bancária - Retorno de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274326863
version: 99
---

# Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Ao realizar o retorno de um arquivo que tem duas linhas, uma de baixa e outra de registro, para o mesmo boleto associado a mais de um lançamento o sistema não estava baixando o boleto sendo apresentado a mensagem de erro: Chave duplicada  Possíveis causas:   * inclusão de registro cujo valor da chave primária já existe * inclusão de registro cujo valor do índice único já existe |
| **Solução/Implementação:** | Melhoria no processo de retorno bancário para o tratamento correto quando no arquivo existir mais de uma linha para o mesmo boleto que esteja associado a mais de um lançamento. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 762115 |
| **Requisito:** | FIN000169 |

divs
