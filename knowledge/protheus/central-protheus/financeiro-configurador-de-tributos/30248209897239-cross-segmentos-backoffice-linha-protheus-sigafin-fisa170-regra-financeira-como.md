---
article_id: 30248209897239
category: Financeiro - Configurador de Tributos
content_hash: 443568ca8089f7eccab1c8e7f534b9bd25a08a3509663b656d586b29cc24ec69
fetched_at: '2026-06-28T22:37:46.119766+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Regra financeira
  - Como calcular via configurador de tributos o vencimento de impostos pela data
  de emissão da Invoice ou da NF. Serviço de Importação
type: support-article
updated_at: '2025-09-15T19:40:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30248209897239-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Regra-financeira-Como-calcular-via-configurador-de-tributos-o-vencimento-de-impostos-pela-data-de-emiss%C3%A3o-da-Invoice-ou-da-NF-Servi%C3%A7o-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193760407) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como calcular, via configurador de tributo, o vencimento de impostos pela data de emissão da invoice ou NF. Serviço de Importação.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12  
  
**Solução**Para que o vencimento dos impostos seja gerado com data de emissão da invoice ou da NF. de serviço de importação, é necessário criar uma **Regra de Vencimento** para o imposto, neste caso o **IRRF**, e atrelar a uma **Regra Financeira** conforme exemplo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193761431)](blob:https://totvssuporte.zendesk.com/0c4f50cf-2138-40f0-b46b-1cbbe6c13284)

Nos passos a seguir, a demonstração de todas as regras que compõem a **Regra Financeira**.

**Regra título:**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248209877783)](https://centraldeatendimento.totvs.com/hc/article_attachments/30248209877783)

**Regra cálculo:**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193763863)**](blob:https://totvssuporte.zendesk.com/91f4d056-e771-43af-8235-7f3bc52d868c)

**Regra vencimento:**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/30275739701399)](https://centraldeatendimento.totvs.com/hc/article_attachments/30275739701399)

**Regra retenção:**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193765783)**](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193765783)

A seguir, todas as **regras financeiras**, o cálculo dos tributos no **Documento de Entrada** e os títulos de impostos no **Financeiro**.

**Regras financeiras:**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248209881239)](blob:https://totvssuporte.zendesk.com/9cb45f97-cdf9-4581-abdc-198b06f64d94)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193766935)

**Documento de Entrada - tributos genéricos.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193767575)

**Financeiro - Contas a pagar - títulos**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/30248193768215)](blob:https://totvssuporte.zendesk.com/ab965b56-0c1f-4746-bbd7-f1716de9f1cd)

**Saiba mais**

[Configurado de Tributos - Regras Financeiras](https://tdn.totvs.com/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
