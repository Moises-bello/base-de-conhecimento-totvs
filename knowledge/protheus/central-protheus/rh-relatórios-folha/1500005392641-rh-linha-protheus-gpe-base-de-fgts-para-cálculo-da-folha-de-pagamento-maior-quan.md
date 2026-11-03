---
article_id: 1500005392641
category: RH - Relatórios Folha
content_hash: b6b2cf123f65f4809a1fa3189c5da929faa04417dea8638e97614d7f46b96330
fetched_at: '2026-06-28T22:43:17.436130+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Base de FGTS para cálculo da Folha de Pagamento
  maior quando possui verba de Falta
type: support-article
updated_at: '2025-07-31T05:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005392641-RH-Linha-Protheus-GPE-Base-de-FGTS-para-c%C3%A1lculo-da-Folha-de-Pagamento-maior-quando-possui-verba-de-Falta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25976905765399) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No cálculo da Folha de Pagamento é apresentada a **base do FGTS** (Fundo de Garantia do Tempo de Serviço) maior quando existe a verba de **Falta (ID0054)**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**O sistema **não realiza** o abatimento de Faltas na Base de FGTS, quando na verba, a **incidência** do campo Ref. a 13º está como S - Sim.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.** Acesse a rotina de **Verbas (GPEA040)** através do menu **Atualizações > Definições de Cálculo > Verbas (GPEA040),** e selecione a verba de **Falta** com **Id.0054,** e na Aba de **Incidências,** altere o campo de **Referência do 13º Salário** para **Não:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007446241)**

**2.** Após ajuste, basta recalcular a Folha de Pagamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25978138766103)

**Saiba mais:**[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)
