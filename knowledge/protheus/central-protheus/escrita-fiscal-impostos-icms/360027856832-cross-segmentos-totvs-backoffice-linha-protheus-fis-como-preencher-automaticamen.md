---
article_id: 360027856832
category: Escrita Fiscal - Impostos - ICMS
content_hash: e2b12967e4cdbcc7230cf2a6ed863d4e9c74676b5f59f06681bc95c74bb34048
fetched_at: '2026-06-28T22:39:24.115503+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como preencher automaticamente
  o campo FT_VICPRST para geração da tag vICMSSubstituto?
type: support-article
updated_at: '2025-07-28T15:04:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027856832-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-preencher-automaticamente-o-campo-FT-VICPRST-para-gera%C3%A7%C3%A3o-da-tag-vICMSSubstituto
---

**Dúvida**

Como preencher automaticamente o campo FT\_VICPRST para geração da tag vICMSSubstituto?

**Ambiente**

Protheus – Livros fiscais– A partir da versão 11.80  
  
**Solução**

Implementada solução para que a tag **vICMSSubstituto** seja gerada com base nas informações inseridas nos campos **D1\_ICMNDES**, **D1\_BASNDES** e **D1\_ALQNDES**, quando a operação possui **CST 60**, porém, não se é o imediato da cadeia da operação.

Importante!

Na situação detalhada nesse documento, as informações referente ao ICMS já recolhido anteriormente será preenchido manualmente nos campos **D1\_ICMNDES**, **D1\_BASNDES** e**D1\_ALQNDES**.  
De acordo com essas informações será gerada a tag **vICMSSubstituto** com a seguinte variação:

* Caso o parâmetro **MV\_ULTAQUI**seja igual a **3**:  
  **Base Retido**= D1\_BASNDES / Quantidade de Entrada \* Quantidade de Saída **Valor do Próprio do Substituto**= ((Base Retido \* (MV\_ICMPAD/100)) - D1\_ICMNDES) / Quantidade de Entrada \* Quantidade de Saída
* Caso o parâmetro **MV\_ULTAQUI**seja qualquer outro valor que não **3:  
  Base Retido**= D1\_BASNDES **Valor do Próprio do Substituto**= ((Base Retido \* (MV\_ICMPAD/100)) - D1\_ICMNDES)

Exemplo de configuração

MV\_estado = SP  
MV\_ULtaqui = 1  
  
  
1) nota fiscal de entradas = RS  
![](https://totvssuporte.zendesk.com/attachments/token/5utENno8TqQhfwchC7hQCbgkQ/?name=inline-1209824182.png)  
TES  
Calcula icms = não  
Atualiza estoque = sim  
L fiscal icms = outros  
CST = 60  
MKP ICM COMP = sim  
Marg solid = nunca  
  
  
Os campos  
**D1\_ICMNDES**, **D1\_BASNDES** e **D1\_ALQNDES**) ​= preenchidos de forma manual.  
  
![](https://totvssuporte.zendesk.com/attachments/token/ba1rq4UiLAlFRUsfvPW3xuQ7l/?name=inline-1209517767.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/6Oy9fpBnNUFwiyVxZsnSPRGur/?name=inline1067545435.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/7qePvzTMHdewGWbyWqRunlEPT/?name=inline-2114492773.png)​  
  
Na nota fiscal de saídas CFOP 5405  
TES

Atualiza estoque = sim  
Calcula icms = não  
L fiscal icms = outros  
CST = 60  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/7UVkZmsKHLGYwiA2z5kiJspef/?name=inline-1607431196.png)​  
tipo de cliente = revendedor  
  
![](https://totvssuporte.zendesk.com/attachments/token/SFGi60k48MYdJNExhKtwZ2aah/?name=inline-1785466236.png)​  
  
Para o tipo de cliente consumidor Final a TAG do ICMS ST recolhido anteriormente não será gerada.
