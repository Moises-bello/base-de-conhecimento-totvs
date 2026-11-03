---
article_id: 360018586011
category: Originação de Grãos (OG)
content_hash: 48610c841d8fbc7d7458c1c034aeb9eaf8a07210d067757a14f17ed439a68bed
fetched_at: '2026-06-28T22:45:38.842595+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Contrato no romaneio com e sem pesagem
type: support-article
updated_at: '2025-06-25T11:16:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018586011-Agro-Linha-Protheus-AGR-Contrato-no-romaneio-com-e-sem-pesagem
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20283908250519)*** Tempo aproximado para leitura: **00:00:30 min  
  
Ocorrência**Nas rotinas **OGA251 -****Romaneio sem Pesagem** e **OGA250** **- Romaneio com Pesagem** ocorre erro ao informar o contrato: **invalid macro source (SSYacc0105e: Error token failed, no valid token) :{|| OGX010TC(FwFldGet('NJJ\_TIPO')),FwFldGet('NJJ\_CODENT'),FwFldGet('NJJ\_LOJENT'),FwFldGet('NJJ\_CODSAF'),FwFldGet('NJJ\_CODPRO')) } on FWSXB:GETSPECSHOW(FWSXB.PRW) 31/08/2018 13:40:11 line : 325**  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse erro ocorre porque o conteúdo da coluna XB\_CONTEM referente à tabela NJJ está incorreto.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **APSDU**;  
2. Procure pelo arquivo **SXB** e filtre pela tabela **NJJ.** Lembrando de deixar na opção de **Contém a Expressão**;  
3. Procure pelo **XB\_ALIAS = NJJ001** e **XB\_TIPO = 2** e altere o conteúdo para: **OGX010CT( OGX010TC(FwFldGet('NJJ\_TIPO')))**.
