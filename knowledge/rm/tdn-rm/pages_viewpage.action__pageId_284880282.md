---
content_hash: 26671c0184c21b625c3b23fbad718fcb4ae443e05ae0250a04d054e3fe0b4114
fetched_at: '2026-06-29T00:08:37.636676+00:00'
page_id: '284880282'
product: rm
source: tdn-rm
title: 575893 EDUCACIONAL01-158 DT Impressão de boleto trava ao pedir para exportar
  para PDF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880282
version: 101
---

# IMPRESSÃO DE BOLETO TRAVA AO PEDIR PARA EXPORTAR PARA PDF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Impressão de Boleto |
| **Situação/Requisito:** | Ao selecionar um boleto e executar o processo imprimir boleto, o mesmo está travando ao pedir para exportar em PDF. |
| **Solução/Implementação:** | Alteração da chamada para geração do relatório que era assíncrona para chamada síncrona a fim de evitar que a tela de aguardando execução trave o sistema como um todo. Anteriormente, as duas chamadas assíncronas estavam entrando em conflito fazendo com que uma ficasse aguardando o término da execução da outra causando um travamento do sistema. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
