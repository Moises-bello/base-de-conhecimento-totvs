---
content_hash: d6bff5f69ccdbeb1e2ae581867c3d9f74569349239e83aee3765e3d654dc35c9
fetched_at: '2026-06-28T21:35:28.005650+00:00'
page_id: '6066554'
product: fluig
source: tdn-fluig
title: WS Sync Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/WS+Sync+Sender
version: 9
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é enviar uma mensagem de retorno ao Web Service caso este esteja funcionando de forma síncrona (necessita de uma resposta para que continue seu ciclo). O componente WS Synchronous Sender trabalha de forma síncrona, ou seja, ele sempre irá utilizar métodos como o SendMessageSync.

Caso o método Sync não seja utilizado, não será necessário utilizar este componente, e será retornada no log uma mensagem de erro, informando que o método utilizado não é síncrono.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender WS Synchronous Sender. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |
