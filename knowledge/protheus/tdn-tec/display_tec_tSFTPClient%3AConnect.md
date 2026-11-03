---
content_hash: a0c811fa5848feedcecd2668f1ffbbd83211845ebc406656d1099a92679d4e98
fetched_at: '2026-07-02T19:24:28.550336+00:00'
page_id: '799251963'
product: protheus
source: tdn-tec
title: tSFTPClient:Connect
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AConnect
version: 7
---

Estabelece uma conexão com um servidor SFTP ( SSH File Transfer Protocol ) utilizando o modo de autenticação por usuário e senha.

## Sintaxe

```
TSFTPClient():Connect( < cServer >, < cPort >, < cUser >, < cPassword > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cServer | caractere | Endereço do servidor SFTP a ser conectado | X |  |
| cPort | caractere | Número da porta do servidor SFTP | X |  |
| cUser | caractere | Login do usuário | X |  |
| cPassword | caractere | Senha do usuário | X |  |

## Retorno

Conforme a tabela abaixo, esta função retonará um valor numérico. Além disso, no arquivo console.log serão registradas informações adicionais importantes caso forem detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status de conexão ao servidor SFTP |

## Exemplo

```
user function sftp_open_close_connection()

  local nRet1, nRet2
  local oSftp1 = tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor","Fs74!@bz*@54/")
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

### Lista de códigos de erros e seus respectivos significados

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
