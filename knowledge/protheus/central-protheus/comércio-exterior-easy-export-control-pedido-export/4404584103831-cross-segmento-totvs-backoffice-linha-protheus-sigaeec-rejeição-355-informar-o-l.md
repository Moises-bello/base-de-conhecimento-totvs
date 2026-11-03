---
article_id: 4404584103831
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 957c51acf082afe66a8651b783c3e2d28aa604da3f88daea92f577b8302c48c0
fetched_at: '2026-06-28T22:36:59.072803+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Rejeição 355:
  Informar o local de saída do Pais no caso da exportação'
type: support-article
updated_at: '2022-07-14T00:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404584103831-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Rejei%C3%A7%C3%A3o-355-Informar-o-local-de-sa%C3%ADda-do-Pais-no-caso-da-exporta%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição abaixo:  
355 Rejeição: Informar o local de saída do Pais no caso da exportação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Easy Export Control – A partir da versão 11.80  
  
**Solução**Para criação da *tag*, será verificada as informações da via de transporte definido na aba transporte, verifica-se o cadastro de Portos/Aeroportos onde é retornado o conteúdo do campo **Y9\_ESTADO e Y9\_DESCR.**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404572697239/mceclip5.png)  
  
A rejeição  também pode indicar a falta do Local de despacho, esta informação é preenchida no Embarque exportação campo **EEC\_URFDSP**.  
![](https://totvssuporte.zendesk.com/attachments/token/BMbU6nZvK9N9wnETffFviXfZl/?name=inline1457300656.png)

Cadastro de portos e aeroportos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360055661613/mceclip0.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404572826007/mceclip7.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404584093079/mceclip6.png)

* **Exemplo do XML:**

**![EXPORTACAO_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360096282413/EXPORTACAO_1.PNG)**

* **Validação da Sefaz:**

![EXPORTACAO_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360094018474/EXPORTACAO_2.PNG)
