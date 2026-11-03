---
article_id: 1500007522941
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b3a7387cd5fcdd07a4d0567910de8d4147f09a3718a8a8b6b65394d25b37039b
fetched_at: '2026-06-28T22:38:41.259599+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Valor unitário e Impostos no Faturamento
type: support-article
updated_at: '2021-04-28T22:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007522941-MP-FAT-Valor-unit%C3%A1rio-e-Impostos-no-Faturamento
---

**Dúvida**Composição de Impostos e Valor Unitário no faturamento.  
  
**Ambiente**Microsiga Protheus – a partir da versão 12.1.27 .

**Solução** **ICMS**O valor unitário de um item já é composto pelo ICMS + Lucro;  
  
**IPI**  
Para o IPI será necessário que o preço de venda já contemple o ICMS, pois a base do IPI é o preço final de venda do produto x alíquota = valor do IPI, onde o mesmo é agregado no total da NF;  
  
**Regra Comercial**  
  
Há empresas que solicitam que o valor do item do Pedido seja o mesmo que o valor da NF de saída. Esta operação não é possível quando há imposto que agrega no total, uma vez que o fato gerador do imposto é a emissão da NF.

Um imposto pode mudar de alíquota entre a emissão do Pedido de Vendas e a emissão da NF devido a  legislação, portanto, até a emissão da NF o valor é incerto

É possível visualizar o valor total com os impostos na Planilha Financeira do Pedido, onde o sistema realiza uma simulação em tela (não há gravação dos valores apresentados por se tratar de uma projeção somente).

**Valor unitário deduzido de impostos para agregar somente ao final**

A empresa pode incluir o valor unitário, deduzido dos impostos, na tabela de preços (entendendo que ao gerar a NF o valor imposto será somado).

**Importante :** Dúvidas sobre o cálculo e base de impostos a orientação será realizada pela equipe de suporte TOTVS Fiscal  
  
Situações diferentes da apresentada acima a empresa poderá solicitar uma melhoria pela Central Colaborativa ou acionar o gerente de Contas TOTVS:   
<https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001704573-TOTVS-Backoffice-Linha-Protheus-Faturamento-Faturamento>
