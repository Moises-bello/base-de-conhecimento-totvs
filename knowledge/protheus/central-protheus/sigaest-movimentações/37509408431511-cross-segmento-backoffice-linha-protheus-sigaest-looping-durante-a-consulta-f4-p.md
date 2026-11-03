---
article_id: 37509408431511
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 345f8b195b6c52884cfe6b532096d05abfa8b4d9013403f493c589a1a4d923a7
fetched_at: '2026-06-28T22:38:55.641560+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Looping durante a
  consulta F4 por LOTE na rotina Solicitação ao Armazém.
type: support-article
updated_at: '2026-01-07T18:48:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37509408431511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Looping-durante-a-consulta-F4-por-LOTE-na-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

Ao acessar a rotina Solicitação ao Armazém, ocorre um looping ao usar a consulta F4 no campo de lote.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37509408424087) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao acessar a rotina Solicitação ao Armazém apresenta um Looping ao selecionar a consulta F4 no campo de lote, na função F4LOTE.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Verificamos que esse looping, podem ocorrer devido a ordenação dos campos da tabela SD3 estarem divergentes do padrão.

No final do artigo segue o dicionário de dados da tabela SD3, gerado na data 07/01/2026 da release 12.1.2510.

**Observação:**

A tabela coletada no dia 07/01/2026 avaliar novos patch caso a ordenação seja alterada.

**Saiba Mais**:

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
