---
article_id: 360019538492
category: ADVPL - Ponto de Entrada
content_hash: 3b9152353915b339165d56f4152c78605608929598de9669efe4ee14380cebb0
fetched_at: '2026-06-28T22:40:11.565252+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Ponto de entrada FA090SE5
  não funciona
type: support-article
updated_at: '2021-12-21T20:22:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019538492-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-FA090SE5-n%C3%A3o-funciona
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:00 min****Ocorrência**Estou utilizando o ponto de entrada FA090SE5, porém o mesmo não funciona.  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**   
Esse incidente ocorre, pois a houve mudança no ponto FA090SE5, não é possível mais utilizar a *reclock* é necessário retornar a variável com a *string* a ser gravada.  
  
**Solução**Segue exemplo conforme documentação.

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
User function FA090SE5()  
  
Local cNumero := SE2->E2_NUM  
Local cPrefixo := SE2->E2_PREFIXO  
Local cParcela := SE2->E2_PARCELA  
Local cFornece := SE2->E2_FORNECE  
Local cLoja := SE2->E2_LOJA  
Local _CMOTBX := CMOTBX //Motivo de Baixa  
  
Local cHistor := ""  
  
IF _CMOTBX = "DEBITO CC"  
cHistor := cPrefixo+cNumero+cParcela+cFornece+cLoja  
END  
  
Return(cHistor)
```

**Saiba mais**[DT\_FA090SE5\_Grava\_dados](http://tdn.totvs.com/display/PROT/DT_FA090SE5_Grava_dados)
