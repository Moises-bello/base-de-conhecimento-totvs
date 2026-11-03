---
content_hash: 365795b273a94186af28548cd2e4ccee65a8d2ace9d410f71294e46cc01aa412
fetched_at: '2026-06-29T00:11:37.388561+00:00'
page_id: '777271146'
product: rm
source: tdn-rm
title: DT - Resilição - Salário Composto - Parâmetro 'Não lançar evento(s) de saldo
  salário a ser(em) reduzido(s)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777271146
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Resilição - Salario Composto |
| País: | Brasil |
| Story | [DRHCALCRM-915](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-915) |

## **02.** **VERSÕES**

**Versões:**

* + **12.1.2209.249**
  + **12.1.2302.174**
  + **12.1.2306.118**

## **03. SITUAÇÃO/REQUISITO**

Ao efetuar uma resilição quando são informados os eventos de salários compostos a serem reduzidos e o funcionário opte por reduzir apenas um dos eventos, o sistema estava calculando também os eventos que não tinham sido informados na tela de Cadastro de Resilição.

O cliente também informou que mesmo reduzindo a jornada do evento, não deseja que sejam lançados os eventos de saldo de salário que seram reduzidos e que eles sejam usados somente no cálculo do valor para base de cálculo das verbas calculadas na resilição (férias, 13º Salário, etc.).

## **04. SOLUÇÃO**

O sistema passou a calcular a resilição considerando somente os eventos de salários compostos a serem reduzidos informados na tela de Cadastro de Resilição.

Foi criado o parâmetro **"Não lançar evento(s) de saldo salário a ser(em) reduzido(s)"** na tela de parâmetros do cálculo da resilição, onde o usuário terá a opção de lançar ou não lançar os eventos de saldo de salário que sofreram redução.

## **05. EXEMPLO**

Vamos considerar que tenho um funcionário com os salários compostos informados abaixo:

Em **RM | RH | Folha de Pagamento | Rescisão | Resilição | Tipo de Resilição |**  **Parametrização de Eventos**:

 

Em **RM | RH | Folha de Pagamento | Administração de Pessoal | Funcionário | Anexos | Movimento | Resilição**:

**Observação:** Ao efetuar o cálculo, será realizada uma interseção dos eventos informados na tela de '**Parametrização dos Eventos**' cadastrados no **Tipo de Resiliçã**o e os eventos informados no **Movimento de Resilição**. 

Ao clicar no botão '**Calcular**' será apresentada a tela de 'Parâmetros' da Resilição:

Com o parâmetro '**Não lançar evento(s) de saldo salário a ser(em) reduzido(s)**', **desmarcado**, será lançado o evento de saldo de salário no movimento da resilição, conforme abaixo:

Caso **não** queira que seja lançado o evento de saldo de salário no movimento da resilição, basta marcar o parâmetro '**Não lançar evento(s) de saldo salário a ser(em) reduzido(s)**' da tela de parâmetro da Resilição:

Com o parâmetro '**Não lançar evento(s) de saldo salário a ser(em) reduzido(s)**', **marcado**, não será lançado o evento de saldo de salário no movimento da resilição, conforme abaixo:

**Observação**: Vale observar que devido ter informado somente o evento 0253, o sistema calculou a resilição considerando somente os eventos de salários compostos a serem reduzidos informados na tela de Cadastro de Resilição.

Após realizado o cálculo da resilição, foi atualizada a Composição Salarial - Salário Composto e também o Histórico Salarial do funcionário:

**Composição Salarial - Salário Composto**

**Histórico Salarial do funcionário**

## **06.** **ASSUNTOS RELACIONADOS**

* [Resilção](https://tdn.totvs.com/pages/viewpage.action?pageId=452719201)
* [Resilição - Tipos de Resilição](https://tdn.totvs.com/pages/viewpage.action?pageId=452719391)
* [DT - Resilição](https://tdn.totvs.com/pages/viewpage.action?pageId=284854431)
