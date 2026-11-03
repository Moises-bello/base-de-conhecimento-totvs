---
article_id: 4402435493271
category: SIGAEST - SALDOS
content_hash: f0cf2795de3494556ee82e6d535e8a2654a8ab3a4ae244238e847c134bb27915
fetched_at: '2026-06-28T22:39:14.830509+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Analise de
  divergência de Saldo Atual/Posição de produtos com controle de Lote e/ou Endereço
type: support-article
updated_at: '2026-03-26T21:47:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402435493271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-Analise-de-diverg%C3%AAncia-de-Saldo-Atual-Posi%C3%A7%C3%A3o-de-produtos-com-controle-de-Lote-e-ou-Endere%C3%A7o
---

Este artigo orienta a investigar divergências no saldo de produtos com controle de lote e endereço. Recomenda usar pelo menos três fontes: relatório MATR282 para conferir saldos entre tabelas SB2, SB8 e SBF; relatórios MATR255 e MATR425 para posição de estoque; relatórios MATR275 e MATR435 para histórico de movimentações; e consultas diretas nas tabelas. Para correção, sugere estornar movimentos ou usar a rotina Refaz Saldos (MATA300).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39324511705367) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como investigar se o saldo de um produto com controle de rastreabilidade (lote/sub-lote) e/ou controle de endereçamento está correto e como identificar a origem de uma eventual divergência?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para analisar a homogeneidade dos saldos de estoque em produtos com controle de lote e endereço, é fundamental comparar os dados entre diferentes fontes de consulta do sistema (relatórios, consultas em tela e tabelas). A recomendação é **sempre utilizar ao menos três fontes de embasamento** para confirmar uma divergência.

**1. Relatório de Conferência de Saldos (**[**MATR282**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000317301-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Como-incluir-o-relat%C3%B3rio-MATR282-no-menu)**):**

* Acesse: **Módulo 04 (Estoque/Custos) -> Relatórios -> Genéricos -> Conferência de Saldos**.
* Este relatório identifica divergências entre as tabelas **SB2** (Saldos Físico e Financeiro), **SB8** (Saldos por Lote) e **SBF** (Saldos por Endereço).
* **Parametrização Crítica:** Defina "Saldo a Considerar" = **Movimento** e "Data Referência" = **Data base do ambiente** ([**detalhes neste artigo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-MP-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF)).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402426587415)

**2. Relatórios de Posição de Estoque (MATR255 e MATR425):**

* **MATR255 (Endereço):** Relatórios -> Endereçamento -> Saldo em Estoque.
* **MATR425 (Lote):** Relatórios -> Rastreabilidade -> Saldo em Estoque.

Ao emitir, verifique além da quantidade as colunas de **Empenho, Validade, Endereço e Lote**, garantindo que o saldo disponível não está menor devido a reservas (empenhos).

Perguntas como**"Data de Validade de Lote De/Até"*****,*** **"Armazém De/Até", "Do Endereço De/Até", "Do Lote De/Até"**, devem ser preenchidas com o máximo critério.

![Posicao_de_Estoque_por_Lote_e_Endereco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402428187671)

**3. Relatórios de Kardex (MATR275 e MATR435):**

* **MATR275 (Endereço):** Relatórios -> Endereçamento -> Kardex.
* **MATR435 (Lote):** Relatórios -> Rastreabilidade -> Kardex.

Estes relatórios mostram o histórico de entradas e saídas. Devem ser parametrizados com os mesmos critérios (datas, armazéns, lotes) para que a análise seja coesa.

Perguntas como **"De/Até Data", "Armazém De/Até", "Do Endereço De/Até", "Do Lote De/Até"**devem ser preenchidas com o máximo critério.

![Kardex_por_Lote_e_Endereco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402435049111)

**4. Consulta via Base de Dados (Tabelas):**

Para usuários com maiores privilégios de acesso à Base de Dados, podem consultar as tabelas de Saldos por Lote e por Endereço (tabelas SB8 e SBF). Realizando a comparação com a tabela SB2 (que irá trazer o saldo total aglutinando todos os lotes e endereços). Essa consulta pode ser feita via **Consultas -> Cadastros -> Genéricos** ou via **APSDU/Banco de Dados**:

* **SB2:** Campos `B2_QATU` (Saldo Atual) e `B2_EMPENHO` (Saldo Empenhado).
* **SB8:** Campos `B8_SALDO` (saldo físico atual) e `B8_LOTECTL` (código do lote) e `B8_EMPENHO` (saldo físico empenhado).
* **SBF:** Campos `BF_QUANT`(quantidade física atual), `BF_LOCALIZ` (código do endereço), `BF_LOTECTL` (código do lote) e `BF_EMPENHO`(quantidade física empenhada).

![Consulta_Generica_e_APSDU.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402435368855)

Com essas fontes de embasamento ficará mais fácil identificar se de fato há uma divergência de Lote e Endereçamento no seu ambiente.

**5. Correção de Divergências:**

* Identifique se a divergência foi causada por algum movimento específico e tente realizar o estorno para reestabelecer a coesão.
* Caso a origem não seja identificada, execute a rotina **Refaz Saldos (MATA300)**. Esta rotina remonta os saldos (incluindo lote e endereço) com base nos registros de movimentações e requisições.

Em caso de maior necessidade de auxílio, basta contatar o suporte técnico da TOTVS. É importante que na abertura do ticket seja evidenciada as bases de análises apontadas neste artigo para que possamos melhor compreender o cenário de divergência.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Dicas de Analise de divergência de Saldo Atual/Posição de Saldo em Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009601821)

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
