---
content_hash: 840001c87c92e1e25cf26e3fe7b79b96bb0922976a4b31d6afc21a62fccb7019
fetched_at: '2026-06-28T21:35:28.103176+00:00'
page_id: '6066580'
product: fluig
source: tdn-fluig
title: Mock Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/Mock+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade deste componente é simular ações que podem ser realizadas em um determinado Web Service.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do Mock Receiver. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Server | Ao clicar em "List Servers" são listados todos os servidores configurados no Fluig ESB. É necessário selecionar um deles para obter um Serviço e uma operação. |
| Service | Ao clicar em "List Services" são listados todos os serviços do servidor configurado no Fluig ESB. É necessário selecionar um deles para obter uma operação. |
| Operation | Ao clicar em "List Operations" são listadas todos as operações do servidor configurado no Fluig ESB. Selecionar uma delas. |
| Synchronous | Indica se o processo será síncrono ou assíncrono. Caso selecionado, indica que o mesmo espera uma resposta à sua requisição, portanto, se faz necessário a utilização do componente Mock Sender. |
