---
article_id: 360016751031
category: ADVPL - Ponto de Entrada
content_hash: db8d619e8c1a9c28c5ac48da56f7a23a12441e02ef2829e7807041c31b50c974
fetched_at: '2026-06-28T22:40:11.803581+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  F240MARK gera o erro 'invalid field name in Alias SE2TMP'
type: support-article
updated_at: '2021-12-29T15:03:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016751031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-F240MARK-gera-o-erro-invalid-field-name-in-Alias-SE2TMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Erro '*invalid field name in Alias* SE2TMP' ao gerar borderô de pagamento, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para os campos da tabela **SE2** que não fazem parte da estrutura original da tabela temporária **SE2TMP**, o ponto de entrada [**F240ADCM**](http://tdn.totvs.com/pages/releaseview.action?pageId=6071345) deve ser utilizado para adicionar o campo. Como exemplo, para a necessidade de adicionar o campo **E2\_JUROS**, se faz necessário seguir as implementações a seguir:

```
#Include 'Protheus.ch'  
  
User Function F240MARK()  
Local aArea := GetArea()  
Local aRet := PARAMIXB  
  
aadd(aRet,{"E2_JUROS","","Juros", "@E 99,999,999,999,999.99"})  
  
RestArea(aArea)  
  
Return aRet
```

```
#Include 'Protheus.ch'  
  
User Function F240ADCM()  
Local aCamposADCM := {}  
  
aAdd(aCamposADCM,'E2_JUROS')  
  
Return aCamposADCM
```
