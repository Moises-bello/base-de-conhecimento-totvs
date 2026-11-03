---
content_hash: 14d51b5e76c219d4088928cfb86851e9fa767d8b3adbad193c32b5ac59133f3e
fetched_at: '2026-06-28T21:35:28.098384+00:00'
page_id: '6066578'
product: fluig
source: tdn-fluig
title: OnError
type: documentation
url: https://tdn.totvs.com/display/fluig/OnError
version: 9
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é definir ações a serem tomadas quando ocorrer algum erro no sistema.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Send As | Permite a seleção do tipo de mensagem a ser enviada.  * **ESB Message**: retorna para o próximo componente a mensagem original de entrada; * **Error Message**: envia para o próximo componente apenas o erro gerado pelo ESB * **ESB Exception (Both)**: retorna a mensagem original e o erro gerado. |

É importante lembrar que o componente OnError só pode ser ligado a um componente Receiver pois, caso ocorra algum erro em qualquer parte do processo, é ele que será acionado e sua configuração será executada. Sua saída pode ser redirecionada para o envio de e-mail, por exemplo.
