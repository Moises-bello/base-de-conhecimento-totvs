---
content_hash: 5fe6fa75eca82d53984c5fe267bb9f1017d8807cff0e244aa114b897c34eb706
fetched_at: '2026-06-29T00:10:09.295773+00:00'
page_id: '452719620'
product: rm
source: tdn-rm
title: Código de Cálculo 120 - Pensão Alimentícia Sobre 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719620
version: 6
---

Desconto do tipo valor 120 e Dedutível IRRF 13º. Este evento permite a utilização de fórmulas para o cálculo.

**Atenção**

Quando o funcionário tiver desconto de pensão alimentícia judicial, deverá verificar a petição da pensão enviada pelo juiz, e se necessário deverá criar os eventos de pensão abaixo:

* Pensão Alimentícia Judicial: evento do tipo desconto com código de cálculo 13 e dedutível de IRRF. Este evento deverá ser informado no código fixo do funcionário para que seja lançado no movimento de folha ou rescisão.
* Pensão Alimentícia sobre Férias: evento do tipo desconto com código de cálculo 113 e Dedutível IRRF Férias. Este evento deverá ser informado em: Eventos Adicionais Global ou Adicionais de Férias, para que seja descontado no recibo de férias. Para desconto na rescisão deverá cadastrar como código fixo ou marcar a opção "Lança eventos adicionais de férias na rescisão" em Opções | Parâmetros | RM Labore | Param. Rescisão.
* Pensão Alimentícia sobre 13º Salário: evento do tipo desconto com código de cálculo 120 e Dedutível IRRF 13º. Este evento deverá ser informado no código fixo do funcionário para que seja descontado no lançamento do 13º Salário ou rescisão.
* Pensão Alimentícia sobre Participação nos Lucros: evento do tipo desconto com código de cálculo 121 e dedutível de IRRF, sendo que nesse caso se estiver marcado como dedutível IRRF e possui cc 121, é considerado no IRRF PL cc 127 - IRRF Participação nos Lucros. Este evento deverá ser informado no código fixo do funcionário para que seja descontado no movimento de folha ou rescisão.

**Observação**

Para que o sistema calcule a pensão alimentícia sobre a 1ª Parcela do 13º Salário nas férias, é necessário informar o evento com código de cálculo 120 – Pensão Alimentícia sobre 13º salário no campo Eventos Adicionais Global ou Adicionais de Férias.

IMPORTANTE:

Quando acrescenta fórmula em códigos de cálculo relacionados a Pensão Alimentícia apresenta a mensagem abaixo, nesse caso deve também acrescentar o movimento no anexo do dependente para que cálculos de diferenças futuras considerem esse valor para inserir novo movimento no anexo do dependente.

*Atenção!*

*O lugar correto para informar a fórmula para o cálculo da pensão alimentícia é dentro do cadastro do dependente de pensão.*

*Para assim, o sistema poder identificar que o valor calculado é deste pensionista, e inserir o registro na respectiva movimentação.*

*Caso seja utilizada fórmula no evento, não será possível atualizar automaticamente o movimento de pensão.*

---

Códigos de Cálculo
