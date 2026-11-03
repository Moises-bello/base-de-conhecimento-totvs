---
article_id: 4415098519959
category: NFe - Nota Fiscal Eletrônica
content_hash: da65b6cc4a0352c70c49c1f2810f1bb3b0b12a3cbfc3027020745a1e183f551b
fetched_at: '2026-06-28T22:40:05.415417+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 869 Rejeição: Valor
  do troco incorreto'
type: support-article
updated_at: '2025-07-25T18:46:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415098519959-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-869-Rejei%C3%A7%C3%A3o-Valor-do-troco-incorreto
---

**Dúvida**

Como solucionar a rejeição abaixo 869 Rejeição: Valor do troco incorreto ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Somatório do valor dos pagamentos ***(id:YA03, tag:vPag)*** maior que o total da nota **(id:W16, tag: vNF)** e sem informação no campo vTroco ***(id:YA09).***

1. Caso a nota seja feito pelo módulo do faturamento a ***TAG vTroco e gerada apenas, através do ponto de entrada abaixo:***

**[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)**

Observação: Caso queira deixar o valor padrão (tag <tPag>), não há necessidade de alterações nos valores do array 'AdetPag'.

2. Realize um teste ***com RDMAKE padrão do link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

3. Após isso, ***exclua a nota e gere novamente.***

* **Saiba mais:**

Se a nota for realizada pelo módulo do Loja mesmo que seja NFe verificar os procedimentos abaixo:

[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014024552)

* ***Validação da Sefaz:***

***![869_validacao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4415097643287)***
