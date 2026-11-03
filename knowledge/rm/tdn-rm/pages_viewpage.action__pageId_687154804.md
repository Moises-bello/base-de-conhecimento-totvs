---
content_hash: 6226f8671547a35025a843bb2239040d6ad3292ca7deba6df3287d4c941e5f2e
fetched_at: '2026-06-29T00:11:20.594426+00:00'
page_id: '687154804'
product: rm
source: tdn-rm
title: Lançar complemento de diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687154804
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Esse parâmetro será usado para o cálculo do valor a complementar na diária do trabalhador rural. Para isso é preciso preencher os campos “Regra para mínimo garantido para diária” e “Tarefa complemento de diária mínima” do Parametrizador / Folha Agrária / Parâmetros da filial / Cálculo.

A regra de cálculo da tarefa agrária pode estar configurada como segue abaixo:

* A finalidade deverá ter o campo “Tarefa de Produção” desmarcado;
* O campo “Tipo de cálculo” deverá ter sido marcado a opção “Depende de outras Tarefas”;
* A prioridade de cálculo deverá ser maior que as Tarefas produção;
* O campo “Validar quantidade de Diária” e “Incide no Cálculo do Homem-Dia” podem estar marcados ou não.
* O campo “Complemento de Diária Mínima” deve estar marcado.

Deverá zerar o valor unitário caso:

* Não Tenha no dia Tarefa cuja finalidade seja “Tarefa de Produção”; OU
* O campo “Lança complemento de diária” NÃO tenha sido marcado;
* Tendo falta, cadastrada a ocorrência para esse dia no histórico de ocorrência com o campo “Impede complemento de Diária” no tipo de ocorrência marcado não poderá lançar complemento de diária.

Exemplo de cálculo da diária mínima:

* Equação: (Salário / Carga horaria mensal) / Carga horária do dia
* Exemplo: 850,00 / 220h \* 8h = 30,91 (exemplo segunda à sexta)

   850,00 / 220h \* 4h = 15,46 (exemplo sábado carga horário de 4h)

* O valor lançado nesse complemento será a diária mínima menos a soma das tarefas de produção. Caso o valor seja positivo.

**Situações para complemento de diária**

**Complementa a diária**

* Atestado Médico - Rotina de Produção calcula esta tarefa verificando histórico de afastamento do tipo ‘P’ (quando afastamento menor 15 dias), ou seja, quando o afastamento acontece depois que houve um período trabalhado no dia.
* CAT - Rotina de produção calcula esta tarefa verificando histórico de afastamento do tipo acidente do trabalho, ou seja, quando o afastamento acontece depois que houve um período trabalhado no dia.
* Quando não atingiu a produção
  + Ocorrências cadastradas no histórico de ocorrências e que o tipo de ocorrência “Impede complemento de diária” não esteja marcado.
  + Ocorrências sem cadastro no histórico de ocorrências.

**Não complementa a diária (Valor vem da regra ‘valor da diária’)**

* Não atingiu a produção
  + Ocorrências cadastradas no histórico de ocorrências e que o tipo de ocorrência “Impede complemento de diária” esteja marcado.

## **02. EXEMPLO DE UTILIZAÇÃO**

Existe a tarefa lançada como diária, foi calculada a pausa remunerada e as duas somam para o cálculo do complemento de diária.

**Como fica o Log de cálculo do complemento de diária:**

Funcionário Chapa: 00005

    Dia quinta-feira, 6 de maio de 2021:

        Tarefa: 00001 - Análise de sistemas TAREFA DIÁRIA Regra: 3 - DIÁRIA  - Prioridade: 4

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 02 Tipo: Diaria Evento: 7771

        Salário do Funcionário: 3.469,32

        Jornada do Dia Obtida do Ponto: 8,00

        (Salario / jornada Mensal \* Jornada Diária) = Preço Unitário dia

        (3.469,32 / 220,00 \* 8,00) = 126,1571

        (Quantidade \* Preço Unitário) = Valor Ganho

        (0,1050 \* 126,1571) = **13,2500**

        Tarefa atualizada na produção.

        Tarefa: 90304 - PAUSAS Regra: 16 - PAUSA REMUNERADA - Prioridade: 10

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 04 Tipo: Empreita Evento: 9304

        Quantidade de pausas: 1

        Minutos das pausas  : 15

        Tarefa: 00001 - Análise de sistemas TAREFA DIÁRIA 120 minutos 13,25 (Diaria)

        Denominador: 480,00 maior entre Jornada Planejada: 480,00 Soma das Horas de Produção: 120,0000

        Indice: (120,00 / 480,00) = 0,2500

        Valor Diaria: (3.469,32 / 13.200,00 \* 480,00) = 126,1571

        Pausa: (126,16 / 480,00) \* (0,2500 \* 15,0000) = 0,9856 (Diaria)

        Soma das pausa das tarefas de produção: 0,9856

        Preço Unitário: (0,9856 / 1) =  0,9856

        (Quantidade \* Preço Unitário) = Valor Ganho

        (1,0000 \* 0,9856) = **0,9900**

        Tarefa atualizada na produção.

        Tarefa: 00006 - Vender Produtos - TAREFA DEPENDE DE OUTRAS Regra: 12 - COMPL DE DiÁRIA - DEPENDE DE OUTRAS TAREFAS - Prioridade: 889

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 06  Tipo: Diaria Evento: 7004

        Preço Unitário: 14,2400 Somátorio das produções de prioridades menor a 889 ou prioridades não informada

**(Quantidade \* Preço Unitário) = Valor Ganho**

**(1,0000 \* 14,2400) = 14,2400**

        Tarefa: 00004 - Suporte aplicativo RM Vitae TAREFA MINIMO DIÁRIA Regra: 4 - MINIMO DIÁRIA - Prioridade: 5

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 04 Tipo: Empreita Evento:

        (Salario / jornada Mensal ) = Preço Unitário Mínimo Diária.

        (3.469,32 / 220,00 ) = 15,7696

        (Quantidade \* Preço Unitário) = Valor Ganho

        (1,0000 \* 15,7696) = 15,7700

        Calculo do complemento de Produção. Diária Mínima - Valor obtido  = Valor a Complementar

**(15,7700 - 14,2400) = 1,5300**

        Tarefa incluida na produção.

Foi lançado da seguinte forma:

Uma tarefa para a pausa remunerada

Uma tarefa para o complemento de diária

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetro | Lançar complemento de diária |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
