---
content_hash: d13a7453ca8c4714958500e11c6558d3a05d16380a4494d9a9743102e7b1e138
fetched_at: '2026-07-02T19:24:28.604860+00:00'
page_id: '799252478'
product: protheus
source: tdn-tec
title: tSFTPClient:RemoveDirectory
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3ARemoveDirectory
version: 2
---

Apaga um diretório vazio no servidor remoto.

## Sintaxe

```
tSFTPClient():RemoveDirectory( < cDirectory > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cDirectory | caractere | Nome do diretório que será apagado no servidor remoto. | X |  |

## Retorno

Conforme a Tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da tentativa de eliminar o diretório do servidor SFTP. |

## Exemplo

```
user function sftp_remove_directory1() 

  local nRet1, nRet2
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    ConOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:RemoveDirectory("testedirA")
  if (nRet2 <> 0)
    ConOut("Falha em remover o diretório do servidor SFTP")
    return .F.
  endif

return .T.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_REMOVEDIR\_OK | Operação executada com sucesso |
| -10 | SFTP\_REMOVEDIR\_FAIL | Falha em remover o diretório |
