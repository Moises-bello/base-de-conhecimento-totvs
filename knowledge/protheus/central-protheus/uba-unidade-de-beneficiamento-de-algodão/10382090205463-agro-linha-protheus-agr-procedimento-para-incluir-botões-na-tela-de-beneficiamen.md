---
article_id: 10382090205463
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: bac86d2c60d0ee96343029c463dd8472d5e3490246013a6f951942d63ae8ac38
fetched_at: '2026-06-28T22:45:35.564965+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para incluir botões na tela de Beneficiamento
type: support-article
updated_at: '2025-06-18T13:20:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10382090205463-Agro-Linha-Protheus-AGR-Procedimento-para-incluir-bot%C3%B5es-na-tela-de-Beneficiamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21069463991703) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Como incluir botões na tela do beneficiamento?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
**Solução**Foi desenvolvido o **AG615BTN - Permitir criar novos objetos na tela do Beneficiamento de Fardão**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10381905243543)

`User Function AG615BTN()`

`Local oObjTela  := PARAMIXB[1]`

`Local oSizeTela := PARAMIXB[2]`

`Private oBtn    := NIL`

`oBtn  := TButton():New(oSizeTela:aPosObj[1,1] + 65 , oSizeTela:aPosObj[1,2], OemToAnsi("label do botão"), oObjTela, { || U_Função() }, 045, 015,,, .f., .t., .f., , .f.,,, .f. )`

`Return nil`
