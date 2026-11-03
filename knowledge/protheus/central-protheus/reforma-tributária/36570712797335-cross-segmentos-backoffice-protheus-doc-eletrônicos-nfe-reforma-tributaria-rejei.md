---
article_id: 36570712797335
category: Reforma Tributária
content_hash: ae557d598a7b452b1239d314a8a5f9aecae81ca902052df3b7bfc9911307c0de
fetched_at: '2026-06-28T22:39:53.756674+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1041: Valor do IBS da UF difere do calculado [nItem: 999]'
type: support-article
updated_at: '2025-12-19T17:43:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36570712797335-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1041-Valor-do-IBS-da-UF-difere-do-calculado-nItem-999
---

**Dúvida**  
Como corrigir a Rejeição 1041: Valor do IBS da UF difere do calculado [nItem: 999]  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Se informado grupo IBS de competência das Unidades Federadas (gIBSUF):  
- Valor do IBS Estadual (vIBSUF) deverá ser resultante de: vIBSUF = (gIBSCBS/vBC x (pIBSUF / 100)) - vDif - vDevTrib

**Observação 1**: Aceitar uma tolerância de 0,01 a mais ou a menos

**Observação 2**: Em caso de preenchimento do grupo de redução (gIBSUF/gRed) a alíquota utilizada deverá ser a tag Alíquota Efetiva (gIBSUF/gRed/pAliqEfet): vIBSUF = (gIBSCBS/vBC x (pAliqEfet / 100)) - vDif - vDevTrib

Para não ocorrer a rejeição 1041 é necessario que o Protheus e TSS estejam com as atualizações da documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

Obs: Caso seu TSS esteja em ambiente Cloud e seja compartilhado não haverá necessidade de solicitar atualização, pois a equipe TSS Cloud mantem o TSS sempre atualizado.
