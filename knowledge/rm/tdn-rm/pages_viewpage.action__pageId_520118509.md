---
content_hash: d4eb61c0c8c7fa9c22f53ff3e008434313c8ddd394f0132cb442b35f2568816c
fetched_at: '2026-06-29T00:10:30.914380+00:00'
page_id: '520118509'
product: rm
source: tdn-rm
title: Taxas de cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520118509
version: 15
---

Atenção

Este cadastro deverá ser utilizado somente para quem tem o modelo Rede-CyberSource habilitado.

Este cadastro permite o controle das taxas cobradas pelas adquirentes nas vendas por cartão de crédito ou débito. Após o processo de conciliação dos recebimentos das vendas realizadas com cartão, será possível verificar se as taxas cobradas estão de acordo com as taxas contratadas.

O controle das taxas será realizado da seguinte forma:

Quando a confirmação do pagamento do cartão for efetuada, a taxa vigente será armazenada nas informações da transação. No processo de conciliação dos recebimentos das vendas realizadas com cartão, será verificado se esta taxa está de acordo com a taxa contratada.

Caso não haja taxa armazenada nas informações da transação, no momento da conciliação, será buscada a primeira taxa inativa com data de vigência até a data do pagamento. Se não houver taxas inativas até a data do pagamento, será utilizada a taxa vigente.

Obs: As taxas das adquirentes (Cielo, CyberSource e GetNet) para pagamento parcelado serão calculadas utilizando o  valor total da transação fazendo com que o arredondamento fique consistente conforme operadoras.

**Identificação**

Nesta aba são apresentadas informações que identificam a taxa.

Filial

Informe a filial que contratou a solução de venda com cartão. Não é necessário informar caso o contrato seja feito por coligada.

Inativo

Identifica se a taxa está inativa. Ao marcar a taxa como inativa, o campo 'Vigente Até' será habilitado.

Adquirente

Informe a adquirente referente à taxa contratada.

Tipo de venda

Informe o tipo de venda referente à taxa contratada.

Bandeira

Informe a bandeira referente à taxa contratada.

Taxa

Informe o valor da taxa (%) contratada junto à adquirente.

Faixa de parcelas

É possível informar uma taxa para o tipo de venda *Crédito parcelado*, por faixa de números de parcelas.

Vigente Até

Apresentada somente quando a taxa está inativa. Deve ser preenchida com o último dia de vigência da taxa, seguindo os seguintes passos:

Passo 01:

1. Acesse a tela em Movimentações Bancárias > Cartão de Crédito/Débito > Mais > Taxa de Cartão
2. Acesse a taxa cadastrada e que estava anteriormente com a vigência ativa, ou seja, **a taxa antiga** que estava em uso.
3. Selecione o campo "Inativo", que irá desbloquear o campo "Vigente até".
4. Preencha o campo "Vigente até" com a data do último dia de vigência dessa taxa.
5. Clique em Salvar.

Exemplo:

Passo 02:

1. Crie uma nova taxa, com as mesmas informações de adquirente, tipo de venda e bandeira da taxa anterior, porém, agora informe a **taxa atual vigente** .Não marque a opção inativo para a segunda taxa.
2. Clique em Salvar.

Passo 03:

1. Execute o Passo 01 e Passo 02, nessa ordem, para todos os tipos de venda e bandeiras que estão inclusos no cenário de alteração de taxa da adquirente em questão.
