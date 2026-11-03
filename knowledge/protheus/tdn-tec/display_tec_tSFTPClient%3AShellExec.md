---
content_hash: 8aa5fadc9256ea5822e969c39a3f1b462ebb93828a78fa0bd2444a30892bc74f
fetched_at: '2026-07-02T19:24:28.617159+00:00'
page_id: '799252491'
product: protheus
source: tdn-tec
title: tSFTPClient:ShellExec
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AShellExec
version: 2
---

Envia um comando customizado para o servidor remoto via SSH.

## Sintaxe

```
tSFTPClient():ShellExec( < cCommand > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cCommand | caractere | Comando para ser executado no SHELL do servidor remoto | X |  |

## Retorno

Conforme a tabela abaixo esta função retonará o valor numérico. Além disso, o console.log conterão informações importantes adicionais caso for detectados erros.

Conforme a tabela abaixo esta função retornará os seguintes status:

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da execução do comando no servidor SFTP. |

## Exemplo

```
user function sftp_shellexec() 

  local nRet1, nRet2, nRet3
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    ConOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:ShellExec("echo 1234567890abcdefgh > quoteOK_TLPP.txt")
  if (nRet2 <> 0)
    ConOut("Falha em executar o comando no Shell remoto do servidor")
    return .F.
  endif

return .T.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_SHELLEXEC\_OK | Operação executada com sucesso |
| -10 | SFTP\_SHELLEXEC\_FAIL | Falha ao executar o comando Shell no servidor SFTP |
