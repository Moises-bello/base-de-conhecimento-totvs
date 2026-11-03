---
article_id: 33325130340887
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 7501be028acd6caecc668fd950c165a7be780deca6736d777503a29428639fc6
fetched_at: '2026-06-28T22:39:15.769789+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  cálculo do CBS/IBS no Configurador de Tributos?
type: support-article
updated_at: '2026-05-06T20:35:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33325130340887-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-c%C3%A1lculo-do-CBS-IBS-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108696855) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como configurar o cálculo do CBS/IBS no Configurador de Tributos?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2310  
  
**Solução**

**A configuração apresentada abaixo é um exemplo, que poderá servir como base para a criação do cenário específico da sua empresa.**

**Recomenda-se validar junto à sua equipe Fiscal ou Contábil a memória de cálculo que deverá ser aplicada às suas operações.**

## Tributos

CBSFED - CBS FEDERAL

ID. TRIBUTO - 000062

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108699543)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325130278423)

IBSEST - IBS ESTADUAL

ID. TRIBUTO - 000060

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108701591)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108703255)

## Perfil de Produto

Criar um Perfil de produto e incluir TODOS no campo Cód. Produto.

Todos os produtos serão considerados nesse perfil.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108704791)

## Perfil de Operação

Utilizar o Perfil de Operação 000051 - TODOS OS CFOPS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108705687)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108706583)

## Perfil de Participante

Criar um Perfil de Participante e incluir TODOS os Fornecedores e Cliente.

No campo Participante digite a palavra TODOS e no campo Loja ZZ ou quantidade caracteres que possua em seu ambiente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108707223)

## Perfil de Origem/Destino

Utilizar o Perfil 000002 - Todas as UFS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108707735)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325130293015)

## Regra de Base de Cálculo

Na Regra de Base de Cálculo utilizar a opção 11 - Fórmula Manual.

# Atenção!!!

**Nessa operação também serão calculados pelo Configurador de Tributos o ICMS, PIS e COFINS.**

**Os tributos mencionados acima, devem ser configurados primeiro e somente depois criar a Base do cálculo do CBS/IBS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108710167)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325130294935)

### Fórmula de cálculo utilizada para criar a Base de cálculo do CBS/IBS.

( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS ) - ( O:DESCONTO +  VAL:P00002 + VAL:C00001 + VAL:I00001 )

Legenda tributos da fórmula:

VAL:P00002 = valor calculado do PIS

VAL:C00001 = valor calculado do COFINS

VAL:I00001 = valor calculado do ICMS

## Regra de Alíquota

Na Regra de Alíquota utilizar a opção 04 - Alíquota Informada Manualmente no campo Valor Origem.

CBS FEDERAL- Alíquota 0,9%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33325108712215)

IBS ESTADUAL - Alíquota 0,1%

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34176967558039)

## Configuração para a Regra de Escrituração:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

## Regra de Cálculo - Documentos Fiscais

Regra de cálculo - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34176967565591)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34176967574679)

Regra de cálculo - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34176967575575)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34176967574679)

## 

## Calculo apresentado no Pedido de venda.

A nota possui os seguintes valores:

* + Valor total **(O:VAL\_MERCADORIA ): R$ 1.000,00**
  + Valor de ICMS **( VAL:I00001 ): R$ 120,00**
  + Valor de PIS **(VAL:P00002 ) : R$ 14,52**
  + Valor de COFINS **( VAL:C00001 ): R$ 66,88**

A Base de Cálculo do **CBS**e do **IBS** cadastrada foi: **( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS ) - ( O:DESCONTO +  VAL:P00002 + VAL:C00001 + VAL:I00001 )**

Aplicando os valores = **R$ 1.000,00 - (R$ 14,52 + R$ 66,88 + R$ 120,00) = R$ 798,60**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34712133077527)

How To: [MP - SIGAFIS - Configurar IBS/CBS p/ transmissão de Docs Fiscais](https://www.youtube.com/watch?v=abAh3M7tg9s)
