---
content_hash: 2f50e45660d63694e3fc5b45c5c4162040a49fdfcbaf450bd99209cc0155bbce
fetched_at: '2026-07-02T19:24:28.556239+00:00'
page_id: '799252030'
product: protheus
source: tdn-tec
title: tSFTPClient:ConnectPubKey
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AConnectPubKey
version: 6
---

Estabelece uma conexão com um servidor de SFTP ( SSH File Transfer Protocol ) utilizado o modo de autenticação por usuário com a chave publica e senha da chave publica.

## Pré-requisito

Para que a conexão com o servidor SFTP seja bem sucedida, é preciso configurar as chaves pública e privada e a respectiva senha da chave pública na seção [SFTP] do arquivo de configuração do AppServer. Exemplo de como configurar:

```
[SFTP]
privatekey   = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa
publickey    = D:\Keys\SFTPDEV_PREFERED\withpass\id_rsa.pub
certpassword = m1nh4S3nH4fl3!SXHL3SSD
ShellExec    = 1
```

## Sintaxe

```
TSFTPClient():ConnectPubKey( < cServer >, < cPort >, < cUser > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cServer | caractere | Endereço do servidor SFTP a ser conectado | X |  |
| cPort | caractere | Número da porta do servidor | X |  |
| cUser | caractere | Login do usuário | X |  |
| cUserPassword | caractere | Senha do usuário | X |  |

## Retorno

Conforme a Tabela abaixo esta função retonará o valor numérico. Além disso, o console.log conterão informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status de conexão ao servidor SFTP |

## Exemplo

```
user Function sftp_open_close_connection_ex2()

  local nRet1, nRet2
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:ConnectPubKey("server1.exemplo.local","2222","josevitor")
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

Note que neste método de conexão, temos dois tipos de senhas que são a do usuário e a da chave pública.

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
