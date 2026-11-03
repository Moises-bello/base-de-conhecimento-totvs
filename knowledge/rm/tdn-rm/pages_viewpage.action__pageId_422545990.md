---
content_hash: cc2d040c9b43b03318f2f3d3ae8762fa1163c3ec71921e2617c44776322ab430
fetched_at: '2026-06-29T00:09:22.528441+00:00'
page_id: '422545990'
product: rm
source: tdn-rm
title: Finalização do Cálculo da Compensação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545990
version: 3
---

O processo de finalização impede que novas guias sejam adicionadas ou removidas.  
Para finalizar o processo de Compensação, deverá ser informado obrigatoriamente, o Numero do Pedido gerado pela SRF através de Declaração de Compensação feita na PER/DCOMP. Esse processo criará automaticamente, se houver um saldo remanescente a ser compensado, um registro no cadastro de compensação com todos os dados da guia original e o valor do crédito restante, para que possa ser utilizado em novas compensações.   
A atualização dos lançamentos financeiros ocorrerá após a finalização da compensação.  
   
Caso o valor do débito não seja totalmente compensado, será gerado um lançamento financeiro com o valor residual do débito, ou seja, será possível compensar parcialmente uma guia de débito.  O processo de cálculo será o mesmo, mas quando essa situação ocorrer e a guia já tiver lançamento financeiro, então será atualizado o campo "Desconto" do mesmo, o que fará com que ao baixar, o valor compensado seja descontado. Se a integração com o financeiro ainda não ocorreu, ao realizar esse processo o valor gerado será "Valor da guia" – "Valor compensado".   
   
Antes de finalizar o processo de compensação, a guia de débito poderá ser excluída, desde que desvincule essa guia do cadastro.   
Ao desvincular os débitos e salvar o cadastro, o sistema irá apagar os valores gravados anteriormente. Desta forma, o usuário poderá recalcular a compensação.  
Após selecionar a guia a ser compensada não será permitido, alterar, excluir ou baixar o lançamento financeiro correspondente.  
   
Para as guias selecionadas para compensação, cuja compensação foi utilizada totalmente e as guias estiverem integradas ao Sistema de Gestão Financeira, deverá ser realizada a Baixa por Destrato. Esse procedimento será realizado manualmente após ser finalizada a compensação.   
Caso o valor do débito seja totalmente compensado, o sistema não integrará a guia com o TOTVS Gestão Financeira.  
***Observação***: Os juros não incidirão na compensação de créditos do PIS e COFINS, pois estes são contribuições e não impostos. É compensado somente o valor do crédito existente.

# Saldo Negativo

Desde que:

1) Existe Lançamento Fiscal com Tributo Federal (Ex.: IRRFPJ);  
2) O período de apuração do Tributo Federal (Ex.: IRRFPJ) foi encerrado;  
3) A Guia do Período foi gerada;  
4) Foi cadastrado/parametrizado a compensação de tributo federal para o IRRFPJ com o tipo: Saldo Negativo IRPJ ou CSLL;  
5) Foi associada a guia do IRRFPJ gerada no encerramento do período no cadastro de compensação de tributo federal (anexo guias de débito para compensação)

Ao executar o cálculo das compensações de tributos federais, os valores calculados (aba Valores) devem estar corretos e a guia DARF do período deve compensar o valor correspondente.
