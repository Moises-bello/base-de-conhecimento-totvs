---
article_id: 360000091867
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: d1149ffaa4034db6c130514424de101ffb18b65fd6bd706b7bb8fc5825e5f58a
fetched_at: '2026-06-28T22:39:44.400387+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pagamento antecipado
  para a purchase order
type: support-article
updated_at: '2022-07-20T15:37:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000091867-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pagamento-antecipado-para-a-purchase-order
---

**Dúvida**Como incluir um pagamento antecipado para a Purchase Order, no módulo de importação?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução****PAGAMENTO ANTECIPADO - IMPORTAÇÃO**

No sistema Easy Import Control o controle de câmbio antecipado foi desenvolvido de forma a oferecer ao usuário um controle flexível e seguro de utilização do saldo credor (antecipado).

Todo pagamento antecipado de câmbio, tem como referência uma Proforma Invoice, ou seja, não importa quantos embarques sejam efetuados para atender um mesmo PO, o fato é que o pagamento antecipado está vinculado à uma única Proforma.

**Pré-requisitos**

1. Registrar o PO com uma condição de pagamento antecipado;
2. Informar no PO (capa) o Nº da Proforma Invoice .

Após registrar o Purchase Order (PO), deve-se registrar o pagamento antecipado e, para tanto, deve-se executar os seguintes procedimentos:

1. Acionar o menu Atualizações-> Financeiro-> Controle de Câmbio.
2. Acionar o Incluir.
3. No campo Tipo” selecionar a opção Adiant. PO
4. No campo Processo/PO, deve-se informar o número do PO que possui câmbio antecipado
5. Acionar o Salvar.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000145608/mceclip5.png)

Para fechar o câmbio e gerar o título no SIGAFIN, deve-se proceder da mesma maneira de um cambio comum, ou seja, selecionar a parcela a ser fechada e preencher os campos: No. Contrato, Data Contrat., Liquidação e Taxa Cambio. Repare que ao editar a parcela, o campo Invoice é automaticamente preenchido com o número da Proforma Invoice informada no PO.

**Obs.**: Dessa forma, tem-se o registro do pagamento antecipado, que está baseado no PO.

**Compensação:**

Após o registro do primeiro embarque, deve-se registrar o mesmo no controle de câmbio para o devido controle das demais parcelas. Mesmo que o processo possua uma única parcela de pagamento, ou seja, trate-se de um pagamento 100% antecipado, deve-se lançar o processo de Embarque/Desembaraço no Controle de Câmbio, pois é necessário vincular o pagamento antecipado à invoice utilizada no embarque.  
Ao preencher os dados da Invoice nas rotinas de Embarque/Desembaraço, o Câmbio tipo **Desembaraco** é incluso automaticamente na rotina de Controle Câmbio.

Posicione sobre o Câmbio do tipo **Desembaraco** e em outras ações\Alterar;  
Será apresentada uma tela semelhante a tela a seguir, apresentando as parcelas de acordo com a condição de pagamento da Invoice informada no Embarque/Desembaraço.

A tela abaixo refere-se a um Processo cuja condição de pagamento é a seguinte:

50% antecipado  
20% 30 dias após o embarque  
30% 60 dias após o embarque

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000141927/mceclip6.png)

Note que apesar do pagamento antecipado já ter sido registrado com base na Proforma Invoice, o sistema apresenta a parcela relacionada ao pagamento antecipado respectiva ao embarque que está sendo registrado.  
Isto ocorre para que se possa relacionar o pagamento antecipado com o embarque efetivo, ou seja, para que se possa confirmar a utilização da remessa de dinheiro ao exterior efetuada.  
Os procedimentos a seguir, além de permitir vincular o saldo adiantado ao fornecedor à Invoice utilizada no embarque, também permite abater este saldo das demais parcelas do câmbio.  
Para tanto, deve-se proceder da seguinte forma:  
Após o lançamento do processo de Embarque/Desembaraço, no menu Controle Câmbio em:

1. Atualizações\Financeiro\Controle posicionar no cambio que deseja efetuar a manutenção;
2. Acione Alterar, posicione na parcela que ira associar o Pagamento Antecipado;
3. Em Outras Ações deve-se acionar o botão **Pagamentos Antecipados** para se visualizar o pagamento antecipado relacionado a este processo;
4. Ao acionar o botão será apresentada a seguintes telas, selecione **01- Adiantamento por PO**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000141947/mceclip7.png)
5. O sistema verifica se existe pagamento antecipado relacionado ao PO informado no embarque e apresenta o valor liquidado.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000142067/mceclip0.png)
6. Deve-se dar um duplo clique na parcela para que a mesma seja lançada neste controle de câmbio e possa ser utilizada na distribuição do adiantamento para as demais parcelas.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360000145788/mceclip1.png)

Desta forma, tem-se 4 parcelas relacionadas ao embarque, inclusive a primeira parcela correspondente ao 50% adiantado do nosso exemplo.
