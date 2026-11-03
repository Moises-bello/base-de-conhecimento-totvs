---
article_id: 1500002321641
category: ADVPL - Web Service
content_hash: 9549e14ba9811181dbceaec93eec85664e148ed95e51379ec37fb508849f351b
fetched_at: '2026-06-28T22:40:10.359135+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Falha de conexão
  SSL : HTTPGet'
type: support-article
updated_at: '2021-12-29T12:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002321641-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Falha-de-conex%C3%A3o-SSL-HTTPGet
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao realizamos o teste na função **HTTPGet**() está gerando o erro de falha de conexão SSL e a função HttpGetStatus(@cErro) está retornando 10060.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – Todas versões  
  
**Solução**Ajustar a configuração da chave **SSLConfigure** no appserver.ini conforme abaixo:  
[SSLConfigure]  
HSM =0  
SSL2=0  
SSL3=0  
TLS1\_0=0  
TLS1\_1=0  
TLS1\_2=1  
Verbose =1  
TryProtocols=1  
  
**Saiba mais**  
[Seção [SSLConfigure]](https://tdn.totvs.com/pages/viewpage.action?pageId=6064865)  
[Como\_corrigir\_erros\_com\_SSL\_e\_TLS](https://tdn.totvs.com/display/public/TSS/TSS0027_Como_corrigir_erros_com_SSL_e_TLS)
