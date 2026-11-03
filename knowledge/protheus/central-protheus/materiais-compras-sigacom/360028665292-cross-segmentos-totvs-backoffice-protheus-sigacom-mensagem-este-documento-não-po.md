---
article_id: 360028665292
category: Materiais - Compras (SIGACOM)
content_hash: af760e3b50a8dca328bdaea46f571ac08ce4951fae5ad5819736692d25c883a1
fetched_at: '2026-06-28T22:41:13.025839+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Mensagem: Este Documento
  não possui controle de aprovação ou deve ser aprovado pelo controle de alçada'
type: support-article
updated_at: '2022-05-16T21:12:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028665292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-Este-Documento-n%C3%A3o-possui-controle-de-aprova%C3%A7%C3%A3o-ou-deve-ser-aprovado-pelo-controle-de-al%C3%A7ada
---

**Ocorrência**

Mensagem: Este Documento não possui controle de aprovação ou deve ser aprovado pelo controle de alçada

**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Causa**

Sistema não permite a inclusão e alteração do pedido de compra e ao visualizar os aprovadores apresenta o mensagem "Este Documento não possui controle de aprovação ou deve ser aprovado pelo controle de alçada"

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054839194/mceclip0.png)**

Tabela SAL não contém o mesmo compartilhamento de DBL   
  
**Solução**

O erro ocorre no ambiente, porque SAL não contém o mesmo compartilhamento de  DBL.  
Estas duas tabelas necessitam que o compartilhamento sejam iguais, pois a DBL é filha da SAL. 

Segue exemplo de como deve ser o compartilhamento, lembrando que temos 03 entidades que podem ficar diferentes conforme regra de negócio, porém sempre mantendo o mesmo compartilhamento entre as duas tabelas.

Segue exemplo onde as duas tabelas contém o mesmo compartilhamento:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029817432/mceclip4.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029817192/mceclip3.png)

Há um alerta com valide que apresenta o help a seguir para o usuário ao abri a rotina de Grupo de Aprovação (**MATA114**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058314953/mceclip0.png)
