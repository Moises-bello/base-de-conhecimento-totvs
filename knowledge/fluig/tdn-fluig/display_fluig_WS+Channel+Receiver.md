---
content_hash: 7c71ba7aa2458b732a0e91bcee2140d716660aebcd71e2de39cbf8eac2285012
fetched_at: '2026-06-28T21:35:27.962642+00:00'
page_id: '6066548'
product: fluig
source: tdn-fluig
title: WS Channel Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/WS+Channel+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é receber as mensagens enviadas de um dispositivo externo para o Fluig ESB via Web Service.

Este componente cria um serviço passivo de Web Service, aguardando que outros serviços se conectem a ele, ao contrário do WS Receiver, que invoca um Web Service para colher as informações.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do receiver WS Channel. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |

Ao contrário dos outros objetos, que possuem propriedades de destino, o receiver WS Channel utiliza o nome do objeto como sendo o nome do canal de onde será obtida a informação.
