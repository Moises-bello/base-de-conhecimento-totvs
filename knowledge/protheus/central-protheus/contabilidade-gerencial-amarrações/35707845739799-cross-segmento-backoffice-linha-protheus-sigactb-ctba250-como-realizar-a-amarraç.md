---
article_id: 35707845739799
category: Contabilidade Gerencial - Amarrações
content_hash: 4df054eacc57b3dae52b5f2a82f978a9fdea86cee76f9e47fa8efccd7e2ca8e7
fetched_at: '2026-06-28T22:41:05.771728+00:00'
product: protheus
section_id: 1500001548302
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250 - Como realizar
  a amarração das entidades contábeis de 1 para N considerando regra por nivel.
type: support-article
updated_at: '2025-10-17T18:28:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707845739799-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Como-realizar-a-amarra%C3%A7%C3%A3o-das-entidades-cont%C3%A1beis-de-1-para-N-considerando-regra-por-nivel
---

**Dúvida**  
Como realizar a amarração das entidades contábeis, considerando uma entidade para diversas.

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Contabilidade Gerencial - Todas Versões

**Solução:**

Hoje somente é possível amarrar uma entidade a várias, utilizando o parâmetro MV\_CTBAMAR = 2.

Com esta configuração o sistema permite realizar a amarração de várias contas ao mesmo centro de custo e vice-versa, este conceito se aplica a todas as entidades. 

Exemplo de amarração com parâmetro  MV\_CTBAMAR =  2:

Acesse o módulo 34 Contabilidade Gerencial -> Atualizações -> Cadastros -> Amarrações:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35707861992471)

Ao ser aberta a tela:

* Filtre as entidades que deseja no painel a esquerda;
* Marque as entidades que deseja no painel central;
* Selecione aplicar seleção no painel central;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35707845711127)

Verá que no painel inferior terá a amarração entre de diversas contas para um centro de custo.

Este conceito se aplica a todas as entidades não se limitando a conta e centro de custo.

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250: Validação de Amarrações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es)  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA250: Como o Protheus trata as amarrações contábeis?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018756531-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Como-o-Protheus-trata-as-amarra%C3%A7%C3%B5es-cont%C3%A1beis)
