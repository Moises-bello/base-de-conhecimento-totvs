---
content_hash: 1a5b2c251f2f2a55e35104c2356d92d152f1ec2ce2fe79fdbfbd06b2e93f45b6
fetched_at: '2026-07-02T19:24:28.868844+00:00'
page_id: '863897489'
product: protheus
source: tdn-tec
title: Melhoria - Unificação dos binários para Linux printer e pdfprinter
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=863897489
version: 1
---

Melhoria - Unificação dos binários printer e pdfprinter

|  |  |
| --- | --- |
| Situação | Em versões anteriores o binário printer funcionava somente em sistemas operacionais Linux com GUI (interface gráfica). Como alternativa, caso a GUI não estivesse presente no Linux, tornava-se obrigatório o uso do binário pdfprinter, sendo que este permitia somente impressões em arquivo PDF, possuindo portanto menos recursos que o binário printer convencional. |
| Ocorrência | Necessidade de evolução do SDK e bibliotecas da TOTVS Printer para versões mais atuais e com novos recursos. |
| Melhoria | O binário printer recebeu diversas implementações para rodar também em sistemas operacionais Linux sem interface gráfica, habilitando nesses casos a saída em Spool, arquivos .xlsx e etc. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4859 * Disponível a partir da versão TOTVS Printer 3.0.0 |
