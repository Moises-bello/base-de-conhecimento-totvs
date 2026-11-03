---
article_id: 1500000311822
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 5e6b1b3968978f7e948159276aaad69b9c228767c23713c04e4c06e22e09c99b
fetched_at: '2026-06-28T22:39:56.333566+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - BRASILIA:
  Rejeição 252 - Ambiente informado diverge do Ambiente de recebimento? '
type: support-article
updated_at: '2025-07-14T21:33:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000311822-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-BRASILIA-Rejei%C3%A7%C3%A3o-252-Ambiente-informado-diverge-do-Ambiente-de-recebimento
---

**Dúvida**Ao transmitir ocorre a rejeição '252 - Ambiente informado diverge do Ambiente de recebimento' para nota fiscal de serviços de Brasília.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Essa rejeição ocorre quando **foi autorizada a nota em ambiente de produção** e o **cancelamento está sendo enviado em ambiente de homologação**, ou **vice versa.**  
1- Verifique os parâmetros de transmissão das notas em **Outras ações -> Parâmetros -> NFe** , o ambiente em que a nota foi autorizada.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061523533/mceclip1.png)  
  
2- Verifique os parâmetros de evento **Outras ações -> Parâmetros ->** **Eventos**, o ambiente precisa ser o mesmo em que a nota foi autorizada.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060589694/mceclip2.png)

Salve a configuração no botão **+GRUPO ADMINISTRADOR: SALVAR**

3- Após isso, em **Outras ações -> Transmissão** faça novamente a  transmissão da nota e monitore.
