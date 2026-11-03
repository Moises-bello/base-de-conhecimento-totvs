---
article_id: 15824025253527
category: SIGAEST - LEGAIS
content_hash: 8821221b2a5cf299aa3bf9a84b689a9992b7869505fde906e249897538fcf473
fetched_at: '2026-06-28T22:38:51.682137+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FISA061 - Como tratar
  o FCI para produtos que não são mais importados?
type: support-article
updated_at: '2023-07-06T16:45:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15824025253527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FISA061-Como-tratar-o-FCI-para-produtos-que-n%C3%A3o-s%C3%A3o-mais-importados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15824029524503) Tempo aproximado para leitura: **00:02:15 min** **Dúvida**

Como fazer produtos que outrora foram adquiridos através de operação de importação, mas que atualmente são adquiridos no mercado nacional, para que não considerem mais no FCI?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para tratar essa especificidade, foi implementado tratamento para considerar os valores de VI (Valor da Parcela Importada) e Quantidade se a data da última compra do componente considerando o campo de "Situacao Tributaria(D1\_CLASFIS)" ou não de acordo com o parâmetro "MV\_FCIPERI".

| **Nome de Var.** | MV\_FCIPERI |
| --- | --- |

| **Tipo** | Caracter |
| **Cont. Por** | F |
| **Descrição** | U = Padrão / F = Considera operação nacional |

**Saiba mais;**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Importações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9121923559959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FCI-Como-interpretar-o-c%C3%A1lculo-do-Valor-Importado-A8-VLRVI-em-Importa%C3%A7%C3%B5es-?source=search)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Produções?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9129246051479)*
