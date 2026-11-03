---
content_hash: 5e74677710e040d7e2a2c2584d71e236f326dba1f9783ba956ec9515dddd5480
fetched_at: '2026-07-02T19:24:28.567448+00:00'
page_id: '799252066'
product: protheus
source: tdn-tec
title: tSFTPClient:Directory
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3ADirectory
version: 2
---

Semelhante a função Directory da classe TFTPClient, lista os arquivos e diretórios do servidor SFTP remoto.

## Sintaxe

```
tSFTPClient():Directory( < cPath > )
```

## Parâmetro

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cPath | caractere | Caminho de diretório onde será feita a busca da lista de todos arquivos e subdiretórios. | X |  |

## Retorno

Conforme a tabela abaixo esta função retornará os seguintes valores numéricos. Além disso, o console.log conterá informações importantes adicionais caso for detectados erros.

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| aRet | vetor | Retorna um array de subarrays, sendo que cada subarray contém informações sobre cada arquivo que atenda o parâmetro *cPath*. |

## Exemplo

```
user function sftp_list_files()

  local nRet1, nI
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha ao conectar ao servidor SFTP")
    return .F.
  endif

  aListFiles := oSftp1:Directory("/download/")
  if (Len(aListFiles) == 0)
    conOut("Falha em listar os diretórios do servidor remoto")
    return .F.
  endif

  conOut("### Lista de arquivos:")
  For nI := 1 to len(aListFiles)
    //Listar nome do arquivo encontrado (posição 1 do subarray)
    conOut(aListFiles[nI][1])
  Next

return .T.
```

## Observações

O subarray de resposta tem a seguinte estrutura:

| Posição | Tipo | Informação |
| --- | --- | --- |
| 1 | caracter | Nome do arquivo |
| 2 | numérico | Tamanho do arquivo |
| 3 | data | Data da ultima alteração do arquivo |
| 4 | caracter | Hora do arquivo |
| 5 | caracter | Atributo do arquivo: no caso de diretório irá conter um 'D', caso contrário será vazio |
