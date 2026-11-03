---
content_hash: 9ac1a947de36cc9a51d55e1af2b8a38dae2cdb10c22fbcfcfa775a7ee2798e1e
fetched_at: '2026-06-28T21:35:27.972288+00:00'
page_id: '6066551'
product: fluig
source: tdn-fluig
title: HTTP Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/HTTP+Sender
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é enviar informações do Fluig ESB através de protocolo HTTP.

Este componente envia informações para um sistema externo através de uma conexão HTTP, conectando-se ao servidor, ao contrário do HTTP Channel Sender, que cria um serviço passivo e aguarda um sistema externo se conectar a ele para buscas as informações.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender HTTP. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |
| Queue Name | Inserir o nome da fila a ser utilizada para a comunicação HTTP. Este campo serve para quando se precisa mandar informações para outro diagrama no Fluig ESB, que possui um HTTPChannelReceiver. |
| Host Name | Inserir o nome do host a ser utilizado para a comunicação HTTP. Caso a porta a ser utilizada não seja a padrão (8085), é necessário informar a porta a ser utilizada. Ex.: localhost:8088, caso a porta a ser utilizada seja a 8088. |
| SSL | Quando selecionado, indica que o serviço suporta uma conexão segura (HTTPS). |
| Service | Inserir o nome do serviço HTTP a ser solicitado. Este serviço pode ser configurado através das configurações do servidor **Internal HTTP Server / Grupo HTTP Channel** no campo **Name**. Se este campo for deixado em branco, o Fluig ESB utilizará o valor padrão: **/servlet/TOTVSHTTPChannel**. |
| Authorization | Inserir o código de identificação que permite a autenticação com um serviço TOTVS. |
| Return Type | O componente HTTPSender pode ter outros componentes ligados a ele que recebe uma mensagem de acordo com a configuração desse campos:  1. **Service Result**: envia o resultado da chamada do serviço para o próximo componente. 2. **Original Message**: envia a mensagem original recebida pelo HTTPSender para o próximo componente. 3. **Both:** cria uma mensagem nova agregando a mensagem recebida no HTTPSender mais a mensagem retornada pelo serviço. A mensagem criada segue o formato:  ... ... ]]> |
