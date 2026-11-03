---
content_hash: 12883630c9aa974e9c8cd863e546e409a66e7dadce55c6444cf3ba22d682bef0
fetched_at: '2026-06-29T00:08:15.732081+00:00'
page_id: '244922086'
product: rm
source: tdn-rm
title: TVHOGT_DT_DATA_MUDANCA_BANCO_PAGAMENTO_ADMISSÃO_FUNCIONÁRIO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244922086
version: 111
---

# ADMISSÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário* |
| **Situação/Requisito:** | *No cadastro de um novo funcionário os campo de "Data de mudança" são automaticamente preenchidos com a data de admissão.* *Porém na tela de cadastro de "Banco pgto/Financeiro" se o CÓDIGO DO BANCO (001 por exemplo) é alterada a data de histórico de banco assume o dia primeiro (01) ao invés da data correta, que seria a data de admissão.*  *O problema somente ocorre se o CÓDIGO DO BANCO é alterado.* |
| **Solução/Implementação:** | *Mantida a data de mudança igual a data de admissão para caso de alteração manual do código do banco.* |
| **Chamados relacionados:** | *TVHOGT* |

divs
