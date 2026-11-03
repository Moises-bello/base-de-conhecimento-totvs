---
article_id: 38140766772247
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: a64041c706cb0f6a348d0af65e61b1fc4f15578d46d75738ea538653676bbd25
fetched_at: '2026-06-28T22:39:15.753367+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Impossibilidade
  de preenchimento do CST de Devolução quando informado cClassTrib
type: support-article
updated_at: '2026-02-03T20:20:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38140766772247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Impossibilidade-de-preenchimento-do-CST-de-Devolu%C3%A7%C3%A3o-quando-informado-cClassTrib
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38140766762647) Tempo aproximado para leitura: **10:00 min**  
  
**Ocorrência**  
Quando possui o cClassTrib de IBS e CBS informado na Regra de Escrituração, o campo de **CST Dev** fica permanece bloqueado e não permite preenchimento.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310  
  
**Causa**  
Quando a **R****egra de Escrituração** possui o campo **cClassTrib** informado, o sistema não permite o preenchimento do **CST Dev.**  
  
**Solução**  
Esse comportamento é padrão do sistema, isso ocorre porque o **cClassTrib utilizado na nota de origem** é o mesmo aplicado automaticamente na nota de devolução.

Quando o **cClassTrib** está configurado na Regra de Escrituração, ele passa a ser o responsável pela definição da tributação, não sendo necessário o preenchimento do campo de **CST Dev**.

O uso do **cClassTrib** garante consistência tributária entre a nota de origem e a devolução, evitando divergências fiscais.

**Documentações relacionadas:**

[Escrita Fiscal - Reforma Tributaria - CBS e IBS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/33305945453079-Escrita-Fiscal-Reforma-Tributaria-CBS-e-IBS)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Atualização para Reforma Tributária e Adequação para a Reforma Tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34792278750999-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Atualiza%C3%A7%C3%A3o-para-Reforma-Tribut%C3%A1ria-e-Adequa%C3%A7%C3%A3o-para-a-Reforma-Tribut%C3%A1ria)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
