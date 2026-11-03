---
article_id: 360035537654
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3c7ba5b583b55c928d5b4cb585a0a00282eedd52066f2f7ffd7080bbac8babc0
fetched_at: '2026-06-28T22:38:29.787345+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Contrato de Parceria (FATA400)
type: support-article
updated_at: '2025-10-21T11:03:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035537654-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Contrato-de-Parceria-FATA400
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35773842302615) Tempo aproximado para leitura: **00:05************:00 min******

**Dúvida**

Como funciona o fluxo do Contrato de Parceria (FATA400) no módulo Faturamento e quais são suas particularidades?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.

**Solução**

O Contrato de Parceria tem por finalidade gerenciar o controle de parcerias para o processo de venda, com o objetivo de atender às seguintes situações:

* Quando o comprador quer garantir a entrega de determinado material ou bem;
* Quando o adquirente encomenda a fabricação de um equipamento e necessita dos documentos emitidos pelo vendedor para fins de obtenção de financiamento;
* Para o pagamento antecipado de qualquer bem a ser adquirido;
* Para a garantia do preço de venda.

Através do Contrato de Parceria são gerados dois Pedidos (**MATA410**), um para geração de cobrança no financeiro e outro apenas para remessa, similar à venda com entrega futura, porém possui vínculo formal entre os pedidos gerados e o contrato de origem.

O campo C6\_CONTRAT é alimentado quando o pedido de venda é oriundo de um contrato de parceria.

**Particularidades importantes para o fluxo:**

1 - TES de Cobrança: Caso haja necessidade de escrituração fiscal para o recebimento antecipado, é fundamental configurar corretamente o TES de Cobrança, com:

Gera Duplicata = S

Atualiza Estoque = N

2 - Como as entregas não possuem data efetiva, os contratos não devem ser considerados pelo MRP.

3 - Condição de pagamento: Se o pedido de venda gerado a partir de um contrato possuir uma condição de pagamento não vinculada ao contrato, os campos  
C6\_PRCVEN, C6\_TES, C6\_CONTRAT e C6\_ITEMCON serão limpos automaticamente.

Essa validação é feita pelo gatilho do campo C5\_CONDPAG.

**Parâmetros**

**MV\_ALTCTR** -> Permitir alterar o preço de contratos de parceria parcialmente atendidos

**MV\_ALTCTR2** -> Para pedidos gerados na Opção Aprovar em Outras Ações:

Com conteúdo 2 o sistema não permite que o Pedido gerado com TES de Cobrança seja alterado ou excluído

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013803782)

**MV\_ALTCTR3** -> Permite ou não a alteração do valor unitário do pedido de venda gerado a partir de Contrato de Parceria:

.F. Não permite alterar o valor do preço unitário no pedido de venda para um valor menor do que estipulado no contrato de parceria, mas se for o valor maior é permitido.  
  
.T. Permite alterar, independente se é o superior ou inferior, o preço estipulado no contrato de parceria.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014198702)

Em ambos os casos é permitida a inclusão de mais itens no Pedido de Vendas.

**MV\_PRCCTR** -> Define se caso exista contrato de parceria, o sistema ira utiliza-lo durante a captação do Pedido de Vendas ou Orçamento.

**MV\_ACRSDUP** -> Especifica se o acréscimo financeiro será considerado independente do TES estar configurado com Gera Duplicata igual a Sim.

**Observação:** O Contrato de Parceria não realiza provisões financeiras no contas a receber, esta finalidade foi desenvolvida para o contrato proveniente do módulo Gestão de contratos. Para maiores informações sobre esse processo entrar em contato com a equipe Protheus Compras (SIGAGCT).

**Saiba mais:**

* [Parcerias (FATA400 - SIGAFAT)](https://tdn.totvs.com/x/NBLAFQ)
* [Qual o procedimento de Venda para Entrega Futura?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019090451-MP-FAT-Venda-para-Entrega-Futura)
