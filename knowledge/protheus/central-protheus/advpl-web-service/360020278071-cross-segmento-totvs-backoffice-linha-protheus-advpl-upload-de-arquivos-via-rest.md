---
article_id: 360020278071
category: ADVPL - Web Service
content_hash: 7144601a618058176efe8550b35d9a57eb34a44c5fb7a47cfdc0f01039612ad7
fetched_at: '2026-06-28T22:40:10.525276+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -Upload de arquivos
  via rest
type: support-article
updated_at: '2025-03-17T16:24:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020278071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Upload-de-arquivos-via-rest
---

**Dúvida**Como enviar um arquivo por meio de uma requisição REST?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para retornar qualquer arquivo via serviço REST basta ler o arquivo com a classe de sua preferência (por performance indicamos a utilização da classe FwFileReader() utilizando o método FullRead()).

Após a leitura envie o arquivo e o cabeçalho abaixo, pois eles indicam que o download do arquivo pode ser realizado pelo navegador (caso a chamada ocorra por meio do mesmo).

Importante: Somente é possível manipular arquivos abaixo do RootPath do Protheus.  
  
**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
#Include "RESTFUL.ch"  
  
// DECLARAÇÃO DO SERVIÇO REST  
WSRESTFUL DOWNLOAD_FILE DESCRIPTION "Serviço para teste de envio de arquivo."  
    // DECLARAÇÃO DO MÉTODO GET  
    WSMETHODGET DESCRIPTION"Retorna um arquivo por meio do método FwFileReader()."  
END WSRESTFUL  
  
// MÉTODO GET  
WSMETHOD GET WSREST DOWNLOAD_FILE  
    Local cFile := ""// VALORES RETORNADOS NA LEITURA  
    Local oFile := FwFileReader():New("/NR5.pdf") // CAMINHO ABAIXO DO ROOTPATH  
  
    // SE FOR POSSÍVEL ABRIR O ARQUIVO, LEIA-O  
    // SE NÃO, EXIBA O ERRO DE ABERTURA  
    If (oFile:Open())  
        cFile := oFile:FullRead() // EFETUA A LEITURA DO ARQUIVO  
  
        // RETORNA O ARQUIVO PARA DOWNLOAD  
        Self:SetHeader("Content-Disposition", "attachment; filename=NR5.pdf")  
        Self:SetResponse(cFile)  
  
        lSuccess := .T. // CONTROLE DE SUCESSO DA REQUISIÇÃO  
    Else  
        SetRestFault(002, "can't load file") // GERA MENSAGEM DE ERRO CUSTOMIZADA  
  
        lSuccess := .F. // CONTROLE DE SUCESSO DA REQUISIÇÃO  
    EndIf  
Return (lSuccess)
```

  
**Saiba mais**  
[REST ADVPL](http://tdn.totvs.com/display/framework/REST+ADVPL)  
[FWFILEREADER](http://tdn.totvs.com/display/framework/FWFileReader)  
[Download de arquivo via Rest](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024403851)
