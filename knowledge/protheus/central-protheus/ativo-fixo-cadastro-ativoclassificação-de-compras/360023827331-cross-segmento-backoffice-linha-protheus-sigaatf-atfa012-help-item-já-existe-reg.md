---
article_id: 360023827331
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 5d7a3b174f17a0baf900d3755b5b42e3e5292a8c08bee4d1c5f585ef3c687e85
fetched_at: '2026-06-28T22:41:48.287902+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF  - ATFA012 Help: Item
  "Já existe registro com está informação". '
type: support-article
updated_at: '2023-11-30T15:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023827331-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Help-Item-J%C3%A1-existe-registro-com-est%C3%A1-informa%C3%A7%C3%A3o
---

**Dúvida**

Ao tentar cadastra o bem sistema apresenta mensagem **Help : Item**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021363112)  
  
**Ambiente**  
Microsiga Protheus – Ativo fixo – A partir da versão 11.80

**Causa**

Mensagem é apresentada pois foi informado  "Cod. do bem " e " Item"  de um bem já existente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021298711)  
  
**Solução**

Verifique se existe na filial posicionada registro com o mesmo Código do bem e item, existindo utilizar outros valores a chave de validação é  N1\_FILIAL + N1\_CBASE + N1\_ITEM.

Não existindo entrar em contato com suporte do módulo.
