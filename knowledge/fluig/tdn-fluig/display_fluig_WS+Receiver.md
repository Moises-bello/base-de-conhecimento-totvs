---
content_hash: 075996fcf06b83eea79fd7603565915585c911cc828dfc143c2f28c47823f4ea
fetched_at: '2026-06-28T21:35:27.981804+00:00'
page_id: '6066552'
product: fluig
source: tdn-fluig
title: WS Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/WS+Receiver
version: 15
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é receber as mensagens enviadas de um dispositivo externo para o Fluig ESB via Web Service.

Este componente invoca um Web Service para colher as informações das quais necessita, ao contrário do WS Channel Receiver, que cria uma serviço passivo, aguardando outros sistemas se conectarem a ele para buscar as informações. As configurações gerais para o componente estão descritas abaixo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do receiver WS. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |

O componente ainda possui configurações específicas que estão dividas nas seguintes abas:

## SOAP Request Settings

| Campo | Descrição |
| --- | --- |
| WSDL URL | Inserir o endereço utilizado na conexão com o web service. Informando o WSDL URL e estando conectado à internet o Fluig ESB é capaz de ler o WSDL e listar as operações disponíveis no campo **Operation** através do botão **List Operations**. |
| Operation | Selecionar o nome da operação a ser executada. |
| Soap Action | Identificar qual ação do protocolo SOAP deve ser executada. |
| Tabela | A tabela define os parâmetros que a operação escolhida acima deve receber. A ordem dos parâmetros definidos na tabela deve respeitar a ordem definida na operação do web service. Os botões localizados ao lado direito da tabela servem para alternar a ordem dos parâmetros. Os campos disponíveis são:   * **Name:** Inserir uma identificação para o parâmetro. Este valor é utilizado apenas no Fluig ESB como uma identificação para o Editor,não tendo a necessidade de manter o mesmo nome do campo do XML. * **Data Type**: Inserir o tipo do parâmetro. (O Fluig ESB utiliza esse campo para fazer parse do valor informado.). Poderá ser: **Text**: quando o parâmetro a ser passado é String (texto); **Number**: quando o parâmetro a ser passado é um número inteiro. Ex.: 150; **Big Number**: quando o parâmetro a ser passado é um número inteiro, porém muito grande. Ex.: 152165894553; **Decimal**: quando o parâmetro a ser passado é um número racional. Ex.: 150,33; **Boolean**: quando o parâmetro a ser passado é um valor do tipo Verdadeiro ou Falso. Ex.: true; **File**: quando o parâmetro a ser passado é um arquivo. No campo value deverá ser informado o caminho completo para o arquivo que se deseja enviar como parâmetro. Ex.: c:\temp\dados.xml. * **Value**: Valor do parâmetro |

## WS-Security Settings

| Campo | Descrição |
| --- | --- |
| Use Username Token | Quando selecionado, indica que será utilizado autenticação nas mensagens de Web Service. |
| Username | Inserir o nome do usuário para a autenticação do serviço. |
| Password | Inserir a senha do usuário para a autenticação do serviço. |
| Password Type | Selecionar o tipo de senha.   * **Password Text**: senha como String. * **Password Digest:** senha codificada usando a função SHA-1 (*Secure Hash Algorithm*). |

## STS Settings

A aba STS Settings habilita as possíveis configurações de autenticação com servidores STS. Segue abaixo a descrição dos parâmetros de configuração para autenticação com serviços STS:

| Campo | Descrição |
| --- | --- |
| Use STS | Permite habilitar/desabilitar autenticação com servidores STS. |
| WSDL URL | Exibe o endereço WSDL do serviço de autenticação STS. |
| Service Name | Exibe o nome do serviço de autenticação STS. |
| Endpoint Name | Exibe o nome do endpoint de autenticação STS. |

### STS Properties

| Campo | Descrição |
| --- | --- |
| Username | Inserir o nome do alias no armazenamento de chaves (keystore) para obter a chave pública do usuário para enviar para o STS (somente quando utilizar chave pública). |
| Keystore | Inserir o caminho do arquivo de armazenamento de chaves no formato JKS (Java Key Store) utilizado na autenticação com o servidor STS. |
| Keystore Password | Inserir a senha de acesso ao keystore. |
| Alias | Inserir o apelido do certificado dentro do keystore. |
| Alias Password | Inserir a senha do apelido do certificado. |

### WS-Authentication

| Campo | Descrição |
| --- | --- |
| Use Username Token | Quando selecionado, indica que será utilizada autenticação do tipo usuário/senha na comunicação com o Servidor STS. |
| Username | Inserir o nome do usuário para a autenticação com o servidor STS. |
| Password | Inserir a senha do usuário para a autenticação com o servidor STS. |
| Password Type | Selecionar o tipo de senha:  * **PasswordText:** senha como literal (string). * **PasswordDigest:** senha codificada usando a função SHA-1 (Secure Hash Algorithm). |

### WS-Signature

| Campo | Descrição |
| --- | --- |
| Use Digital Signature | Quando selecionado, indica que será utilizada assinatura digital para assinar as mensagens com o servidor STS. |
| Keystore | Inserir o caminho do arquivo de armazenamento de chaves no formato JKS (Java Key Store) utilizado na assinatura da mensagem. |
| Keystore Password | Inserir a senha de acesso ao keystore. |
| Alias | Inserir o apelido do certificado dentro do keystore. |
| Alias Password | Inserir a senha do apelido do certificado. |

### WS-Encription

| Campo | Descrição |
| --- | --- |
| Use Cipher | Quando selecionado, indica que será utilizada criptografia na troca de mensagens com o servidor STS. |
| Keystore | Inserir o caminho do arquivo de armazenamento de chaves no formato JKS (Java Key Store) utilizado na criptografia da mensagem. |
| Keystore Password | Inserir a senha de acesso ao keystore. |
| Alias | Inserir o apelido do certificado dentro do keystore. |
| Alias Password | Inserir a senha do apelido do certificado. |

### HTTP Authentication

| Campo | Descrição |
| --- | --- |
| Use HTTP Authentication | Quando selecionado, indica que será utilizado autenticação HTTP básica com o servidor STS. |
| Username | Inserir o nome do usuário para a autenticação. |
| Password | Inserir a senha para a autenticação. |
