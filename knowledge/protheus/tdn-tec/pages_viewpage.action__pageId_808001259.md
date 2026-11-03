---
content_hash: b516f836d90d5b455ae1270943c6b8d26658c7853c3a57cf597be12694d3e16a
fetched_at: '2026-07-02T19:24:28.682276+00:00'
page_id: '808001259'
product: protheus
source: tdn-tec
title: Correção - Download de arquivo pelo TWebEngine Linux sempre falha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808001259
version: 1
---

Tentar realizar o download de um arquivo pelo TWebEngine em ambiente Linux não abre a janela para selecionar o caminho do arquivo, e consequentemente sempre falha.

|  |  |
| --- | --- |
| Situação | Falha no download de arquivo pelo TWebEngine Linux. |
| Ocorrência | Não é exibida uma janela para definir onde o arquivo será salvo, ocasionando a falha de download. |
| Correção | Foi adicionada a janela para seleção do caminho para salvar o arquivo, e o download é executado normalmente. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4442 * Disponível em builds superiores a 20.3.2.2 |
