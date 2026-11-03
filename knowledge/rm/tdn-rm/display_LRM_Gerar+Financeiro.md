---
content_hash: 39f514ca54080483ab092144ba11ecd7ef6c580a6354775c1d401c395317351f
fetched_at: '2026-06-29T00:09:25.315256+00:00'
page_id: '423938119'
product: rm
source: tdn-rm
title: Gerar Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+Financeiro
version: 3
---

Este processo somente estará disponível em tipos de movimentos que forem parametrizados para não faturarem na inclusão, ou seja, quando da inclusão do movimento, o sistema não gera os lançamentos financeiros relacionados a este movimento.  
Este processo pode ser utilizado quando o documento fiscal da mercadoria é recebido pela Empresa, porém os boletos ou as Ordens de Pagamento são recebidos em um outro momento.  
Desta forma, evita-se a geração incorreta dos dados financeiros, aguardando uma confirmação física dos dados de pagamentos.  
Para a execução deste processo, podem ser selecionados um ou mais movimentos.  
Quando selecionado mais de um movimento, é possível realizar o faturamento Agrupado, utilizando a opção "Agrupar Todos". Utilizando esta opção, será gerado um único lançamento financeiro, para todos os movimentos selecionados. A opção "Agrupar Todos", não esta disponível para tipos de movimento parametrizados para "Utilizar Meio de Pagamento" e/ou movimentos que já possuam meio de pagamento.   
Ao final do processo, o sistema mostra um log da execução do processo, apresentando informações caso a rotina não tenha sido feita corretamente para os movimentos selecionados.  
Após a finalização do processo, os movimentos selecionados que tiveram seus dados financeiros gerados de forma correta, passarão para o status "A Pagar" (movimentos de compras) ou 'Faturado' (movimentos de vendas).  
Caso os dados financeiros dos movimentos estejam incorretos, basta selecioná-lo e executar a rotina de Reabrir Financeiro, afim de desfazer o processo executado.
