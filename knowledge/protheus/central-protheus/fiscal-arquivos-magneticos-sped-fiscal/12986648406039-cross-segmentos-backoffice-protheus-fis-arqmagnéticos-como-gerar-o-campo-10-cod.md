---
article_id: 12986648406039
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: adcf947bec52580c6f89ada84965e1cada7d8f3b521a195a098507cc22833f77
fetched_at: '2026-06-28T22:42:02.647159+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  campo 10 - COD_CTA no registro H010 do Sped Fiscal?
type: support-article
updated_at: '2023-03-10T11:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12986648406039-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-10-COD-CTA-no-registro-H010-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida** Como gerar o campo **10 - COD\_CTA** no registro **H010** do **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para levar a conta contábil para o registro **H010 - Inventário**, é necessário que o campo **Cta Contabil -  B1\_CONTA** no cadastro do produto esteja preenchido.  
  
Caso a nota já tenha sido lançada sem tal informação, basta informar a **conta contábil** no campo **B1\_CONTA** e gerar novamente o **Sped Fiscal** que o campo será devidamente apresentado com o dado.

Também é possível informar a conta através do ponto de entrada **SPDFIS07**:  
[SPDFIS07 - Conta Contábil registro H010](https://tdn.totvs.com/pages/releaseview.action?pageId=702821885)
