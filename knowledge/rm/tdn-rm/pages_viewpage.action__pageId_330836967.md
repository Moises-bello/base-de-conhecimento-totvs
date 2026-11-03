---
content_hash: 1189d1f42d43d723a3869c335ee2c5c6a46a39236cb33c27e61e741525bfce83
fetched_at: '2026-06-29T00:08:49.499390+00:00'
page_id: '330836967'
product: rm
source: tdn-rm
title: DT Desconto por antecipação - Associar descontos por antecipação para matrizes
  aplicadas ou campus/polos da matriz aplicada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330836967
version: 5
---

# Desconto por antecipação - Associar descontos por antecipação para matrizes aplicadas ou campus/polos da matriz aplicada

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **TOTVS Gestão Educacional** |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **Desconto por antecipação.** | **Desconto por antecipação*.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Associar descontos por antecipação à matriz aplicada ou campus/polo da matriz aplicada.* | *Associar descontos por antecipação à matriz aplicada ou campus/polo da matriz aplicada.* | |  |  | |
| **Cadastros Iniciais:** | **Cadastro de Matrizes Curriculares*.* |
| **Parâmetro(s):** | **N/A** |
| **Ponto de Entrada:** | **N/A** |
| **Tickets relacionados** | **N/A** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-1092* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | ***N/A*** |
| **Tabelas Utilizadas:** | *SHabilitacaoFilialDescPontual, SHabFilialCampusDescPontual.* |
| **Sistema(s) Operacional(is):** | ***N/A*** |

## Descrição

Foi criado o processo "Associar desconto por antecipação para Matrizes Aplicadas ou Campus/Polos", através dele é possível vincular desconto(s) por antecipação para várias matrizes aplicadas ou campus/polos das matrizes aplicadas.

## Associar descontos por antecipação para Matrizes Aplicadas ou Campus/Polos

No módulo Educacional o processo 'Associar desconto por antecipação para Matrizes Aplicadas ou Campus/Polos' é acessado através dos processos de matrizes curriculares (Currículo e Oferta → Matrizes Curriculares → Processos → Associar descontos por antecipação para Matrizes Aplicadas ou Campus/Polos).

O processo permite que sejam associados descontos por antecipação a matrizes aplicadas e a campus/polos das matrizes aplicadas.

Passos para a execução do processo:

* Acessar o cadastro de matrizes curriculares.
* Selecionar matrizes curriculares.
* Clicar em 'Processos' → 'Associar descontos por antecipação para Matrizes Aplicadas ou Campus/Polos'.
* Selecionar se descontos por antecipação serão associados a 'Matriz Aplicada' ou 'Campus/Polo da Matriz Aplicada'.
* Informar se eventuais vínculos pré-existentes serão sobrescritos ou não.
* Visualizar grid de matrizes aplicadas ou campus/polos das matrizes aplicadas (De acordo com a seleção feita anteriormente na tela do processo), filtradas pela(s) matriz(es) curricular(es) selecionadas antes de acionar o processo.
* Caso existam registros que não devam ser associados, selecioná-los e clicar em 'Remover'.
* Ao lado estará presente a grid de Desconto por antecipação, onde é possível realizar filtros, para refinar a busca e também é possível selecionar registros que não deverão ser associados e clicar em 'Remover'.
* Clicar em executar e todos os registros mostrados na visão 'Todas as matrizes aplicadas' ou 'Todos os campus/polos das matrizes aplicadas' (De acordo com a seleção feita anteriormente na tela do processo) bem como todos os descontos por antecipação existentes na respectiva grid serão associados.
* Ao final será exibido um log informativo, onde consta quais e quantos vínculos foram feitos e quais e quantos não foram e os motivos da eventual não associação.

Segue abaixo exemplo da utilização do processo:

Importante:

Assim como na associação direta nos cadastros a associação de desconto por antecipação via processo também validará inclusões de descontos por antecipações com vigências sobrepostas.

Exemplo:

       (Associação inválida  - Vigências sobrepostas em 01/2017)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

       (Associação válida  - Vigências não sobrepostas)

* Campus 9
* Associação 1: Desconto por antecipação de   a
* Associação 2: Desconto por antecipação de   a

Essa validação impedirá que Descontos por Antecipação com conflito de vigência sejam associados a uma mesma matriz aplicada ou a um campus/polo de uma matriz aplicada.

(Permissão no perfil do usuário)
