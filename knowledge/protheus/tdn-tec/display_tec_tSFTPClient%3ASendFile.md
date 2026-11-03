---
content_hash: 38ec6aa5ad6635974fb9c48fe8786d8d91a16e49a4a049a4097daee01757738a
fetched_at: '2026-07-02T19:24:28.613330+00:00'
page_id: '799252487'
product: protheus
source: tdn-tec
title: tSFTPClient:SendFile
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3ASendFile
version: 2
---

Transfere um arquivo da máquina local para um servidor remoto.

## Sintaxe

```
tSFTPClient():SendFile( < cLocalFile >, < cRemoteFile > )
```

## Parâmetros

Os parâmetros que está função recebe são descritos pela a tabela abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cLocalFile | caractere | Nome do arquivo na máquina local que serão transferido para o servidor (caminho relativo ao RootPath do Protheus Server). | X |  |
| cRemoteFile | caractere | Nome que será dado ao arquivo no servidor remoto. | X |  |

## Retorno

Conforme a Tabela abaixo esta função retonará o valor numérico. Além disso, o console.log conterão informações importantes adicionais caso for detectados erros.

Conforme a Tabela abaixo esta função retornará os seguintes status | Retorno | Tipo | Descrição | |--|--|--| | nRet | numérico | Status da tentativa de transferir arquivo local para o servidor SFTP. |

## Exemplo

```
user function sftp_upload1()

  local nRet1, nRet2
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    ConOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:SendFile("jabutiFeliz.txt","uploadedOK_class.txt")
  if (nRet2 <> 0)
    ConOut("Falha em enviar o arquivo para o servidor SFTP")
    return .F.
  endif

return .T.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_UPLOADFILE\_OK | Operação executada com sucesso |
| -10 | SFTP\_UPLOADFILE\_FAIL | Falha em transferir o arquivo para o servidor SFTP remoto |
