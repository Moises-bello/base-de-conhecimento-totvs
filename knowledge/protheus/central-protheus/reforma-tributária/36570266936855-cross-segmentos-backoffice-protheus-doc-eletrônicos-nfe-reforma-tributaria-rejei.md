---
article_id: 36570266936855
category: Reforma Tributária
content_hash: a8e49bdfc4a20f6e3905105d308f0d00d1f2036935eb7796bf8a8c53a1351206
fetched_at: '2026-06-28T22:39:53.753260+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1035: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente
  [nItem: 999]'
type: support-article
updated_at: '2025-11-25T13:02:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36570266936855-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1035-Valor-da-Al%C3%ADquota-Efetiva-do-IBS-da-UF-calculado-incorretamente-nItem-999
---

**Dúvida**  
Como corrigir a Rejeição 1035: Valor da Alíquota Efetiva do IBS da UF calculado incorretamente [nItem: 999]?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Se informado grupo de Redução de Alíquota (gIBSUF/gRed):  
- Alíquota Efetiva (tag: pAliqEfet) deve ser o resultado de:

- Se NÃO houver compra governamental (grupo gCompraGov não informado): pAliqEfet = pIBSUF × (1 - pRedAliq / 100).

- Se houver compra governamental (grupo gCompraGov informado):  
pAliqEfet = pIBSUF × (1 - pRedAliq / 100) × (1 - gCompraGov/pRedutor / 100).  
Exemplo: Redução de 40% na alíquota:  
Alíquota vigente (A): 10%  
Redução na alíquota (R): 40%  
Redutor de compras governamentais (RG): 5%  
Alíquota Efetiva (E): E = A \* (1 - R)\*(1- RG) E = 10 \* (1 - 0,4) \*(1 - 0,05) = 5,7 Observação: O cálculo da pAliqEfet deve considerar 4 casas decimais, com arredondamento na última casa decimal.

Para não ocorrer a rejeição 1035 é necessario que o Protheus e TSS estejam com as atualizações da documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

Obs: Caso seu TSS esteja em ambiente Cloud e seja compartilhado não haverá necessidade de solicitar atualização, pois a equipe TSS Cloud mantem o TSS sempre atualizado.
