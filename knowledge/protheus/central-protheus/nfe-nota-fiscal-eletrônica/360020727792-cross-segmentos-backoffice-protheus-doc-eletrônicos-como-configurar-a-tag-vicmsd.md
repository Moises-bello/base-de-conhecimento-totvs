---
article_id: 360020727792
category: NFe - Nota Fiscal Eletrônica
content_hash: d2fcb3229f2426d9b6252ba761a99b777e40b8bc16d95f29b15ecafe6dbdab64
fetched_at: '2026-06-28T22:40:05.644615+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como configurar
  a TAG vICMSDeson para suframa
type: support-article
updated_at: '2025-07-18T18:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020727792-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-a-TAG-vICMSDeson-para-suframa
---

**Dúvida**Como configurar a TAG vICMSDeson para suframa ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Para gerar a **TAG vICMSDeson** para Suframa é necessário verificar se o grupo da situação tributária na nota técnica  contempla as **TAGs vICMSDeson e motDesICMS**

1. Preencher no TES a Situação tributária do ICMS Sit. trib. ICM ***F4\_SITTRIB**   **40, 41 e 50***

***![20220419_140813.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548474445335)***

2. Preencher no TES os campos Mot. Desone ***F4\_MOTICMS= 7 e*** Calcula ICMS ***F4\_ICM= Sim***

***![20220419_141455.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548565053335)***

***![20220419_142200.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548748789399)***

3. Preencher no TES a situação tributária do Pis e do Cofins **Sit. trib. PIS F4\_CSTPIS = 06 e do Sit. trib. COF.  F4\_CSTCOF = 06**

**![20220419_141639.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548616713367)**

4. Preencher para o  **ICMS-ST** Situação tributária do ICMS Sit. trib. ICM **F4\_SITTRIB =** **30.**

**![20220419_142010.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548708284951)**

5. Preencher no TES os campos Mot. Desone  **F4\_MOTICMS= 7 e** Calcula ICMS **F4\_ICM= Sim**  com Agrega solid **F4\_AGREG = S- Sim.**

**![20220419_142310.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5548745022999)**

* **Saiba mais:**

Se houver apenas cálculo de **Pis e Cofins** poderá utilizar **outras situações tributárias**, mas apenas se houver só cálculo de Pis e Cofins **sem ICMS suframa**. Neste caso não preencher o motivo de desoneração no TES.

**Para Suframa é gravado o conteúdo na tabela SD2:**

* **Para o ICMS, Pis e Cofins** = D2\_DESCZFR
* **Para o Pis =**D2\_DESCZFP
* **Para o Confins =** D2\_DESCZFC

**Para Suframa é gravado o conteúdo na tabela SD1:**

* **Para o ICMS, Pis e Cofins** = D1\_DESCZFR
* **Para o Pis =**D1\_DESCZFP
* **Para o Confins =** D1\_DESCZFC

Caso seja nota de **SUFRAMA**realizar as configurações abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](CROSS%20Segmentos%20-%20TOTVS%20Backoffice%20Linha%20Protheus%20-%20FIS-%20Como%20configurar%20o%20sistema%20para%20calcular%20SUFRAMA?)

* **Importante:**

Caso o **Pis e o Cofins** não possa ser destacado na **TAG Vdesc** utilizar o parâmetro do link abaixo:  
  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como atender a Portaria Suframa 275/2009 no XML](Cross%20Segmentos%20-%20Backoffice%20Protheus%20-%20Doc.%20Eletr%C3%B4nicos%20-%20Como%20atender%20a%20Portaria%20Suframa%20275/2009%20no%20XML)

* **Saiba mais:**

**Caso** a empresa seja emitente **do Simples Nacional:**

Para o **Simples nacional** o sistema calcula o Suframa, porém não levamos para o XML, pois não há nenhum grupo do **CSOSN** que tenha a **TAG Vicmsdeson.**  
  
Sendo assim, para que não cause a rejeição o suframa **não pode** ser calculado. Verifique com a Sefaz se esse desconto pode ser na TAG ***vDESC*** ou direto no valor do Produto.  
  
Caso seja na ***Vdesc*** poderá utilizar os campos de desconto no cadastro de produto.

* **Saiba mais:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 934 Rejeição : Não informado valor do ICMS desonerado ou o Motivo de desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025687693)
