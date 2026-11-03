---
article_id: 23910652146327
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 1f72bf6e85aed5353fa4801e258b98c128c02c78b6def9d6955c189a36851e6b
fetched_at: '2026-06-28T22:39:52.186940+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro AppComponent
  is not defined on {|E,OSCRIPT| USEREXCEPTION(E), .F.  }(EASYJS.PRW)
type: support-article
updated_at: '2024-11-21T20:14:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23910652146327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-AppComponent-is-not-defined-on-E-OSCRIPT-USEREXCEPTION-E-F-EASYJS-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23910652118935) Tempo aproximado para leitura: **00:01:00 min****Dúvida**

Ao efetuar uma inclusão na rotina de **LPCO (EICLP401)**  esta gerando um erro. O que fazer para que não ocorra esta erro? Quando o APP do **LPCO** não abrir, o que fazer?

```
AppComponent is not defined on {|E,OSCRIPT| USEREXCEPTION(E), .F. }(EASYJS.PRW) 28/02/2024 10:20:50 line : 203  
  
Called from EASYJS:RUNJSSYNC(EASYJS.PRW) 28/02/2024 10:20:50 line : 678  
Called from EASYPOUI:ACTIVATE(EASYPOUI.PRW) 29/01/2024 09:54:34 line : 152  
Called from GETFORMPOUI(EICLP401.PRW) 25/03/2024 11:23:46 line : 669  
Called from {|OPANEL,OVIEW| GETFORMPOUI(OPANEL,OVIEW, 1)}(EICLP401.PRW) 25/03/2024 11:23:46 line : 178
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – a partir da versão 12.1.27  
  
**Solução**

* Confirmar no inspetor de objetos se o ambiente está atualizado, com a última versão do **EASYPOAPP.app** disponibilizado no pacote acumulado do SIGAEIC.
* Verificar se o ambiente está abrindo outros APPs.
* Recomendamos abrir a rotina de **Catálogo de Produtos (EICCP400)**; para verificar se este é executado corretamente
* Deve-se checar se o ambiente está configurado para abrir um apps, para isso verifique o **AppServer**.**ini**, as informações a seguir:
  + Se a chave **[GENERAL] app\_environment** está configurada com o ambiente.
  + Se existir a chave **[DRIVERS] MultiProtocolPort** e **[DRIVERS]MultiprotocolPortSecure,** se estão configuradas com os conteúdos 1 e 1 .
  + Abaixo exemplo de das informações configuradas no **AppServer.ini**:
  + ![kcs drivers.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27974448349335)
