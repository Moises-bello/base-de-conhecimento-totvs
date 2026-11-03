---
article_id: 360056868914
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 359053f1c30b6e11dd6cadfd743e216c8290cbfc1459055be01e4925a36011a7
fetched_at: '2026-06-28T22:39:58.574839+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: Element
  ''{http://www.abrasf.org.br/nfse.xsd}FraseSecreta'
type: support-article
updated_at: '2021-12-17T14:55:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056868914-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-Element-http-www-abrasf-org-br-nfse-xsd-FraseSecreta
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura, ocorre a falha de schema abaixo:  
  
Element '{http://www.abrasf.org.br/nfse.xsd}FraseSecreta': [facet 'minLength'] The value has a lenght of '0'; this underruns the allowed minimum lenght of '6'.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096538034/mceclip1.png)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Isso ocorre pois a frase secreta disponibilizada e informada pela prefeitura para o contribuinte não esta sendo preenchida no Wizard.cfg.  
  
**Solução**Fazer o preenchimento do campo 'Frase Secreta' com o conteúdo que a prefeitura informou.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098853513/mceclip2.png)  
  
**Obs.: É de extrema importância também preencher os campos Usuário e Senha (também informados pela prefeitura) para correta comunicação do TSS com a prefeitura.**
