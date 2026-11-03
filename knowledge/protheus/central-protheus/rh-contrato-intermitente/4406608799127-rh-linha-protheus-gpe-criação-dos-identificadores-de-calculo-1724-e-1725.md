---
article_id: 4406608799127
category: RH - Contrato Intermitente
content_hash: c0fca65137560dbbf846d5c891129ea6d902d204e48f0d61901c51b147de5091
fetched_at: '2026-06-28T22:43:40.112243+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Criação dos identificadores de calculo 1724 e 1725
type: support-article
updated_at: '2025-04-15T17:39:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406608799127-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-dos-identificadores-de-calculo-1724-e-1725
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25868785828503)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Criação dos identificadores de calculo **1724 e 1725** para **Férias Antecipadas Intermitente** e **13º Antecipado Intermitente**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Sistema está bloqueando a alteração do contrato do funcionário (prevista na lei e no eSocial) de contrato intermitente para indeterminado.  
Está validando se existem convocações (quaisquer), sendo que deveria avaliar e bloquear apenas para quando existirem convocações ativas.  
  
**Solução**

Realizado ajuste para somente bloquear a alteração se existirem convocações com inicio ou fim igual ou posteriores ao período ativo.

Foi criado dois novos identificadores de cálculo:

**1724** - Férias Antecipadas Intermitente (Desconto)

**1725** - 13. Antecipado Intermitente  (Desconto)

Para que seja descontado, no momento do cálculo da rescisão, as verbas de férias e 13º pagas no período que o funcionário possuía contrato intermitente.

Estas verbas devem ser cadastradas com as mesmas incidências das verbas de Férias (ID.: 0072) e 2ª Parcela do 13º (ID.: 0024), para que os impostos sobre férias e 13º sejam calculados corretamente.  
  
**Saiba Mais**  
O ambiente deve estar devidamente atualizado com o pacote de expedição continua do RH: <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao_continua>

[RH - Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
