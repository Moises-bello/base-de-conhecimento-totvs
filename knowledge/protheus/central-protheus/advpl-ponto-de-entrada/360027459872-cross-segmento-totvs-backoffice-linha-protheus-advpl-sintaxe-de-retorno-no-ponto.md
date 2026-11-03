---
article_id: 360027459872
category: ADVPL - Ponto de Entrada
content_hash: 828df1f2ed71e5cb077a4f4ee809f1d44f7280de2ea5f719953b95e7d89d50d9
fetched_at: '2026-06-28T22:40:12.878762+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Sintaxe de retorno
  no ponto de entrada F370E2F
type: support-article
updated_at: '2021-12-21T20:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027459872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Sintaxe-de-retorno-no-ponto-de-entrada-F370E2F
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como é a sintaxe do ponto de entrada F370E2F? A string deve ser passada com expressões em advpl ou sql?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de entrada [F370E2F](http://tdn.totvs.com/display/public/mp/F370E2F+-+Complementa+filtro+--+11762) permite a manipulação da filtragem a ser realizada no processo, filtragem esta que é realizada pela [IndRegua](http://tdn.totvs.com/pages/releaseview.action?pageId=6814909), portanto a sintaxe teve ser em **ADVPL**.   
O ponto de entrada em questão recebe, por PARAMIXB, toda a string de filtragem padrão, e permite tanto complementar essa filtragem como desconsiderar toda a filtragem padrão e criar uma nova filtragem, conforme exemplos a seguir:

**Complemento do filtro:**

```
#Include 'Protheus.ch'  
  
User Function F370E2F()  
cFor := PARAMIXB  
  
cFor += .AND. E2_FORNECE == '000001' .AND. E2_LOJA == '01'  
  
Return cFor
```

**Novo Filtro:**

```
#Include 'Protheus.ch'  
  
User Function F370E2F()  
cFor := PARAMIXB  
  
cFor := E2_FILIAL == "'+xFilial("SE2",cFilAnt)+'" .AND. E2_FORNECE == '000001' .AND. E2_LOJA == '01'  
  
Return cFor
```
