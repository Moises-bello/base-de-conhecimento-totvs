---
article_id: 4418725006615
category: ADVPL - Web Service
content_hash: cdf9dd674a3a6f5f306d373ccea732a8730a19e5590dfba509b542eee009aa3f
fetched_at: '2026-06-28T22:40:10.430067+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao utilizar
  SetValue da classe TWsdlManager.
type: support-article
updated_at: '2022-01-11T15:12:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418725006615-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-utilizar-SetValue-da-classe-TWsdlManager
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:45 min****Ocorrência**Utilizando o método **SetValue**da classe **TWsdlManager**para preenchimento de parâmetros em um webservice, o **XML** apresenta falha abaixo na resposta do servidor:

```
Error: elemento inesperado...Os elementos esperados
```

Exemplo de erro utilizando o **API** dos Correios:

```
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Client</faultcode><faultstring>Unmarshalling Error: elemento inesperado (uri:"http://cliente.bean.master.sigep.bsb.correios.com.br/", local:"cep"). Os elementos esperados s├úo &lt;{}cep> </faultstring></soap:Fault></soap:Body></soap:Envelope>
```

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Causa**A falha ocorre pois, a **API** neste caso necessita do prefixo de **namespace** antes dos nomes das *tags* na mensagem **SOAP**.  
  
**Solução**Utilize a propriedade **lUseNSPrefix**, para enviar o **namespace**.  
`oWsdl:lUseNSPrefix := .T.`  
  
**Saiba mais**  
[lUseNSPrefix](https://tdn.totvs.com/display/tec/TWsdlManager%3AlUseNSPrefix)

[TWsdlManager](https://tdn.totvs.com/display/tec/Classe+TWsdlManager)
