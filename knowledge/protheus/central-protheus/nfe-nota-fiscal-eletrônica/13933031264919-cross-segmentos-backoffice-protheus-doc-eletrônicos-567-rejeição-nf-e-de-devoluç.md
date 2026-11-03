---
article_id: 13933031264919
category: NFe - Nota Fiscal Eletrônica
content_hash: c97b6d879a9ee8d520f4eb34084a38ad17f8dd444d3487a458db3f7414b32992
fetched_at: '2026-06-28T22:40:05.140099+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 567 Rejeição: NF-e
  de devolução com valor do ICMS da UF Destino superior a NF-e devolvida'
type: support-article
updated_at: '2025-06-18T14:25:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13933031264919-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-567-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-com-valor-do-ICMS-da-UF-Destino-superior-a-NF-e-devolvida
---

**Dúvida**Como solucionar a 567 Rejeição: NF-e de devolução com valor do ICMS da UF Destino superior a NF-e devolvida ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896006166679)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896006169111)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![545_rej_monitor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896013123223)

4. Verifique se o ***valor da TAG vICMSUFDest*** e igual da nota de origem, conforme o XML de exemplo:

* ***XML da nota de origem:***

![origem_567.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13932956766871)

* ***XML da nota de devolução:***

***![567_devolu__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13933027253399)***

* ***Validação da Sefaz:***

![valida__o_da_sefaz.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13932624023575)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13933156774167)
