---
article_id: 22107017385495
category: Financeiro - Consultas / Relatórios
content_hash: 89f66ee4959cd14ec2e286fa20a03b8f012224c751b0749f9e3a0af7f10410a1
fetched_at: '2026-06-28T22:37:58.480920+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR130 - Valores líquidos
  no relatório de contas a receber
type: support-article
updated_at: '2024-04-29T20:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22107017385495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR130-Valores-l%C3%ADquidos-no-relat%C3%B3rio-de-contas-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22107025391639) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como tratar os valores líquidos no relatório de contas a receber?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**No **Contas a receber**, os impostos são tratados como abatimento e temos os campos no parâmetro do relatório **FINR130** que atua exatamente nesta situação  "**Considera Abatimento? = Sim**" e **"Abatimentos?"**.  
  
- **Abatimentos**: Possui três tipos seleções sendo "**Listar**", "**Não Listar"** e "**Não Considerar**".  
- **Listar**: Os valores de impostos (Abatimentos) serão listados no relatório sendo demonstrado o valor do titulo a menor.  
- **Não Listar**: Os valores de impostos (Abatimentos) "não" serão listados no relatório sendo demonstrado o valor do titulo a menor.  
- **Não Considerar**: Os valores de impostos (Abatimentos) "não" serão listados no relatório e o valor do titulo será demonstrado em sua totalidade sem considerar os abatimentos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22107124015639)

Mas esta situação só é possível se o abatimento dos impostos forem na emissão, desse modo seria viável  a sua demonstração, uma vez que eles já iriam existir devido a sua geração ser na emissão. Caso seja na baixa do título, o relatório **FINR130** vai demonstrar apenas os valores totais **"bruto"**.

**Saiba Mais:**[FINR130 - Títulos a Receber - Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=547226162)
