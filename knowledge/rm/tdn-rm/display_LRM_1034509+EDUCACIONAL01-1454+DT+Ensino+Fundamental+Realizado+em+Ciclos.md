---
content_hash: cc5fc2bd4cb595c2b20835a1d5a7ca7e91be7230db3ea3763a7a4ddb4adbe607
fetched_at: '2026-06-29T00:08:36.260666+00:00'
page_id: '284471249'
product: rm
source: tdn-rm
title: 1034509 EDUCACIONAL01-1454 DT Ensino Fundamental Realizado em Ciclos
type: documentation
url: https://tdn.totvs.com/display/LRM/1034509+EDUCACIONAL01-1454+DT+Ensino+Fundamental+Realizado+em+Ciclos
version: 105
---

# ENSINO FUNDAMENTAL REALIZADO EM CICLOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | T*****otvs Educacional***** |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Após enviar o arquivo do censo, foi retornada a seguinte mensagem de erro: O campo "Ensino fundamental organizado em ciclos" não pode ser preenchido quando a escola não possuir turma(s) do ensino fundamental.   No sistema não temos esse campo disponível para preenchimento. |
| **Solução/Implementação:** | Foi incluído o campo "Ensino fundamental realizado em ciclos" na tela de Dados do Censo da Filial (para a versão 12.1.13 e 12.1.14) e na tela de Instituição do MEC (a partir da versão 12.1.15).   A rotina de preparação do arquivo para o Educacenso foi alterada para não enviar a informação de ensino fundamental realizado em ciclos quando não existir turmas de ensino fundamental na instituição. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
