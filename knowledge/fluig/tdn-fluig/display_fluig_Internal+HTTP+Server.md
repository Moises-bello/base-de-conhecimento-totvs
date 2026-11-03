---
content_hash: 5c161113e3eaeed29fb1063d60fc3ef659119ee2dd77a4f35acd0e5bece47533
fetched_at: '2026-06-28T21:35:27.925133+00:00'
page_id: '6066536'
product: fluig
source: tdn-fluig
title: Internal HTTP Server
type: documentation
url: https://tdn.totvs.com/display/fluig/Internal+HTTP+Server
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

Na aba Internal HTTP Server é possível realizar as configurações do servidor HTTP e Web Service do Fluig ESB. A tela está dividida apropriadamente em três grupos: Internal HTTP Server, HTTP Channel, WS Channel.

### Internal HTTP Server

Permite realizar as configurações gerais do servidor HTTP e Web Service do  Fluig ESB.

| Campo | Descrição |
| --- | --- |
| Port | Porta onde deverá ser executado o servidor HTTP. Por padrão, a porta é 8085. |
| SSL | Habilita a autenticação de segurança, caso deseje que o servidor HTTP possua SSL. |
| SSL Port | Porta onde deverá ser executado o servidor HTTP com autenticação SSL. Por padrão, a porta é 443. |
| Keystore | Informe, buscando através do botão 'Upload' o keystore previamente gerado pelo órgão certificador que será utilizado pelo HTTP Server na conexão SSL. |
| Password | Informe a senha do keystore que será utilizado pelo HTTP Server na conexão SSL. |
| Alias Password | Inserir a senha do certificado. |

Caso a opção **SSL** seja habilitada, o Fluig ESB somente permitirá conexões HTTPS (modo seguro) tanto para conexões via HTTP e Web Services.

Ao realizar as configurações necessárias para opção SSL informando 'Keystore' e 'Password' corretamente é feito upload do arquivo .jks no diretório conf do Fluig ESB.

### HTTP Channel

No grupo **HTTP Channel** é possível realizar configurações do servlet que será utilizado para os componentes: HTTPChannel Receiver, HTTPChannel Sender, HTTP Receiver e HTTP Sender.

| Campo | Descrição |
| --- | --- |
| Name | Nome do serviço HTTPChannel. |

Para verificar se o componente HTTPChannel interno do Fluig ESB está ativo, basta acessar a seguinte URL:http://[servidor]:[porta]/[nameServiceHttpChannel]?hello

Será exibida a mensagem **Hello**, o endereço IP da estação e a mensagem **The service is running properly**.

### WS Channel

Realiza configurações do servlet que será utilizado para os componentes: WSChannel Receiver e WSChannel Sender.

| Campo | Descrição |
| --- | --- |
| Path | Diretório de localização do web service. |
| Service Name | Nome do serviço que será utilizado. |
| Namespace | URL de definição do namespace. |
| Time Out | Tempo em segundos para que o usuário seja notificado quando o recurso não estiver respondendo. |

O subgrupo **WSDL 1.1** permite configurar os tipos de dados utilizados pelo servidor web service. Em subgrupo **WebServices** exibe ao usuário as informações configuradas nos campos anteriores.

Por meio desta, é possível visualizar informações sobre: **URL**, **WSDL**, **Use** e **Style**. Para conferir os serviços que estão disponíveis, basta acessar a URL: http://localhost:[porta]/ws

É possível acessar serviços passivos dos componentes WS Channel Sender ou Receiver, à espera de algum acionamento externo a partir desses métodos. Dentre os principais métodos disponíveis podemos citar:

* **retrieveMessage** e **retrieveMessageAsBinary** - Esta operação tem por objetivo retornar a primeira mensagem de um determinado canal de saída.
* **sendMessage** e **sendMessageAsBinary** - Esta operação tem por objetivo enviar uma mensagem a uma determinada fila de entrada do Fluig ESB de forma assíncrona.
* **sendMessageSync** – Esta operação tem por objetivo enviar uma mensagem a uma determinada fila de entrada do Fluig ESB de forma síncrona.
* **existService** - Esta operação tem por objetivo validar a existência de um determinado canal.
