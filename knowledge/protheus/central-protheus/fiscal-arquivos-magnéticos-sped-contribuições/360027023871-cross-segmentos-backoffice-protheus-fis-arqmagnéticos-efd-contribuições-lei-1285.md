---
article_id: 360027023871
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: e4664e36d3128800e69389911f91f366fb86b87ab269417918e9041ae931d3c7
fetched_at: '2026-06-28T22:42:05.210419+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Lei 12.859 crédito EFD Contribuições Nafta Petroquímica
type: support-article
updated_at: '2023-01-04T18:08:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027023871-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Lei-12-859-cr%C3%A9dito-EFD-Contribui%C3%A7%C3%B5es-Nafta-Petroqu%C3%ADmica
---

**Dúvida**  
Procedimentos de configuração referente o cálculo e Lei 12.859 crédito EFD Contribuições Nafta Petroquímica.  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução  
  
Apuração**

**TES**  
PIS/COFINS (F4\_PISCOF) = Ambos

Cred. PIS/COF = Credita

Tp Regime (F4\_TPREG) = Não cumulativo

**PARÂMETROS**

MV\_TXPIS = 1.65

MV\_TXCOFIN = 7.6

**Retenção**  
Para a retenção de 1,00% e 4,60%, configure a natureza e outros cadastros:

**NATUREZA**

Calcula PIS (ED\_CALCPIS) = Sim

Percentual de PIS (ED\_PERCPIS) = 1,00

Calcula COFINS (ED\_CALCCOF) = Sim

Percentual de COFINS (ED\_PERCCOF) = 4,60

**PRODUTOS**

Retem PIS (B1\_PIS) = Sim

Retem COFINS (B1\_COFINS) = Sim
