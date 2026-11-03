---
article_id: 18952192624791
category: Financeiro - Baixas a Pagar
content_hash: fa3c80102ee90707cd9c75c912d77f4b97936e291891dfcaed887b58bd1b77bc
fetched_at: '2026-06-28T22:37:24.877522+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBAFIN / FINA080 - Qual o lançamento
  padrão que será contabilizado os impostos LP 510 ou LP 530 quando temos um Título
  NF de PJ com impostos  IRPJ / PCC parametrizados para gerar impostos na baixa do
  tipo NF
type: support-article
updated_at: '2026-03-25T14:41:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18952192624791-Cross-Segmentos-Backoffice-Linha-Protheus-CTBAFIN-FINA080-Qual-o-lan%C3%A7amento-padr%C3%A3o-que-ser%C3%A1-contabilizado-os-impostos-LP-510-ou-LP-530-quando-temos-um-T%C3%ADtulo-NF-de-PJ-com-impostos-IRPJ-PCC-parametrizados-para-gerar-impostos-na-baixa-do-tipo-NF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18952180437271) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**

Qual o lançamento padrão que será contabilizado os impostos LP 510 ou LP 530 quando temos um título NF de PJ com impostos IRPJ/PCC parametrizados para gerar impostos na baixa do tipo NF?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - Todas as versões.  
  
**Solução**

Para contabilizar os impostos que ainda serão gerados, no momento da baixa de um título do **tipo NF,** os impostos serão automaticamente criados e terão que ser contabilizados também pelo **LP 530.**

Sugere-se as seguintes configurações (ou uma ou outra) para obtenção de valores do **IRRF** na contabilização dos **LPs 530** (**baixa C.Pagar)** e **532** (**baixa Borderô**):  
  
o    **E2\_VRETIRF**  
o    If (**E5\_PRETIRF** $ “ /4”, **E5\_VRETIRF**,0)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18952201974423)](https://centraldeatendimento.totvs.com/hc/article_attachments/18952201974423)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/18952232848279)](https://centraldeatendimento.totvs.com/hc/article_attachments/18952232848279)

**Saiba mais:**

[A retenção de IRRF na baixa passa a ter controle de retenção semelhante ao existente](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[para Pis, Cofins e Csll. Com essa melhoria, temos facilitado o controle de pendência](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[de retenção de impostos quando o mínimo para retenção não é atingido.](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[No entanto, algumas mudanças nos procedimentos para contabilização das](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[rotinas abaixo sofreram alterações](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[(dependendo da configuração dos lançamentos padrões referente a baixa de contas a pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)  
[(LP 530 e 532) do cliente).](https://tdn.totvs.com/pages/releaseview.action?pageId=6070741)

[4843069 DSERFINP-23489 DT Campos E2\_PIS, E2\_COFINS e E2\_CSLL zerando na Contabilização](https://tdn.totvs.com/pages/releaseview.action?pageId=498442607)

[Contabilização para títulos de impostos pcc - contas a pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=73075505)
