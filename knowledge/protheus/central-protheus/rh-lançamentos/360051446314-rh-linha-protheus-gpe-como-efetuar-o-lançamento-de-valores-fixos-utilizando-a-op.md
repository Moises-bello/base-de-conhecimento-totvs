---
article_id: 360051446314
category: RH - Lançamentos
content_hash: 17cc7769202651741c7bbbceba1b109ec9d1f194d77926bab784919b22407240
fetched_at: '2026-06-28T22:43:31.176950+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o lançamento de valores fixos utilizando
  a opção de acumulador
type: support-article
updated_at: '2025-07-24T18:05:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051446314-RH-Linha-Protheus-GPE-Como-efetuar-o-lan%C3%A7amento-de-valores-fixos-utilizando-a-op%C3%A7%C3%A3o-de-acumulador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26071132931991) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Como efetuar o lançamento de valores fixos utilizando a opção de acumulador?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Cadastramento de três verbas (podem ser mais ou menos verbas, desde que existe a verba que irá ser base para realizar a acumulação e a verba que seja a acumulação) pra cadastrar as verbas acesse **Atualizações > Definições de Cálculos > Verbas (GPEA040)**:

457 – Bônus acumulado (ele quem vai acumular o valor das outras verbas)

458 e 459 – Verbas que serão utilizadas para acumulação

![](https://tdn.totvs.com/download/attachments/527832819/image2019-12-23_18-10-48.png?version=1&modificationDate=1577135686557&api=v2)

* No cadastro de verbas Inclua a expressão no filtro da verba 457 (dentro da verba que será a que vai acumular os valores). Clique no campo Expr. Filtro e dê um TAB, clique em **Outras Ações > Incluir**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21185485014679)

* Preencha os campos **Código** e **Expressão** e clique em **Expressão de filtro > Expressão**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21185485027863)

* Digite a expressão e **Adiciona**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21185485035415)

* No cadastro de verbas Incluída expressão no filtro da verba 457 (dentro da verba que será a que vai acumular os valores).

![](https://tdn.totvs.com/download/attachments/527832819/image2019-12-23_18-12-42.png?version=1&modificationDate=1577135686493&api=v2)

* Inclusão de verba nos lançamentos fixos acesse Atualizações > Lançamentos > Lançamentos Fixos (GPEA550):

![](https://tdn.totvs.com/download/attachments/527832819/image2019-12-23_18-13-19.png?version=1&modificationDate=1577135686463&api=v2)

* Lançamento das duas verbas que devem ser usadas para a base de acumulação:

![](https://tdn.totvs.com/download/attachments/527832819/image2019-12-23_18-13-55.png?version=1&modificationDate=1577135686390&api=v2)

Cálculo efetuado:

![](https://tdn.totvs.com/download/attachments/527832819/image2019-12-23_18-10-23.png?version=1&modificationDate=1577135686590&api=v2)

O sistema acumulou os valores das duas verbas utilizadas para base e aplicou os 10% definidos nos valores fixos.

**Saiba mais:**

[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)
