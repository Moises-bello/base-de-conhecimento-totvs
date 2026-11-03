---
article_id: 4409566848407
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d80e6ba77365b163b328a7b21cc6db00023d8b437c6a572775a1f5f520cf52a1
fetched_at: '2026-06-28T22:38:38.489020+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como emitir
  uma remessa de comodato no módulo Faturamento
type: support-article
updated_at: '2021-10-22T21:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409566848407-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-emitir-uma-remessa-de-comodato-no-m%C3%B3dulo-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como emitir uma nota de remessa de comodato no módulo Faturamento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

A **Nota de Comodato** é caracterizado como  um ***empréstimo*** de produto ou bem a terceiros.

Dentro módulo faturamento, sendo o próprio cliente quem está emprestando, o processo que deverá ser efetuado da seguinte forma:

***1 -*** Pedido de vendas (**mata410**)***do tipo** **N- normal;***

***2-***Informe o cliente para quem se efetuará o empréstimo;

***3***- Informe a condição de pagamento (a informação é necessária,  devido o campo ser obrigatório o preenchimento no pedido de venda);

**4-**Informe o produto na linha item do pedido;

***5-*** Informe **um TES (mata080)**que controla **poder de terceiros remessa**, movimentação de ***estoque igual a sim*** e ***não gera financeiro***;

**6**-Confirme o Pedido, libere-o e fature-o.

O retorno do bem se dará através de :

***1-***Inclusão de ***N******ota de entrada (mata103) do tipo B- benficiamento;***

***2-***Utilize um **TES** que deverá controlar **poder de terceiros devolução**, movimentação de ***estoque igual a sim*** e ***não gerar financeiro;***

***3-*** Em outras ações, selecione a opção origem para selecionar os dados de terceiros da nota de origem.

***4-*** Confirme as informações de terceiro e salve a nota de entrada para gerar o retorno do empréstimo.

Em caso de cobrança do tempo do empréstimo, deverá emitir um ***pedido do tipo Normal, com*** **TES** que **não controla poder de terceiros**, **não movimenta estoque** e **só movimenta financeiro.**

 Mais detalhes e exemplos do processo, acesse a FAQ de **Poder DE/EM Terceiro**, aba empréstimos.

**Saiba Mais: [Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)**
