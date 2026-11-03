---
content_hash: 78aea5274b1c2db9efd22dc2b0040febfa061ab213e7ebbea875b5e18539cc8f
fetched_at: '2026-06-28T21:35:27.957564+00:00'
page_id: '6066546'
product: fluig
source: tdn-fluig
title: HTTP Channel Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/HTTP+Channel+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

Criar um canal de entrada para recebimento de dados via protocolo HTTP. Cria um serviço passivo aguardando ser executado, ao contrário do HTTP Receiver, que busca as informações com base em um serviço HTTP.

| Campo | Descrição |
| --- | --- |
| Name | Nome para o componente HTTP Channel Receiver. Este nome será utilizado para sistemas externos enviarem informações para o Fluig ESB. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |

Ao contrário dos outros objetos, que possuem propriedades de destino, o receiver HTTP Channel utiliza o nome do objeto como sendo o nome do canal de onde será obtida a informação.
