---
content_hash: a7e122da3acaa1ea34f1d0264c87f27bc3be0f914b90f9e2891be6179b947c53
fetched_at: '2026-06-29T00:09:26.118875+00:00'
page_id: '423938266'
product: rm
source: tdn-rm
title: Acerto de Ganho / Perda de 2º Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938266
version: 5
---

Neste módulo o usuário poderá realizar ajustes nos saldos de 2º Valor das contas contábeis. Este ajuste elimina as variações sofridas pelas contas devido as variações ocorridas nas cotações da moeda (Cotação utilizando 4 casas decimais).

O sistema irá calcular o saldo do 1º e do 2º Valor das contas contábeis quebrando por Filial e Centro de Custo até a data informada.

O saldo do 1º valor, que será dividido pelo valor da cotação da 2ª moeda no último dia do mês informado, é comparado ao saldo do 2º valor. Se houver diferença entre estes saldos, o sistema criará lançamentos utilizando a conta informada no campo CONTA DESTINO até que os saldos sejam acertados.

Os lançamentos gerados terão o 1º valor zerado e a diferença lançada no 2º valor. Esta diferença será então debitada ou creditada conforme seu saldo, seguindo o seguinte critério:

Se a diferença for positiva, será debitada a conta da diferença e creditada a Conta de Ganho e Perda informada no campo CONTA DESTINO.

Se a diferença for negativa, será debitada a Conta de Ganho e Perda informada no campo CONTA DESTINO e creditada a conta da diferença.

**Campos a serem preenchidos:**

Data do Acerto  
Informe a data que será utilizada no ajuste. Os saldos serão calculados até esta data, e ajustados pelo valor informado para a moeda nesta data.  
Caso não exista valor cadastrado para a moeda nesta data, o sistema utilizará para o cálculo do ajuste o último valor cadastrado na base de dados imediatamente anterior à data informada.

Conta Destino  
Preencha com conta que será utilizada para gerar os lançamentos de ajuste dos saldos e que irá receber os valores das diferenças encontradas.

Filial a Operar  
Será a filial para qual será feito o ajuste ou deixe em branco para que o sistema faça o ajuste de todas as filiais.

Histórico de Destino  
Informe um Histórico para constar nos lançamentos gerados para o ajuste.

Complemento de Histórico  
Descreva um complemento de histórico caso haja necessidade.

Tabela de Índices  
Indique o índice que você quer utilizar no cálculo do ajuste. Este índice pode ser o utilizado normalmente, como também pode ser qualquer outro índice da sua base de dados desde que esteja com os valores da cotação cadastrados corretamente.  
Caso não exista cotação cadastrada para a moeda no último dia do mês da data informada para o ajuste, o sistema utilizará para o cálculo do ajuste a última cotação da moeda cadastrada na base de dados imediatamente anterior à esta. Por isto é muito importante que você verifique, antes de realizar este ajuste, se sua tabela de índices está completa.

Grupo Contábil de Origem  
Informe os grupos contábeis que sofrerão o ajuste.

Faixa de Contas de Origem  
Indique as faixa de contas contábeis que sofrerão o ajuste.

Filtro Por Lotes  
Informe na tela os lotes desejados. Ao executar o processo, caso existam lotes selecionados, o filtro será aplicado na busca dos lançamentos contábeis. Caso contrário, serão considerados os lançamentos de todos os lotes.

**Exemplo:**

1) Em 31/12/2017 o saldo da conta 1.1.1.1.001 é de:  
1º Valor -  R$ 100.000,00 (D)  
2º Valor -  US$ 50.000 (D)  
Ajustando os saldos desta conta, utilizando o índice de US$ 1.95 cadastrado nesta data teremos:  
R$ 100.000,00 / 1.95 = US$51.282.  
Este ajuste gera uma diferença de US$ 1.282 que será debitada na conta 1.1.1.1.001 e creditada em uma Conta de Ganho e Perda.  
Desta forma o saldo da Conta 1.1.1.1.001 na data 31/12/2017 será:  
R$ 100.000,00 no 1º Valor  
US$ 51.282 no 2º Valor.  
Este ajuste poderá ser feito por Filial e por Centro de Custo.  
   
2) Em 16/01/2018 o saldo da conta 2.1.1.1.019 é de:  
1º Valor - R$ 2.000,00(D)  
2º Valor - R$ 1.500,00(D)  
Ajustando os saldo desta conta, utilizando o índice de US$ 1,6000, cadastrado no último dia deste mês 31/01/2018, teremos:  
R$ 2.000,00 / 1,60 = US$ 1.250,00  
Este ajuste gera uma diferença de US$ 250,00 que será creditada na conta 2.1.1.1.019 e debitada em uma Conta de Ganho e Perda.  
Desta forma o saldo da conta 2.1.1.1.019 na data 16/01/2018 será:  
R$ 2.000,00 - 1º Valor  
US$ 1.250,00 - 2º Valor --- ( 1.500,00 (D) – 250,00 (C) )  
Este ajuste poderá ser feito por Filial e por Centro de custo.
