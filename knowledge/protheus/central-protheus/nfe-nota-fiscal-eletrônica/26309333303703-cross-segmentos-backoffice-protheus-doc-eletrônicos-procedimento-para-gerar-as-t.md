---
article_id: 26309333303703
category: NFe - Nota Fiscal Eletrônica
content_hash: 18e22e3ab6f4041dfe06c9ebb8e76cdf9394e9fd9844ef60ca7ffe91db21d322
fetched_at: '2026-06-28T22:40:00.142752+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Procedimento para
  gerar as TAGs de impostos zeradas quando se tratar se nota sobre cupom
type: support-article
updated_at: '2024-09-11T20:53:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26309333303703-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Procedimento-para-gerar-as-TAGs-de-impostos-zeradas-quando-se-tratar-se-nota-sobre-cupom
---

**Dúvida**  
Procedimento para gerar as TAGs de impostos zeradas quando se tratar se nota sobre cupom?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para geração das tags de impostos zeradas quando se tratar de uma nota sobre cupom, é necessária a criação do parâmetro MV\_ZERCPM.

*Criação do parâmetro MV\_ZERCPM*

Acesse o configurador:

![](https://tdn.totvs.com/download/attachments/700510098/image2022-7-28_15-39-45.png?version=1&modificationDate=1659035594057&api=v2)

Autentique-se com suas credenciais:

![](https://tdn.totvs.com/download/attachments/700510098/image2022-7-28_16-1-38.png?version=1&modificationDate=1659035593980&api=v2)

Acesse o item referente a parâmetros:

![](https://tdn.totvs.com/download/attachments/700510098/image2022-7-28_16-6-4.png?version=1&modificationDate=1659035593907&api=v2)

Selecione a sua empresa (1), depois clique em incluir (2).

![](https://tdn.totvs.com/download/attachments/700510098/image2022-7-28_16-7-10.png?version=1&modificationDate=1659035593803&api=v2)

Preencha o campo Nome de Var. com o valor: MV\_ZERCPM; Tipo: 1-Caractere; Cont. Por: 1

![](https://tdn.totvs.com/download/attachments/700510098/image2022-7-28_16-8-12.png?version=1&modificationDate=1659035593703&api=v2)

**Observação:**

O campo Cont. Por = 1 é para gerar a nota sobre cupom com os valores das TAGs de impostos zerados, quando preenchido com 0 irá seguir o fluxo padrão.
