---
content_hash: 353f2fd7ca8b7f682b52539735ba1e8c33a17373ce6a4e27cb7727f92ce19394
fetched_at: '2026-06-29T00:05:55.884372+00:00'
page_id: '146967545'
product: rm
source: tdn-rm
title: Utilizando a atividade "Se/Senão"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146967545
version: 10
---

## **CONTEÚDO**

1. #### **Visão Geral**
2. #### **Exemplo de utilização**
3. #### **Como utilizar a atividade de SE/SENÃO para executar em uma API**

## **01. VISÃO GERAL**

Primeiramente é necessário arrastar a atividade "Se/Senão" para o "fluxo de trabalho" sequencial em sua fórmula visual.

**Objetivo:** A finalidade da atividade "Se/Senão" é criar uma estrutura condicional, onde se **atender** a condição sistema continuará no fluxo das atividades.

|  |
| --- |
|  |

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as **propriedades** da atividade

|  |
| --- |
| A atividade "Se/Senão" pode possuir mais de um branch dentro da mesma atividade. |

## **02. EXEMPLO DE UTILIZAÇÃO**

Neste exemplo é necessário preencher somente a propriedade condições, que possuí dois tipos "**Condição de Regra Declarativa"**e**"Condição de Código".**

|  |  |
| --- | --- |
| * **Condição de Regra Declarativa:** Condição que permite utilizar códigos em C#.      Observação Quando utilizado parenteses em condições, o componente valida se realmente é  necessário a utilização do parenteses.  Caso queira forçar a utilização do parenteses na condição, utilize operadores  lógicos ao invés de condicionais.  Ex:  Usando condicional:  Condição: (true && false) || True  Após análise do componente: true && false || True    Usando Lógico:  Condição: (true & false) | True  Após análise do componente: (true & false) | True | * **Condição de Código:** Condição que permite utilizar os atributos do sistema. |

## **03.****COMO UTILIZAR A ATIVIDADE DE SE/SENÃO PAR EXECUTAR EM UMA API**

      Em execuções em API, a atividade Se/Senão tem o mesmo comportamento do descrito acima. A única diferença será para utilizar campos do contexto de API nas condições do if/else.

      No exemplo abaixo vamos mostrar como referenciar um campo da API para fazer uma condição. Vamos considerar que o contexto de usuário (UserControllerServer) já esteja selecionado.  Leia mais sobre [Fórmula Visual em API](https://tdn.totvs.com/x/9YynI). 

      Na a condição: this.ApiService.GetViewModelValue("\_Items.UserName").ToString() == "Teste\_01", será verificado se a propriedade userName do usuário é igual a 'Teste\_01'.
