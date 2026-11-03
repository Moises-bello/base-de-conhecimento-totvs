---
article_id: 360036175113
category: RH - Recibos e Cheques
content_hash: bf31bd5b575f477b71c5cee4ebc44b51ed838075b9a3336fef9608fa26117177
fetched_at: '2026-06-28T22:43:29.604221+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a impressão do recibo de pagamento
  para matriculas aleatórias?
type: support-article
updated_at: '2021-06-07T14:14:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036175113-RH-Linha-Protheus-GPE-Como-parametrizar-a-impress%C3%A3o-do-recibo-de-pagamento-para-matriculas-aleat%C3%B3rias
---

**Dúvida**Como parametrizar o sistema para que imprima o recibo de pagamento para matrículas aleatórias de uma única vez?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para imprimir o recibo de pagamento para matriculas aleatórias (que não são sequenciais), deve ser parametrizado na aba FILTRO, conforme abaixo:

1. Ir para a aba **Filtro**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047394513/mceclip0.png)  
  
2. Clique em **Campo** e escolha **Matrícula** e clique em **Operador** e escolha **Esta Contido em**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046531234/mceclip1.png)  
  
3. No campo **Expressão** coloque as matriculas a serem impressas separadas por um espaço:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046531354/mceclip2.png)  
  
4. Clique em **Incluir**, assim as matriculas serão incluídas conforme abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047395493/mceclip3.png)  
  
5. Clique no **botão Param.**, e nas perguntas **Matricula De?** e **Matricula Até?** deixe conforme abaixo:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047396053/mceclip4.png)  
  
6. Clique em **OK** e imprima os recibos.
