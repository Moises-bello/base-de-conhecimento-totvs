---
article_id: 12292862449559
category: Financeiro - Contas a Pagar
content_hash: f52e985c77751284554b84ed7fffa7b75e8c7ab2a669322232dd5e24610bf6af
fetched_at: '2026-06-28T22:38:08.447066+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - FINA820 - Como é apresentado
  retenções no registro Q100 do LCDPR
type: support-article
updated_at: '2023-02-09T23:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12292862449559-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Como-%C3%A9-apresentado-reten%C3%A7%C3%B5es-no-registro-Q100-do-LCDPR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Como é apresentado retenções no registro Q100 do LCDPR?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**

As retenções realizadas pelo adquirente de produção do produtor rural, como despesa no (**registro Q100**) utiliza o código**“999** – **Numerário em trânsito” no campo COD\_CONTA, o CPF ou CNPJ** do adquirente no campo **ID\_PARTIC** e apontado o número da **nota fiscal** de origem do valor retido no **campo HIST** do registro. A mesma regra deve ser aplicada em casos de **abatimentos de vendas** que ocorrem posteriormente à operação **(descontos condicionais concedidos)**.

**Exemplo**Com abatimento de **ISS gerado na emissão** e posteriormente pago:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12292416426903)**

**Saiba mais**

[LCDPR - Livro Caixa Digital do Produtor Rural - Valores Retidos | Descontos Condicionais/ Abatimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=551443455)
