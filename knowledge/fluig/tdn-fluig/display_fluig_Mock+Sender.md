---
content_hash: bdc286125200de412d15bdc8d2049ea4d2e2f583de16963e6ff4c2a22ad551c6
fetched_at: '2026-06-28T21:35:28.105744+00:00'
page_id: '6066581'
product: fluig
source: tdn-fluig
title: Mock Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/Mock+Sender
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é enviar uma mensagem de retorno ao Web Service caso este esteja funcionando de forma síncrona (necessita de uma resposta para que continue seu ciclo).

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender Mock Sender. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |
