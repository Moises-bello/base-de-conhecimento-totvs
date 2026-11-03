---
content_hash: 923f63dfe7aff6ec70ebd3d16c85e483a8bda3ed1749b0fdbe8cd77421d6f622
fetched_at: '2026-06-29T00:11:03.351930+00:00'
page_id: '621010284'
product: rm
source: tdn-rm
title: Controle da Aprovação de Lançamentos a Pagar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621010284
version: 29
---

## **01. VISÃO GERAL**

Através da integração do TOTVS Gestão Financeira com o Fluig, é possível realizar o controle de aprovação de lançamentos a pagar. Ao habilitar esse processo serão gerados workflows no Fluig com os dados dos lançamentos a pagar inclusos, alterados (algumas situações parametrizadas) ou reenviados através de um processo específico, onde um usuário com o papel de aprovador deverá acessar o formulário do Fluig e após análise aprovar ou não o lançamento. Ao habilitar esse controle, os lançamentos a pagar terão alguns processamentos financeiros restritos de acordo com o status em que se encontram, essas condições serão listadas nesse documento.

**Observação: O lançamento de tributo gerado a partir de um lançamento com o status de aprovação igual a aprovado será gerado com o status de aprovação também aprovado.**

## **02. EXEMPLOS DE UTILIZAÇÃO**

### Inclusão de Lançamentos a Pagar

Ao incluir um lançamento financeiro a Pagar através do formulário, estando configurado o controle de aprovação integrado ao Fluig, esse lançamento será criado por padrão como Pendente de Aprovação e um workflow será gerado.

### Importação de Lançamentos

Na importação de lançamentos no formato XML ou TXT, os lançamentos a Pagar só serão importados se estiverem com status de aprovação Aprovado ou Pendente. Os lançamentos a Pagar que estiverem com os demais status não serão importados e serão informados no log do processo de importação.

### Alteração de lançamento

Ao alterar valores de um lançamento a pagar, se o controle de aprovação estiver habilitado nos parâmetros do sistema, será calculado o valor líquido do lançamento com e sem os valores alterados, sendo que, a diferença entre os dois cálculos será comparada com o valor estipulado na parametrização. Caso a diferença exceda o valor parametrizado, podemos ter os comportamentos a seguir baseados no status do controle de aprovação:

**Lançamentos com status Aprovado:** Será gerado um novo workflow de aprovação e o lançamento terá o status alterado para Pendente Aprovação.

**Lançamentos com status Pendente:** Será cancelado o workflow atual e um novo workflow será gerado para aprovação sendo que o status continua como Pendente Aprovação.

Em caso de alteração de valores de lançamento estipulado em moeda estrangeira, os respectivos valores líquidos (inicial, e após alteração) serão primeiramente convertidos para a moeda de circulação nacional (R$), e em seguida submetidos ao procedimento acima estipulado. Em caso de alteração da moeda do lançamento, este também será submetido ao procedimento acima estipulado, independente de alteração do valor do lançamento.

### Vínculos

O processo de vínculo será permitido para os lançamentos que estiverem com status "Não se aplica", "Pendente" e "Aprovado".

Para lançamentos com status "Não se aplica": não houve nenhuma mudança comportamental em relação ao padrão do sistema.

  Para lançamentos a pagar com status "Pendente":

* + Ao realizar o vínculo no valor total do lançamento o workflow existente no Fluig será cancelado e o status do lançamento será atualizado para "Aprovado".
  + Caso o vínculo seja correspondente ao valor parcial do lançamento, será cancelado o workflow no Fluig e será criado um novo com o valor remanescente a pagar.

Para lançamentos a pagar com status "Aprovado": no processo de desvincular será verificado se o valor está dentro da margem de alteração parametrizada, se sim o status será mantido. Caso contrário, o workflow existente no Fluig será cancelado, um novo será enviado e o status será modificado para       "Pendente".

### Geração de lançamento de IR

O lançamento de IR gerado a partir de uma nota seguirá o status de aprovação do lançamento pai. Caso a configuração de data base para geração seja "Emissão", e a nota criada com status "Pendente aprovado", o lançamento de IR seguirá este status e terá seu próprio workflow de aprovação no Fluig.

### Inclusão de fatura

       A inclusão de fatura será permitida apenas para lançamentos com status de aprovação "Não se aplica" ou "Aprovado".

       O status de aprovação dos vencimentos de fatura serão determinados da seguinte forma:

* Se todos os lançamentos faturados estiverem com o status "Não se aplica", os vencimentos de fatura terão o status "Não se aplica";
* Se pelo menos um dos lançamentos faturados estiver com o status "Aprovado", os vencimentos de fatura terão o status "Aprovado".

### Reenvio para Controle de Aprovação no Fluig

Através do processo "Reenvio para Controle de Aprovação no Fluig" na tela de lançamentos. Esse recurso permite que sejam enviados para aprovação somente os itens que estiverem com status do controle de aprovação como "Não se Aplica" ou "Reprovado", gerando o workflow de aprovação de cada um dos lançamentos processados.

## **03. PARAMETRIZAÇÃO FLUIG**

Para a utilização da integração com o Fluig é necessário configurar em Ambiente | Parâmetros | Parâmetros Globais | Aba Integração Fluig informar o Endereço do Servidor do Fluig, Usuário/Senha do administrador do Fluig e Id da Empresa do Fluig.

A comunicação entre o Fluig e o módulo Financeiro, será feita através do dataserver de lançamento *[FinLanDataBR](https://apitotvslegado.z15.web.core.windows.net/FinLanDataBR.html?Objeto=FinLanDataBR).*Através dos campos Codcoligada e Idlan (informação recebida pelo Fluig no recebimento do workflow), será feita a identificação do lançamento a ser aprovado/reprovado.

Deve ser usado o método SaveRecord, informando no campo STATUSAPROVACAO o status da aprovação, onde 2 indica "aprovado" e 3 "reprovado".

***Importante:*** para mais informações sobre a instalação e configuração do Fluig, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=257623022).

**04. PARAMETRIZAÇÃO TOTVS GESTÃO FINANCEIRA**

****Os parâmetros de Controle de Aprovação estão disponíveis na etapa 02.01.01.01 Lançamentos da parametrização de Contas a Pagar****

| Parâmetro | Descrição |
| --- | --- |
| Utiliza controle de aprovação de lançamento | Habilita a funcionalidade para a coligada se estiver marcado. |
| Processo Fluig | WorkFlow do Fluig que será utilizada para controlar o fluxo de aprovação. |
| Valor máximo permitido de alteração sem reaprovação | Esse valor será utilizado durante a alteração de valores do lançamento, para definir se alterações  do lançamento superiores a esse valor deve colocar o lançamento novamente no fluxo de aprovação.  Observações:   * Campos alterados do lançamento que estão sob essa regra:  ValorDesconto, ValorOp1, ValorOp2, ValorOp3, ValorOp4, ValorOp5, ValorOp6, ValorOp7, ValorOp8, ValorJuros, ValorCap, ValorMulta, JurosDia, CapMensal, MultaDia, FormulaJuros, FormulaCapitalizacao, FormulaMulta, FormulaDesconto, FormulaValorOp1, FormulaValorOp2, FormulaValorOp3, FormulaValorOp4, FormulaValorOp5, FormulaValorOp6, FormulaValorOp7, FormulaValorOp8, DataEmissao, DataVencimento, ListaValoresIntegracaoLancamento.  * Caso o lançamento tenha moeda diferente da configurada na conta caixa selecionada será feita conversão do valor, usando as cotações cadastradas, para a moeda da conta caixa antes de realizada a comparação. Para que a validação seja feita corretamente, é obrigatória a conta caixa no lançamento em moeda estrangeira. |

Ao habilitar o controle de aprovação, os lançamentos já existentes assumem o status "Não se Aplica" e para que sejam considerados pelo controle de aprovação, precisarão passar pelo processo de "Reenvio para Controle de Aprovação no Fluig".IMPORTANTE!

## **05. BLOQUEIO DE PROCESSAMENTO FINANCEIRO**

Ao habilitar esse controle, os lançamentos a pagar terão alguns processamentos financeiros restringidos considerando o status em que se encontram.

Conforme descrito, a seguir:

* **Lançamentos a pagar com status "Pendente Aprovação" não permitem a execução de:** Baixa, Fatura, Parcelamento, Inclusão em Borderô e Alteração valor do IRRF.
* **Lançamentos a pagar com status "Reprovado" não permitem a execução de:** Baixa, Fatura, Parcelamento, Inclusão em Borderô e Vínculo.
* **Lançamentos a pagar com status "Aprovado" não permitem a execução de:** Parcelamento e Alteração valor do IRRF.
* **Lançamentos a pagar com status "Não se Aplica" não sofrem nenhum tipo de bloqueio.**
