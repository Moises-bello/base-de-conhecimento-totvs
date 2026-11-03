---
article_id: 20199081147287
category: Financeiro
content_hash: 89aebc4969df15fac2210246787e9e5bd99acd2cb312b35d28eee87e2a62fea7
fetched_at: '2026-06-28T22:38:01.262844+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Compensação PA x NF
  com impostos distintos (Títulos DIC)
type: support-article
updated_at: '2024-01-02T20:19:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20199081147287-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Compensa%C3%A7%C3%A3o-PA-x-NF-com-impostos-distintos-T%C3%ADtulos-DIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20199056685719) Tempo aproximado para leitura: **00****:10:00 min** **Dúvida**Compensação de PA x NF com impostos distintos, qual o comportamento do sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

1 - **Geração e utilização de título do tipo DIC**

A partir do release **12.1.23**, a rotina de Compensação Contas a Pagar (**FINA340**) passa a gerar o novo tipo de título "**DIC"** (**Diferença dos Impostos Compensados**). 

O **DIC** é gerado ao realizar a compensação de um adiantamento (**PA**) com uma nota, cujas retenções de impostos sejam diferentes das aplicadas no pagamento do adiantamento. Sua finalidade é representar, no sistema, a diferença de valores referentes aos impostos que não foram retidos no adiantamento, mas foram retidos na nota.

Quando realizada a **baixa do** **DIC,** é gerado um movimento de entrada, indicando recebimento desse valor. Já quando é realizada a **compensação do DIC**, a nota a qual o mesmo fora compensado terá um valor financeiro menor a ser pago ao fornecedor.

As movimentações do **DIC** não geram impostos. Contudo, seu valor compensado será considerado para composição da base de cálculo dos impostos para as baixas e/ou compensações subsequentes da nota que fora compensada com o **DIC** em questão.

**Exemplo de geração do DIC:**  
O cliente faz um pagamento adiantado (**PA**) de **R$** **10.000,00** sem retenção de impostos.

O fornecedor emite a nota (**NF**) sobre o valor dos serviços prestados no valor **R$ 20.000,00** com retenção de impostos (**Pis/Cofins/Csll**) de **4,65%** (**R$ 930,00**).

Valor que será considerado na compensação: **R$ 10.000,00.**

Valor de impostos devido a União (Governo):**R$ 465,00**.

Como não houve retenção de impostos no pagamento desse adiantamento e haverá retenção na nota, ao realizar a compensação entre esses títulos será gerado um **DIC**referente ao valor dos impostos retidos na nota (**R$ 465,00**). Nesse caso, o saldo da nota ficará **R$ 10.000,00** e o saldo do adiantamento será **zerado**.

Demais regras de geração e utilização do DIC:

* O **DIC** somente será gerado se o saldo líquido da nota for maior ou igual ao saldo do adiantamento;
* Para manter a integridade dos impostos devidos, não é possível compensar um **DIC** com um título que possua retenção de imposto na baixa, caso essa compensação fosse zerar o saldo da nota;
* Não é possível selecionar títulos do tipo **DIC** simultaneamente com **PA** e/ou **NDF** em um mesmo processo de compensação;
* Ao tentar cancelar uma compensação com um **DIC**, caso a nota tenha impostos na baixa e tenha baixas posteriores a compensação em questão, será exibida uma mensagem para o usuário, indicando que o valor do **DIC** já foi utilizado na composição da base de imposto de outra baixa e os valores de impostos não serão recalculados. O usuário terá a opção de seguir ou não com esse cancelamento;
* Não é possível cancelar um processo de compensação, caso essa compensação tenha gerado um **DIC** e o mesmo já tenha sido utilizado em outro processo de compensação. Nesse caso, deve-se primeiro cancelar a compensação com o **DIC**.

**Saiba Mais: [Título tipo DIC](http://tdn.totvs.com/pages/releaseview.action?pageId=354465728)**
