---
content_hash: 9e6712ad79e85711c3e9a5c5908a81668bb0cb65cec2799bf51a87d3c322af9b
fetched_at: '2026-06-29T00:10:01.934572+00:00'
page_id: '452718801'
product: rm
source: tdn-rm
title: Código de Cálculo 13 - Pensão Alimentícia Judicial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718801
version: 9
---

Desconto do tipo valor e Dedutível IRRF. Este evento permite a utilização de fórmulas para o cálculo.

**Atenção:**

Quando o funcionário tiver desconto de pensão alimentícia judicial, deverá verificar a petição da pensão enviada pelo juiz, e se necessário deverá criar os eventos de pensão abaixo:

* Pensão Alimentícia Judicial: evento do tipo desconto com código de cálculo 13 e dedutível de IRRF. Este evento deverá ser informado no código fixo do funcionário para que seja lançado no movimento de folha ou rescisão.
* Pensão Alimentícia sobre Férias: evento do tipo desconto com código de cálculo 113 e Dedutível IRRF Férias. Este evento deverá ser informado em: Eventos Adicionais Global ou Adicionais de Férias, para que seja descontado no recibo de férias. Para desconto na rescisão deverá cadastrar como código fixo ou marcar a opção "Lança eventos adicionais de férias na rescisão" no Parametrizador.
* Pensão Alimentícia sobre 13º Salário: evento do tipo desconto com código de cálculo 120 e Dedutível IRRF 13º. Este evento deverá ser informado no código fixo do funcionário para que seja descontado no lançamento do 13º Salário ou rescisão.
* Pensão Alimentícia sobre Participação nos Lucros: evento do tipo desconto com código de cálculo 121 e dedutível de IRRF, sendo que nesse caso se estiver marcado como dedutível IRRF e possui cc 121, é considerado no IRRF PL cc 127 - IRRF Participação nos Lucros. Este evento deverá ser informado no código fixo do funcionário para que seja descontado no movimento de folha ou rescisão.
* A prioridade do evento é informada automaticamente pelo sistema, podendo ser alterada somente quando é utilizada fórmula de valor.

  IMPORTANTE:

  Quando acrescenta fórmula em códigos de cálculo relacionados a Pensão Alimentícia apresenta a mensagem abaixo, nesse caso deve também acrescentar o movimento no anexo do dependente para que cálculos de diferenças futuras considerem esse valor para inserir novo movimento no anexo do dependente.

  *Atenção!*

  *O lugar correto para informar a fórmula para o cálculo da pensão alimentícia é dentro do cadastro do dependente de pensão.*

  *Para assim, o sistema poder identificar que o valor calculado é deste pensionista, e inserir o registro na respectiva movimentação.*

  *Caso seja utilizada fórmula no evento, não será possível atualizar automaticamente o movimento de pensão.*

  ---

  Códigos de Cálculo
