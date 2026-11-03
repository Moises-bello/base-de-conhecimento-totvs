---
article_id: 360021541971
category: ADVPL - Classe e Função
content_hash: 899357621b9e222f24579a394bddd23964958ec768b38087b0c2351f5a5fb822
fetched_at: '2026-06-28T22:40:15.722998+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criando gatilho
  com User Function para validar a execução em rotina especifica
type: support-article
updated_at: '2022-01-05T15:09:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021541971-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criando-gatilho-com-User-Function-para-validar-a-execu%C3%A7%C3%A3o-em-rotina-especifica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Como criar um gatilho para que seja executado apenas em uma rotina especifica?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**As vezes existe a necessidade de um gatilho só poder ser executado em uma rotina especifica, para isso é necessário a criação de um gatilho chamando uma User Function e posteriormente validar se é exatamente a rotina que deverá ser executado.

Exemplo - Gatilho:

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360018210191/Capturar.JPG)

Fonte

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
user function e5debito()  
  
Local cConta := ''  
Local n := 0  
  
While ALLTRIM(PROCNAME(n)) <> ""  
  
  If PROCNAME(n) == "FA100REC"  
  
    cConta := '3.1.1 '  
  
  ENDIF  
  
  n+=1   
  
EndDo  
  
return cConta 
```

Ou seja, neste exemplo, estamos utilizando a função ProcName para sabermos a origem da chamada.   
  
**Saiba Mais**[Procname](http://tdn.totvs.com/display/tec/ProcName)[Gatilhos](http://tdn.totvs.com/pages/releaseview.action?pageId=312157626)
