---
article_id: 29070091595799
category: NFe - Nota Fiscal Eletrônica
content_hash: 1612172ff9b2555b2d550e7e8bf8eda06ae395482c977867e13bdbe305839833
fetched_at: '2026-06-28T22:40:00.010946+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 374 Rejeição :
  CFOP incompatível com o grupo de tributação'
type: support-article
updated_at: '2025-01-08T17:31:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29070091595799-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-374-Rejei%C3%A7%C3%A3o-CFOP-incompat%C3%ADvel-com-o-grupo-de-tributa%C3%A7%C3%A3o
---

**Dúvida**  
Como solucionar a rejeição Rejeição 374 : CFOP incompatível com o grupo de tributação

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

A rejeição ocorre em dois cenários, primeiro cenário caso seja emitida uma nota Nfe com **CFOP=1.933, 2.933, 5.933 ou 6.933** (Aquisição ou prestação de serviço), **sem o grupo de tributação pelo ISSQN**.

Para identificar se foi gerado esse imposto na nota pode ser conferido os impostos calculados pela tabela CD2 filtrada pelo numero do documento ou acesse na planilha financeira do pedido de venda.

Para notas com ISSQN é necessário que seja preenchido na TES utilizada os campos **F4\_ISS=SIM** e **F4\_LFISS=Tributado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29070091568919)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29070091572887)

No segundo cenário caso seja emitida uma nota Nfe com **CFOP diferente de 1.933, 2.933, 5.933 e 6.933** (Aquisição ou prestação de serviço), com o **grupo de tributação pelo ISSQN escriturado**.

Neste caso é necessário validar o calculo do imposto do ISSSQN é devido, se sim, devem alterar o CFOP da nota para uma das opções determinadas pela NT 2019.005: 1.933, 2.933, 5.933 e 6.933 no campo **F4\_CF** da TES utilizada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29070096152471)

Após os ajustes, exclua a nota e gere novamente.

Validação da Sefaz:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29070091576855)**
