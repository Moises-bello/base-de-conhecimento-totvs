---
content_hash: f693465e63754cc922bb70e33514441ab9d8fe47fc4dba8d3998e566bfcd58a7
fetched_at: '2026-07-02T19:24:28.578892+00:00'
page_id: '799252110'
product: protheus
source: tdn-tec
title: tSFTPClient:GetLastResponse
type: documentation
url: https://tdn.totvs.com/display/tec/tSFTPClient%3AGetLastResponse
version: 2
---

Retorna a resposta do último comando executado no servidor SFTP remoto. É importante observar que este código de erro é utilizado normalmente para diagnóstico, uma vez que está relacionado a camada SSH.

## Sintaxe

```
tSFTPClient():GetLastResponse( < cRefLastResponse > )
```

## Parâmetro

Os parâmetros que esta função recebe são descritos abaixo:

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cRefLastResponse | caractere | Variável de referência para retorno da mensagem de erro. | X | X |

## Retorno

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Código de String com a resposta do último comando que foi executado no servidor SFTP. |

A descrição do último erro ocorrido é retornada na variável por referência enviada como parâmetro.

## Exemplo

```
user Function sftp_getlastresponse()

  local nRet1, nRet2, cLastMsg
  local oSftp1 := tSFTPClient():new()

  nRet1 = oSftp1:Connect("server1.exemplo.local.br","2222","josevitor", "Fs74!@bz*@54/")
  if (nRet1 <> 0)
    conOut("Falha em conectar ao servidor SFTP")

    nRet2 := oSftp1:GetLastResponse(cLastMsg)

    conOut("### Código de erro: ", nRet2)
    conOut("### Última Mensagem: ", cLastMsg)
  endif

Return
```

### Lista de códigos de erros e seus respectivos significados

| Código | Símbolo | Descrição |
| --- | --- | --- |
| 0 | SSH2\_FX\_OK | Operação executada com sucesso |
| 1 | SSH2\_FX\_EOF | Final de arquivo |
| 2 | SSH2\_FX\_NO\_SUCH\_FILE | Arquivo não encontrado |
| 3 | SSH2\_FX\_PERMISSION\_DENIED | Permissão negada |
| 4 | SSH2\_FX\_FAILURE | Falha na camada SFTP |
| 5 | SSH2\_FX\_BAD\_MESSAGE | Mensagem incorreta retornada pelo servidor |
| 6 | SSH2\_FX\_NO\_CONNECTION | Não conectado |
| 7 | SSH2\_FX\_CONNECTION\_LOST | Conexão perdida com o servidor SFTP remoto |
| 8 | SSH2\_FX\_OP\_UNSUPPORTED | Operação não suportada |
| 9 | SSH2\_FX\_INVALID\_HANDLE | Handler inválido |
| 10 | SSH2\_FX\_NO\_SUCH\_PATH | Caminho de diretório não encontrado |
| 11 | SSH2\_FX\_FILE\_ALREADY\_EXISTS | Arquivo já existente |
| 12 | SSH2\_FX\_WRITE\_PROTECT | Proteção de arquivo ativa |
| 13 | SSH2\_FX\_NO\_MEDIA | Mídia não encontrada |
| 14 | SSH2\_FX\_NO\_SPACE\_ON\_FILESYSTEM | Sem espaço no sistema de arquivos |
| 15 | SSH2\_FX\_QUOTA\_EXCEEDED | Quota de disco excedida |
| 16 | SSH2\_FX\_UNKNOWN\_PRINCIPLE | Principle Desconhecido |
| 17 | SSH2\_FX\_LOCK\_CONFlICT | Conflito de Lock |
| 18 | SSH2\_FX\_DIR\_NOT\_EMPTY | Diretório não-vazio |
| 19 | SSH2\_FX\_NOT\_A\_DIRECTORY | Diretório inválido |
| 20 | SSH2\_FX\_INVALID\_FILENAME | Nome de arquivo inválido |
| 21 | SSH2\_FX\_LINK\_LOOP | Loop de Link |
