---
article_id: 4408647550231
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 36fffd34189140d460befcb778c941a1ea01673c71785622a38ed44cc230760c
fetched_at: '2026-06-28T22:39:36.850125+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alíquotas de PIS
  e COFINS retenção somente pelo cadastro de natureza
type: support-article
updated_at: '2021-09-15T20:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408647550231-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquotas-de-PIS-e-COFINS-reten%C3%A7%C3%A3o-somente-pelo-cadastro-de-natureza
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como configurar o sistema para as alíquotas de PIS e COFINS retenção validarem somente o cadastro da natureza?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS -  a partir da release P12.1.25  
  
**Solução**

O sistema determinam a ordem de validação das alíquotas de PIS e COFINS retenção através dos parâmetros MV\_TPALPIS e MV\_TPALCOF

|  |  |
| --- | --- |
| MV\_TPALPIS | Indica como é obtida a alíquota do PIS para retenção:  1 = apenas do cadastro de naturezas;  2 = do cadastro de produtos, ou do cadastro de naturezas, ou do parâmetro **MV\_TXPIS** (conteúdo padrão); o Sistema considera o primeiro percentual que estiver preenchido, nessa sequência de prioridade. |
| MV\_TPALCOF | Indica como deve ser obtida a alíquota da COFINS para retenção:  1 = apenas do cadastro de naturezas;  2 = ou do cadastro de produtos, ou do cadastro de naturezas, ou do parâmetro **MV\_TXCOFIN** (conteúdo padrão); o Sistema considera o primeiro percentual que estiver preenchido, nessa sequência de prioridade. |

Outro processo que pode ser utilizado é o seguinte:  
  
Deixar o cadastro do produto sem alíquotas de PIS/COFINS e utilizar os parâmetros MV\_TXPIS e MV\_TXCOFIN para as alíquotas de PIS/COFINS apuração.

E para PIS/COFINS retenção as alíquotas no cadastro de natureza.
