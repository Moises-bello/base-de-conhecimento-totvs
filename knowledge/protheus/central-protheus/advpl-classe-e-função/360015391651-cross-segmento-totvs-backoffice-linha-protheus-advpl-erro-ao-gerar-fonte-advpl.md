---
article_id: 360015391651
category: ADVPL - Classe e Função
content_hash: 3a7a4c1c9477387e86f8b6a51082496a3774e09dffc3ad2efda6603bb61a6318
fetched_at: '2026-06-28T22:40:15.797295+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro ao gerar fonte
  ADVPL
type: support-article
updated_at: '2022-01-03T14:55:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015391651-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-gerar-fonte-ADVPL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Estou tentando criar uma função WSDL Client, pelo TDS e gera o erro abaixo:  
**\*\*\* ERRO AO GERAR FONTE ADVPL \*\*\***

WSCERR066 / INVALID WSDL Content-Type (Content-Type: text/html;charset=utf-8)  
WSCERR048 / SOAP FAULT env:Server  
WSCERR072 / HTTP REQUEST ERROR (HTTP/1.1 400 Bad Request)  
WSCERR054 / SOAP:BINDING não localizado no WSDL  
WSCERR017 / [HTTPS] Requisição retornou NIL. ( 0 : )  
Invalid function return for WSDLSource Call.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010337772/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**O erro ocorre quando o TDS não entende algumas tags do xml, pois o seu xml é mais complexo.  
  
**Solução**Utilize a Classe [TWsdlManager](http://tdn.totvs.com/display/tec/Classe+TWsdlManager).  
[TWsdlManager ParseURL](http://tdn.totvs.com/display/tec/TWsdlManager%3AParseURL)  
  
Observação: Outras dúvidas relacionadas a classe como certificados e autenticações acesse a documentação: [Acesso a Web Services que exigem certificados de CA](http://tdn.totvs.com/display/tec/Acesso+a+Web+Services+que+exigem+certificados+de+CA)
