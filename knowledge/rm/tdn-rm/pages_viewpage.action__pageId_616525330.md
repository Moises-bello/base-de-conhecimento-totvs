---
content_hash: cd483792c98e2fbc348fadf9eb8d15a31d47e4c684260a5753eb043dd4dda427
fetched_at: '2026-06-29T00:10:59.839592+00:00'
page_id: '616525330'
product: rm
source: tdn-rm
title: Diagnose e Terapia (SADT)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616525330
version: 34
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Validações**
   1. **Validação específica do padrão Unimed Belém**
   2. **Validação específica do padrão Unimed Juiz de Fora**
   3. **Caderno de gabarito**
3. **Cálculo do valor**
4. **Regras**
   1. **Atualização do médico responsável pelo exame no pedido**
   2. **Preenchimento do número da guia**
   3. **Divisão de cobrança**
   4. **Retorno**
   5. **Regra do cobrança de exames de tomografia e ressonância**
5. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A página de Diagnose e Terapia serve para visualizar exames lançados para o atendimento e para ser lançadas manualmente pelo faturamento.

## **02. VALIDAÇÕES**

* Validações do Registro do Atendimento
  + Deverá estar com o status diferente de "Cancelado"
* Validações da Parcial
  + - Deverá estar com o status diferente de "Faturada", "Liberada" ou "Cancelada".
    - Não poderá ter nota fiscal emitida e o convênio particular.
* Validações do Centro de Custo
  + Obrigatório se o parâmetro "Centro de Custo obrigatório nos lançamentos?" estiver marcado em Parâmetros Gerais > Faturamento II
  + Paciente interno
    - Matmed
      * Obrigatório se o parâmetro "Centro de Custo sem possibilidade de alteração" estiver marcado
    - Outros lançamentos
      * Obrigatório se o parâmetro "Centro de Custo vinculado ao leito sem possibilidade de alteração" estiver marcado
  + Paciente Externo
    - Obrigatório se o parâmetro "Centro de Custo vinculado a Estação de Trabalho sem possibilidade de alteração" estiver marcado
* O item deve estar na faixa de diagnose terapia

* É verificado a compatibilidade do exame com o sexo do paciente. Campo Sexo no cadastro dos itens da Tabela de Procedimentos e Serviços
* Caso o item tenha incidência de filme, é validado se a incidência informado no lançamento é menor que o definido na tabela. Caso seja, o item não é salvo e uma mensagem é exibida.
* Item estornado não pode ser alterado
* O item especial não pode ser alterado. Deve ser estornado e incluído novamente pela página Especial.
* O valor da taxa e serviço incluído deverá ser maior que 0.
* Validações do campo Data:
  + A data do exame deve estar dentro do período da parcial
  + A data/hora de início não pode ser maior que a data/hora final
  + A hora final não pode ser menor que a hora inicial
* Validações do padrão Unimed Belém

  + O número da guia é obrigatório para paciente interno.
* Validações do padrão Unimed Juiz de Fora

  + Não permite incluir um lançamento repetido, com o mesmo item, na mesma data/hora.
* Validações do Caderno de Gabarito

  + Ao salvar um exame, o sistema verifica se existe um gabarito em aberto para a conta e se comporta de acordo com os parâmetros gerais:
  + Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Questionar inclusão no pacote". O sistema pede a confirmação do usuário para incluir a diária no pacote. Ou seja, a diária será cobrada além do pacote.
  + Se os parâmetros estiverem marcados: "Verificar existência de Gabarito ao incluir novo item - Elaboração de Contas"  e "Ação ao identificar Gabarito: Incluir automaticamente no pacote". O sistema não pede confirmação e incluirá a diária automaticamente junto com o pacote.
  + Caso não tenha um gabarito em aberto, a diária não será cobrada
* Cadastro de Função Medica na Aba de Diagnose e Terapia que poderá ser informada no xml da TISS, caso preenchida.

## **03. CÁLCULO DE VALOR**

falseValorRegra geral

Para o cálculo do valor do exame, o sistema segue a seguinte ordem de prioridade nas tabelas a consultar:

1. Tabelas de preços diferenciadas (se existir para o plano)
   1. Tabela especial
   2. Tabela de procedimentos
2. Tabelas das condições contratuais
   1. Tabela especial
   2. Tabela de procedimentos

Se não encontrar o item na tabela especial, o sistema procura na tabela de procedimento.

As tabelas podem ser tanto em reais, quanto em quantidade de CH. Para o uso de CH é necessário configurar no cadastro de Condições Financeiras, os valores de CH.

Fator

Nas condições contratuais com os convênios, pode-se definir um fator de multiplicação para os exames. Assim, o sistema sempre considerar este valor.

Caso o mesmo não esteja definido para ser utilizado, o cálculo do fator vai se basear nas regra da AMB ou CBHPM.

Para o padrão AMB, se for atendimento interno e o parâmetro "Utiliza histórico de leitos para cálculo de fator de acomodação" estiver marcado, o sistema localiza o leito ocupado na data do lançamento do exame e obtém o fator de acomodação.

Hora Extra

Para considerar o acréscimo de hora extra no cálculo do exame, é necessário marcar o parâmetro "Adicional data e hora extra para exames". O sistema verifica se o atendimento é de urgência/emergência, se a data de lançamento está dentro das regras de hora extra e aplicará o percentual, de acordo com as parametrizações no cadastro de "Padrão de Faturamento e Codificação"

 

Filme radiológico

O filme radiológico pode ser lançado de duas formas:

* Compondo o valor do exame
* Destacado ou seja, um outro lançamento

O valor é o mesmo, porém somente a forma que aparece na conta é onde está a diferença.

falseFilmeCálculo e Parametrizações

Para o cálculo, o sistema considera a metragem de filme configurado no cadastro de procedimentos e no valor do filme, baseado no cadastro das Condições Financeiras, anexo Valor de filme.

O valor do filme pode ser configurado com uma valor padrão ou básico, que será utilizado caso não tenha nenhum outro valor definido mais específico. O sistema segue a seguinte ordem para obter o valor do filme:

1. Item
2. Grupo
3. Especialidade
4. Básico

Para lançar o filme destacado do exame, deve-se marcar o parâmetro abaixo:

Deve-se também informar o código do filme a ser lançado, nos Padrões de Faturamento e Codificação

DestacadoValor somado ao exameIncidência Extra

Para o cálculo da incidência extra, o sistema considera os seguintes parâmetros:

* Percentual incidência extra: é o percentual que será aplicado ao valor do exame
* Valor do filme destacado no lançamento de exames radiológicos,

FilmeLançamento

 

Valor do exame: 100,00

Valor do filme: 0,3080 x 19,40 = 5,9752 = 5,98

Incidência extra: 3 - 2 = 1 \* 100 \* 20/100 = 20,00

DestacadoValor somado ao exame

Valor: Valor do exame + valor do filme = 100 + 5,88 = 105,98

Incidência extra = valor da incidência + valor do filme = 20 + 5,98 = 25,98

IPSEMG e IAMSPE

Para esses convênios a regra para obter a tabela de procedimentos é a mesma da regra geral. A diferença está na obtenção dos valores.

Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços.

Filtre pelo código da tabela utilizada pelo convênio e selecione um item de Diagnose e terapia. Em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

O sistema seleciona o valor de acordo com a vigência mais atual e o valor unitário da taxa corresponde ao campo Vlr. Total e o valor total corresponderá à quantidade dedo item, multiplicado pelo valor unitário.

## **04. REGRAS**

* **ATUALIZAÇÃO DO MÉDICO RESPONSÁVEL**

Nos lançamentos Diagnose e Terapia, após alterar o prestador vinculado ao lançamento, o sistema deve atualizar, no pedido de exames, o médico responsável por este exame no pedido.

* **REGRA DENTRO/FORA DA CONTA**

Ao salvar o exame, o sistema verifica o credenciamento do prestador junto ao convênio:

Se Indireto: gravar a coluna EXAMEFORA com o valor FALSO. O prestador deve receber pela instituição.

Se Direto, for diferente do prestador principal e o parâmetro  "Lançar item como "Fora da Conta" para prestadores credenciados diretamente com o convênio" marcado : EXAMEFORA = T, gravar VERDADEIRO. O prestador credenciado diretamente, receberá pelo convênio, e não pela instituição.

Se existir regra de dentro/fora da conta, este deve prevalecer. Ver cadastro de Regra dentro/fora da conta.

* **PREENCHIMENTO DO NÚMERO DE GUIA**

Caso o convênio utilize o padrão TISS (e não seja do padrão especial Unimed Lavras e Unimed Belém) e exista número de guia para a parcial de lançamento, o sistema preencherá automaticamente o campo "Nro. guia". Se existir o mesmo procedimento, a guia selecionada será esta. Caso contrário, será a primeira da lista.

* **DIVISÃO DE COBRANÇA**

Existem duas formas para ocorrer a divisão de cobrança de exames.

As duas precisam que os campos "Divisão de cobrança" e "Prestador divisão de honorários" estejam preenchidos.

O campo "Divisão de cobrança" deve ser marcado antes de se incluir o registro. Após a sua inclusão, o campo não pode ser alterado.

DivisaoCobrancaPor percentual

Para esse tipo é necessário realizar o cadastro da regra de cada prestador e os respectivos exames e percentual o cada um receberá. O restante é lançado em nome do prestador principal da unidade de faturamento.

Portanto para utilizar essa regra, é necessário informar como o prestador do lançamento, o próprio médico. O sistema identificará que o mesmo possui regra cadastrada e preencherá os campo "Divisão de cobrança" e "Prestador divisão de honorários" automaticamente.

Por valor

Já a divisão por valor, corresponde a realizar o lançamento para a instituição com o valor do custo operacional e outro lançamento para o prestador que executou o exame com o valor do honorário. Para que isso ocorra, o procedimento deve ter os dois valores informados, seja em quantidade de CHs ou em reais.

Ao realizar o lançamento, informe o prestador como sendo aquele que receberá os custos operacionais.

O valor do filme vai para o prestador com o custo operacional. Somente o honorário será para o prestador informado em "Prestador divisão de honorários"

* **REGRAS DE RETORNO**

Ao lançar um exame, o sistema verifica as regras de lançamento de retorno para não cobrá-lo. Para mais detalhes, consultar a documentação 

* **REGRA DE COBRANÇA DE EXAMES**

Rotina responsável por aplicar as regras de incidências dos exames realizados no mesmo dia, Para mais detalhes, consultar a documentação

## **05. TABELAS UTILIZADAS**

* SZATENDSADT
