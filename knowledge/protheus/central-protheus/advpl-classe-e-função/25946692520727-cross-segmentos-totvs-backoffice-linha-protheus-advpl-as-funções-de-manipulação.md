---
article_id: 25946692520727
category: ADVPL - Classe e Função
content_hash: 85e6ad1254cfe62d91451d46128f0824c79baf15f3c14b697d81705bcc4adfa5
fetched_at: '2026-06-28T22:40:21.580097+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - As funções de manipulação
  de arquivo (FOpen, FCreate, FRead, FClose) funcionam via schedule?
type: support-article
updated_at: '2026-01-20T14:44:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25946692520727-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-As-fun%C3%A7%C3%B5es-de-manipula%C3%A7%C3%A3o-de-arquivo-FOpen-FCreate-FRead-FClose-funcionam-via-schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25946719726231) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**As funções de manipulação de arquivo (FOpen, FCreate, FRead, FClose) funcionam via schedule?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Sim. As funções de manipulação de arquivo (FOpen, FCreate, FRead, FClose) podem ser utilizados via schedule.

\*\*Lembrando que o acesso ao diretório é apenas ao Rootpath (Protheus\_DATA) em estado de job.

**Exemplo**

```
User Function exemplo()  
  
Local cFile := ""// VALORES RETORNADOS NA LEITURA  
Local oFile := FwFileReader():New('\imp\1.pdf') // CAMINHO ABAIXO DO ROOTPATH  
  
RpcSetEnv("99","01")  
  
// SE FOR POSSÍVEL ABRIR O ARQUIVO, LEIA-O  
// SE NÃO, EXIBA O ERRO DE ABERTURA  
If (oFile:Open())  
cFile := oFile:FullRead() // EFETUA A LEITURA DO ARQUIVO  
lSuccess:= .T.  
nHandle:=FCREATE("\teste\1.pdf")  
FWrite(nHandle, cFile)  
FClose(nHandle)  
else  
lSuccess:= .F.  
endif  
  
Return
```

**Saiba mais:**

[Manipulação de arquivos, discos e IO](https://tdn.totvs.com/pages/viewpage.action?pageId=6063692)
