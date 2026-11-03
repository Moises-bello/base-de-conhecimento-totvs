---
content_hash: b6b163b67f48d36ddfce73ddf4b6dd43906987bfb6c8d4cc31fdd4d0d986bbd5
fetched_at: '2026-06-29T00:09:17.683734+00:00'
page_id: '421388617'
product: rm
source: tdn-rm
title: Incluir Extrato Correspondente
type: documentation
url: https://tdn.totvs.com/display/LRM/Incluir+Extrato+Correspondente
version: 9
---

Com este processo é possível realizar a inclusão de extrato de caixa correspondente aos registros do arquivo bancário.

Exemplo

Ao realizar a conciliação você identifica que existe um registro bancário que não possui um Extrato de Caixa correspondente. Para que a conciliação seja finalizada neste momento você pode incluir um Extrato de Caixa com os mesmos dados do registro bancário.

Passo a Passo

* Selecione o registro bancário;
* Inicie o processo "Incluir Extrato Correspondente".
* É apresentada a janela de edição de Extrato de Caixa já contendo informações do registro bancário.
  + Importante: Caso o número do documento do extrato bancário selecionado possua mais de 20 posições, na etapa anterior o sistema apresentará uma mensagem conforme o modelo abaixo:

* + E quando for feita a inclusão para múltiplos registros utilizando a opção *"Um Extrato para cada registro de reconciliação, informando os dados somente uma vez"* será apresentado a tela conforme o modelo a seguir:

         Devido a estrutura das tabelas relacionadas, o limite do campo do número do documento no extrato de caixa é de 20 caracteres, não sendo possível aumentar este tamanho nos parâmetros do TOTVS Gestão Financeira. Logo, o sistema truncará o número do documento para utilizar até 20 posições. Diante disso, se houver este cenário, é recomendado não utilizar o campo 'Número do documento' na [etapa da conciliação](https://tdn.totvs.com/pages/viewpage.action?pageId=421388551), pois nesse caso haverá divergência entre o número do documento do extrato de caixa correspondente e o número do documento do extrato bancário.

* Informe a Filial e outras informações necessárias.
* Conclua a inclusão do Extrato de Caixa.
* O Extrato de Caixa incluído é apresentado na visão.

**Incluir extrato correspondente selecionando vários registros bancários**

Selecionando vários registros bancários é possível incluir Extrato de Caixa Correspondente utilizando três formas de geração:

Um Extrato para cada registro de reconciliação selecionado

Será apresentada uma janela de edição de Extrato de Caixa para cada registro bancário, podendo ser selecionadas informações diferentes para cada Extrato.

**Observação:**

Caso os registros de Reconciliação selecionados possuam a mesma conta/caixa, o sistema irá carregar os defaults automaticamente.  
As informações abaixo são apresentadas de acordo com o registro bancário:

* Operação
* Conta/Caixa
* Data
* Número Documento
* Valor
* Histórico

As informações abaixo não poderão ser alteradas:

* Conta/Caixa
* Valor

Um Extrato para cada registro de reconciliação, informando os dados somente uma vez

Será apresentada uma única janela de edição de Extrato de Caixa, que será base para todos os Extratos criados.  
O preenchimento desta janela será da seguinte forma e as informações abaixo não poderão ser alteradas e serão preenchidas nos extratos de caixa de acordo com as informações de cada registro bancário.

* Operação
* Conta/Caixa
* Data
* Número Documento
* Valor
* Histórico

As informações abaixo poderão ser alteradas e serão únicas para todos os extratos de caixa incluídos.

* Filial
* Centro de Custo
* Departamento
* Natureza Orçamentária/Financeira
* Evento Contábil
* Tabelas Opcionais

Um Extrato por Conta/Caixa dos registros de reconciliação selecionados

**Atenção:**  
Para utilizar essa forma de geração os registros bancários da mesma Conta/Caixa devem ser da mesma "natureza", ou seja, todos de "saque" ou todos de "depósito".  
Os registros bancários que possuem as categorias "Cheque", "Transferência" e "CPMF", não podem ser selecionados juntos, ou seja, registros bancários que possuem a categoria "cheque", não podem ser selecionados juntos com registros que possuem a categoria "CPMF".  
Será apresentada uma janela de edição de Extrato de Caixa para cada Conta/Caixa de registros bancários selecionados.

As informações abaixo são apresentadas de acordo com os registros bancários:

* Operação
* Conta/Caixa
* Data
* Número Documento
* Valor
* Histórico

As informações abaixo não poderão ser alteradas:

* Conta/Caixa
* Valor

O "Valor" é o total de todos os registros da Conta/Caixa.  
A "Data", o "Número Documento" e o "Histórico" são apresentados de acordo com o registro da última "Data", podendo ser alterados.
