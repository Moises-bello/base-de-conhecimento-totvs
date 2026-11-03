---
content_hash: 0d05389a13e4aef38398317cd5b0bf1b9d2fd83953b6640f39b2947a24a091e2
fetched_at: '2026-07-02T19:24:29.454224+00:00'
page_id: '889102953'
product: protheus
source: tdn-tec
title: Correção - Impressão em PDF não funciona
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=889102953
version: 1
---

Correção - Impressão em PDF não funciona

|  |  |
| --- | --- |
| Situação | Ao tentar imprimir um relatório em PDF através de qualquer módulo do Protheus, tanto no Servidor quanto no Cliente, o relatório em PDF não é gerado nem exibido na tela. |
| Ocorrência | Uma falha no agente TOTVS Printer durante o tratamento dos parâmetros recebidos impedia a correta geração do PDF. |
| Correção | A TOTVS Printer recebeu um ajuste para tratar corretamente os parâmetros de impressão recebidos para geração de PDF. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-5235 * Disponível a partir da versão 3.0.1 |
