---
article_id: 4411288614935
category: Call Center - Telecobrança
content_hash: 724703816683bf72bf6934c5726aa0359955c31deb61a92d1c84cc0b10fcb677
fetched_at: '2026-06-28T22:41:28.521410+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - Prazo da
  Regra de Seleção TMKA160
type: support-article
updated_at: '2021-10-22T16:17:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411288614935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Prazo-da-Regra-de-Sele%C3%A7%C3%A3o-TMKA160
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Configuração do prazo da Regra de Seleção TMKA160.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - a partir da versões.  
  
**Solução**O Prazo / Dias **K0\_PRAZO** precisa da configuração do campo Ordem **K0\_ORDEM**, pois define a sequência dos períodos de realização da cobrança para cada grupo de operadores.

Exemplo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Regra | Ordem | Descrição | Prazo | O que significa? |
| 000001 | 000010 | Regras de cobrança para primeiros contatos | 30 | Serão selecionados os títulos em aberto e vencidos com até trinta dias de atraso. |
| 000002 | 000020 | Regras de cobrança com maior rigor | 60 | Serão selecionados os títulos em aberto e vencidos entre o 31º dia até o 90º dia da data base. |
| 000003 | 000030 | Regras de cobrança jurídica | 90 | Serão selecionados os títulos em aberto e vencidos entre o 61º a 90º. |

* Na regra "000001", por exemplo, representa o intervalo do vencimento inicial do título a partir da data base com prazo de 30 dias de vencimento.
* Na regra "000002", representa o intervalo do vencimento inicial do título a partir da regra antecessora (000001) com o prazo de 60 dias.
* Na regra "000003", representa o intervalo do vencimento inicial do título a partir da regra antecessora (000002) com o prazo de 90 dias.
