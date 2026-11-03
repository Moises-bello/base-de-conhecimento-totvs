---
article_id: 15923466950167
category: NFe - Nota Fiscal Eletrônica
content_hash: bb6eff580f00bcafb5811c14925ef8e43cd458056101c6ac04041ddd448967e4
fetched_at: '2026-06-28T22:40:05.135918+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 566 Rejeição: NF-e
  de devolução com valor do FCP superior a NF-e devolvida'
type: support-article
updated_at: '2025-06-16T17:03:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15923466950167-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-566-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-com-valor-do-FCP-superior-a-NF-e-devolvida
---

**Dúvida**Como solucionar 566 Rejeição: NF-e de devolução com valor do FCP superior a NF-e devolvida ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15923414998167)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15923466908567)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![545_rej_monitor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15923438512535)

4. Verifique se o ***valor da TAG vFCP*** e igual da nota de origem, conforme o XML de exemplo:

* ***XML da nota de origem:***

![566](https://centraldeatendimento.totvs.com/hc/article_attachments/15923428452119)

* ***XML da nota de devolução:***

![566](https://centraldeatendimento.totvs.com/hc/article_attachments/15923454040855)

5. O valor da TAG ***vFCP deve bater com os valores levados no bloco ICMSTOT*** subtraindo e somando de acordo com o esperado pela regra de sua totalizadora.

![610_Rejei__o_2020.005.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/15923444943639)

6. Para notas com os valores corretos na rejeição ***566 temos um parecer da consultoria de segmentos:***

***[Clique Aqui](https://www.totvs.com/blog/fiscal-clientes/nt-2022-005-v-1-10-rejeicao-nas-nf-e-de-devolucao/)***

7.Se sua empresa for do ***Regime normal e a devolução de emitente do Simples Nacional,*** realizar as configurações link abaixo:

***[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=619742950)***

* ***Validação da Sefaz:***

![566](https://centraldeatendimento.totvs.com/hc/article_attachments/15923428458903)
