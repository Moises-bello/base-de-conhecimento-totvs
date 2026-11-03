---
content_hash: 4d4b1930522a0fda4194fd23b5a59fafe15a48c07e20604fb7671209c7e2c19e
fetched_at: '2026-07-02T19:24:27.936205+00:00'
page_id: '697697806'
product: protheus
source: tdn-tec
title: Melhoria - Adicionado parametro função GetClientIP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697697806
version: 1
---

|  |  |
| --- | --- |
| Situação | Função GetClientIP retornava sempre o IP do Broker quando estava utilizando o mesmo para conexão entre o Smartclient e o Appserver |
| Ocorrência | Quando o smartclient estava se conectando através de um Broker, a função GetClientIP sempre retornava o IP do broker |
| Melhoria | Foi criado um parametro logico opcional, que quando passado verdadeiro, o AppServer envia uma mensagem ao Smartclient e o mesmo envia o IP real o qual ele esta utilizando para se conectar ao Broker e do Broker ao Appserver. |
| Informações adicionais | * Referente à ocorrência: [DTCLIENT01-3409](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-3409) * Disponível em builds superiores a 20.3.1.0 do Smartclient e AppServer |
