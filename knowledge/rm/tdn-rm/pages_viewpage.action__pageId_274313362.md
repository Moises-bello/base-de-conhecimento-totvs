---
content_hash: ae42616118573a61455b02c450b49e27739a53561acdd86e18cd9675f9f976c7
fetched_at: '2026-06-29T00:08:33.340558+00:00'
page_id: '274313362'
product: rm
source: tdn-rm
title: 790525 EDUCACIONAL01-681 DT Não grava recuo de parametrização de paragrafo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274313362
version: 103
---

# Complemento da Disciplina

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cadastro de complemento da disciplina |
| **Situação/Requisito:** | O espaço do campo "Descrição do complemento da disciplina" não é respeitado o espaçamento, gravado no banco de dados.  Ao realizar uma consulta na tabela SCOMPLDISC observamos que o HTML gravado possuía um espaçamento (exemplo: margin:0pt 0pt 0pt 36pt;), ao gerar um relatório ou visualizar a informação no portal o sistema apresentava o texto considerando o espaçamento cadastrado no banco de dados, porem ao editar o cadastro de complemento da disciplina o sistema mostrava o texto como se não tivesse nenhum espaçamento. |
| **Solução/Implementação:** | Melhoria no cadastro de complemento da disciplina para que a formatação do texto respeite a parametrização do recuo de parágrafo ao salvar o cadastro. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 790525 |
| **Requisito:** |  |

divs
