---
content_hash: 8c215dc0ff06420bfd896d2a5e908dda61461d7c225554a6b8d23663f8a5ef01
fetched_at: '2026-06-28T21:35:27.960198+00:00'
page_id: '6066547'
product: fluig
source: tdn-fluig
title: HTTP Channel Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/HTTP+Channel+Sender
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é disponibilizar as mensagens no Fluig ESB para que um dispositivo externo recupere-as via HTTP.

Este componente cria um serviço passivo para envio de informações através do Fluig ESB, ao contrário do HTTP Sender que se conecta a um serviço HTTP para enviar as informações.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender HTTP Channel. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |

Ao contrário dos outros objetos, que possuem propriedades de destino, o sender HTTP Channel utiliza o nome do objeto como sendo o nome do canal onde será disponibilizada a informação.
