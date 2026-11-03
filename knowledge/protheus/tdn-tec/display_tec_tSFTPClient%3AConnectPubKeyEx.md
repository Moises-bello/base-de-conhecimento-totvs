---
content_hash: c5f7a49d2feae7b542fa57376e9a7ae9987f8412e61c0a1744d42bb86ff19595
fetched_at: '2026-07-02T19:24:28.563009+00:00'
page_id: '799252040'
product: protheus
source: tdn-tec
title: tSFTPClient:ConnectPubKeyEx
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AConnectPubKeyEx
version: 6
---

Estabelece uma conexão com um servidor de SFTP ( SSH File Transfer Protocol ) utilizando o modo de autenticação por login e senha de usuário e ainda com um chave pública e senha desta chave registradas no INI do Application Server.

Este método se difere do ConnectPubKey pois realiza a autenticação em duas etapas (Usuário + Senha) e (Chaves Pública e Privada + Senha da Chave). É um caso especial onde o servidor SFTP encontra-se configurado para realizar autenticação múltipla por mais de um fator de autenticação.

## Pré-requisito

Para que a conexão com o servidor SFTP seja bem sucedida é preciso configurar as chaves pública e privada e a respectiva senha da chave pública na seção [SFTP] do arquivo de configuração do Application Server. Exemplo de como configurar:

```
[SFTP]
privatekey   = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa
publickey    = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa.pub
certpassword = m1nh4S3nH4fl3!SXHL3SSD
ShellExec    = 1
```

## Sintaxe

```
TSFTPClient():ConnectPubKeyEx( < cServer >, < cPort >, < cUser >, < cUserPassword > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cServer | caractere | Endereço do servidor SFTP a ser conectado | X |  |
| cPort | caractere | Número da porta do servidor SFTP | X |  |
| cUser | caractere | Login do usuário | X |  |
| cUserPassword | caractere | Senha do usuário | X |  |

## Retorno

Conforme a tabela abaixo, esta função retonará um valor numérico. Além disso, no arquivo console.log serão registradas informações adicionais importantes caso forem detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status de conexão ao servidor SFTP. |

## Exemplo

```
user function sftp_open_close_connection_ex1()

  local nRet1, nRet2
  Local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:ConnectPubKeyEx("server1.exemplo.local","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:Disconnect()
  if (nRet2 <> 0)
    conOut("Falha em desconectar ao servidor SFTP")
    return .F.
  endif

Return .T.
```

## Observações

Note que neste método de conexão, temos dois tipos de senhas que são a do usuário e a da chave pública, no entanto a senha da chave pública é configurada no arquivo de configuração do Application Server.

Segue a lista de códigos de status de retorno indicando sucesso ou falha de conexão:

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_OK | Sucesso de conexão ao servidor SFTP |
| -1 | SFTP\_HOST\_NOT\_FOUND | Servidor remoto não encontrado |
| -2 | SFTP\_SOCKET\_FAIL | Falha no socket da conexão |
| -3 | SFTP\_CONNECTION\_FAIL | Falha ao conectar no servidor remoto |
| -4 | SFTP\_SESSION\_INIT\_FAIL | Falha ao inicializar o socket |
| -5 | SFTP\_HANDSHAKE\_FAIL | Falha no HandShake da camada SSH |
| -6 | SFTP\_SFTP\_INIT\_FAIL | Falha ao inicializar o subsistema de SFTP |
| -28 | SFTP\_KNOWNHOSTS\_READ\_FAIL | Falha ao realizar leitura do host |
| -30 | SFTP\_KNOWNHOSTS\_FINGERPRINT\_FAIL | Falha ao realizar leitura da assinatura |
| -31 | SFTP\_KNOWNHOSTS\_MISMATCH | Assinatura não-conforme no arquivo de KNOWNHOSTS |
| -32 | SFTP\_KNOWNHOSTS\_NOTFOUND | Assinatura não-encontrada no arquivo de KNOWNHOSTS |
| -33 | SFTP\_KNOWNHOSTS\_CHECK\_FAILURE | Falha ao verificar o arquivo de KNOWNHOSTS |
