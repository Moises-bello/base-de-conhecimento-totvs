---
article_id: 4410783995799
category: NFe - Nota Fiscal Eletrônica
content_hash: 9755932d91b81741821182203476d4478f1f0c2371a5e7b57a3f5bb24fcd0dd6
fetched_at: '2026-06-28T22:40:01.619869+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 999 Rejeição -
  Série indevida para a NFP referenciada (000=NFP/SE 001=NFP 100=NFP/SE modelo novo).'
type: support-article
updated_at: '2021-10-15T13:14:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410783995799--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-999-Rejei%C3%A7%C3%A3o-S%C3%A9rie-indevida-para-a-NFP-referenciada-000-NFP-SE-001-NFP-100-NFP-SE-modelo-novo
---

**Dúvida**Como solucionar 999 Rejeição - Série indevida para a NFP referenciada (000=NFP/SE 001=NFP 100=NFP/SE modelo novo)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Como corrigir as rejeições:**

**Rejeição 999 - Série indevida para a NFP referenciada (000=NFP/SE 001=NFP 100=NFP/SE modelo novo).**

**Parecer da SEFAZ-MT:**

Quando uma NFP for referenciada em uma NF-e de entrada, no preenchimento dos dados em "Notas Fiscais Referenciadas de Produtor (refNFP)", em se tratando de modelo 4 (NFP) o campo "Série" só poderá ser preenchido com os números:

000 (se for NFP Série Especial);

001 (se for NFP modelo 4) ou;

100 (se for NFP Série Especial novo modelo, emitido pelo ICMS Transparente).

Caso seja utilizada outra numeração de "série" para estes casos, retornará a seguinte mensagem de rejeição "A Série ou o número da NFP referenciada estão incompatíveis".

Além de só poderem ser utilizadas as numerações 000, 001 e 100 no campo "Série" da NFP referenciada, também deve-se levar em consideração as seguintes numerações das NFP a serem referenciadas:

**1)**    Para a SÉRIE “000” (NFP/SE), a numeração da NFP referenciada deve ser maior que 11.000.000 e menor que 16.000.000;

**2)**   Para a SÉRIE “001” (NFP modelo 4), a numeração da NFP referenciada deve ser maior que 16.000.000;

Para a SÉRIE “100” (NFP/SE novo modelo emitido pelo ICMS Transparente), a numeração da NFP referenciada deve ser maior ou igual a 1 e menor que 2.000.000.

**Solução:**

Conforme a regra demonstrada no parecer da SEFAZ, a Nota Fiscal do Produtor deverá ser incluída no documento de entrada com a **serie 000, 001 ou 100.**

Além disso, deve ser incluída **a série do parâmetro **MV\_ESPECIE Ex: 001=SPED;** (isso se verifica no configurador)**
