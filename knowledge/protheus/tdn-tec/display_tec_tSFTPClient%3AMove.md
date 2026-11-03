---
content_hash: cd985e29d33877a52702e121a69fdf3339c6c670cea6de4664fbd80fe2631528
fetched_at: '2026-07-02T19:24:28.593853+00:00'
page_id: '799252391'
product: protheus
source: tdn-tec
title: tSFTPClient:Move
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AMove
version: 3
---

Permite que um arquivo hospedado em um servidor SFTP remoto possa ser renomeado ou até transferido de uma pasta para outra.

## Sintaxe

```
tSFTPClient():Move( < cOldName >, < cNewName > )
```

## Parâmetros

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cOldName | caractere | Caminho e nome do arquivo no servidor SFTP remoto que será movido ou renomeado. | X |  |
| cNewName | caractere | Novo nome e/ou caminho de diretório que será assumido pelo arquivo no servidor SFTP. | X |  |

## Retorno

Conforme a tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Status da tentativa de mover ou renomear arquivo no servidor SFTP. |

## Exemplo

```
user function sftp_rename_file()

  local nRet1, nRet2, nRet3
  local oSftp1 := tSFTPClient():new()

  nRet1 := sftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    ConOut("Falha em conectar ao servidor SFTP")
    return .F.
  endif

  //eliminar previamente os arquivos existentes
  oSftp1:RemoveFile("TLPPrename.txt")
  oSftp1:RemoveFile("renamedTLPP.txt")

  //criar novos arquivos
  nRet2 := oSftp1:MakeFile("TLPPrename.txt")
  if (nRet2 <> 0)
    ConOut("Falha em criar um arquivo para testes no servidor SFTP")
    return .F.
  endif

  nRet3 := oSftp1:Move("TLPPrename.txt", "renamedTLPP.txt")
  if (nRet3 <> 0)
    ConOut("Falha em renomear o arquivo")
    return .F.
  endif

return .T.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_MOVEFILE\_OK | Operação executada com sucesso |
| -10 | SFTP\_MOVEFILE\_FAIL | Falha em mover ou renomear o arquivo |
