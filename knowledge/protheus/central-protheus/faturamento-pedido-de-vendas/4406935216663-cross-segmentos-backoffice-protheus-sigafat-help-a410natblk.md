---
article_id: 4406935216663
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 51887114d980136c7e4753f939f55419d6380c5810f8cfacc7c30cc8ea9014cb
fetched_at: '2026-06-28T22:38:39.812293+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410NATBLK
type: support-article
updated_at: '2024-03-13T20:59:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406935216663-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410NATBLK
---

**Ocorrência**Ao salvar o Pedido de Venda ocorre Help A410NATBLK.  
![help.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4406938795799)  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**Indica que foi configurado (nos parâmetros MV\_1DUPNAT / MV\_2DUPNAT) para considerar a Natureza do Cadastro do Cliente/Fornecedor de acordo com o Tipo de Pedido (C5\_TIPO).

Porém, a Natureza preenchida está bloqueada (inativo), conforme informação do Help de tela. É necessário utilizar uma natureza que esteja ativa.

**Solução**

Realize a seguinte verificação:

1. Se for uma nota de diferente de "Devolução" ou "Beneficiamento":

* Avalie o Conteúdo do parâmetro MV\_1DUPNAT
* Se estiver apontando para SA1->A1\_NATUREZ, verifique a Natureza preenchida neste campo, no Cadastro do Cliente (CRMA980);
* Se estiver apontando para SC5->C5\_NATUREZ, verifique a Natureza preenchida neste campo, no cabeçalho do Pedido de Vendas (MATA410);

2. Se fo uma nota de "Devolução" ou "Beneficiamento"

* Avalie o Conteúdo do parâmetro MV\_2DUPNAT
* Se estiver apontando para SA2->A2\_NATUREZ, verifique a Natureza preenchida neste campo, no Cadastro do Fornecedor;
* Se estiver apontando para SC5->C5\_NATUREZ, verifique a Natureza preenchida neste campo, no cabeçalho do Pedido de Vendas (MATA410);

Ao identificar a Natureza que o sistema esta utilizando, verifique se a mesma se encontra bloqueada para uso em seu cadastro.

Desbloqueando a Natureza ou mudando ela, o sistema deixará de apresentar o help.

**Saiba mais:   
[FAT0038\_A410NATVZO\_A410NATUSO\_A410NATCLI\_A410NATPED\_ A410NATBLK \_ no Pedido de Vendas (MATA410)](https://tdn.totvs.com/x/h_ruDQ)**
