---
content_hash: a58cd8bc83b489bc0c63e2e72a474b03064a0085d6b2a1e75d119308bce67dd4
fetched_at: '2026-06-29T00:09:18.156207+00:00'
page_id: '421388692'
product: rm
source: tdn-rm
title: Baixa Completa
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+Completa
version: 9
---

Processo dinâmico de baixar um ou vários lançamentos com a grande vantagem de poder utilizar um ou vários meios de pagamento para o processo de baixa total ou parcial.   
Opções para a Baixa Completa:

Um lançamento com vários meios de pagamento

Ao baixar o Lançamento você pode utilizar vários meios de pagamento. Acessando Anexos/Baixas do Lançamento você verá que foram gravados tantos itens de baixa(FLANBAIXA) quantos forem os Meios de Pagamento utilizados. . No extrato de caixa (dependendo da opção indicada para gerar um extrato para cada Lançamento ou gerar um extrato para todos) serão gravados tantos registros quantos forem os Meios de Pagamento utilizados na Baixa. . A Contabilização on-line será realizada de acordo com o Item de Baixa e será gravada no lote definido através do Assistente de Implantação de Processos (etapa Contabilização).

Um meio de pagamento para vários lançamentos

Você poderá selecionar vários Lançamentos e indicar apenas um meio de pagamento. . No extrato de caixa (dependendo da opção indicada para gerar um extrato para cada Lançamento ou gerar um extrato para todos) será gravado o respectivo registros de acordo com o Meios de Pagamento utilizado na Baixa. . A Contabilização on-line será realizada de acordo com o Item de Baixa e será gravada no lote definido através do Assistente de Implantação de Processos (etapa Contabilização).

Vários lançamentos com vários meios de pagamento

Você poderá selecionar vários Lançamentos e baixá-los através de vários meios de pagamento. . Para cada lançamento baixado serão gerados respectivamente, "n" registros na FLANBAIXA(Anexos/Baixas do Lançamento) de acordo com os meios de pagamento utilizados. . Serão gerados "n" registros no extrato correspondente aos meios de pagamento utilizados na baixa. . A contabilização será realizada de acordo com o meio de pagamento utilizado na baixa e será gerada diretamente no Gestão Contábil no lote definido através Assistente de implantação de processos (etapa Contabilização).

**Observação**

Ao baixar mais de um lançamentos serão apresentadas duas opções para que seja indicada a forma de se ratear o valor baixado sendo:

Proporcional ao valor líquido

O valor baixado de cada lançamento selecionado será proporcional ao valor ora informado para baixa.

Na ordem dos Lançamentos

O valor baixado será tratado de acordo com a ordem dos Lançamentos selecionados.  
   
  
   
Cálculo:  
Lançamento no valor de 1000,00:

1000,00 + 500,00 = 1500,00

Regra de 3

1500,00 = 100%

1000,00 = X %

300,00 \* 100/1500 = 20%

1000,00 \* 20% = 200,00............. Dinheiro

1000,00 \* 100/1500 = 66,67%

1000,00 \* 66,67% = 666,67......... Cheque

200,00 \* 100/1500 = 13,33%

1000,00 \* 13,33% = 133,33.........Cheque pré-datado  
   
Lançamento no valor de 500,00:

1000,00 + 500,00 = 1500,00

Regra de 3

1500,00 = 100%

500,00 = X %

300,00 \* 100/1500 = 20%

500,00 \* 20% =  100,00............... Dinheiro

1000,00 \* 100/1500 = 66,67%

500,00 \* 66,67% = 333,33..........Cheque

200,00 \* 100/1500 = 13,33%

500,00 \* 13,33% = 66,67.............Cheque pré-datado

**Contabilização**

Quando realizada baixa de lançamentos contábeis é carregada tela para que seja contabilizado os itens de baixa de acordo com as seguintes opções:

Evento contábil padrão para todos itens de baixa  
Aqui será informado um evento padrão que será usado para contabilizar todos os itens de baixa carregados na tela, substituindo o evento dos lançamentos carregados. Para que a contabilização ocorra para o evento informado é preciso usar a opção "Aplicar Evento".

Aplicar Evento  
Ao informar evento contábil no campo anterior é preciso clicar nessa opção para que a contabilização seja executada para todos os lançamentos selecionados.

Carregar contabilização  
Ao clicar nesta opção o sistema carrega e valida o evento contábil de cada item para a tela. Ao avançar a contabilização ocorrerá de acordo com o evento carregado.

Editar  
Essa opção poderá ser usada caso tenha necessidade de alterar manualmente a contabilização de baixa.

Independentemente da moeda da conta/caixa, a contabilização é sempre realizada na [Moeda Corrente parametrizada no TOTVS Gestão Contábil](https://tdn.totvs.com/display/LRM/Moedas), realizando a conversão conforme a cotação.
