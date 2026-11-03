---
content_hash: 898fa8f75659965f9f4f03c81221a870e09241ed653aa6d51fd80b4973ee0b64
fetched_at: '2026-07-02T19:24:28.601014+00:00'
page_id: '799252459'
product: protheus
source: tdn-tec
title: tSFTPClient:ReceiveFile
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AReceiveFile
version: 4
---

Trasfere um arquivo do servidor remoto para a máquina local.

## Sintaxe

```
TSFTPClient():ReceiveFile(< cLocalFile > , < cRemoteFile >)
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cLocalFile | caractere | Caminho completo (pasta + nome do arquivo) que será dado ao arquivo na máquina local. | X |  |
| cRemoteFile | caractere | Caminho completo (pasta + nome do arquivo) do arquivo no servidor remoto que será transferido. | X |  |

## Retorno

Conforme a Tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da tentativa de transferência do arquivo do servidor para máquina local. |

## Exemplo

```
user function sftp_download1()

  local nRet1, nRet2
  local oSftp1 := tSFTPClient():new()
  
  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    ConOut("Falha em conectar ao servidor SFTP.")
    return .F.
  endif

  nRet2 := oSftp1:ReceiveFile("downloadedTLPP_OK.txt","./somefileA.txt")
  if (nRret2 <> 0)
    ConOut("Falha em transferir um arquivo do servidor SFTP.")
    return .F.
  endif

return .T.
```

## Observação

Caso o arquivo apontado por cLocalFile já exista, ele será sobrescrito. Esse caminho é relativo ao ROOTPATH do Application Server. Caso o caminho de diretório não exista, a função retornará um código de erro.

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_RECEIVEFILE\_OK | Operação de transferência de arquivo executada com sucesso |
| -24 | SFTP\_SFTP\_REMOTE\_PATH\_FAIL | Caminho de diretório não reconhecido no servidor SFTP |
| -23 | SFTP\_SFTP\_OPEN\_FILE\_FAIL | Falha na abertura do arquivo do servidor para iniciar a transferência |
| -26 | SFTP\_TIMEOUT\_FAIL | Tempo de transferência excedido |
