---
content_hash: 79f068248c68df171878557f9acc8e4eb33babe2af09bdb0fe0cae37fea58124
fetched_at: '2026-07-02T19:24:28.609156+00:00'
page_id: '799252481'
product: protheus
source: tdn-tec
title: tSFTPClient:RemoveFile
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3ARemoveFile
version: 2
---

Remove um arquivo hospedado no servidor SFTP remoto.

## Sintaxe

```
tSFTPClient():RemoveFile(< cFilename >)
```

## Parâmetros

Os parâmetros que a função recebe, estão descritos conforme:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cFileName | caractere | Nome do arquivo no servidor remoto que será removido. | X |  |

## Retorno

Conforme a Tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectado erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da tentativa de excluir o arquivo do servidor SFTP. |

## Exemplo

Neste exemplo, um arquivo é criado e em seguida removido.

```
user function sftp_remove_file()

  local nRet1, nRet2, nRet3
  local oSftp1 = tSFTPClient():new()

  nRet1 := oSftp1:Connect(REMOTE_SFTP_SERVER,REMOTE_SFTP_SERVER_PORT,TTESTUSER_NAME, TESTUSER_PASSWORD)
  if (nRet1 <> 0)
    conOut("Falha ao conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:MakeFile("remover_arquivo.txt")
  if (nRet2 <> 0)
    ConOut("Falha ao criar o arquivo")
    return .F.
  endif

  nRet3 := oSftp1:RemoveFile("remover_arquivo.txt")
  if (nRet3 <> 0)
    ConOut("Falha ao remover o arquivo")
    return .F.
  endif

return .T.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_REMOVEFILE\_OK | Operação executada com sucesso |
| -10 | SFTP\_REMOVEFILE\_FAIL | Falha na tentativa de remover o arquivo do servidor SFTP |
