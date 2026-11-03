---
article_id: 1500007525521
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 301c4ce8bbf996cd8bcad070bde94f97c1f3359d0e1a709290665bf8efdc9cd7
fetched_at: '2026-06-28T22:39:36.760183+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  retenção de impostos - Cliente órgão público '
type: support-article
updated_at: '2021-06-22T13:02:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007525521-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-reten%C3%A7%C3%A3o-de-impostos-Cliente-%C3%B3rg%C3%A3o-p%C3%BAblico
---

**Dúvida**Qual a configuração necessária para cálculo e retenção (PCC e IRRF) para cliente órgão público?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**Para que ocorra o cálculo e retenção do PCC / IRRF deverá configurar os cadastros a seguir:

**Cadastro do Cliente**

Rec. COFINS (A1\_RECCOFI) = P - Empresa Pública  
Rec. PIS (A1\_RECPIS) = P - Empresa Pública  
Rec. CSLL (A1\_RECCSLL) = P - Empresa Pública  
Modo Abat. Im. (A1\_ABATIMP) = 2 - Efetua retenção

Recolhe IRRF (A1\_RECIRRF) = 1 - SIM (caso o cliente seja o responsável pelo recolhimento) ou 2 - Não (Caso o prestador do serviço seja o responsável pelo recolhimento).  
Vlr. Mín. IRRF (A1\_MINIRF) = 1 – Sim - O Sistema não considera o parâmetro MV\_VLRETIR que possui o valor mínimo para retenção do IRRF.

**Cadastro de Natureza**

Calcula PIS (ED\_CALCPIS) = Sim

Percentual de PIS (ED\_PERCPIS) = Informe a alíquota

Calcula COFINS (ED\_CALCCOF) = Sim

Percentual de COFINS (ED\_PERCCOF) = Informe a alíquota

Calcula CSLL (ED\_CALCCSL) = Sim

Percentual de CSLL (ED\_PERCCSL) = Informe a alíquota

Calcula IRRF (ED\_CALCIRF) = SIM

Porc. IRRF (ED\_PERCIRF) = Informe a alíquota

**Cadastro do Produto**

Retém PIS (B1\_PIS) = Sim

Retém COFINS (B1\_COFINS) = Sim

Retém CSLL (B1\_CSLL) = Sim

Ret. Operação (B1\_RETOPER) = Sim - Não considera valor mínimo de retenção

Impos. Renda (B1\_IRRF) = Sim

**Cadastro do TES**

Gera Dupl. (F4\_DUPLIC) = S - sim

Agrega Valor (F4\_AGREG) = S - sim
