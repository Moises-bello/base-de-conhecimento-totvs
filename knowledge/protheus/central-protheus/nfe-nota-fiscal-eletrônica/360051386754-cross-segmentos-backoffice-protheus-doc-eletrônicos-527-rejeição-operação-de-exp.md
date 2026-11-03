---
article_id: 360051386754
category: NFe - Nota Fiscal Eletrônica
content_hash: 1ddcdca26157f8436fbd5502749c21f26d3a97ab12c638220dc03c0fed822b77
fetched_at: '2026-06-28T22:40:05.086040+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 527 Rejeição: Operação
  de Exportação com informação de ICMS incompatível'
type: support-article
updated_at: '2025-08-11T23:48:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051386754-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-527-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-de-Exporta%C3%A7%C3%A3o-com-informa%C3%A7%C3%A3o-de-ICMS-incompat%C3%ADvel
---

**Dúvida**Como solucionar a rejeição 527 Rejeição: Operação de Exportação com informação de ICMS incompatível ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se o CFOP iniciado por 7 a Sefaz considera que se trata de uma operação de exportação.

1- Caso seja necessário **alterar o CFOP** altere pelo TES da nota no campo **Cod. Fiscal "F4\_CF":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20868553259671)

2- Após isso, exclua a nota e gere novamente.

3- **Se o CFOP** estiver correto sendo **iniciado por 7 é necessário que a** situação tributária do ICMS **seja 41 ou CSOSN 300 Para simples Nacional conforme o exemplo abaixo:**

* Regime Normal

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080801714)

* Regime do Simples Nacional

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081872433)

3- Altere a situação tributária no TES no campo  **Sit. trib. ICMS** **(F4\_SITTRIB) = 41**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20868567785239)

4- Após isso, exclua a nota e gere novamente. Se for utilizar o mesmo pedido digite novamente o TES para alterar a situação tributária no pedido.

5- Se emitente do Simples Nacional Altere a situação tributária no TES no campo  **F4\_CSOSN "Campo Cod. Sit. SN" = 300**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20868553279383)

6 - Após isso, exclua a nota e gere novamente.

* **Saiba mais:**

Exceção: A regra acima não se aplica para a NF-e de devolução (finNFe=4).

* **Validação da Sefaz:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080801094)
