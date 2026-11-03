---
content_hash: 113d413d7d8e74f4698286ea1c690eb3506f2cf3436c3a462953164c720a6f92
fetched_at: '2026-07-02T19:24:28.570926+00:00'
page_id: '799252091'
product: protheus
source: tdn-tec
title: tSFTPClient:Disconnect
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3ADisconnect
version: 2
---

Encerra a conexão com o Servidor SFTP remoto.

## Sintaxe

```
tSFTPClient():Disconnect()
```

## Exemplo

```
user Function sftp_disconnect()

  local nRet1, nRet2
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:Disconnect()
  if (nRet2 <> 0)
   conOut("Falha em desconectar do servidor SFTP")
   return .F.
  endif

Return .T.
```

## Retorno

Conforme a Tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da desconexão do servidor SFTP. |

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_SUCCESS | Sucesso ao desconectar |
| -8 | SFTP\_SSH2\_SHUTDOWN\_FAIL | Falha ao desligar o subsistema na camada SSH2 |
| -9 | SFTP\_SESSION\_DISCONNECT | Falha em desconectar a sessão SFTP/SSH2 |
