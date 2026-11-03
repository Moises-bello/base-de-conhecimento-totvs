---
content_hash: ab8957d03f031d0992f553dd16af53e10068c77aedcceb15daab231603c131e3
fetched_at: '2026-06-29T00:08:59.502589+00:00'
page_id: '362460816'
product: rm
source: tdn-rm
title: RMSAU-3931 DT Erro na integração com EMS quando utiliza Backoffice diferentes
  por coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362460816
version: 1
---

# Erro na integração com EMS quando utiliza Backoffice diferentes por coligada

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Solicitação de Pedido de Nota Fiscal |
| **Situação/Requisito:** | Na funcionalidade de Pedido de Nota fiscal, ao clicar no botão para enviar os dados para o EMS, ocorre erro de object reference. Isso ocorreu após parametrizar o sistema para utilizar o Backoffice Datasul na coligada 1 e o Backoffice RM na coligada 2. |
| **Solução/Implementação:** | Realizado o ajuste na camada de integração. O sistema deve verificar se há integração do Saúde com o EMS na coligada corrente e na coligada global. Caso, uma das duas esteja habilitada, a integração deve ocorrer |
