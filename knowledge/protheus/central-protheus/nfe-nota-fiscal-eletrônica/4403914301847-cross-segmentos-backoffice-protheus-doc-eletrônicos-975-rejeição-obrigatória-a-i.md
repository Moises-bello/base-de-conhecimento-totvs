---
article_id: 4403914301847
category: NFe - Nota Fiscal Eletrônica
content_hash: 54a30ba962cbf22c9feee5acccb2ada6e590b92766366485c82ccd83f28c1ab8
fetched_at: '2026-06-28T22:40:01.614088+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 975 Rejeição :
  Obrigatória a informação do identificador do CSRT e do Hash do CSRT'
type: support-article
updated_at: '2021-09-08T19:42:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403914301847--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-975-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3ria-a-informa%C3%A7%C3%A3o-do-identificador-do-CSRT-e-do-Hash-do-CSRT
---

**Dúvida**Como solucionar a rejeição abaixo:

975 Rejeição : Obrigatória a informação do identificador do CSRT e do Hash do CSRT  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado o grupo do **Responsável Técnico** é obrigatória a informação do  
identificador do **CSRT (tag: idCSRT) e Hash do CSRT (tag: hashCSRT)**  
**Observação:** Implementação a critério da UF

1 - A informação do identificador do **CSRT e do Hash do CSRT,** só são obrigatórias caso seja informado o **responsável técnico**. Neste momento as UFS de obrigatoriedade do responsável técnico são **AM, MS, PE, PR, SC e TO e SC.** **Conforme** o link abaixo:

***[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024938732)***

2- Caso seja as UFs acima há uma ISSUE aberta no desenvolvimento para atender a **Nota Técnica 2020.005,** abrir um ticket no suporte para associar:

**DSERTSS1-15988**

3- Caso seja uma UF diferente,  Será necessário **criar o parâmetro manualmente** caso não tenha no configurador ou **alterar manualmente** caso esteja como **lógico para Caractere** conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045665794/mceclip0.png)

* **Parâmetro no Configurador:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042201073/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041365354/mceclip4.png)

4- Deixe o parâmetro em **branco " Sem conteúdo":**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045665994/mceclip1.png)

 5 - Após isso, **exclua a nota e gere** novamente.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403914578839/mceclip0.png)**
