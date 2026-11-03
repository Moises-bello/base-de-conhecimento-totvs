---
article_id: 12814913224855
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d943cbdfe374644877cb4f1a6291fc120b14340bb93cf490a3744f361f8079a5
fetched_at: '2026-06-28T22:38:57.069711+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - HELPS MA265CAPAC,  MA265LOCDF
  e MA265DIMEN como ajustar?
type: support-article
updated_at: '2023-03-03T10:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12814913224855-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-HELPS-MA265CAPAC-MA265LOCDF-e-MA265DIMEN-como-ajustar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Ao tentar endereçar um produto exibe os HELPS ***MA265CAPAC,*** ***MA265LOCDF OU MA265DIMEN***, como devo ajustar o ambiente?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12815458104087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12816235545367)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Os helps ***MA265CAPAC,*** ***MA265LOCDF ou MA265DIMEN*** são exibidos devido utilizar controle de capacidade nos endereços da rotina **CADASTRO DE ENDEREÇOS (MATA015)** tabela SBE.

***Exemplo:*** endereçar uma quantidade superior ao **campo BE\_CAPACID**, nesse cenário vai apresentar o help **MA265CAPCID**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12815658941847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12815957041943)

Caso desejar não utilizar essa funcionalidade, pode alterar o **parâmetro** **MV\_CAPLOCA para .F.** dessa forma inibe a avaliação da capacidade dos endereços.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/12815809444759)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)
