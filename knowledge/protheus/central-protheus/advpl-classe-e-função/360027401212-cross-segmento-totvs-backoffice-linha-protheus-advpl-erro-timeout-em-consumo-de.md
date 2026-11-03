---
article_id: 360027401212
category: ADVPL - Classe e Função
content_hash: 3acca6feac383c5977b84e570592aad91804bcdc9214765eb42d295ed144015e
fetched_at: '2026-06-28T22:40:15.822786+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro timeout em
  consumo de WebService
type: support-article
updated_at: '2021-10-04T13:27:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027401212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-timeout-em-consumo-de-WebService
---

**Dúvida**O WS onde o processamento é superior a 2 minutos, gerando o seguinte mensagem no console.log:

WSCERR044 / Não foi possível POST : URL http://XX.X.X.X:XXXX/server.asmx ( 999 : Invalid HTTP Connection )

O Client é gerado via TDS  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.  
  
**Solução**Na questão de geração via TDS é necessário utilizar a Classe [TWsdlManager](http://tdn.totvs.com/display/tec/Classe+TWsdlManager), pois devido a complexidade o wsdl algum recursos ficaram limitado.    
Sobre Timeout verifique as documentações da Classe através do saiba mais.  
  
**Saiba mais**  
[nConnectTimeout](http://tdn.totvs.com/display/tec/TWsdlManager%3AnConnectTimeout)  
[nTimeout](http://tdn.totvs.com/display/tec/TWsdlManager%3AnTimeout)
