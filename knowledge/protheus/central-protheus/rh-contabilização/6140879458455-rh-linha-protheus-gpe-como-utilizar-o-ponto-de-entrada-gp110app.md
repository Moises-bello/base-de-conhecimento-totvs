---
article_id: 6140879458455
category: RH - Contabilização
content_hash: 20e63a4d84a241004c94bbabea00b2968d202de8094fe9308d54c486e113bafc
fetched_at: '2026-06-28T22:43:45.888758+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o ponto de entrada GP110APP
type: support-article
updated_at: '2025-07-17T13:14:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6140879458455-RH-Linha-Protheus-GPE-Como-utilizar-o-ponto-de-entrada-GP110APP
---

**Descrição:**

O ponto de entrada GP110APP permite alterar variáveis de parametrização no processo de contabilização das provisões de férias e de 13º salário.

**Programa Fonte**

```
GPEM110.PRX
```

**Sintaxe**

GP110APP - Parametrização da contabilização da Folha ( [ ] )

**Parâmetros:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

Retorno

()

Observações

**Situação para Utilização**

Durante o processo de contabilização das provisões, o Sistema faz um resumo geral incluindo todas as filiais, matrículas, centros de custo e categorias para processamento.

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
| cCateg | Categorias | Caracter | Informe as letras das categorias desejadas na contabilização |

**Exemplos:**

#INCLUDE "Protheus.CH"  
User Function GP110APP()  
//cCateg := "ACDEGHIJMPST"cCateg:= "CMPST"  
RETURN nil

![GP110APP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22875285573399)

Veja Também

[GP110QRY - Inclusão de Campo - Query](https://tdn.totvs.com/pages/viewpage.action?pageId=6079117), [Contabilização da Folha](https://tdn.totvs.com/pages/viewpage.action?pageId=6079243)

**Variáveis**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |

**Saiba Mais:**[RH-Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
