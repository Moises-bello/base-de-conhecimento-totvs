---
article_id: 4412771530135
category: NFe - Nota Fiscal Eletrônica
content_hash: 9c564f189fb4fa8253bc918eb9eeaa370c77432f9a9fe3b2a0cec4fe4a125221
fetched_at: '2026-06-28T22:40:00.264239+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  875 Rejeição:
  Percentual de FCP inválido'
type: support-article
updated_at: '2023-10-23T13:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771530135--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-875-Rejei%C3%A7%C3%A3o-Percentual-de-FCP-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição abaixo:  
874 Rejeição: Percentual de FCP inválido ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado percentual de **FCP (id:N17b)**, percentual de FCP validado conforme tabela de alíquota definida por UF do emitente **(tag:enderEmit/UF, id:C12).**

1. **O Percentual do FCP** deve ser configurado conforme a lista das UFS abaixo **(Ao clicar no link será aberto um excel):**

[Tabela de Alíquotas de FCP por UF (atualizada em 03/05/2023)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=uthum2eC3is=)  
Tabela contendo as alíquotas por UF do Fundo de Combate à Pobreza (FCP)

2. Configure a nota **conforme o link abaixo:**

<https://tdn.totvs.com/display/public/PROT/CADUF+-+UFxUF>

3. Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

Os campos de base do FECP, **Percentual do FECP e Valor do FECP estão abaixo:**

* CD2\_BFCP
* CD2\_PFCP
* CD2\_VFCP

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412765057943)
