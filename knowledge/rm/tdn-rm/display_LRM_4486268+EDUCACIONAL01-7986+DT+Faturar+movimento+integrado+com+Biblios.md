---
content_hash: 211e6a64f13defdf5298353559da14e4ed0dc4212558004b20c87325618af31b
fetched_at: '2026-06-29T00:09:58.820631+00:00'
page_id: '452711770'
product: rm
source: tdn-rm
title: 4486268 EDUCACIONAL01-7986 DT Faturar movimento integrado com Biblios
type: documentation
url: https://tdn.totvs.com/display/LRM/4486268+EDUCACIONAL01-7986+DT+Faturar+movimento+integrado+com+Biblios
version: 77
---

# FATURAR MOVIMENTO NO TOTVS GESTÃO DE ESTOQUE, COMPRA e FATURAMENTO INTEGRADO COM TOTVS GESTÃO BIBLIOTECÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Faturar movimento* |
| **Situação/Requisito:** | No módulo "Totvs Gestão de Estoque, Compra e Faturamento", ao executar o processo “Faturar/Receber” do movimento de compra integrado com o "Totvs Gestão Bibliotecária", apresentava mensagem de erro: "Não existe nenhuma transação aberta para fazer o Commit". Somente ocorria quando a Publicação não tinha Fornecedor cadastrado e o movimento estava preenchido com um código de fornecedor. |
| **Solução/Implementação:** | Melhoria na mensagem ao validar o faturamento de um movimento integrado com Totvs Gestão Bibliotecária com o Totvs Gestão de Estoque, Compras e Faturamento.  Apresentava mensagem de erro: "Não existe nenhuma transação aberta para fazer o Commit". Com a alteração, passamos a detalhar o real problema ocorrido durante a gravação e o comando do banco de dados (caso exista). Por exemplo: “Violação de chave estrangeira. The INSERT statement conflited with the FOREIGN KEY constraint FKLEXEMPLAR\_LPUBFCFO. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
