---
article_id: 13761982324375
category: NFe - Nota Fiscal Eletrônica
content_hash: 5cbf8d51619bbdc7c5ae1dbe43e60a3b1a6660c87cbe1a2c8c10e798bb01d675
fetched_at: '2026-06-28T22:40:05.108708+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 545 Rejeição: NF-e
  de devolução com valor total superior a NF-e devolvida'
type: support-article
updated_at: '2025-06-17T12:19:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13761982324375-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-545-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-com-valor-total-superior-a-NF-e-devolvida
---

**Dúvida**Como solucionar 545 Rejeição: NF-e de devolução com valor total superior a NF-e devolvida ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15420572130583)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15420547212695)**

3. Clique no **botão Schema; Copie e Cole o conteúdo completo do XML.**

![545_rej_monitor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13764266431639)

4. Verifique se o ***valor da TAG Vnf*** e igual da nota de origem, conforme o XML de exemplo:

* ***XML da nota de origem:***

![xml_de_devolucao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13762893158807)

* ***XML da nota de devolução:***

![XML_de_origem.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/13762892266007)

5. O valor da TAG ***vNF deve bater com os valores levados no bloco ICMSTOT*** subtraindo e somando de acordo com o esperado pela regra de sua totalizadora.

![610_Rejei__o_2020.005.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/15420572141591)

6. Para notas com os valores corretos na rejeição ***545 temos um parecer da consultoria de segmentos:***

***[Clique Aqui](https://www.totvs.com/blog/fiscal-clientes/nt-2022-005-v-1-10-rejeicao-nas-nf-e-de-devolucao/)***

7.Se sua empresa for do ***Regime normal e a devolução de emitente do Simples Nacional,*** realizar as configurações link abaixo:

***[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=619742950)***

* ***Validação da Sefaz:***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/13761806595479)***
