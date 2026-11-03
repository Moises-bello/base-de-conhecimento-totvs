---
article_id: 5151712642839
category: ADVPL - Classe e Função
content_hash: c6ae17f694201e7d34d81ade05866f2f0e3d78c1491d499c609e348b8df20564
fetched_at: '2026-06-28T22:40:20.758392+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Mensagem: An exception
  occurred ar 1:0 WsdlParser Exception: Could not parse schema http://schemas.xmlsoap.org/wsdl/'
type: support-article
updated_at: '2022-08-12T18:28:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5151712642839-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mensagem-An-exception-occurred-ar-1-0-WsdlParser-Exception-Could-not-parse-schema-http-schemas-xmlsoap-org-wsdl
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao utilizar o método ParseURL ou ParseFile apresenta a mensagem de erro: An exception occurred ar 1:0 WsdlParser Exception: Could not parse schema <http://schemas.xmlsoap.org/wsdl/> , como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.27  
  
**Solução**

O problema ocorre em decorrência de mudanças dos serviços da Microsoft (responsáveis por validações dos **XSDS**) que alterou no mês de Abril de 2022 a forma de conexão do protocolo (de HTTP para HTTPS). Com isso, os serviços que não utilizam certificados, passaram a ter a conexão recusada pelos servidores da Microsoft;

Não houve mudança em nossa camada (appserver) para contornar a falha é necessário utilizar a propriedade **bNoCheckPeerCert** para desabilitar o check de CAs, conforme abaixo, para correção do incidente:

```
oWsdl := TWsdlManager():New()   
oWsdl:bNoCheckPeerCert := .T. // Desabilita o check de CAs  
```

Ou a propriedade  **lSSLInsecure** como T.  
  
**Saiba mais**  
[TWsdlManager:bNoCheckPeerCert](https://tdn.totvs.com/display/tec/TWsdlManager%3AbNoCheckPeerCert)  
[URLs acessadas pela TWsdlManager](https://tdn.totvs.com/display/tec/URLs+acessadas+pela+TWsdlManager)  
[TWsdlManager:lSSLInsecure](https://tdn.engpro.totvs.com.br/display/tec/TWsdlManager%3AlSSLInsecure)
