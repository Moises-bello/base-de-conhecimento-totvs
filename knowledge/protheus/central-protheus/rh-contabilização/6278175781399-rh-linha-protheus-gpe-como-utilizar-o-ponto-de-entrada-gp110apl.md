---
article_id: 6278175781399
category: RH - Contabilização
content_hash: 1d5d0b6cc2732eff7178575ee47fb940fa6b7e5fe7298fcbbac4f3249ab60af5
fetched_at: '2026-06-28T22:43:45.873835+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110APL
type: support-article
updated_at: '2025-07-17T13:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6278175781399-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110APL
---

**Descrição:**

O ponto de entrada GP110APL permite alterar variáveis de parametrização no processo de contabilização dos lançamentos da folha de pagamento e do 13º Salário.

**Programa Fonte**

| GPEM110.PRX |
| --- |

 

**Sintaxe**

| GP110APL - Parametrização da contabilização da folha ( [ ] ) |
| --- |

Retorno

()

Observações

**Situação para Utilização**

Durante o processo de contabilização da folha de pagamento e do 13º Salário, o Sistema faz um resumo geral incluindo todas as filiais, matrículas, centros de custo e categorias para processamento.

Atualmente, esta parametrização é realizada internamente, havendo a necessidade de contabilizar algumas categorias funcionais de forma diferenciada.

A criação do ponto de entrada permite configurar as seguintes informações: filial inicial/final, matrícula inicia/final, centro de custo inicial/final e categorias funcionais a contabilizar, de forma que não seja necessário diferenciá-las.  

**Variáveis Disponíveis**

|  |  |  |  |
| --- | --- | --- | --- |
| Variável | Conteúdo | Tipo | Observações |
| cFilDe | Filial De | Caracter | Informe o código inicial das filiais |
| cFilAte | Filial Até | Caracter | Informe o código final das filiais |
| cCcDe | Centro de Custo De | Caracter | Informe o código inicial do centro de custos |
| cCcAte | Centro de Custo Até | Caracter | Informe o código final do centro de custos |
| cMatDe | Matrícula De | Caracter | Informe o número inicial de matrícula do funcionário |
| cMatAte | Matrícula Até | Caracter | Informe o número final de matrícula do funcionário |
| cCat | Categorias | Caracter | Informe as letras das categorias desejadas na contabilização |

**Exemplos:**

#INCLUDE "Protheus.CH"

User Function GP110APL()

//cCateg:="CMPST"  
RETURN nil

![GP110APL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22969098086551)

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
