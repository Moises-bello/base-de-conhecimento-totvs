---
content_hash: e3c742ea13dcb28ffadc546f44408121aed39d758ccb069cd075f7dacfc974e9
fetched_at: '2026-07-02T19:24:26.613528+00:00'
page_id: '521644141'
product: protheus
source: tdn-tec
title: Correção - Queda no SmartClient ao imprimir relatório R3 em impressora PDF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521644141
version: 2
---

Feita alteração para que a queda não ocorra e a impressão seja feita com sucesso.

|  |  |
| --- | --- |
| Situação | Ao imprimir um relatório R3 em impressora PDF o SmartClient é abortado. |
| Ocorrência | A janela para selecionar o arquivo PDF a ser salvo segura a execução do SmartClient, porém a finalização da impressão acontece enquanto esta janela está aberta, ocasionando a queda. |
| Correção | A continuação da impressão não pode ocorrer enquanto um arquivo PDF a ser salvo não for escolhido. Para surtir efeito a correção necessita do AppServer 17.3.0.17 ou superior. |
| Informações adicionais | * Referente ao chamado: 64421552 * Referente à ocorrência: DTCLIENT01-57 * Disponível em builds superiores a 17.3.0.11 |
