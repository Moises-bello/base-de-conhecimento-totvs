---
article_id: 4410337748631
category: ADVPL - Classe e Função
content_hash: 1e1df1338cbe48993fc8a19948cf585276175f395e45809eb907c9ba2b38ba14
fetched_at: '2026-06-28T22:40:20.673851+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como corrigir a
  mensagem "Uso de Return dentro do BeginTransaction"
type: support-article
updated_at: '2021-10-08T18:35:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410337748631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-corrigir-a-mensagem-Uso-de-Return-dentro-do-BeginTransaction
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao utilizar o codeanalysis tivemos o retorno "**Uso de Return dentro do BeginTransaction**", como resolver?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Neste caso, é necessário encerrar a transação antes do return, para não ocorrer um divergência no banco de dados.

Segue um exemplo (<https://tdn.totvs.com/pages/viewpage.action?pageId=271843449>)

```
Function Grava01()  
  
BEGIN TRANSACTION  
  
//-------------------------------------------------------------------  
//Bloco de Gravação A  
//Dentro deste bloco será realizado alguma gravação no banco de dados  
//-------------------------------------------------------------------  
  
Grava02()  
  
//-------------------------------------------------------------------  
//Bloco de Gravação D  
//Dentro deste bloco será realizado alguma gravação no banco de dados  
//-------------------------------------------------------------------  
  
END TRANSACTION  
  
Return  
  
Function Grava02()  
  
BEGIN TRANSACTION  
  
//-------------------------------------------------------------------  
//Bloco de Gravação B  
//Dentro deste bloco será realizado alguma gravação no banco de dados  
//-------------------------------------------------------------------  
  
DisarmTransaction()  
  
Break  
  
//-------------------------------------------------------------------  
//Bloco de Gravação C  
//Dentro deste bloco será realizado alguma gravação no banco de dados  
//-------------------------------------------------------------------  
  
END TRANSACTION  
  
Return
```

Caso tenha dúvidas, deve ser reportado através do **DevForum.**  
<https://devforum.totvs.com.br/>

**Saiba mais**  
[Guia de desenvolvimento da linha Microsiga Protheus](https://tdn.totvs.com/display/public/PROT/Guia+de+desenvolvimento+da+linha+Microsiga+Protheus)  
[Boas práticas - TotvsTec](https://tdn.totvs.com/pages/viewpage.action?pageId=641841855)
