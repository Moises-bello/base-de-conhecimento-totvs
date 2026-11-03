---
article_id: 360051286113
category: RH - Folha de Pagamento
content_hash: f302752438921b7b23950d0b1af5f5e157faf42a8f9151db845f7a6ab79ce27c
fetched_at: '2026-06-28T22:44:12.049940+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de folha apresenta verba de custo de provisão
  de férias e 13º (ID's 0194, 0195 e 0196)
type: support-article
updated_at: '2025-08-11T21:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051286113-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-folha-apresenta-verba-de-custo-de-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-ID-s-0194-0195-e-0196
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337358003863) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Cálculo de folha apresenta verbas de custo de provisão de férias e 13º.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Preenchimento das colunas "% Prov. Fer.", "% Prov. 13º" e "% Prov. Resc", na tabela S037.  
 **Solução**Acesse **>Atualizações >Definição de Cálculo >Manutenção de Tabela >Tabela S037** e exclua o percentual informado para as colunas **"% Prov. Fer.", "% Prov. 13º" e "% Prov. Resc":  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9448647744535)**

**Conceito:**Esses Identificadores de cálculo, funcionam como uma "Provisão Sintética". Eles são usados quando o cliente não deseja usar a rotina de provisão (Miscelânea - Provisão - Provisão 13/ Férias), então utilizam apenas um % de provisionamento na tabela S037 (Versão 12 - Atualizações - Definição de Cálculo - Manutenção de Tabela), onde tem 3 colunas pra informar os percentuais que serão gerados sobre esta verba, que são os campos: "% Prov. Fer.", "% Prov. 13º" e "% Prov. Resc".

Logo, são utilizados esses campos para calcular essas verbas apenas quando não é utilizada mensalmente a rotina de provisão e mesmo assim deseja fixar um percentual sobre a folha pra levar estas verbas para contabilidade.

**Importante:** Para saber como compor o valor que formará a base de cálculo para a provisão na folha, verifique a configuração descrita na documentação disponível no link abaixo e realize os ajustes conforme sua necessidade:   
[RH - Linha Protheus - GPE - Funcionalidade do campo RV\_CUSTO no cadastro de verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6503898874007-RH-Linha-Protheus-GPE-Funcionalidade-do-campo-RV-CUSTO-no-cadastro-de-verbas?source=search)  
  
**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
