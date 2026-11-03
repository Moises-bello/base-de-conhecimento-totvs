---
article_id: 360024672454
category: Faturamento - Cenários de Venda
content_hash: 8a98022516ac524b2ddb9bd3f7a5a385a02f2f30cc1818d817ffb01005ef47c2
fetched_at: '2026-06-28T22:38:33.993572+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT -Bloqueio de venda
  de produto sem tabela de preço
type: support-article
updated_at: '2023-07-12T21:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024672454-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Bloqueio-de-venda-de-produto-sem-tabela-de-pre%C3%A7o
---

**Dúvida**

No sistema é possível bloquear o produto que não está cadastrado na tabela de preço (**OMSA010**)para que não seja vendido? 

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

No padrão do sistema não é possível, por que o conceito do faturamento é efetuar a venda independente de uso de tabela de preço.   
Se realmente há a necessidade de se bloquear o produto (**MATA010**) que não esteja vinculado a uma tabela de preço, para que não seja vendido por um preço não estabelecido, recomenda-se efetuar a validação por ponto de entrada na pedido de venda(**MATA410**), seja na linha de item ou no botão confirmar:  
  
**M410LIOK** - ***[M410LIOK - Valida&ccedil;&atilde;o de linha de pedido](http://tdn.totvs.com/pages/viewpage.action?pageId=6784149)***  
  
**MT410TOK** - ***<http://tdn.totvs.com/pages/viewpage.action?pageId=6784353>***

**Obs:** Se houver a necessidade do bloqueio também no orçamento de vendas **(MATA415),**recomenda-se efetuar o mesmo processo com os pontos de entrada **A415LIOK** (linha do item) e **A415TDOK** (botão confirmar), a documentação pode ser obtida através do artigo: **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada da rotina MATA415](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028294312-MP-FAT-Pontos-de-Entrada-MATA415)**
