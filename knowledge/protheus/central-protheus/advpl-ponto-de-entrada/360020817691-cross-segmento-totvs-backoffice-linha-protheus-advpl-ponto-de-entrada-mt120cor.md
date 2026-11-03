---
article_id: 360020817691
category: ADVPL - Ponto de Entrada
content_hash: e69d8b5cf58b1baf88ca3e6b131370284ef042e2d8266564a531e7e104671597
fetched_at: '2026-06-28T22:40:12.641903+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MT120COR
type: support-article
updated_at: '2026-01-23T20:19:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020817691-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MT120COR
---

**Dúvida**Qual seria o ponto de entrada para **MATA121** semelhante a **MA410COR** ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Na **MATA121** podemos utilizar o ponto **MT120COR** para manipular Manipula regras de cores de status na mBrowse

**Exemplo:**

```
User Function MT120COR()  
  
Local aNewCores := aClone(PARAMIXB[1])  
  
// aCores  
  
aAdd(aNewCores,{ 'C7_CONAPRO== "B" .And.C7_QUJE < C7_QUANT', 'BR_AZUL'})  
//-- Bloqueado  
  
aAdd(aNewCores,{ 'C7_QUJE==0 .And. C7_QTDACLA==0','ENABLE'})  
//-- Pendente  
  
aAdd(aNewCores,{ 'C7_QUJE>=C7_QUANT', 'DISABLE'})  
//-- Atendido  
  
aAdd(aNewCores,{ 'C7_QTDACLA >0', 'BR_LARANJA'})  
//-- Pedido Usado em Pre-Nota  
  
Return (aNewCores)
```

**Saiba Mais:**[MT120COR - Manipula regras de cores de status na mBrowse](http://tdn.totvs.com/display/public/PROT/MT120COR+-+Manipula+regras+de+cores+de+status+na+mBrowse)
