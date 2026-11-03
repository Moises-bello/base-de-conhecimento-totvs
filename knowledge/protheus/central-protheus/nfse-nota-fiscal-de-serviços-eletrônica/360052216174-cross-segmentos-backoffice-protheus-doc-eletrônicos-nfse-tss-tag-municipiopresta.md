---
article_id: 360052216174
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e62aba3cffddf97fe3eb962c12ea85ba4ca61be76ef81bc8345587e99af9a4e4
fetched_at: '2026-06-28T22:39:58.598828+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: Tag
  MunicipioPrestacao (São Paulo)'
type: support-article
updated_at: '2021-10-06T19:10:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052216174-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-Tag-MunicipioPrestacao-S%C3%A3o-Paulo
---

**Dúvida**Por que a tag <MunicipioPrestacao> não foi destacada no XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**De acordo, com o layout webservice de SP o município de prestação não pode ser gerado no XML quando a prestação/tributação for em SP ou no exterior, caso seja enviado ocorrerá a rejeição 1223, segue abaixo:  
  
*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085361313/mceclip1.png)*  
Detalhes:  
- *[http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais](https://www.google.com/url?q=http://notadomilhao.prefeitura.sp.gov.br/cidadao/informacoes-gerais/manuais&sa=D&source=hangouts&ust=1597414820741000&usg=AFQjCNHwDNUoQUjUv_doz4fTZKBd5mvXyw)*
