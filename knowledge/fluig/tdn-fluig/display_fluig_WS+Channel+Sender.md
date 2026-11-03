---
content_hash: 01f2f6de632ebb294d18ccd031ede0827ef6d2065f4a99c15fedb508cf4a785b
fetched_at: '2026-06-28T21:35:27.965198+00:00'
page_id: '6066549'
product: fluig
source: tdn-fluig
title: WS Channel Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/WS+Channel+Sender
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é disponibilizar as mensagens no Fluig ESB para que um dispositivo externo recupere-as via Web Service.

Este componente cria um serviço passivo para o envio de informações através de um Web Service, ao contrário do WS Sender, que se conecta a Web Service externo para enviar as informações.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender WS Channel. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |

Ao contrário dos outros objetos, que possuem propriedades de destino, o sender WS Channel utiliza o nome do objeto como sendo o nome do canal onde será disponibilizada a informação.
