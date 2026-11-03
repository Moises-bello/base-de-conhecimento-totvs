---
article_id: 36278209449623
category: Financeiro - Configurador de Tributos
content_hash: e7a2965b50749a7ec425c649de33b3c145b86b9540b9042b0d0a8332d2821905
fetched_at: '2026-06-28T22:37:45.808760+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FISA170 - O imposto está sendo
  gerado no financeiro, porém deveria constas apenas o calculo na NF
type: support-article
updated_at: '2025-11-12T12:25:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36278209449623-Cross-Segmentos-Backoffice-Linha-Protheus-FISA170-O-imposto-est%C3%A1-sendo-gerado-no-financeiro-por%C3%A9m-deveria-constas-apenas-o-calculo-na-NF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36278209437335) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
As regras fiscal e financeira foram configuradas; contudo, é necessário que o TX do imposto não seja levado ao financeiro. Qual procedimento deve ser adotado?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210.  
  
**Solução**  
Para que o imposto não seja gerado no financeiro, a regra fiscal não deve estar vinculada à regra financeira.

**Regra Fiscal → Regra de Cálculo do Documento Fiscal → Regra de Cálculo do Documento Fiscal.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36278209437719)

Localize a regra fiscal, clique em **Alterar** e desvincule a **Regra Financeira.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36278209439383)

Alternativamente, é possível criar uma cópia da regra, mantendo duas versões: uma com a regra financeira vinculada e outra sem vínculo financeiro.

Para realizar a cópia, acesse **"Outras Ações"** e, em seguida, selecione a opção **"Copiar"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36278209439511)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
