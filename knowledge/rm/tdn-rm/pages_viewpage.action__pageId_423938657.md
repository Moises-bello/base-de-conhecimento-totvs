---
content_hash: 70e30ded4f32ba90619002a197324ba15f3e6d8619cadf9fe7fa25c8af6151a5
fetched_at: '2026-06-29T00:09:28.088575+00:00'
page_id: '423938657'
product: rm
source: tdn-rm
title: Estrutura - Distribuição Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938657
version: 6
---

A alteração da distribuição gerencial pode ser feita indicando-se *manualmente* as contas de origem, de destino, percentuais para a nova distribuição ou utilizando-se, conforme descreveremos a seguir, uma *estrutura* previamente cadastrada contendo informações pré-definidas de contas e percentuais para o novo rateio.  
   
A Estrutura de lançamento gerencial possibilitará ao usuário definir moldes de distribuição gerencial, para ser utilizado no processo de Alteração da Distribuição Gerencial. Cada molde conterá informações pré-definidas de contas e percentuais para o novo rateio.   
   
A alteração da distribuição gerencial pode ser realizada de diversas formas e para algumas delas você poderá cadastrar uma estrutura correspondente. Conforme a parametrização utilizada, uma estrutura pode ter mais de um molde de rateio, cada um deles com modelos de rateios distintos para diversas contas contábeis. Ao utilizar uma estrutura o novo rateio será feito conforme as informações pré-definidas no seu molde.  
Para incluir uma estrutura, informe um código e uma descrição.  
Se o parâmetro "Usar Conta Contábil" estiver marcado, deverá ser informada no molde uma conta contábil e a forma de distribuição que será feita para esta conta.

**Exemplo:**

Conta Contábil: 1.1.1.1.001  
Distribuição gerencial:  
5.01 – 50%   
5.02 – 50%  
Desta forma sempre que esta estrutura for informada no processo, os lançamentos que possuírem a conta 1.1.1.1.001, a débito ou a crédito, terão a sua distribuição conforme informado nesta estrutura.

**Observação:**

Não poderá ser informada uma mesma conta contábil que foi utilizada em outros moldes cadastrados nesta mesma estrutura. A distribuição gerencial pode ser repetida.  
Se o parâmetro "Usar Conta Contábil" estiver desabilitado, será permitido apenas o cadastro de um molde com a distribuição gerencial desejada. A nova distribuição informada neste molde será aplicada para todos os lançamentos conforme filtros selecionados o momento da execução.

**Observações:**

* Uma vez salva a estrutura com este parâmetro habilitado não é possível desabilitá-lo e vice-versa.
* A distribuição gerencial informada no molde deve fechar em 100%. Caso esteja diferente de 100%, o molde não será salvo.
