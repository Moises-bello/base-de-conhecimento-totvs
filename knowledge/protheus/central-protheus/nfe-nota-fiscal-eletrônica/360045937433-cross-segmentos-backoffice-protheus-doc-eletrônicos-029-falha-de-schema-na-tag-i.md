---
article_id: 360045937433
category: NFe - Nota Fiscal Eletrônica
content_hash: b08ffc42c6f2795be26bfb549886407de65700e75727a6440def8f9555e8fb57
fetched_at: '2026-06-28T22:40:03.154206+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  029: Falha de
  schema na Tag <ICMS>'
type: support-article
updated_at: '2025-07-09T12:21:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045937433-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-ICMS
---

**Dúvida**

Como solucionar a falha de Schema referente a TAG ICMS ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao gerar falha de Schema referente ao **ICMS** verifique se o seu XML gerou conforme o exemplo abaixo:  
  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/Pa52J7eu4mGZt810de0tI9289/?name=inline243025923.png)​  
  
  
2- Conforme o XML acima não foi preenchido a situação tributária do **ICMS**que é obrigatória.  
  
  
3- Para a correção preencher o CST do ICMS, campo no TES **F4\_SITTRIB** deve estar preenchido **Sit. trib. ICM**  
  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/v5tWGe5MHFcRlcP3zxkv0S1PH/?name=inline-1526359182.png)  
  
  
4- Após isso, exclua a nota e gere novamente. Se for utilizar o mesmo pedido digite novamente a TES para que a situação tributária fique correta.

* ***Caso Seja emitente do Simples Nacional***

1 - Para a correção preencher o **CSONS** do ICMS no TES o campo **F4\_CSOSN** deve estar preenchido **Cod. Sit. SN**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347640381207)**

2 - Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** **MV\_CODREG =** **1**

3- Após isso, exclua a nota e gere novamente. Se for utilizar o mesmo pedido digite novamente a TES para que a **situação tributária fique correta.**

* **Saiba mais:**

**Se estiver preenchido no TES:**

1- Verifique se está correto o campo C6\_CLASFIS "**Sit. trib"** este campo deve estar como **exemplo 000**, O primeiro número é referente a **origem do produto e os outros dois referente a situação tributária do ICMS.**  
  
  
2- Exclua essa nota no pedido de **vendas ou compra digite novamente o TES** e verifique se irá atualizar o campo Sit. trib. com **exemplo 000** conforme abaixo:  
  
  
​![C6_CLASFIS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347640397207)  
  
  
3- Se não estiver atualizando é possível **alterar manualmente.**

4- Após isso, gere o **documento e transmita.**
