---
article_id: 360052081034
category: Escrita Fiscal - Impostos - ICMS
content_hash: 753388e1c496a6a364c6bfee21776186799e0903612c54b76bffae82c303bdf8
fetched_at: '2026-06-28T22:39:24.272223+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Abatimento do ICMS
  do Custo do Item
type: support-article
updated_at: '2021-07-28T14:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052081034-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Abatimento-do-ICMS-do-Custo-do-Item
---

**Dúvida**Como efetuar o abatimento do ICMS do custo do item  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Verificar o conteúdo do parâmetro abaixo:

**MV\_CREDICM**: Indica abatimento do valor do ICMS

Este parâmetro indica que o valor do ICMS será abatido do custo do item no documento de entrada. Para que isso ocorra, o TES utilizado no item deve estar configurado com os campos F4\_CREDICM igual a S e F4\_AGREG igual a I (ICMS+Mer).

     -Se o valor do parâmetro for falso (.F.) então o valor do ICMS não será abatido do custo do item (funcionamento padrão do sistema);  
     -Se o valor do parâmetro for verdadeiro (.T.) então o valor do ICMS será abatido do custo do item.

O mesmo é utilizado nas seguintes rotinas:

     -Acerto do custo de entrada (MATA190)  
     -Documento de entrada (MATA103)  
  
**Configuração:**

Tipo de conteúdo: Lógico  
 Descrição: Determina se o valor do ICMS será abatido do custo do item ao utilizar TES com os campos F4\_CREDICM igual a S e F4\_AGREG igual a I.  
 Valor padrão: .F.
