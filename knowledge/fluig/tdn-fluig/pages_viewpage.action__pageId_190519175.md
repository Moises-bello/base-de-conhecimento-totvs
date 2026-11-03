---
content_hash: c4cd769b0780968300c4c9e131561a1369c02af6aeafd98766bbe9449ebd19c1
fetched_at: '2026-06-28T21:35:19.103878+00:00'
page_id: '190519175'
product: fluig
source: tdn-fluig
title: DES - Utilização do hAPI.getCardValue() com campos tipo multipla escolha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190519175
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Utilização do hAPI.getCardValue() com campos tipo múltipla escolha.

# Causa

Campos do tipo múltipla escolha tem um tratamento diferente dos campos simples.

Um campo do tipo 'checkbox', 'radio' ou um 'select' (combo-box) por exemplo, no banco de dados fica armazenado o valor da propriedade 'value' no campo, mas caso não houver esta propriedade, os campos 'radio' e 'checkbox' ficam com o valor "on" no banco de dados, enquanto o 'select' fica com o valor da descrição de uma das opções.

Assim como um campo simples, caso o mesmo não for preenchido ou não for selecionado uma opção em um campo, o retorno no hAPI.getCardValue() será vazio.

# Solução

Uma boa prática no desenvolvimento de formulários é sempre utilizar a propriedade 'value'!

Isto faz com que seja armazenado exatamente o valor desejado, sendo possível assim **tratar os dados** posteriormente **em workflows e relatórios** por exemplo.   
Abaixo tem um exemplo especificamente da propriedade 'value' em alguns campos para melhor entendimento:

xml
 
Cartão:
 
 
Cartão:
Visa
Master
Elo
 ]]>

Para recuperar as informações nos wofklows, basta utilizar o hAPI.getCardValue("campoNameNoHTML"). Quando for consultado o valor do campo "Cartão" como no exemplo acima, o retorno será o do 'value', por exemplo: "visa" ou "master". No caso do campo 'ckAtendimentoFaturado' ocorre a mesma coisa, exemplo:

js

# Observações

Apesar de não ser utilizado aqui, pois é somente um exemplo, é **muito importante seguir a [Style Guide](https://style.fluig.com/) para o desenvolvimento de formulários!**

Para mais detalhes sobre desenvolvimentos sobre a plataforma, verifique as documentações de [formulários](http://tdn.totvs.com/x/U4l8B) e [processos](http://tdn.totvs.com/x/widbB).
