---
content_hash: 56fc0ea377b06eaa1f205ffd4a4ed8814ca217aba0548e645ca86bc1e372b09b
fetched_at: '2026-06-29T00:11:20.629818+00:00'
page_id: '687156746'
product: rm
source: tdn-rm
title: Parametrizador - Folha Agrária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687156746
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Descrição por item**
3. **Tela Parâmetros da Folha Agrária**
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Parametrização necessária para a utilização da folha agrária

## **02. DESCRIÇÃO POR ITEM**

## **Configurações Gerais**

Através do parâmetro "**Usa Folha Agrária**" habilite o menu de folha agrária.

**Campo complementar de funcionários que recebem comissão** será utilizado para identificação dos funcionários que recebem comissão. Por exemplo, funcionário saqueiro que é o que carrega sacas para abastecer caminhões, armazéns e outros.

**Máscara para unidade agrária** tem a finalidade de definir e validar o escalonamento em níveis da unidade agrária de produção quanto sua divisão no campo. Exemplo: 999.9999. Onde os primeiros 999 seriam um setor e o segundo 9999 seriam seus lotes.

* + Caracteres para ser aplicado na máscara:

'#' - Números;

'L' - Alfabético e de preenchimento obrigatório;

'A' - Alfanumérico e que os dígitos devem ser preenchidos obrigatoriamente;

'a' - Alfanumérico, podendo ser digitados letras e números;

'Q' - Qualquer caractere, menos os separadores ( : . , ; / );

'.' - Como o separador.

* + Máximo permitido de 30 caracteres.

## **Parâmetros da Filial**

### Valores Default

As informações de **Unidade Agrária, Fração Agrária e Programação** serão utilizadas para a definição da unidade agrária, no lançamento de CAT, Previdência e demais complementos quando não existir um lançamento anterior.

### Cálculo

O **Período global de produção** é o Intervalo de datas destinado a limitar os dias de produção referente à competência de pagamento da folha em que os eventos da produção serão lançados:

**Dias a retroceder na inclusão automática do preço unitário na unidade agrária**

Este parâmetro será utilizado na inclusão automática de preço unitário na unidade agrária (Teste). Informando quantos dias deverá retroceder para obtenção do último preço unitário na unidade agrária e assim inserir novo preço unitário baseado nesse retrocesso caso não exista no momento do processo da folha agrária.

**Regra para mínimo garantido para diária**

Este parâmetro informa como deverá se obter a remuneração mínima para um dia de trabalho. Utilizado para cálculos de complementos diversos quando a produção não atinge este valor. Deverá informar a regra de cálculo existente no cadastro de Regra de Cálculo da Tarefa Agrária.

**Tarefa complemento de diária mínima**

Essa tarefa deve ser do tipo Depende de outras tarefas e com prioridade maior que as tarefas que serão complementadas.

O parâmetro de tarefa para Complemento de Diária Mínima. Define a tarefa de cálculo para obtenção do valor a ser pago quando o funcionário não atinge a diária mínima.

**Observação:**

1 - Ideal que esta regra seja do tipo “Mínimo Diária” ou “Diária”. O cálculo para este parâmetro já sugere uma Diária.

2 - Tarefa de complemento de diária deve ter prioridade maior que a tarefa de afastamento porque o complemento do afastamento deve ser calculado primeiro e abatido do complemento de produção porque o afastamento tem prioridade sobre a produção

**Tarefa para Pausa Remunerada**

Essa tarefa deve ser do tipo Pausa Remunerada para ser utilizada no lançamento da produção agrária.

**Tarefa do DSR**

Define a tarefa de cálculo em que é informada a regra de cálculo para o DSR.

**Tarefa para Feriado Normal**

Define a tarefa de cálculo para lançar o feriado na linha de produção quando o funcionário não possui produção, afastamento, férias.

**Tarefa para Feriado em Dobro**

Define a tarefa de cálculo para lançar o feriado na linha de produção quando o funcionário possui produção.

### Comissão

**Período de liberação para digitação das comissões** definirá a data de início e fim para o lançamento de comissões assim como a competência a ser considerada como pagamento.

A informação da **Tabela de cálculo para comissão de saqueiro** será utilizada para definir a tabela de cálculo informando às faixas para o cálculo da remuneração por quantidade de sacos transportados.

A informação do **Evento para pagamento de comissão de saqueiro** será utilizada para lançar na folha de pagamento o evento contendo o valor a pagar das comissões

### Tarefa para Afastamento

São as tarefas de cálculo para efetuar a remuneração em dias que o funcionário está afastado por acidente de trabalho ou previdência, correspondente aos 15 dias de responsabilidade da empresa.

## **Tipos de Tarefa Agrária**

Os tipos de tarefas cadastradas nestes parâmetros serão utilizados para os módulos que selecionarem somente tarefas agrárias. As tarefas agrárias serão cadastradas utilizando o cadastro do módulo de Gestão de Pessoas em Gestão Organizacional / Tipo de Atividade Executada.

## **03.** **TELA Parâmetros da Folha Agrária**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Folha Agrária | Acessa parâmetros da folha agrária |
| Configurações Gerais | Parametriza o uso da folha agrária e outros parâmetros |
| Parâmetros da Filial | Parametriza valores específicos por filial |
| Tipos de Tarefa Agrária | Seleciona os tipos de tarefa agrária |

## **04. TABELAS UTILIZADAS**

* PPARAMADICIONAIS
* PPARAMFILIAL
