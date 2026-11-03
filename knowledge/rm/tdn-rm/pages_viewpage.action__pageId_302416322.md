---
content_hash: 61f61b0bc9bb08f27c5f5445a52edc92337fd58e6944a5c5577e15299b8a34cf
fetched_at: '2026-06-29T00:08:43.562749+00:00'
page_id: '302416322'
product: rm
source: tdn-rm
title: 531124 EDUCACIONAL01-205 DT Motivo da Alteração do Termo de Compromisso de
  Estágio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=302416322
version: 99
---

# MOTIVO DA ALTERAÇÃO DO TERMO DE COMPROMISSO DE ESTÁGIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Termo de Compromisso de Estágio |
| **Situação/Requisito:** | Ao realizar qualquer alteração no "Termo de Compromisso de Estágio", informando um motivo de alteração, o sistema não estava gravando no "Histórico das Alterações do Termo de Compromisso do Estágio" o motivo selecionado, deixando o campo vazio |
| **Solução/Implementação:** | Alteração na rotina de gravação de log no "Histórico das alterações do termo de compromisso do estágio" para gravar o motivo da alteração mesmo que o status seja modificado de "Assinado" para "Pendente assinatura" durante a gravação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | [EDUCACIONAL01-2746](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2746) |
| **Requisito:** | N/A |

divs
