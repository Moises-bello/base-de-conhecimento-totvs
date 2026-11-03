---
article_id: 360016775931
category: Financeiro - Contas a Pagar
content_hash: df3c550eb3266f00db3f11cf42fce7650c0afe5ce39637c947a5adba50b08491
fetched_at: '2026-06-28T22:38:07.098996+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Data de Vencimento
  do PCC gerado de acordo com a emissão ou  baixa
type: support-article
updated_at: '2025-05-09T19:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016775931-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Data-de-Vencimento-do-PCC-gerado-de-acordo-com-a-emiss%C3%A3o-ou-baixa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31354176872343)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Data de Vencimento do PCC gerado conforme a emissão ou baixa.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**

**Definição de Vencimento dos Títulos de Impostos de PCC no Contas a Pagar**

A data de vencimento dos títulos de impostos relativos ao PCC (Programa de Capacitação Continuada) varia conforme o momento em que ocorre a retenção do imposto:

1. **PCC Retido na Emissão do Título**  
   Quando a retenção do PCC ocorre no momento da **emissão** do título, o vencimento dos respectivos impostos será sempre no **dia 20 do mês subsequente à data de vencimento do título**.  
   *Exemplo:* Se um título tem vencimento em **12/10/2018**, o vencimento do imposto de PCC será em **20/11/2018**.
2. **PCC Retido na Baixa do Título**  
   Quando a retenção do PCC se dá no momento da **baixa** do título, o vencimento dos impostos será definido como o **dia 20 do mês subsequente à data da baixa**.  
   *Exemplo:* Um título emitido em **28/09/2018**, com vencimento em **12/10/2018**, mas cuja baixa foi efetuada em **28/09/2018**, terá o vencimento dos impostos de PCC em **20/10/2018**.
3. **Configuração do Comportamento via Parâmetro**  
   O comportamento descrito é controlado pelo parâmetro **MV\_BX10925** no módulo de Contas a Pagar (FINA050), com os seguintes valores possíveis:

* **"1"** – cálculo do PCC realizado na **baixa** do título;
* **"2"** – cálculo do PCC realizado na **emissão** do título.

**Saiba mais**

[Data\_de\_Vencimento\_dos\_impostos](https://tdn.totvs.com/display/public/PROT/FIN0074_CPAG_Data_de_Vencimento_dos_impostos)
