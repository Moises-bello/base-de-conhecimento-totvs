---
content_hash: 63a315f94d05b5c4298b50a68261fce174391c41da5a0fcce4104c1f65b02ac2
fetched_at: '2026-06-28T21:35:27.968296+00:00'
page_id: '6066550'
product: fluig
source: tdn-fluig
title: HTTP Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/HTTP+Receiver
version: 12
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é receber informações no Fluig ESB através de protocolo HTTP.

Este componente se conecta a um servidor HTTP para buscar as informações que necessita, ao contrário do HTTP Channel Receiver, que cria um serviço passivo e aguarda conexão externa.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do receiver HTTP. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Queue Name | Inserir o nome da fila a ser utilizada para a comunicação HTTP. Este campo serve para quando for preciso mandar informações para outro diagrama no Fluig ESB, que possui um HTTPChannelSender. |
| Host Name | Inserir o nome do host a ser utilizado para a comunicação HTTP. |
| SSL | Quando selecionado, indica que o serviço suporta uma conexão segura (HTTPS). |
| Service | Inserir o nome do serviço HTTP a ser solicitado. Este serviço pode ser configurado através das configurações do servidor **Internal HTTP Server / Grupo HTTP Channel** no campo **Name**. Se este campo for deixado em branco, o Fluig ESB utilizará o valor padrão: **/servlet/ESBHTTPChannel**. |
| Authorization | Inserir o código de identificação que permite a autenticação com um serviço TOTVS. |
