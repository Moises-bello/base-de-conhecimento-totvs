---
content_hash: 0332a7d69904e3e4d3c3cf3ba30708f212a35709aa8e0fc42b9a132ef5044827
fetched_at: '2026-06-29T00:10:01.493097+00:00'
page_id: '452718753'
product: rm
source: tdn-rm
title: Recalcular Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718753
version: 4
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Recalcular Rescisão**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310 e Superiores

## **02. VISÃO GERAL**

O cadastro da rescisão contratual, no momento da demissão do funcionário, é feito no anexo do cadastro de funcionários ou no cadastro global de rescisão.

O módulo Recalcular Rescisão é utilizado para realizar o recálculo das rescisões ao final de vários cadastros.

Para o recálculo das rescisões deverá ser preenchido um intervalo do período da rescisão com Data Inicial e Data Final, informar o Código de Quebra das seções e verificar a Seleção dos Funcionários que serão recalculados.

O recálculo da rescisão pode ser utilizado também para recalcular apenas uma rescisão de acordo com a seleção da chapa dentro da Seleção de Funcionários.

## **03. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios: Base exemplo

Funcionário 00001 

Funcionário 00009 com férias partidas terminando no mês para ser lançado e finalizado

Com rescisão cadastrada pelo módulo Cadastro Global 

Tipo 2 - Sem justa causa

Aviso Indenizado 30 dias

Marcando o parâmetro “Gravar rescisão com férias a lançar ou a finalizar”

11Recalcular com parâmetro “Executar Parâmetros de Cálculo da Rescisão” desmarcado

Funcionário 00001: Lança no envelope os eventos básicos da rescisão 

Funcionário 00009: Não calcula e apresenta mensagem ao final da execução do recálculo: Existem férias lançada e não finalizada para o período 17/07/2023 a 15/08/2023. A rescisão não foi processada para a chapa 00009.

2Recalcular com parâmetro “Executar Parâmetros de Cálculo da Rescisão” marcado

Marcando os parâmetros:

* Lança e/ou finaliza férias automaticamente
* Lança Códigos Fixos na Rescisão
* Desconta Vale transporte na Rescisão
* Empréstimos Todos

Destacando os dados referentes aos parâmetros temos:

Funcionário 00001

Funcionário 00009

## **04.** **TELA Recalcular Rescisão**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Intervalo de datas para recálculo: Data Inicial | Informar a data inicial para o recálculo da rescisão |
| Intervalo de datas para recálculo: Data Final | Informar a data final para o recálculo da rescisão |
| Quebra de seção | Informar a quebra de seção |
| Seleção de Funcionário | Informe aqui o tipo de demissão para o grupo de funcionários que será selecionado |
| Altera Data Pagto com Mês Caixa Posterior ao Patgo Rescisão | O sistema não altera a data de pagto do evento, apenas considera o valor no mês caixa da rescisão. Somente tem o efeito na base de cálculo do IRRF |
| Executar os Parâmetros de Cálculo da Rescisão | Ao avançar será mostrada a tela de parâmetros de cálculo da rescisão |

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Lança e/ou finaliza férias automaticamente | Será lançada e/ou finalizada férias que estejam pendentes caso o parâmetro “Gravar rescisão com férias a lançar ou a finalizar” tenha sido marcado no cadastro global de rescisão |
| Lança Códigos Fixos na Rescisão | Lançará os códigos fixos cadastrados no anexo dos funcionários que estejam parametrizados para lançar na rescisão |
| Desconta Vale Transporte na Rescisão | Descontará o vale transporte conforme parametrização prévia |
| Lança Eventos de Salário Composto na Rescisão | Lançará eventos de salário composto que estejam cadastrados nos funcionários |
| Lança eventos que tomam por base o salário composto | Lançará eventos que tomam por base o salário composto que estejam cadastrados nos funcionários |
| Lança eventos relacionados ao salário composto | Lançará eventos relacionados ao salário composto que estejam cadastrados nos funcionários |
| Lança verbas com insuficiência de saldo | Lançará verbas de insuficiência de saldo conforme parametrização |
| Lança Eventos Programados | Lançará os eventos programados cadastrados no anexo dos funcionários que estejam parametrizados para lançar na rescisão |
| Lança eventos da integração com outros aplicativos | Lançará eventos da integração com outros aplicativos conforme parametrização |
| Lançar a movimentação do Gerenciador de Movimento | Lançará os eventos se o parâmetro “Utiliza Gerenciador de Movimento” estiver marcado no parametrizador e existirem eventos a serem lançados no gerenciador de movimento |
| Lançar Convênio | Somente fica visível se o parâmetro “usa Folha Agrária” estiver marcado e lançará valores do convênio conforme parametrização prévia |
| Lançar Comissão | Somente fica visível se o parâmetro “usa Folha Agrária” estiver marcado e lançará valores da comissão conforme parametrização prévia |
| Lança Saldo Devedor Consignado | Somente fica visível se usar o Consignado e lançará valores do saldo devedor do consignado conforme parametrização prévia |
| Empréstimo (Não lançar / Lançar Todos / Lançar por Tipo) | Conforme marcado será descontado o empréstimo parametrizado no anexo de Empréstimos do cadastro de funcionários |
| Lançar eventos da produção agrária | Somente fica visível se o parâmetro “usa Folha Agrária” estiver marcado e lançará eventos da produção agrária conforme parametrização prévia |

## **05.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
