---
article_id: 7302662965527
category: TAF - eSocial - Eventos Periódicos
content_hash: 1d5b1859142c5fc2f707fa5558dca0e73f77d80a74cd3c2b0243a0413959c364
fetched_at: '2026-06-28T22:45:18.981302+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - Ocorrência: 846
  - Descrição : O somatorio de cada um dos descontos de Contribuicao Previdenciaria
  (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34, 35]) não
  pode ser negativo.'
type: support-article
updated_at: '2026-06-25T12:32:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7302662965527-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-Ocorr%C3%AAncia-846-Descri%C3%A7%C3%A3o-O-somatorio-de-cada-um-dos-descontos-de-Contribuicao-Previdenciaria-codIncCP-31-32-34-35-e-de-IRRF-codIncIRRF-31-32-33-34-35-n%C3%A3o-pode-ser-negativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23813445112855) Tempo aproximado para leitura: **05:00:00 min****Ocorrência**  
Inconsistência retornada ao tentar transmitir o evento do eSocial S-1210:

*"Codigo da Ocorrência: 846 - Descrição : O somatorio de cada um dos descontos de Contribuicao Previdenciaria (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34, 35]) não pode ser negativo."*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1200 (TAFA250) - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social - Todas as versões

**Causa**A inconsistência 846 ocorre pois no envio do registro S-1200 deste funcionário em questão, as rubricas de Desconto com incidência de INSS e IRRF tiveram um valor maior que as rubricas de provento que possuem a incidência de INSS e IRRF.  
  
**Solução**Orientamos a leitura das documentações relacionadas abaixo:

[RH - RM - FOP - eSocial - Erro código 846 - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34]) não pode ser negativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6846770140823)

[RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência RET 846 - O somatório de cada um dos descontos de Contribuição Previdenciária (codIncCP = [31, 32, 34, 35]) e de IRRF (codIncIRRF = [31, 32, 33, 34, 35]) não pode ser negativo, ou seja,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040767034)
