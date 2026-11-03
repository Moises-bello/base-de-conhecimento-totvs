---
article_id: 18190844400023
category: BI - Business- Intelligence - Workflow
content_hash: 005bf6e8b29cc5d7b0ddfb6cb60ea6bac392bcaa9934e1cf8f011d5f0d2a894e
fetched_at: '2026-06-28T22:37:03.107464+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Configuração para uso
  do Workflow com HTTPS
type: support-article
updated_at: '2023-10-11T17:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18190844400023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Configura%C3%A7%C3%A3o-para-uso-do-Workflow-com-HTTPS
---

**Dúvida**Como configurar o envio de *Workflow* com *HTTPS* ?  
  
**Ambiente**MP - BI - A partir da versão 12.1.2210  
  
**Solução**Para utilizarmos o *Workflow* via *link* com HTTPS, precisamos ajustar no appserver.ini as sessões **HTTPS** e **SSLCONFIGURE***.* Ambas precisam existir no ambiente para o correto funcionamento do *Workflow*.

A configuração da seção **[HTTPS]** permite habilitar conexões seguras do Server Protheus, já a sessão **[SSLConfigure]** permite habilitar o Application Server para criptografar e autenticar as informações transmitidas pela internet.

Abaixo, um exemplo de configuração para a sessão **[HTTPS]** e **[SSLConfigure]**:

```
[HTTPS]  
ENABLE=1  
PORT=81  
ENVIRONMENT=P121XX   
PATH=C:\Protheus\P121XX\protheus_data  
XFRAMEOPTIONS= ALLOW-FROM *   
  
[SSLConfigure]  
SSL2=1  
SSL3=1  
TLS1_0=1  
TLS1_1=1  
TLS1_2=1  
CertificateServer=C:\Protheus\P121XX\protheus\bin\appserver\totvs_certificate.crt  
KeyServer=C:\Protheus\P121XX\protheus\bin\appserver\totvs_certificate_key.pem
```

**Saiba mais**

[Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Como configurar um Workflow via Link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020999472)  
[Seção [HTTPS]](https://tdn.totvs.com/pages/viewpage.action?pageId=135496188)  
[Seção [SSLConfigure]](https://tdn.totvs.com/pages/viewpage.action?pageId=6064865)
