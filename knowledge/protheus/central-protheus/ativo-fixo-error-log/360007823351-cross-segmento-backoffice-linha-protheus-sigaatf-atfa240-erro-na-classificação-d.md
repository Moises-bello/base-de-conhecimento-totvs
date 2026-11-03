---
article_id: 360007823351
category: Ativo-Fixo - Error log
content_hash: e9de315843391a2af1e98c16f0905a115ef19b3e2ef5bcafe176f8c5d4d144ff
fetched_at: '2026-06-28T22:41:54.811824+00:00'
product: protheus
section_id: 1500001547442
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -  SIGAATF - ATFA240 - Erro na
  Classificação do bem  "InterFunctionCall: cannot find function AF010VALOR in AppMap
  on"'
type: support-article
updated_at: '2021-09-15T19:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007823351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Erro-na-Classifica%C3%A7%C3%A3o-do-bem-InterFunctionCall-cannot-find-function-AF010VALOR-in-AppMap-on
---

**Ocorrência**ATFA240 - Error log na Classificação do bem:  InterFunctionCall: cannot find function AF010VALOR in AppMap on {|a,b,c,d| FWInitCpo(a,b,c),lRet:=((IIf(aCols[n][1] != "05",POSITIVO(),.T.) .AND. AF010VALOR())),FWCloseCpo(a,b,c,lRet),lRet }(PROTHEUSFUNCTIONMVC.PRX)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12.1.17.  
  
  
**Solução:**

Verifique o conteúdo do X3\_VALID para os campos N3\_VORIG1, (N3\_VORIG2, N3\_VORIG3, etc).  
Para o campo N3\_VORIG1 o conteúdo deve ser AF012AVLR(), e nos demais campos (N3\_VORIG2, N3\_VORIG3, etc), o conteúdo deve ser AF12VLRM().  
  
Segue print da validação conforme ambiente padrão:  
![](https://totvssuporte.zendesk.com/attachments/token/QjARVQbFs34v2Jpe0V8M6cx6F/?name=inline-1876987087.png)​  
  
Após efetuar a verificação/ajuste, realize um novo teste na rotina.

**Saiba mais**

[Como classificar o ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012521571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Aquisi%C3%A7%C3%A3o-de-imobilizado-e-classifica%C3%A7%C3%A3o-de-compras) [imobilizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012521571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA240-Aquisi%C3%A7%C3%A3o-de-imobilizado-e-classifica%C3%A7%C3%A3o-de-compras)

[Atfa240 error log Cannot-find-function-AFA010CTA-in-AppMap](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007146792-MP-SIGAATF-Cannot-find-function-AFA010CTA-in-AppMap)

[ATFA240 - Cancelamento da classificação do bem](https://totvssuporte.zendesk.com/knowledge/articles/360006848432/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360006848432)

[Classificação do Bem não gatilha conta contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006575352-MP-SIGAATF-Ao-classificar-um-bem-o-sistema-n%C3%A3o-carrega-a-conta-cont%C3%A1bil)
