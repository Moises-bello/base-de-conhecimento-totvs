---
content_hash: 84481c5122530862b984090a122949b39bfcf4d1c280a01abb852b552e1861a1
fetched_at: '2026-06-29T00:09:21.029436+00:00'
page_id: '422545770'
product: rm
source: tdn-rm
title: Controle da Compensação Tributos Federais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545770
version: 5
---

Em síntese, o processo de utilização do Controle de Compensações será o seguinte:

1. Reconhecer o Direito a Crédito decorrente de pagamento indevido ou a maior;
2. Registrar o crédito identificado, no cadastro de Compensações, associando ao DARF que gerou o crédito;
3. Efetuar encerramento dos Períodos. Durante a operação de Encerramento, caso exista Crédito cadastrado a Compensar, o Sistema irá avisar da existência destes Créditos;
4. Gerar as Guias DARF normalmente. Estas Guias serão geradas com o valor total que "deveria ser pago". As Guias geradas serão utilizadas posteriormente como Débitos a serem Compensados na DCOMP;
5. Criar a DCOMP no Programa da RFB, vinculando o Crédito resultante do Pagamento a maior e os Débitos que serão compensados, com base no resultado da apuração dos tributos;
6. Associar os Débitos (Guias geradas) a serem compensados;
7. Após a inclusão das Guias de Débitos o sistema irá efetuar os mesmos cálculos executados pelo programa da RFB, através do processo de cálculo.

***Observação***: O cálculo somente será realizado se o campo Data de Transferência estiver informado. Este campo é utilizado para realizar o cálculo da Taxa SELIC acumulada. O Processo de Cálculo poderá ser realizado diversas vezes, desde que o Processo de Finalização não tenha sido realizado. Após a Finalização do Processo o cálculo não poderá ser realizado.

1. Depois de concluído o processo de Atualização do Registro de Compensação, o sistema irá registrar o Valor Compensado nas Guias utilizadas como Débito;
2. Para finalizar o processo de compensação, deverá ser selecionada a opção de Finalizar o Processo de Compensação.
3. Esse procedimento, se houver saldo remanescente, irá gerar um novo cadastro de compensação                contendo os mesmos dados da compensação original, inclusive, a guia original do crédito, para que o usuário possa utilizá-lo para novas compensações. Esse processo somente será executado se o Numero do Pedido estiver preenchido.
4. Gerar DCTF.
