---
article_id: 360015759732
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7e5d260d870850e1fab29e03e0ac0463a6875e999f13e83465d87b47b15e12bf
fetched_at: '2026-06-28T22:39:56.213540+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Substituição
type: support-article
updated_at: '2025-11-27T13:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015759732-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Substitui%C3%A7%C3%A3o
---

**Dúvida**Como realizar o processo de substituição de uma NFSe?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução  
1.** Através da rotina **MATA521A**, exclua o documento de saída que será substituído;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067808154)  
  
**2.** Após, gere um novo Pedido de Venda ou reaproveite o mesmo pedido, preencha os campos **C5\_NFSUBST** e **C5\_SERSUBS** com o número e série **do RPS** que será substituído (anteriormente autorizada);  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067809314)  
  
**3.** Prepare o Documento de Saída;  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068935933)  
  
**4.** Entre na rotina **FISA022** e realize a transmissão do novo RPS gerado;  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068936013)  
  
**5.** Após isso, monitore as duas notas juntas;  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067814194)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067814114)  
  
**Obs**.: *Vale lembrar que a **Substituição não é disponibilizada por todas as prefeituras**.*Poderá verificar a disponibilidade através da relação abaixo: [-](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)[Municípios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)Para municípios sem substituição via Web Services, faça o procedimento via portal da prefeitura e no Protheus execute os itens de 1 a 3, sem fazer transmissão para prefeitura.
