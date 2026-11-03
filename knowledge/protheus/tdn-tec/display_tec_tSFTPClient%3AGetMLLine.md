---
content_hash: 37afc50f9a53cddb3774928b0755fd8756195b1eeacb5f25ff9fdcab6c80cbff
fetched_at: '2026-07-02T19:24:28.585612+00:00'
page_id: '799252135'
product: protheus
source: tdn-tec
title: tSFTPClient:GetMLLine
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AGetMLLine
version: 3
---

Retorna o conteúdo de uma linha específica do buffer de resposta do server após executar uma instrução via método ShellExec.

## Sintaxe

```
tSFTPClient():GetMLLine( < nLine > )
```

## Parâmetro

Os parâmetros desta função estão descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nLine | numérico | Número da linha do buffer de resposta do servidor para a instrução executada via método ShellExec(). | X |  |

## Retorno

Conforme a Tabela abaixo esta função retonará o valor numérico. Além disso, o console.log conterão informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| cRet | caracter | String com o contéudo correspondente a respectiva linha do buffer de resposta do servidor para a execução do método ShellExec(). |

## Exemplo

```
user function sftp_getmlline()

  local nRet1, nRet2, cRet3
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  nRet2 := oSftp1:ShellExec("file --help")
  if (nRet2 <> 0)
    conOut("Falha em executar comando remoto no servidor SFTP")
    return .F.
  endif

  cRet3 := oSftp1:GetMLLine(13)
  if !empty(cRet3)
    conOut("### Conteúdo da linha 13 presente no buffer de resposta do método shellExec: ", cRet3)
  endIf
  
Return .T.
```

## Observação

Para utilizar esta função, é necessário que a chave ShellExec=1 esteja setada no arquivo de configuração do Application Server na seção [SFTP].
