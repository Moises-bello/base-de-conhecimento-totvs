---
content_hash: 3708d1ebe9b5251ad0ef5c609c840567c19c2b83732f531539b3f6c1fe7ee0c5
fetched_at: '2026-07-02T19:24:28.807652+00:00'
page_id: '857902035'
product: protheus
source: tdn-tec
title: Correção - Alerta de inatividade provoca encerramento inesperado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=857902035
version: 1
---

Correção - Alerta de inatividade provoca encerramento inesperado

|  |  |
| --- | --- |
| Situação | Comportamento observado em sistemas Logix. Quando configurado com Inactive Timeout e o tempo de inatividade é atingido, no momento em que a janela de aviso é exibida, o SmartClient é encerrado de maneira abrupta. |
| Ocorrência | Pode ser observado no sistema Logix durante o uso de dois ou mais programas (abas ou workspaces) e com a chave Inactive Timeout habilitada no TOTVS Application Server. Ao atingir o tempo limite de inatividade de uma determinada workspace, uma janela de mensagem é exibida para alertar sobre o encerramento da workspace, porém nesse momento ocorre um problema que encerra de maneira inesperada todo o SmartClient. |
| Correção | Foi aplicada uma proteção no SmartClient para tratar corretamente o encerramento de uma workspace quando ela atingir o tempo limite de inatividade programado. |
| Informações adicionais | * Referente ao chamado: 20322913 e 20549945 * Referente à ocorrência: DTCLIENT01-4839 e DTCLIENT01-4890 * Disponível a partir da build 20.3.2.8 |
