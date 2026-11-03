---
content_hash: e23822a3e89e129d8408f6d36390748ce392e92297859c3de99d7a27a4842d27
fetched_at: '2026-07-02T19:24:28.588990+00:00'
page_id: '799252373'
product: protheus
source: tdn-tec
title: tSFTPClient:MakeFile
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AMakeFile
version: 3
---

Cria um arquivo vazio no servidor SFTP remoto respeitando o caminho de diretório fornecido.

## Sintaxe

```
tSFTPClient():MakeFile( < cFile > )
```

## Parâmetro

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cFile | caractere | Nome do arquivo a ser criado no servidor SFTP remoto. Deve ser informado caminho completo do arquivo. | X |  |

## Retorno

Conforme a tabela abaixo esta função retonará o valor numérico. Além disso, o console.log conterão informações importantes adicionais caso for detectados erros. | Retorno | Tipo | Descrição | |--|--|--| | nRet | numérico | Status da criação de arquivo no servidor SFTP. |

## Exemplo

```
user function sftp_makefile()

  local nRet1, nRet2, nRet3
  local oSftp1 := tSFTPClient():new()

  nRet1 := oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha ao conectar servidor SFTP ",nRet1)
    return .F.
  endif

  nRet2 := oSftp1:RemoveFile("c:/test/my_tlpp_test_file.txt")

  nRet3 := oSftp1:MakeFile("c:/test/my_tlpp_test_file.txt")
  if (nRet3 <> 0)
    conOut("Falha na tentativa de criar arquivo.",nRet3)
    return .F.
  endif
  
return .F.
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SFTP\_MKFILE\_OK | Operação executada com sucesso |
| -10 | SFTP\_MKFILE\_FAIL | Falha em criar o arquivo |
