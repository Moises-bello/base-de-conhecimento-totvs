---
article_id: 360042243573
category: NFe - Nota Fiscal Eletrônica
content_hash: a9ebefed06677658098c02d7011301d921e547bf91c96fabf3e7b4bba0050bf2
fetched_at: '2026-06-28T22:40:05.410025+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 866 Rejeição: Ausência
  de troco quando o valor dos pagamentos informados for maior que o total da nota'
type: support-article
updated_at: '2025-07-28T19:09:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042243573-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-866-Rejei%C3%A7%C3%A3o-Aus%C3%AAncia-de-troco-quando-o-valor-dos-pagamentos-informados-for-maior-que-o-total-da-nota
---

**Dúvida**Como solucionar a Rejeição 866: Ausência de troco quando o valor dos  
pagamentos informados for maior que o total da  
nota ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se gerada a Tag **vPag** maior que a TAG do total da nota  **vNF**  deve ser gerada a TAG **vTroco**

Se a TAG **vTroco** não for gerada **causa a rejeição 866.**

1. Caso a nota seja feito pelo módulo do faturamento a ***TAG vTroco e gerada apenas, através do ponto de entrada abaixo:***

**[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)**

Observação: Caso queira deixar o valor padrão (tag <tPag>), não há necessidade de alterações nos valores do array 'AdetPag'.

2. Realize um teste ***com RDMAKE padrão do link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

3. Após isso, ***exclua a nota e gere novamente.***

* **Saiba mais:**

Se a nota for realizada pelo módulo do Loja mesmo que seja NFe verificar os procedimentos abaixo:

***[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015881672)***

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056685673)
