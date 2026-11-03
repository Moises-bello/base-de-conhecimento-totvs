---
article_id: 360020737352
category: ADVPL - Rotina Automática
content_hash: c164c0e7a622bd8976697a8ca3ffa92e614e523584b3ccbd867fcf9336d7cd84
fetched_at: '2026-06-28T22:40:23.940281+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Como distinguir os erros
  apresentados em uma ExecAuto.
type: support-article
updated_at: '2024-03-06T23:29:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020737352-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-distinguir-os-erros-apresentados-em-uma-ExecAuto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como distinguir o erro apresentado em uma ExecAuto, após a variável lMsErroAuto ficar como verdadeira?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Para distinguir um erro de outro em uma rotina automática deve se utilizar a função mostraerro() para pegar o erro apresentado no array e posteriormente fazer uma comparação para que possa fazer tratamento diferentes para erros diferentes.

```
 IF lMsErroAuto   
 aerro := Mostraerro()   
 //Mostraerro()   
 IF ("Processo invalido" $ aerro)  
 ConOut(aerro)  
 ELSE  
 conout("Nâo é um processo invalido.")  
 ENDIF  
 Conout("Nao foi possivel efetuar o apontamento!")  
 lMsErroAuto := .F.  
 ELSE   
 Alert("Apontado!!!")  
 ENDIF
```

**Saiba mais**

[MostraErro](http://tdn.totvs.com/pages/releaseview.action?pageId=6815088)
