---
article_id: 360018867011
category: ADVPL - Classe e Função
content_hash: f0ef0e608c1b2fc87a4b27df4ba50ea2337b54fb518ee76999aead4582bd9efd
fetched_at: '2026-06-28T22:40:16.907866+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Gatilho entre tabelas
  em rotina mvc
type: support-article
updated_at: '2024-01-19T00:46:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018867011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gatilho-entre-tabelas-em-rotina-mvc
---

**Dúvida**Como utilizar gatilhos para preenchimento dos campos da tabela em rotinas MVC?  
  
**Ambiente**  
Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Crie um gatilho com domínio (X7\_CAMPO) e contradomínio (X7\_CDOMIN) apontando para o campo que irá disparar a ação:

![image2018-8-6_11-3-48.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014385511/image2018-8-6_11-3-48.png)

 Insira a seguinte função no campo Regra e informe o campo ORIGEM e DESTINO:  
  
**REGRA**

```
Eval({|x| FwFldPut("DESTINO", x)}, FwFldGet("ORIGEM"))
```

Obs**:** A função definida no campo Regra (X7\_REGRA) do gatilho deve ser do tamanho da regra.  
  
**Saiba mais**  
[EVAL](http://tdn.totvs.com/pages/viewpage.action?pageId=24346635)  
[FWFLDPUT](http://tdn.totvs.com/display/framework/FWFldPut)  
[FWFLDGET](http://tdn.totvs.com/display/framework/FWFldGet)
