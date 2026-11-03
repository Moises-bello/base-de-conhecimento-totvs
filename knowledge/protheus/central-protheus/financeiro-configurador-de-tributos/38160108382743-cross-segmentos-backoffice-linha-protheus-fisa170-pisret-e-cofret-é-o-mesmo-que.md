---
article_id: 38160108382743
category: Financeiro - Configurador de Tributos
content_hash: 3c8c67d550b0a196afb432250d70065dc07d82d5adf2ed7cb66cca8c6c73ccaf
fetched_at: '2026-06-28T22:37:45.812523+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FISA170 - PISRET e COFRET é o
  mesmo que PIS e COFINS na regra financeira
type: support-article
updated_at: '2026-02-04T18:59:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38160108382743-Cross-Segmentos-Backoffice-Linha-Protheus-FISA170-PISRET-e-COFRET-%C3%A9-o-mesmo-que-PIS-e-COFINS-na-regra-financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38160118556823) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O código **PISRET** e **COFRET** é o mesmo que **PIS** e **COFINS** no financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FISA170 - A partir da release 12.1.2210.  
  
**Solução**  
Para o financeiro, **NÃO.** Para que o sistema gere a retenção de **PIS** e **Cofins**, é **obrigatório** informar exatamente as siglas **PIS** (para retenção do PIS) e **COF** (para retenção do Cofins) na aba, tributos da regra financeira. Caso seja utilizada qualquer outra sigla diferente dessas, o sistema entenderá como um **tributo novo**, e a retenção **não será considerada** como PIS ou Cofins.

O fiscal permite vincular impostos a um **IDTOTVS,**garantindo que sejam reconhecidos como impostos do legado. Por esse motivo, ao cadastrar uma **Regra de Cálculo - Documentos Fiscais**pararetenção do **pis e cofins,**o campo **Tributo (F2B\_TRIB)** deve ser preenchido com a sigla **PISRET** ou **COFRET**. Esses códigos estão vinculados ao **IDTOTVS**, o que faz com que o sistema reconheça corretamente como retenção de **PIS** e **Cofins** nas rotinas fiscais.

**Saiba mais**

[PISRET e COFRET é o mesmo que PIS e COFINS?](https://tdn.totvs.com/pages/releaseview.action?pageId=977862277)
