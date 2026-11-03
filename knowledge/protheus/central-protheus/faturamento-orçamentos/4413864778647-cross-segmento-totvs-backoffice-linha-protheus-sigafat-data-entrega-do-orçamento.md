---
article_id: 4413864778647
category: Faturamento - Orçamentos
content_hash: 2f139544335928794ca57f3f03247b4913a81fdc8abc3f9652655542f1ac6718
fetched_at: '2026-06-28T22:38:24.933359+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Data Entrega
  do Orçamento na Efetivação do Pedido de Vendas
type: support-article
updated_at: '2021-11-22T18:40:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413864778647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Data-Entrega-do-Or%C3%A7amento-na-Efetiva%C3%A7%C3%A3o-do-Pedido-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao efetivar um orçamento antigo para pedido de venda, o mesmo não respeita a data entrega no pedido, levando para o campo data de entrega um valor vencido. 

Exemplo:

|  |  |
| --- | --- |
| Incluiu Orçamento | 10/10/2021 |
| Data entrega | 13/10/2021 |
| Aprovação do Orçamento | 22/11/2021 |
| Pedido de Venda com Data Entrega | 13/10/2021 |

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões  
  
**Causa**Ao efetivar o orçamento não foi atualizado as informações e ajustado o campo data entrega.  
  
**Solução**O campo **CK\_ENTREG**recebe por padrão do sistema a data da variável **dDataCnd**, que por sua vez é alimentada pelo campo **CJ\_EMISSAO**.  
O campo **CJ\_EMISSAO**tem um inicializador padrão **DDATABASE**.      
  
Não há ponto de entrada para alteração de data de entrega, o que pode tentar é utilizar a validação da linha para gerar uma nova data, segue o ponto da linha do orçamento:

**A415LIOK**- <http://tdn.totvs.com/pages/viewpage.action?pageId=6784038>
