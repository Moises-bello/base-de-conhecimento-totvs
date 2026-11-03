---
content_hash: 7a5a150016b57b75ea03a2f984de81c92cbedda96597bfced20b5f32acdb1e94
fetched_at: '2026-07-02T19:24:28.581854+00:00'
page_id: '799252128'
product: protheus
source: tdn-tec
title: tSFTPClient:GetMLCount
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AGetMLCount
version: 2
---

Retorna a quantidade de linhas do buffer de resposta após executar o método ShellExec() da classe TSFTPClient.

## Sintaxe

```
tSFTPClient():GetMLCount()
```

## Retorno

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Número de linhas do buffer de resposta do server para a instrução executada via método ShellExec. Em caso de falha irá retorno o código -1. |

## Exemplo

```
user function sftp_getmlcount()

  local nRet1, nRet2, nRet3
  local oSftp1 := tSFTPClient():new()

  nRret1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:ShellExec("file --help")
  if (nRet2 <> 0)
    conOut("Falha em executar comando remoto no servidor SFTP")
    return .F.
  endif

  nRet3 := oSftp1:GetMLCount()
  if (nRet3 < 0)
    conOut("Falha em recuperar o tamanho do buffer de resposta ")
    return .F.
  endIf
  
  conOut("### Quantidade de linhas presente no buffer: ", nRet3)

Return .T.
```

## Observação

Para utilizar esta função é necessário que a chave ShellExec=1 esteja setada dentro do INI do Aplication Server.
