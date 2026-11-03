---
article_id: 1500002591262
category: NFe - Nota Fiscal Eletrônica
content_hash: cd0f29f80e6c16c22d5a9b599320c333eee637e68205cc1ebd5c2e8f11cd7548
fetched_at: '2026-06-28T22:40:03.200049+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  436 Rejeição :
  Código do meio de pagamento inexistente'
type: support-article
updated_at: '2021-08-27T17:48:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002591262-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-436-Rejei%C3%A7%C3%A3o-C%C3%B3digo-do-meio-de-pagamento-inexistente
---

**Dúvida**Como corrigir a rejeição abaixo:

436 Rejeição : Código do meio de pagamento inexistente.   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Informado meio de pagamento **tPag= Inexistente**

Observação: Regra de validação **valida a partir de 03/05/2021 para homologação e 01/09/2021 para produção**

1- Informe uma forma de conforme a **lista abaixo que consta na Sefaz:**

* **Acrescentado no portal a lista de conteúdo da TPAG:**

[Tabela de Meios de Pagamento - Publicada em 16/03/2021](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=SakNjq9TwFA=)

* Disponível no **Portal Nacional da Nota Fiscal eletrônica:**

![20210819_125957.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406671298327/20210819_125957.gif)

2 - Para informar uma das formas de **pagamento existentes** configurar conforme as documentações abaixo:

[MP - NFE - Como gerar a TAG tPag (forma de pagamento / duplicata / fatura)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985571)

[MP - NFE - Como gerar fatura (forma de pagamento / duplicata / fatura) no XML e no Danfe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025467193)

3- Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

As novas formas de pagamentos criadas na **Nota Técnica 2020.006:**

**16=**Depósito Bancário

**17=**Pagamento Instantâneo (PIX)

**18=**Transferência bancária, Carteira Digital

**19=**Programa de fidelidade, Cashback, Crédito Virtual

* **Importante:**

O ambiente deve estar com atualizados com o pacote da Nota Técnica do link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634)

* **Validação da Sefaz:**

![rejei__o_436.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014483741/rejei__o_436.JPG)
