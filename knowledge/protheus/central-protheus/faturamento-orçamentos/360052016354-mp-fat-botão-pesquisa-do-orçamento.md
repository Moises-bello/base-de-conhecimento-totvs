---
article_id: 360052016354
category: Faturamento - Orçamentos
content_hash: c5f9a2af6e16f0df8a9d8d06cf35c7cb552bd5e3d6c6ecdbba4ead53851917d4
fetched_at: '2026-06-28T22:38:24.994071+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP-FAT-Botão Pesquisa do Orçamento
type: support-article
updated_at: '2021-04-28T15:15:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052016354-MP-FAT-Bot%C3%A3o-Pesquisa-do-Or%C3%A7amento
---

**Dúvida**

Ao efetuar uma pequisa de cliente no botão Pequisa do Outras Ações do browser do Orçamento (**Mata415**), o processo não encontra o registro.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083278034/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084436613/mceclip1.png)  
   
 **Ambiente**

Microsiga Protheus -  a partir do release 12.1.25.  
  
**Solução**

O sistema não vai efetuar a pesquisa só pelo nome do cliente e loja, por que a ordem da pesquisa é número do orçamento, cliente e loja, se fizer a pesquisa com o número do orçamento, o sistema encontra corretamente.  
  
Se quiser efetuar a pesquisa por cliente, utilize a opção cliente, loja e data de emissão:  
![](https://totvssuporte.zendesk.com/attachments/token/QrzLu8xqumxlocW8kcAjCluwU/?name=inline-975516746.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/CXol3qqHPXumZ8svoNAaZwH0S/?name=inline312563597.png)​  
Na consulta por Número+Cliente+Loja, o campo número do orçamento é primordial, na consulta por Cliente+Loja e Emissão, o campo de cliente e loja são primordiais na consulta por isso que encontra corretamente.

O botão pesquisa também traz opções de pesquisa de orçamento por cotação/pedido, número de proposta e por Oportunidade+revisão de oportunidade:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083278614/mceclip2.png)
