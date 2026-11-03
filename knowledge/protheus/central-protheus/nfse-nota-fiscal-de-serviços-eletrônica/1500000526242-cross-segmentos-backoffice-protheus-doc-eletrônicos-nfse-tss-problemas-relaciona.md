---
article_id: 1500000526242
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0135118b401312e308af51aba88077f8e7f374a8edb35b2a3fa551a6101b358b
fetched_at: '2026-06-28T22:39:58.583780+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: Problemas
  relacionados com Certificado Digital'
type: support-article
updated_at: '2021-10-06T19:07:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000526242-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-Problemas-relacionados-com-Certificado-Digital
---

**Dúvida**Como realizar a manutenção e evitar qualquer problema com os arquivos .PEM e configurações atuais do TSS relacionados a Certificado Digital?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Para configurar novamente o certificado digital para NFSE, evitando que qualquer vestígio incorreto esteja no TSS, realizar os passos abaixo:  
  
- Acessar a pasta CERTS dentro dos diretórios de instalação do TSS e **renomear os quatro arquivos .PEM da entidade em questão** (mesma que aparece ao acessar a rotina), exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099449934/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000566222/mceclip1.png)  
  
- **Comentar a seção [SSLConfigure] no appserver.ini do TSS por completo:**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099450074/mceclip2.png)  
  
- **Reiniciar o serviço do TSS e dentro da rotina FISA022 refazer o Wizard.cfg por completo, importando o certificado digital válido e atual.**Com esses procedimentos serão gerados novos arquivos .PEM na pasta CERTS e a seção SSLConfigure será recriada apontando corretamente para o certificado da filial em questão.
