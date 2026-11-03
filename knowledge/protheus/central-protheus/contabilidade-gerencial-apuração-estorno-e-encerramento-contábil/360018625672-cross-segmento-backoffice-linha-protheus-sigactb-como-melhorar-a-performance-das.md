---
article_id: 360018625672
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 1bf640b6ebef45ea9009d8a681151c6d8e32bb330a65d0fbffa1fcafc58b0b34
fetched_at: '2026-06-28T22:41:05.035283+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como melhorar a performance
  das rotinas de contabilização e apuração?
type: support-article
updated_at: '2025-01-22T21:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018625672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-melhorar-a-performance-das-rotinas-de-contabiliza%C3%A7%C3%A3o-e-apura%C3%A7%C3%A3o
---

**Dúvida**

Como melhorar a performance das rotinas de contabilização e apuração?

**Ambiente**

Protheus – SIGACTB – A partir da versão 11.80

**Solução**

Para aumentar a performance das rotinas de **Contabilização On-Line**, **Apuração de Resultado (CTBA211)** e nas rotinas de inclusão de lançamentos pelo CTB (**CTBA101** e **CTBA102**), considere utilizar os seguintes pontos de entrada:

* **GRVCT3**
* **GRVCT4**
* **GRVCT7**
* **GRVCTI**

**Observação ⚠️:**  
Estes pontos de entrada devem retornar logicamente **.F.** (falso).

**Importante 📢️:**

* Com essa configuração, as tabelas de saldos não são atualizadas no momento da inclusão do lançamento. Por isso, é necessário executar periodicamente a rotina de **Reprocessamento**, garantindo que os saldos anteriores exibidos nos relatórios estejam corretos.
* Configure o parâmetro **MV\_ATUSAL** como **N** para acelerar o processo de gravação no **CT2**.
* Para otimizar ainda mais o desempenho, preste atenção ao preenchimento dos parâmetros "de" e "até" nas entidades de custo (**Centro de Custo**, **Item Contábil** e **Classe de Valor**).

**Dica 💡️:** Quando **não** for necessário filtrar essas entidades, **não** utilize o formato usual **<Branco> a ZZZZZZZZZZ**. Nesse caso, deixe os campos "de" e "até" em **BRANCO** para todas as entidades.
