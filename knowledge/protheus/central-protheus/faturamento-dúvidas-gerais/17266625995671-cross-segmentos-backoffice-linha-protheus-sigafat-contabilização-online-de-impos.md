---
article_id: 17266625995671
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 462d3084a51ab40841e2f63617c6188c5c69475b193dbd7ce1e01e48c6682cea
fetched_at: '2026-06-28T22:38:32.996106+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT - Contabilização online
  de impostos da tabela SD2, validando informações da tabela SF2 '
type: support-article
updated_at: '2023-09-04T16:50:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17266625995671-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Contabiliza%C3%A7%C3%A3o-online-de-impostos-da-tabela-SD2-validando-informa%C3%A7%C3%B5es-da-tabela-SF2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17266611726615) Tempo aproximado para leitura: **HH:02:00 min** **Dúvida**Como realizar a contabilização de impostos na tabela SD2, onde faz-se verificações no cabeçalho da NF, na tabela SF2?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**As vezes nas contabilizações dos itens na tabela (SD2 - Itens), é necessário validar certas informações na tabela parceira (SF2 - Cabeçalho), exemplo:

* CT5\_VLR01 = IF(SF2->F2\_RECISS="2", SD2->D2\_TOTAL, 0)

**OBSERVAÇÃO:** O suporte não realiza testes com regras complexas como acima, apenas regras do tipo "SD2 -> D2\_TOTAL + D2\_SEGURO" ou "SD2->D2\_TOTAL"

Ao tentar contabilizar online pela "LP 610", que verifica e utiliza a tabela SD2, no momento da contabilização online, ao ser faturado e contabilizado o registro, no momento em que é contabilizado a nota fiscal de saída, o campo de verificação na SF2 (F2\_RECISS="2") pode não estar preenchido, não contabilizando;

Na mesma regra, contabilizando offline, o registro é contabilizado pois no momento o campo "F2\_RECISS" já está completamente preenchido (a nota foi inteira já estruturada quando a contabilização ocorre).

**Para resolver:**

Contabilize com a regra acima utilizando a "LP 620" que verifica primordialmente a tabela SF2 e depois consegue ainda fazer referência a tabela parceira SD2.
