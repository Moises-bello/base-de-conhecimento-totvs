---
article_id: 360059409254
category: NFe - Nota Fiscal Eletrônica
content_hash: eb9b9d8bcfc913f6999a0ffc0bd6cbd6a78f689400532eac048d9f6626696bcf
fetched_at: '2026-06-28T22:40:01.482862+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 538 Rejeição:
  Total do IPI difere do somatório dos itens '
type: support-article
updated_at: '2021-10-11T17:48:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059409254--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-538-Rejei%C3%A7%C3%A3o-Total-do-IPI-difere-do-somat%C3%B3rio-dos-itens
---

**Dúvida**Como solucionar a 538 Rejeição: Total do IPI difere do somatório dos itens ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O valor do IPI nos itens somados  na TAG **vIPI** deve bater com os valores levados no bloco **ICMSTOT** somando **vIPI de todos os itens.**

* Conforme o link abaixo:

[MP-NFE-Destaque de ICMS e IPI em XML e DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019535652-MP-NFE-Destaque-de-ICMS-e-IPI-em-XML-e-DANFE?source=search)  
  
Os únicos CSTs de IPI que **destacam o imposto são 00 e 49** para **entrada, 50 e 99 para saída.**

1- Altere no TES no campo F4\_CTIPI **Cod. trib. IPI**  
  
  
![mceclip0.png](https://totvssuporte.zendesk.com/hc/article_attachments/360057026893/mceclip0.png)

2 - Para notas que **não seja de importação**, verifique no TES se o **Campo Agrega valor (F4\_AGREG = S)**

**![f4_agreg.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102141393/f4_agreg.JPG)**

3-  Caso já esteja conforme acima verificar **se o ambiente está atualizado:**

* **Protheus:**

[MP - NFE - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

* **TSS:**

[TSS - Atualizações do TSS - Totvs Sped Service - Release 12.1.25 | 12.1.27](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025392671)

4- Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

[Links de todos os artigos de NFe](https://centraldeatendimento.totvs.com/hc/pt-br/sections/207068528-NFe-Nota-Fiscal-Eletr%C3%B4nica)
