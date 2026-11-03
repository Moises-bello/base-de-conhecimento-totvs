---
article_id: 10532184537367
category: NFe - Nota Fiscal Eletrônica
content_hash: 34bccdbd328c7485fcb0e3b60c793fccccf7bfd9f8ce3e984696b8aca9dba361
fetched_at: '2026-06-28T22:40:03.946872+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 356 Rejeição: Informar
  o local de saída do Pais somente no caso da exportação'
type: support-article
updated_at: '2025-06-30T19:26:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10532184537367-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-356-Rejei%C3%A7%C3%A3o-Informar-o-local-de-sa%C3%ADda-do-Pais-somente-no-caso-da-exporta%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição abaixo:

356 Rejeição: Informar o local de saída do Pais somente no caso da exportação  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Informado o local embarque ou de transposição de fronteira (tag:exporta) em operação que não é de exportação (tpNF=0 ou idDest<>3)

1. Verifique se a operação é dentro do pais com CFOP iniciado por 2 ou 5 Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação** e retire o conteúdo dos completo de nota de exportação.

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33157379238423)

2. Se nota de exportação alterar o CFOP ***iniciado em 3 ou 7*** de operação de exportação pelo TES da nota no campo **Cod. Fiscal "F4\_CF".**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33157386310039)

3. Após isso, exclua a **nota e gere novamente.**

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10532247216407)**
