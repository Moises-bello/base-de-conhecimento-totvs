---
article_id: 360034655853
category: RH - Rescisão
content_hash: fdcfff1646a12fa5abfe33125822ec6054279c5bc225e216e0096921464f0c5b
fetched_at: '2026-06-28T22:43:51.945637+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo errado das médias de aviso prévio quando
  o campo RG_MEDATU está igual a S, sistema não considera os últimos 12 meses
type: support-article
updated_at: '2025-07-15T10:54:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034655853-RH-Linha-Protheus-GPE-Calculo-errado-das-m%C3%A9dias-de-aviso-pr%C3%A9vio-quando-o-campo-RG-MEDATU-est%C3%A1-igual-a-S-sistema-n%C3%A3o-considera-os-%C3%BAltimos-12-meses
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33462420809495) Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Calculo errado das médias de aviso prévio quando o campo RG\_MEDATU está igual a S, sistema não considera os últimos 12 meses.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para que o sistema considere **os últimos 12 meses para a média de aviso prévio** quando o campo **RG\_MEDATU** está igual a S, parâmetro **MV\_MEDDIRE** = N, cadastro de sindicato = 0.

No cadastro de verbas, a aba médias, o campo Med. Av. Prev. "RV\_MEDAVI", tem que ficar igual a 12, desta forma o sistema irá considerar os 12 últimos meses para a média de avio prévio indenizado pelo ID de cálculo 0250.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
