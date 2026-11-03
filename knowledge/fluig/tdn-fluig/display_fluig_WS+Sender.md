---
content_hash: 8bc00e92a494f345945a8b59c2df71643948589db51180fe116e77a07cc89df9
fetched_at: '2026-06-28T21:35:27.991835+00:00'
page_id: '6066553'
product: fluig
source: tdn-fluig
title: WS Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/WS+Sender
version: 15
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é enviar informações do Fluig ESB através de uma conexão Web Service.

Este componente faz com que o Fluig ESB invoque um Web Service (tanto interno quanto externo) para enviar as informações que foram geradas, ao contrário do WS Channel Sender que cria um serviço passivo e aguarda conexões externas para buscar estas informações. As configurações gerais para o componente estão descritas abaixo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender HTTP. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado, um registro da execução do sender será gravado no banco do Fluig ESB. |

O componente ainda possui configurações específicas que estão dividas nas seguintes abas:

## SOAP Request Settings

| Campo | Descrição |
| --- | --- |
| WSDL URL | Inserir o endereço utilizado na conexão com o web service. Informando o WSDL URL e estando conectado à internet o Fluig ESB é capaz de ler o WSDL e listar as operações disponíveis no campo **Operation** através do botão **List Operations**. |
| Operation | Selecionar o nome da operação a ser executada. |
| List Operations | Lista as operações definidas no WSDL e preenche o campo Operation se o campo WSDL Path não estiver configurado. |
| Tabela | A tabela define os parâmetros que a operação escolhida acima deve receber. A ordem dos parâmetros definidos na tabela deve respeitar a ordem definida na operação do web service. Os botões localizados ao lado direito da tabela servem para alternar a ordem dos parâmetros. Os campos disponíveis são:   * **Name**: Inserir uma identificação para o parâmetro. * **Data Type**: Inserir o tipo do parâmetro. (O ESB utiliza esse campo para fazer *parse* do valor informado). Poderá ser:   **Text**: quando o parâmetro a ser passado é String (texto);  **Number**: quando o parâmetro a ser passado é um número inteiro. Ex.: 150;  **Big Number**: quando o parâmetro a ser passado é um número inteiro, porém muito grande. Ex.: 152165894553;  **Decimal**: quando o parâmetro a ser passado é um número racional. Ex.: 150,33;  **Boolean**: quando o parâmetro a ser passado é um valor do tipo Verdadeiro ou Falso. Ex.: true;  **File**: quando o parâmetro a ser passado é um arquivo. No campo value deverá ser informado o caminho completo para o arquivo que se deseja enviar como parâmetro. Ex.: c:\temp\dados.xml.  **ESBMessage**: quando selecionado ele assume o valor do parâmetro com base no que é passado:  #: quando é passado o parâmetro “#” no “Value”, será utilizado o XML corrente da transação, que será convertido para String e enviado como parâmetro;  $XPATH: quando é passado o parâmetro “$XPATH” no campo “Value” o Fluig ESB irá pegar os valores com base no XPATH;  Valor: qualquer outro valor informado diferente de “#” e “$XPATH” no campo “Value” será tratado como String;  **XMLMessage**: quando selecionado, o Fluig ESB irá enviar como parâmetro o XML corrente da transação (em formato XML).  **Value**: Valor do parâmetro. |
| Use WS-Addressing | Quando selecionado, chama o serviço usando endereçamento conforme especificação [WS-Addressing](http://www.w3.org/Submission/ws-addressing/). |
| Use SOAP Action | Inclui o *header* SOAP Action na chamada HTTP do serviço. |
| Return Type | O componente WS Sender pode ter outros componentes ligados a ele que recebe uma mensagem de acordo com a configuração desse campos:   1. **Service Result**: envia o resultado da chamada do serviço para o próximo componente. 2. **Original Message**: envia a mensagem original recebida pelo WS Sender para o próximo componente. 3. **Both**: cria uma mensagem nova agregando a mensagem recebida no WS Sender mais a mensagem retornada pelo serviço. A mensagem criada segue o formato:  ... ... ]]> |

## WS-Security Settings

A aba **WS-Security Settings** configura opções relacionadas a segurança da mensagem.

Tem-se quatro abas distintas: **WS-Authentication**, **WS-Signature**, **WS-Encryption** e **HTTP Authentication**. Cada tabela a seguir apresenta opções contidos em cada aba:

### WS-Authentication

| Campo | Descrição |
| --- | --- |
| Use Username Token | Quando selecionado, indica que será utilizado autenticação nas mensagens de Web Service. |
| Username | Inserir o nome do usuário para a autenticação do serviço. |
| Password | Inserir a senha do usuário para a autenticação do serviço. |
| Password Type | Selecionar o tipo de senha.   * **Password Text**: senha como String. * **Password Digest:** senha codificada usando a função SHA-1 (*Secure Hash Algorithm*). |

### Aba WS-Signature

| Campo | Descrição |
| --- | --- |
| Use Digital Signature | Quando selecionado, indica que será utilizado assinatura digital nas mensagens de Web Service. |
| KeyStore | Inserir o nome do diretório onde está gravado o repositório de certificados para assinatura digital das mensagens de Web Service. |
| KeyStore Password | Inserir a senha do repositório de certificados. |
| Alias | Inserir o apelido do certificado dentro do *keystore*. |
| Alias Password | Inserir a senha do certificado. |

### Aba WS-Encryption

| Campo | Descrição |
| --- | --- |
| Use Cipher | Quando selecionado, indica que será utilizada criptografia nas mensagens de Web Service. |
| KeyStore | Inserir o nome do diretório onde está gravado o repositório de certificados para criptografia das mensagens de Web Service. |
| KeyStore Password | Inserir a senha do repositório de certificados. |
| Alias | Inserir o apelido do certificado dentro do *keystore*. |
| Alias Password | Inserir a senha do certificado. |

### Aba HTTP Authentication

| Campo | Descrição |
| --- | --- |
| Use HTTP Authentication | Quando selecionado, indica que será utilizado autenticação HTTP básica. |
| Username | Inserir o nome do usuário para a autenticação do serviço. |
| Password | Inserir a senha do usuário para a autenticação do serviço. |

## Timeout

A partir da atualização  é possível definir o tempo de *timeout*. A parametrização ocorre no arquivo timeout.xml localizado na pasta /conf, sendo 2 minutos o padrão (120000 milissegundos).

Exemplo para aumentar o tempo em 3 minutos é necessário modificar a tag *timeout* para 180000 milissegundos conforme:

180000
]]>
