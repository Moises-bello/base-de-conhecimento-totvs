---
article_id: 360021541631
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: db6af223018da1baaa29f2601a883d2f9abafd64a93feaa8e94b6811cdf0c459
fetched_at: '2026-06-28T22:38:44.208762+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Aglutinação de itens no faturamento
type: support-article
updated_at: '2023-04-25T14:28:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021541631-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Aglutina%C3%A7%C3%A3o-de-itens-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como aglutinar itens no faturamento?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Protheus 12.  
  
**Solução**

Quando determinado produto é incluído no Pedido de Vendas e este possui referências, como por exemplo **Lote** e **Sub-Lote** a informação é registrada em "N" linhas na Tabela **"SC9 - Liberações de pedidos de venda"** e na Tabela **"SD2 - Itens das notas fiscais de saída**" de forma a manter a integridade dos dados, e estabelecer os devidos relacionamentos de cada quantidade com sua respectiva referência.

Ainda que um mesmo produto, por exemplo, possua quantidade suficiente para atender o Pedido, porém, rateada por 2 **Lotes** ou **Sub-Lotes** distintos, serão gerados 2 registros (2 linhas) diferentes na SC9 (de forma a relacionar cada quantidade com o respectivo lote e realizar as integrações do sistema corretamente).

**Assim, não é possível aglutinar as quantidades de um mesmo produto na NF** quando são gerados dois ou mais registros na Tabela SC9 para registro das referências (o DANFE se baseia nas informações da Tabela SD2, então é gerado da mesma forma).

Já para controles de Endereço e Serie não são gravados na SC9 e SD2, mas sim na Tabela SDC.

Deste modo, ao realizar a liberação de Estoque automaticamente o sistema seleciona os Endereços e Series (com base no conceito FEFO) gerando apenas uma linha na SC9.

No entanto, se liberar de forma manual, sendo imprescindível selecionar manualmente cada Endereço/Serie, então, serão geradas sequências de liberação C9\_SEQUEN em linhas distintas da SC9.

De igual modo, se na inclusão do Pedido for imprescindível selecionar manualmente cada Endereço/Serie (incluindo "n" registros para cada endereço / série) também seguirão para a SC9 e SD2 em linhas distintas, e não serão posteriormente aglutinados na Nota.

**Saiba mais:  
[FAT0008 Aglutinar Pedidos de Venda similares no mesmo Documento de Saída](https://tdn.totvs.com/x/nkJtDQ)**
