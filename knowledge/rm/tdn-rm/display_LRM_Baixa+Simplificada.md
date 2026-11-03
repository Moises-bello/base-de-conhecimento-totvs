---
content_hash: 656ad898475f877fb9c1a8c7ed1172d5587bc3944adb1b77633c835d4c7f839c
fetched_at: '2026-06-29T00:09:17.776395+00:00'
page_id: '421388644'
product: rm
source: tdn-rm
title: Baixa Simplificada
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+Simplificada
version: 18
---

Processo rápido, dinâmico e simplificado de baixar/quitar um ou vários Lançamentos de uma só vez. Neste modelo só é possível selecionar um meio de pagamento(exceto cheque) e será necessário informar qual o tipo de agrupamento de extrato escolhido, que poderá ser: 

**Um extrato para cada Lançamento:**  

Na baixa de vários Lançamentos, será gerado um registro no extrato de caixa para Lançamento baixado.  

Campo Número do documento do extrato;

* Preenchido:

         Campo histórico ( utilizando a variável [NUM]) no extrato: Assume o valor do número do documento de cada lançamento origem.

         Campo número do documento no extrato: Assume o valor digitado na tela.

* Não Preenchido:

         Campo histórico ( utilizando a variável [NUM]) no extrato: Assume o valor do número do documento de cada lançamento origem.

         Campo número do documento no extrato: Assume o valor do número do documento de cada lançamento origem.

**Um extrato para todos os lançamentos:**

Será gerado um registro no extrato com o valor total correspondente à soma de todos os valores líquidos dos lançamentos relacionados ao meio de pagamento selecionado.   Ativando a opção "Contabilizar posteriormente" a contabilização poderá ser realizada em outro momento.  

Campo Número do documento do extrato;

* Preenchido:

         Campo histórico  ( utilizando a variável [NUM]) no extrato: Assume o valor digitado na tela.

         Campo número do documento no extrato: Assume o valor digitado na tela.

* Não Preenchido:

         Campo histórico (utilizando a variável [NUM]) no extrato) : Assume o valor do primeiro lançamento origem.

         Campo número do documento no extrato: Assume o valor do primeiro lançamento origem.

**Obs..:**

Ao marcar o parâmetro: "Gerar um extrato para todos os lançamentos", o campo "Número do documento do extrato" será preenchido automaticamente com o valor do número do documento do primeiro lançamento origem, podendo ser editado pelo usuário.

**Resultado:**

* No anexo de cada lançamento(Baixas do Lançamento) foi gravado o registro correspondente à baixa.
* O saldo da conta caixa foi atualizado.
* A contabilização foi realizada de acordo com o meio de pagamento utilizado na baixa e foi gerada diretamente no Gestão Contábil no lote definido através Assistente de implantação de processos (etapa Contabilização).

**Contabilização**

Quando realizada baixa de lançamentos contábeis é carregada  tela para que seja contabilizado os itens de baixa de acordo com as seguintes opções:

Evento contábil padrão para todos itens de baixa  
Aqui será informado um evento padrão que será usado para contabilizar todos os itens de baixa carregados na tela, substituindo o evento dos lançamentos carregados. Para que a contabilização ocorra para o evento informado é preciso usar a opção "Aplicar Evento".

Aplicar Evento  
Ao informar evento contábil no campo anterior é preciso clicar nessa opção para que a contabilização seja executada para todos os lançamentos selecionados.

Carregar contabilização  
Ao clicar nesta opção o sistema carrega e valida o evento contábil de cada item para a tela. Ao avançar a contabilização ocorrerá de acordo com o evento carregado.

Editar  
Essa opção poderá ser usada caso tenha necessidade de alterar manualmente a contabilização de baixa.

Independentemente da moeda da conta/caixa, a contabilização é sempre realizada na [Moeda Corrente parametrizada no TOTVS Gestão Contábil](https://tdn.totvs.com/display/LRM/Moedas), realizando a conversão conforme a cotação.
