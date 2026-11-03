---
content_hash: 34f0d9a5e2353326c07137accb848b384da48eb59fe1e6b0185cf4249825fd3f
fetched_at: '2026-07-02T19:24:26.618991+00:00'
page_id: '521650825'
product: protheus
source: tdn-tec
title: Correção - Iniciar Smartclient por linha de comando usa o broker quando não
  deveria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521650825
version: 1
---

|  |  |
| --- | --- |
| Situação | Utilizar o Smartclient por linha de comando tenta utilizar o broker e falha a conexão |
| Ocorrência | Problema ocorre porque o Smartclient pega a sessão utilizada no ini (Sessão Active) mesmo quando não deveria |
| Correção | Correção feita para não ler a sessão do ini quando os dados de conexão já foram passados por linha de comando |
| Informações adicionais | * Referente ao chamado: 7173248 * Referente à ocorrência: DTCLIENT01-559 * Disponível em builds iguais ou superiores a 7.00.131227A - 13.2.3.42 |
