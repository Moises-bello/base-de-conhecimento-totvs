---
content_hash: 1d49d49c0fbcac2a9b5eae3b3fb07e8647f6913f2e2ed78efb01e4cd230ad575
fetched_at: '2026-06-29T00:08:41.720897+00:00'
page_id: '286745747'
product: rm
source: tdn-rm
title: 1230293 FINANCEIRO01-1953 DT Cadastro Cliente Fornecedor
type: documentation
url: https://tdn.totvs.com/display/LRM/1230293+FINANCEIRO01-1953+DT+Cadastro+Cliente+Fornecedor
version: 93
---

# Cliente/ Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão Financeira. |
| **Função:** | Desvincular/Vincular Cli/For |
| **Situação/Requisito:** | Ao tentar cadastrar Cliente/Fornecedor do exterior é apresentado o erro abaixo:  "Campo 'Cód. Município' foi definido como preenchimento obrigatório pelo usuário supervisor na tela de cadastro de cliente/fornecedor" |
| **Solução/Implementação:** | Ajuste no serviço de inclusão/alteração do cliente/fornecedor para considerar os campos que não devem ser validados como obrigatorio. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000008 |

divs
