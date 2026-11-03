---
article_id: 360023018071
category: ADVPL - Classe e Função
content_hash: d4ffe03b38178f2079ca7aca73ec975ba4a498f76e7ecfaf9cc3048e4b50f655
fetched_at: '2026-06-28T22:40:19.337033+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função FCREATE()
type: support-article
updated_at: '2022-01-10T18:44:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023018071-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-FCREATE
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Qual função posso utilizar para criar arquivos? **Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Cria um arquivo vazio no disco, para operação de escrita em modo exclusivo, com o tamanho de 0 (zero) bytes. Se o arquivo especificado já existe no disco, o arquivo é aberto em modo exclusivo, e seu conteúdo é eliminado ( truncado em 0 bytes ). Caso a operação não seja completa com sucesso, a função retorna o **handler** -1, caso contrário é retornado o **handler** de acesso ao arquivo, para operações de escrita.

```
#include "Fileio.ch"  
  
user function exemplo()  
local nHandle := FCREATE("\Testfile.txt")  
  
    if nHandle = -1  
        conout("Erro ao criar arquivo - ferror " + Str(Ferror()))  
    else  
        FWrite(nHandle, Time() + CRLF)  
        FClose(nHandle)  
    endif  
return
```

**Saiba mais**[FCreate](http://tdn.totvs.com/display/tec/FCreate)  
[FWrite](http://tdn.totvs.com/display/tec/FWrite)  
[Manipulação de arquivos, discos e IO](http://tdn.totvs.com/pages/viewpage.action?pageId=6063692)
