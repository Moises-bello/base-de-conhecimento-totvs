---
article_id: 4411156641303
category: RH - Soluções para error.log
content_hash: 7e5723966577c47e163cbf94a25623ebeec892eac36db6cb54bfeb4cf573e4e9
fetched_at: '2026-06-28T22:44:08.840692+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Erro ao efetuar cálculo de rescisão - type mismatch
  on compare  on FGRAVATRP(GPEXMED.PRX)
type: support-article
updated_at: '2025-09-11T17:45:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411156641303-RH-Linha-Protheus-GPE-Erro-ao-efetuar-c%C3%A1lculo-de-rescis%C3%A3o-type-mismatch-on-compare-on-FGRAVATRP-GPEXMED-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34873704978327) Tempo aproximado para leitura: **00:01:00min****Ocorrência**Ao tentar efetuar **cálculo de rescisão** através da rotina **GPEM040** gera *error log:* "***type mismatch on compare on* FGRAVATRP(GPEXMED.PRX)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões.  
  
**Causa**O erro ocorre pois o parâmetro **MV\_COMISSA** possui o tipo diferente de **NUMÉRICO.**  
  
**Solução**Para correção do erro é necessário a manutenção do parâmetro, conforme o padrão, abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411161132567)

**Saiba Mais:**  
Pacote de Expedição Contínua do Gestão de Pessoal conforme abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
