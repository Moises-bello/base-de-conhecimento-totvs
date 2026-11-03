---
article_id: 360034478794
category: ADVPL - Web Service
content_hash: f5000ccd6d3f22dd3ef40a4accd90f78ebadce030abd945c445d787c7e1881e0
fetched_at: '2026-06-28T22:40:10.262666+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: Client.NoSOAPAction'
type: support-article
updated_at: '2022-02-09T12:27:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034478794-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Client-NoSOAPAction
---

**Ocorrência**Ao realizar o consumo de um serviço *web* SOAP por meio da classe `TWSDLManager()`   é gerado o erro abaixo:

```
Fault Code: ns1:Client.NoSOAPAction
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Causa**O campo **SOAPAction** pode ser utilizado por *firewalls* para filtrar as requisições SOAP (Protocolo Simples de Acesso a Objetos) feitas via HTTP.

Desta forma, um pacote poderia ser filtrado (bloqueado) caso a mensagem não possuísse este campo definido ou com um valor diferente do especificado.  
  
**Solução**Utilizar a propriedade `lAlwaysSendSA` valor verdadeiro.  
  
**Saiba mais**  
[TWsdlManager:lAlwaysSendSA](https://tdn.totvs.com/display/tec/TWsdlManager%3AlAlwaysSendSA)
