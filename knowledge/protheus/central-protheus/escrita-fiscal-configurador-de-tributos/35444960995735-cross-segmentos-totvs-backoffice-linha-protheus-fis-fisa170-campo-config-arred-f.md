---
article_id: 35444960995735
category: Escrita Fiscal - Configurador de Tributos
content_hash: 37bb533de7ecfde63dd9d1b5af3a6d9908dd9110b06637ab5ef1d9f7180528c6
fetched_at: '2026-06-28T22:39:17.710668+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Campo Config
  Arred (F2B_RND) arredondamento de imposto Configurador de Tributos
type: support-article
updated_at: '2025-10-07T16:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35444960995735-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Campo-Config-Arred-F2B-RND-arredondamento-de-imposto-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35444976346135) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Campo Config Arred (F2B\_RND) arredondamento de imposto Configurador de Tributos  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
No Configurador de tributos o arredondamento possui a configuração adequada para definir se os impostos devem ser arredondados ou truncados, que como você já identificou, a tratativa é feita na Regra de Cálculo. 

**Config Arred (F2B\_RND) - Regra de Calculo do Documento Fiscal**  
Neste campo podemos definir como será a regra de arredondamento do tributo, se deverá ser arredondado ou truncado. Este campo não é obrigatório, se estiver vazio o sistema irá adotar o padrão de arredondar o valor calculado. Este campo funcionará em conjunto com o parâmetro **MV\_RNDSOBR**

Utilizados em conjunto com o parâmetro **MV\_RNDSOBR**:

1. Sempre que o **RNDSOBR** estiver como Falso, não teremos o tratamento das sobras e consequentemente os valores serão truncados por item.
2. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* também como Verdadeiro, será efetuado o tratamento de arredondamento por item.
3. Quando o **RNDSOBR** estiver como Verdadeiro e o RND\*\* como falso, será efetuado o tratamento de arredondamento no total do imposto (truncando por item e considerando a sobra).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468596706071)

Essa tratativa é padrão e não tem como ser ajustada, visto que no legado também não tinha como fazer o arredondamento por Fornecedor.
