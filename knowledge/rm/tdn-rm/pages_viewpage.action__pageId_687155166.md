---
content_hash: 0f85a0716aa187646de10a109eef9c5401967ac00f68e331835e31728d22e167
fetched_at: '2026-06-29T00:11:20.605420+00:00'
page_id: '687155166'
product: rm
source: tdn-rm
title: Atualizar preços segundo cadastro de teste e diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687155166
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cálculo de Produção Agrária**
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse parâmetro será calculada a produção agrária de acordo com as regras da Importação da Produção Agrária. Acesse o link para detalhamento [Importação da Produção Agrária](https://tdn.totvs.com/pages/viewpage.action?pageId=643753670).

Será atualizado o campo Valor Ganho da produção com o cálculo de “Quantidade produzida \* Preço Unitário”.

Veja como podem ser configuradas as regras de calculo

* Processa para Tarefa em que a finalidade seja “Tarefa de Produção”.
* A regra de cálculo da Tarefa agrária pode estar configurada como segue abaixo:
  + A finalidade deverá ter o campo “Tarefa de Produção” marcado;
  + O campo ***“Tipo de cálculo”*** não poderá ter sido marcado a opção “Depende de outras Tarefas”;
  + A prioridade de cálculo deverá ser a mais baixa, pois é base para cálculo de outras tarefas;
  + O campo “Validar quantidade de Diária” pode estar marcado.
  + O campo “Incide no Cálculo do Homem-Dia” pode estar marcado;
  + O campo “Complemento de Diária Mínima” deve estar desmarcado.

## **02. EXEMPLO DE UTILIZAÇÃO**

**01 -** Existem os cálculos abaixo referentes as tarefas com preço informado e diária:

**02 –** Foram feitas as seguintes alterações:

No preço informado para o dia 03/05/2021 alterado o valor de 2,00 para 2,50

Na diária a quantidade de 1 para 0,5236

**03 –** Processando o cálculo agrário os valores foram alterados na produção agrária

    Dia segunda-feira, 3 de maio de 2021:

        Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO Regra: 2 - PREÇO INFORMADO - Prioridade: 3

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 07 Tipo: Empreita Evento: 7772

        Preço Unitário informado 2,5000 na Cultura da Vigência na Data da produção 03/05/2021

        (Quantidade \* Preço Unitário) = Valor Ganho

        (1,0000 \* **2,5000**) = 2,5000

        Tarefa atualizada na produção.

        Tarefa: 00001 - Análise de sistemas TAREFA DIÁRIA Regra: 3 - DIÁRIA  - Prioridade: 4

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 02 Tipo: Diaria Evento: 7771

        Salário do Funcionário: 8.123,58

        Jornada do Dia Obtida do Ponto: 8,00

        (Salario / jornada Mensal \* Jornada Diária) = Preço Unitário dia

        (8.123,58 / 200,00 \* 8,00) = 324,9432

        (Quantidade \* Preço Unitário) = Valor Ganho

        (**0,5236** \* 324,9432) = 170,1400

        Tarefa atualizada na produção.

**Atenção:** Quando o cálculo da produção encontra o valor zero para o campo “Valor ganho” a tarefa será excluída da produção de acordo com a regra:

Para a atualização da Produção Agrária será seguida a seguinte regra:

* Caso o valor unitário obtido seja zero deverá:
  + Se existe na produção excluir, exceto quando a regra de cálculo da Tarefa tenha sua finalidade marcada como Tarefa de produção.
  + Se não existe ignora e não inclui
* Caso valor unitário seja maior que zero deverá:
  + Sobrepor se já existir;
  + Incluir se não existir.

Exemplo de parâmetro Marcado e Desmarcado:

Dia 17/05/2021 existe produção para cálculo para o funcionário 00034. No parametrizador estava marcado com valor 2 em dias a retroceder e foi excluído o preço de produção do dia 17/05/2021.

NA MENSAGEM DE AVISO APRESENTA

Inclusão de Preço Unitário na unidade Agrária de Produção não foi realizada, pois não há um Último Preço Unitário na Unidade Agrária que atenderia a restrição de Dias a retroceder referente ao Dia 17/05/2021 Unidade Agrária 01 Fração Agrária 1 Programa 1 Tarefa 00002.

A importação apresenta a mensagem que não importa devido não existir valor unitário inclusive para os dias a retroceder.

Nas condições acima o cálculo procede da seguinte forma:

**PARÂMETRO TAREFA DE PRODUÇÃO** - 'Atualizar preços segundo cadastro de teste e diária' está Desmarcado

Funcionário Chapa: 00034

    Dia segunda-feira, 17 de maio de 2021:

        Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO Regra: 2 - PREÇO INFORMADO - Prioridade: 3

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 07 Tipo: Empreita Evento: 7772

        Regra com Tipo de Calculo PrecoInformado em que o parâmetro 'Atualizar preços segundo cadastro de teste e diária' está Desmarcado não calcula Valor Ganho

        Tarefa atualizada na produção.

**PARÂMETRO TAREFA DE PRODUÇÃO** - 'Atualizar preços segundo cadastro de teste e diária' está Marcado

Funcionário Chapa: 00034

    Dia segunda-feira, 17 de maio de 2021:

        Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO Regra: 2 - PREÇO INFORMADO - Prioridade: 3

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 07 Tipo: Empreita Evento: 7772

        Valor Ganho de 4,00 não foi alterado. Preço unitário zerado

**PARÂMETRO TAREFA DE PRODUÇÃO DESMARCADO** - 'Atualizar preços segundo cadastro de teste e diária' está Desmarcado

Funcionário Chapa: 00034

    Dia segunda-feira, 17 de maio de 2021:

        Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO Regra: 2 - PREÇO INFORMADO - Prioridade: 3

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 07 Tipo: Empreita Evento: 7772

        Regra com Tipo de Calculo PrecoInformado em que o parâmetro 'Atualizar preços segundo cadastro de teste e diária' está Desmarcado não calcula Valor Ganho

        Tarefa atualizada na produção.

**PARÂMETRO TAREFA DE PRODUÇÃO DESMARCADO** - 'Atualizar preços segundo cadastro de teste e diária' está Marcado

Funcionário Chapa: 00034

    Dia segunda-feira, 17 de maio de 2021:

        Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO Regra: 2 - PREÇO INFORMADO - Prioridade: 3

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 07 Tipo: Empreita Evento: 7772

        Valor Ganho de 4,00 não foi alterado. Preço unitário zerado

        Tarefa em que a finalidade não é de produção com preço unitário zerado. **Excluida da Produção e do processamento.**

Veja que a tarefa foi excluída quando o parâmetro Tarefa de Produção em Finalidade da tarefa agrária está desmarcado.

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetro | Atualizar preços segundo cadastro de teste e diária |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
